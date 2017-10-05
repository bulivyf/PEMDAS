import sys
import math

class great_circle_calculator(object):
    """
    Input:
    Reference grid bounds which estimate locations on the surface of the earth.

    Output:
    Printout to console of (lat,long) points at 1km interval within provided grid bounds.
    Displayed values are to three decimal places.

    ASSUMPTIONS:
    1. values entered wont be vastly different (display content will be hard to read).

    WHY impl this way?:
    Problem defined: find an approach to return a (lat, long) destination point 1km away from src at a given bearing.
    Discussion
    This is new territory for me, so I envisaged good answers already existed.  
    So aimed to research rather than solve directly.  From research, absorb, implement then test.

    Research: 
    1. "geo" terminology which covered calculations on the earth surface.  A: Geodesics
    2. approaches for estimating distance across the uneven curving surface of the Earth.
       A: 'haversine', 'great circle' and Rhumb lines.

    Implementation choice:
    * 'great circle' was indicated as a good estimation approach.
    My initial calculations were wildly off, in my represenation of the formula (grr: radians).  
    So looked up how others performed similar; I found the following:
        http://movable-type.co.uk/scripts/latlong.html
        which helped tremendously.
    Later on, the discovery of the following Python package promised a quicker/better (well tested) solution:
        Python: Geodesy library, can solve this question (not used here)
        https://github.com/mrJean1/PyGeodesy/tree/master/dist
    Conclusion:
    It's all about entering the right search terms in the web browser.
    All in all an interesting problem to solve.  With keeping for future ref.
    """
    # latitude (phi)
    src_lat = 0.0 
    # longitude (lambda)
    src_lng = 0.0
    # radius (r), km
    earth_radius = 6371.0

    def set_src_lat_lng(self, source_lat_dec_degrees, source_lng_dec_degrees):
        self.src_lat = self.degs2radians(float(source_lat_dec_degrees))
        self.src_lng = self.degs2radians(float(source_lng_dec_degrees))

    def calc_dest_latlng(self, bearing, km_distance):
        dist_ratio = float(km_distance) / self.earth_radius
        rad_bearing = self.degs2radians(float(bearing))
        sinAplusBwithBearingScale = \
            math.sin(self.src_lat) * math.cos(dist_ratio) + \
            math.cos(self.src_lat) * math.sin(dist_ratio) * math.cos(rad_bearing)

        dst_lat = math.asin( sinAplusBwithBearingScale )
        dst_lng = self.src_lng + \
            math.atan2( \
                math.sin(rad_bearing) * math.sin(dist_ratio) * math.cos(self.src_lat), \
                math.cos(dist_ratio) - math.sin(self.src_lat) * sinAplusBwithBearingScale )
        return self.rads2degrees(dst_lat), self.normalize_longitude(self.rads2degrees(dst_lng))

    def normalize_longitude(self, lng):
        return (lng+540) % 360 - 180

    def degs2sexa(self,dec_degrees): 
        """
        Definition: "sexagesimal" = Degrees°,Mins',Secs", that is:
            < Whole degrees >°, < x in 60 mins of a 1 degree >', < y in 60 secs of a 1 minute >".
        Example: 45°,32',16"
        Note: a zero entry in degree,mins will not show a negative (indicating a W or S location).
        See also: http://www.anycalculator.com/decimaltodegree.htm
        """
        degs = int(dec_degrees)
        mins_scale = math.fabs((dec_degrees - degs) * 60.0)
        mins = int(mins_scale)
        # Make sure W/S is indicated near 0 deg, if no degrees.
        if(dec_degrees < 0 and degs == 0 and mins > 0): 
            mins = -mins
        secs = int((mins_scale - mins) * 60.0)
        # Make sure W/S is indicated near 0 deg, if only secs exist
        if(dec_degrees < 0 and degs == 0 and mins == 0 and sec > 0):
            secs = -secs
        return degs, mins, secs

    def sexa2degs(self,degs,mins,secs):
        return degs + mins/60.0 + secs/3600.0

    def degs2radians(self, dec_degs):
        return float(dec_degs) * math.pi / 180.0

    def rads2degrees(self, radians):
        return float(radians) * 180.0 / math.pi


# MAIN
if __name__ == '__main__':
    minlat = 0.0
    maxlat = 0.1
    minlng = 0.0
    maxlng = 0.1
    print ('ARGS provided: ',str(sys.argv),"\n")
    if len(sys.argv) == 5:
        minlat = float(sys.argv[1])
        maxlat = float(sys.argv[2])
        minlng = float(sys.argv[3])
        maxlng = float(sys.argv[4])
    else:
        print ("Command line use:\n" \
                "\tpython pemdasq1.py <minlat> <maxlat> <minlng> <maxlng>\n" \
                "Purpose: Output a gridded space of (lat, long) points that span across the earth surface in 1km increments." \
                "\nStarts bottom left of grid, projects (lat,long) points going Eastward. "\
                "\nEach consecutive row is a 1km Northern latitude step from the minlat value upwards, to maxlat.\n\n" \
                "Example: python pemdasq1.py 0 .1 0 .1")

    grc = great_circle_calculator()
    lat = minlat
    latInBounds = True
    while(latInBounds):
        lng = minlng
        lngInBounds = True
        print (">>>:(%6.3f,%7.3f) " % (lat, lng), end='')
        row_lat = lat
        while (lngInBounds):
            grc.set_src_lat_lng(row_lat, lng)
            row_lat,lng = grc.calc_dest_latlng(90,1)
            print("(%6.3f,%7.3f) " % (row_lat, lng), end='')
            if lng > maxlng:
                lngInBounds = False
        grc.set_src_lat_lng(lat, lng)
        lat,lng = grc.calc_dest_latlng(0,1)
        if lat > maxlat:
            latInBounds = False
        print()

    print("\nDone")