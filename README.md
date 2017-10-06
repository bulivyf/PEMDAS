Subject: Example Python Code
Author: E.M.Fraser
Date: Oct 6th, 2017

INTRODUCTION
The two .py files are implementations in relation to posed interview questions, which I won't include should they be used for other candidates.  

The code covers:
1. pemdasq1: Output a grid of (lat,lng) for a defined grid area that covers a portion of the Earth surface.
2. pemdasq2: Read a csv file and extract information from the data.

The questions asked for an explanation on why the code was written the given way.  In response, all such comments are in the header of each respective python source file.


DESIGNER NOTES
The code was written as a single file per question.  In a solution that aims to become product worthy a lot more design structuring and thus refactoring will certainly occur.

DEVELOPER NOTES
The Visual Studio IDE was used for this development.  Then the code moved to a directory where github could easily gain the push (without any of the other python code already in use).  Note: PyCUDA experiments are the main motivator for the use of such an IDE (NVIDIA NSight is best in that IDE); no other reason.  

TESTER NOTES
The code was tested within the Visual Studio IDE as part of the main section of the script.  All tests should be performed at the command line.


EOF
