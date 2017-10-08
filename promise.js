/*
Description:
Developed in response to a Javascript problem posed by PEMDAS.
Execution:
Perform three calls to the REST endpoint.  In each get a list of integers back.  
Keep a running total of all the values.
On the client check to see how long the response takes to come back.
If its greater than 100 ms ignore its total, otherwise keep the running total as a "global" variable.
If all three entries fail to return under 100ms, first two lists are summed and kept as the total.

ASSUMPTIONS: 
1. Javascript wasn't a required language for backend processing.
2. JS namespace/package wasn't needed for this amount of code.
For future ref: https://addyosmani.com/blog/essential-js-namespacing/
3. Google chrome is used for execution/testing; ES6+.

Comments
1. When running the Javascript, advise you have the dev tools up in Google (F12).
Output makes more sense through the console.log comments.

Research - JS "Promise patterns":
https://github.com/DukeyToo/es6-promise-patterns

*/
displayTotal = 0; // global var, per question
var refUrl = 'http://127.0.0.1:5000/randnums';
var totalFails = 0;
var grandTotal = 0;

function getData() {
    return new Promise(function(resolve,reject){
        // Max Timeout per call... 1 sec
        setTimeout(function(){resolve();}, 1000);
    });
}

getData()
.then(function(){
    console.log("Call 1: ****************************************************");
    callEndpointBlockedFetch();
    return getData();
})
.then(function(){
    console.log("Call 2: ****************************************************");
    callEndpointBlockedFetch();
    return getData();
})
.then(function(){
    console.log("Call 3: ****************************************************");
    callEndpointBlockedFetch();
    document.getElementById('marco').setAttribute('data-value','polo');
});

const callEndpointBlockedFetch = async() => {
    var limit = 100;

    var start = new Date().getTime();
    const response = await fetch(refUrl);
    const r = await response.json();
    var delta = new Date().getTime() - start;
    console.log("List  = "+r);

    var total = calcTotal(r);
    if(delta < limit) {
        displayTotal += total
        console.log("Response time: "+delta+"ms");
        console.log("Total = "+displayTotal);
        grandTotal = displayTotal;
    }else{
        totalFails += 1;
        console.log("Response time "+delta+"ms >= "+limit+"ms; running total unchanged.");
        if(totalFails == 3){
            console.log("Response time of "+delta+"ms >= "+limit+"ms, exceeds for third time; resetting total to sum of first two lists.");
            displayTotal = grandTotal;
        }
        grandTotal += total;
    }
    console.log("GrandTotal: "+grandTotal)
    document.getElementById('marco').innerHTML = displayTotal;
}

// UTILITY FUNCTIONS
function calcTotal(res){
    var sumVal = 0;
    for(var i = 0; i<res.length;i++){
        sumVal += res[i];
    }
    return sumVal;
}