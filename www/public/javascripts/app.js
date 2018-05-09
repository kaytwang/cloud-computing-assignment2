function home(){
    mDiv=document.getElementById('map');
    mDiv.style.display='none'
    hDiv = document.getElementById('introduction');
    hDiv.style.display='block'
    pDiv=document.getElementById('chart');
    pDiv.style.display='none'
    iDiv=document.getElementById('incomechart');
    iDiv.style.display='none'
}
var m2
function onetwo(){
    mDiv=document.getElementById('map');
    mDiv.style.display='block'
    hDiv=document.getElementById('introduction');
    hDiv.style.display='none'
    pDiv=document.getElementById('chart');
    pDiv.style.display='none'
    iDiv=document.getElementById('incomechart');
    iDiv.style.display='none'

        var map = new google.maps.Map(document.getElementById('map'), {
            center: {lat:-36.630520, lng:144.922716},
            zoom: 7
    });

    var source = new EventSource('http://115.146.86.135/onetwo');
    var div = document.getElementById('one');
    var count = 0
    
    source.onopen = function (event) {

        displayArea(map,'#FFA500')
        
    };
    
    source.onmessage = function (event) {
        try{
            if (count<10000){
                
                var data = event.data;
                var result = JSON.parse(data)

                if(result.sentiment[0]>0){
                    addMoodMarker(map,'happy',result.coordinates.coordinates[1],result.coordinates.coordinates[0])
                }else if (result.sentiment[0]==0){
        //            console.log({mood:"sad"})
                    addMoodMarker(map,'normal',result.coordinates.coordinates[1], result.coordinates.coordinates[0])
                }else{
                    addMoodMarker(map,'unhappy',result.coordinates.coordinates[1],result.coordinates.coordinates[0])
        //            addMoodMarker(map,'normal',result.coordinates.coordinates[1], result.coordinates.coordinates[0])
                }
            }else{
                source.close();
            }
            count++
        }catch(e){
            console.log({error:e})
        }

    };
    
    source.onerror = function (event) {
        m2=map
        console.log({error:event.data})
        source.close();
    };
}

function two(){
    mDiv=document.getElementById('map');
    mDiv.style.display='block'
    hDiv=document.getElementById('introduction');
    hDiv.style.display='none'
    pDiv=document.getElementById('chart');
    pDiv.style.display='none'
    iDiv=document.getElementById('incomechart');
    iDiv.style.display='none'
//    var map = map()
//    var map = initMap()
     var map = new google.maps.Map(document.getElementById('map'), {
    center: {lat:-36.630520, lng:144.922716},
    zoom: 7
    });
    
    var source = new EventSource('http://115.146.86.135/onetwo');
    var div = document.getElementById('two');
    var count = 0
    
    source.onopen = function (event) {
//        console.log({something:event.data})
        displayArea(map,'#C0C0C0')
    };
    
    source.onmessage = function (event) {
        if(count<10000){
            console.log({count:count})
            try{
                var data = event.data;
                var result = JSON.parse(data)
                displaywanghong(map,result.hashtag,result.followers,result.text,result.coordinates.coordinates[1],result.coordinates.coordinates[0])
            }catch(e){
                console.log({error:e})
            }
        }else{source.close()}
        count++
    };
    
    source.onerror = function (event) {

        console.log({error:event.data})
        source.close();
    };
    
}

function three(){
    mDiv=document.getElementById('map');
    mDiv.style.display='block'
    hDiv=document.getElementById('introduction');
    hDiv.style.display='none'
    pDiv=document.getElementById('chart');
    pDiv.style.display='none'
    iDiv=document.getElementById('incomechart');
    iDiv.style.display='none'
    
    pro=document.getElementById('pro');
    pro.style.display='block'
//    var m = initMap()
    var m = new google.maps.Map(document.getElementById('map'), {
    center: {lat:-36.630520, lng:144.922716},
    zoom: 7
    });
    drowSample(m)
    count=0
    var source = new EventSource('http://115.146.86.135/three');
    var div = document.getElementById('three');
    
    
    
    source.onopen = function (event) {
//         displayArea(map,'#F0FFFF')
        console.log({open:event})
    };
    
    source.onmessage = function (event) {
        if (count<1498){
            try{
                var data = event.data;
    //            console.log({data:data})
                var result = JSON.parse(data)
                DisplayIncome(m,result.NAME_2006,result.median06)
    //            console.log({listening:result})
            }catch(e){
                console.log({error:e})
            }
            count++
            console.log({ik:count})
        }else{
            
           }
    };
    
    source.onerror = function (event) {

        console.log({error:event.data})
        source.close();
    };
    
    co = document.getElementById('wanghong');
    co.onclick=function(){cover(m)}
//
//    if(s){
//     cover(m)}
    return m
}

function getProportion(){
    mDiv=document.getElementById('map');
    mDiv.style.display='none'
    hDiv=document.getElementById('introduction');
    hDiv.style.display='none'
    iDiv=document.getElementById('incomechart');
    iDiv.style.display='none'
    pDiv=document.getElementById('chart');
    pDiv.style.display='block'
//line
     
}

function getincome(){
    mDiv=document.getElementById('map');
    mDiv.style.display='none'
    hDiv=document.getElementById('introduction');
    hDiv.style.display='none'
    pDiv=document.getElementById('chart');
    pDiv.style.display='none'
    iDiv=document.getElementById('incomechart');
    iDiv.style.display='block'
}


function getCover(){
     hDiv=document.getElementById('introduction');
    hDiv.style.display='none'
    mDiv=document.getElementById('map');
    mDiv.style.display='block'
    pDiv=document.getElementById('chart');
    pDiv.style.display='none'
    iDiv=document.getElementById('incomechart');
    iDiv.style.display='none'
    var m =three()
    cover(m)
}

function cover(m){
    var source = new EventSource('http://115.146.86.135/onetwo');
    var div = document.getElementById('one');
    
    source.onopen = function (event) {};
    
    source.onmessage = function (event) {
        try{
            if (count<10000){
                
                var data = event.data;
                var result = JSON.parse(data)

                if(result.sentiment[0]>0){
                    addMoodMarker(m,'happy',result.coordinates.coordinates[1],result.coordinates.coordinates[0])
                }else if (result.sentiment[0]==0){

                    addMoodMarker(m,'normal',result.coordinates.coordinates[1], result.coordinates.coordinates[0])
                }else{
                    addMoodMarker(m,'unhappy',result.coordinates.coordinates[1],result.coordinates.coordinates[0])
        //            addMoodMarker(map,'normal',result.coordinates.coordinates[1], result.coordinates.coordinates[0])
                }
            }else{
                source.close();
            }
            count++
        }catch(e){
            console.log({error:e})
        }

    };
    
    source.onerror = function (event) {

        console.log({error:event.data})
        source.close();
    };
}
