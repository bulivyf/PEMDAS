8Read the javaSubject: Example Javascript Code
Author: E.M.Fraser
Date: Oct 8th, 2017


INTRODUCTION
The "promise.*" code relates to a second optional problem posed by PEMDAS.

Objectives:
1. Provide a REST endpoint: Write rudimentary web based response code that provides lists of random numbers;
2. Write Javascript that:
* Calls the REST endpoint (three times), gets the lists and totals the values as they arrive.
* Ignore any list responses that take longer than 100ms. 

DEVELOPER NOTES
Solution for the web endpoint was to use Python Flask.  Its CORS functionality is simple to use and configure.  
The Solution for the front end is Javascript working with a named tag within html.

TESTER NOTES
Web browser used: Chrome (with firebug enabled)
Python 3: Anaconda ("pip install flask", showed flask was pre-exsiting)

To run: 
1. Command prompt at dir with flask py implementation:
python promise.py 
Note the url, assuming url = "http://localhost:5000/"
The endpoint is url+"/randnums"
Test this by navigating to http://localhost:5000/randnums in the webbrowser.
You'll see a list of integers displayed per page refresh.
2. To test the javascript (promise.js), use the provided promise.html file in a webbrowser.
Resulting display will include the total of the three endpoint calls.
Read comments in promise.js for more information on assumptions etc.
