function getData() {
    return new Promise(function(resolve,reject){
        setTimeout(function(){resolve();}, 100);
    });
}
var refUrl = 'http://127.0.0.1:5000/randnums';
var total=0;

function callEndpointFetch(url) {
    fetch(url).then(
        function(response){
            return response.json();
        }//,
        // function(errorurl){
        //     console.log('Error loading ' + errorurl)
        // }
    ).then(
    function(r){
        for(var i = 0; i<r.length;i++){
            console.log(r[i]);
            total += r[i];
        }
        document.getElementById('marco').innerHTML = total
    }
    ).catch(function(error){
        console.log('Call::Fetch failed',error);
    });
}


getData()
.then(function(){
    console.log("Call 1:");
    callEndpointFetch(refUrl);
    return getData();
})
.then(function(){
    console.log("Call 2:");
    callEndpointFetch(refUrl);
    return getData();
})
.then(function(){
    console.log("Call 3:");
    callEndpointFetch(refUrl);
});


// Future Reference only...
function callEndpointXhr(url) {
  return new Promise((resolve, reject) => {
    const xhr = new XMLHttpRequest();
    xhr.open("GET", url);
    xhr.onload = () => 
        resolve(
            console.log("success"+xhr.responseText)
            );
            //xhr.responseText);
    xhr.onerror = () => 
        reject(
            console.log(xhr.statusText)
            );
    xhr.send();
  }).catch(function(error){
    console.log('CallXhr::Fetch failed',error);
});
}
