import sys

class team_attributes(object):
    """
    EXECUTION
    python pemdasq2.py <filename.csv>

    INPUT:
    Valid csv file.

    Output:
    1. average​ ​height​ ​in​ ​inches​ ​of​ ​all outfielders,​ ​
    2. maximum​ ​age​ ​of​ ​the​ ​team,​ 
    3. number​ ​of​ ​players​ ​with​ ​a​ ​last​ ​name​ ​starting​ ​with​ ​the​ ​letter ‘B’.​

    ASSUMPTIONS:
    1. Content of csv file always has valid entries for column data cells:
        Name, Team, Position, Height(inches), Weight(lbs), Age 
    2. First line in csv contains the column names (not relevant for the calculations).
    3. There is at least one line of actual data.
    
    WHY implement this way?:
        Illustrate use of:
            collections; list manipulation, 
            comprehensions; how to build results in one line, both compactly and readably,
            logical subdivision of tasks into smaller, readable blocks; 
                1 scripted function, 
                    to show python can be functional and 
                1 class with several behaviors addressing the reqs of the question, 
                    to show python can also be Object Oriented
                Note: class funtions allow parameter setting so they can look for alternative 
                    values in 'table' data.
            data division as lists of column cell data. That is:
                the meaning originates from the column name so its easy to give it a list name and
                a 'row' is an "idx" into the hypothetical 'table' built from the csv file; 
                    i.e. easy x-ref across the lists.
    """
    names     = []
    teams     = []
    positions = []
    heights   = []
    weights   = []
    ages      = []

    def __init__(self, team_data):
        for l in team_data[1:]:
            refLine = l.split(',')
            self.names.append(refLine[0].strip())            
            self.teams.append(refLine[1].strip())
            self.positions.append(refLine[2].strip())
            self.heights.append(int(refLine[3]))
            self.weights.append(int(refLine[4]))
            self.ages.append(float(refLine[5]))
            print(l)

    def get_average_height(self, position=None):
        ht = 0
        cnt = 0
        if position in self.positions:
            ht_list = [ self.heights[idx] for idx in range(len(self.heights)) if self.positions[idx] == position ]
            avg = sum(ht_list) / float(len(ht_list))
        else:
            avg = sum(self.heights) / float(len(self.heights))
        return avg

    def get_max_age(self, team=None):
        if team in self.teams:
            age_list = [ self.ages[idx] for idx in range(len(self.ages)) if self.teams[idx] == team ]
            max_age = max(age_list)
        else:
            max_age = max(self.ages)
        return max_age

    def get_cnt_of_lastname_startingwith_b(self):
        return len([name for name in self.names if len(name.split(' '))>1 and str(name.split(' ')[1]).upper().startswith('B')])


# UTILITY FUNCTIONS
def get_lines_from_csv_file(filename):
    lines = []
    with open(filename, 'r', encoding='utf-8') as f:
        for l in f.readlines():
            str_line = str(l).replace('\n','').replace(u"\u200b",'').strip()
            lines.append(str_line)
    return lines


# MAIN
if __name__ == '__main__':
    file_name = ''
    print ('ARGS provided: ',str(sys.argv),"\n")

    if len(sys.argv) > 1 and str(sys.argv[1]).endswith(".csv"):
        file_name = str(sys.argv[1])
    else:
        print ("Command line use:\n" \
                "\tpython pemdasq2.py <fileName.csv>\n" \
                "Purpose: To read csv file and extract heightt, age and last name information.\n")

    if(file_name != ''):
        lines = get_lines_from_csv_file(file_name)
        if(len(lines)>1):
            team = team_attributes(lines)
            print('\nAverage height of \'Outfielders\'  = ',team.get_average_height("Outfielder"))
            print('Max age of all \'BAL\' players     = ',team.get_max_age("BAL"))
            print('Total names with last name \'B*\'  = ',team.get_cnt_of_lastname_startingwith_b())
        else:
            print('ERROR: Supplied csv file must have a header and valid data for useful results; number of lines detected = ', len(lines))

    print("\nDone")
