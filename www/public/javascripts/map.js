 

//scenior one
function addMoodMarker(map,needtyype,w,j){
    var iconBase = '/public/images/mood/';
        var icons = {
          happy: {
            icon: iconBase + 'icons8-happy.png'
          },
          unhappy: {
            icon: iconBase +'normal.png'
          },
          normal: {
            icon: iconBase + 'icons8-marker.png'
          }
        };
        var features = {
                    position: new google.maps.LatLng(w,j),
                    type: needtyype//'happy'
                  };

        
//        function addMarker(feature) {
          var marker = new google.maps.Marker({
            position: features.position,
            icon: icons[features.type].icon,
            map: map
          });
//    setsample(map,icons)
}

//scenior two
function addUsersMarker(map,content,needtype,w,j){
    var iconBase = '/public/images/wanghong/';
        var icons = {
          four: {
            icon: iconBase + 'four.png'
          },
          three: {
            icon: iconBase + 'three.png'
          },
          two: {
            icon: iconBase + 'two.png'
          },
            one: {
            icon: iconBase + 'one.png'
          }
        };
        
        var features = {
                    position: new google.maps.LatLng(w,j),
                    type: needtype//'happy'
                  };
    
        if (content!=null){
            var infowindow = new google.maps.InfoWindow({
                content: content
            });
            var marker = new google.maps.Marker({
                position: features.position,
                icon: icons[features.type].icon,
                map: map,
                title:"Tweet"
            });
            marker.addListener('click', function() {
                    infowindow.open(map, marker);
            });
        }else{
          var marker = new google.maps.Marker({
            position: features.position,
            icon: icons[features.type].icon,
            map: map
          });
        }
}

function displaywanghong(map,hashtag,followers,tweet,w,j){
    if(followers<10000){
        addUsersMarker(map,null,'one',w,j)
    }else if((followers>=10000)&&(followers<100000)){
        addUsersMarker(map,tweet,'two',w,j)
    }else if((followers>=100000)&&(followers<1000000)){
        addUsersMarker(map,tweet,'three',w,j)
//        test(map,tweet,'four',w,j)
    }else{
        addUsersMarker(map,tweet,'four',w,j)
//        test(map,tweet,'four',w,j)
//        console.log({h:tweet})
    }
}

function test(map,content,needtype,w,j){
    var marker1 = new google.maps.Marker({
        position: {lat: w, lng: j},
        title:"Tweet",
        map: map
    });
    var infowindow = new google.maps.InfoWindow({
                content: content
            });
//            var marker = new google.maps.Marker({
//                position: features.position,
//                icon: icons[features.type].icon,
//                map: map,
//                title:"Tweet"
//            });
            marker1.addListener('click', function() {
                    infowindow.open(map, marker1);
            });
}

//scenior three
function DisplayIncome(map,name,medIncome){
    if (medIncome<20000){
        drawMap(map,name,color.one)
    }else if ((20000<=medIncome)&&(medIncome<30000)){
        drawMap(map,name,color.two)
    }else if((30000<=medIncome)&&(medIncome<40000)){
        drawMap(map,name,color.three)
    }else if((40000<=medIncome)&&(medIncome<50000)){
        drawMap(map,name,color.four)
    }else{
        drawMap(map,name,color.five)
    }
}

function drowSample(map){
    var legend = document.getElementById('legend');
    legend.style.display="block"
    var iconBase = '/public/images/sample/';
    var icons = {
          "<20000": {
            icon: iconBase + '20000.png'
          },
          "20000~30000": {
            icon: iconBase + '20000~30000.png'
          },
          "30000~40000": {
            icon: iconBase + '30000~40000.png'
          },
            ">50000": {
            icon: iconBase + '50000.png'
          }
        };
        for (var key in icons) {
          var type = icons[key];
          var name = key;
          var icon = type.icon;
          var div = document.createElement('div');
          div.innerHTML = '<img height=10px height=10px src="' + icon + '"> ' + name;
          legend.appendChild(div);
        }

        map.controls[google.maps.ControlPosition.RIGHT_BOTTOM].push(legend);
}

function drawMap(map,needname,c){
    var currentlocation = new Array;
    for(var ind = 0; ind < vic.city.length; ind++){
        var name = vic.city[ind].properties.Suburb_Name;
        name = name.replace(/(\s*$)/g, "")
//        console.log({name:name})
        if(name==needname){
            var testlist = vic.city[ind].geometry.coordinates[0];
            if (vic.city[ind].geometry.type!="MultiPolygon"){

                currentlocation = transit(testlist)
                drawArea(map,currentlocation,c)

            }else{

                testlist = vic.city[ind].geometry.coordinates;

                if(testlist.length!=1){
                    var location =new Array;
                    for(var inde = 0; inde<testlist.length;inde++){
                        if(testlist[inde].length!=1){

                            location = transit(testlist[inde])

                        }else{

                            if (testlist[inde][0].length!=1){
                                location = transit(testlist[inde][0])

                            }else{
                                location = transit(testlist[inde][0][0])}
                        }  
                        drawArea(map,location,c)
                    }
                }
            }
        }
    }
}

function displayArea(map,c){

    var currentlocation = new Array;
    for(var ind = 0; ind < vic.city.length; ind++){
        var testlist = vic.city[ind].geometry.coordinates[0];
        var name = vic.city[ind].properties.Suburb_Name;
        if (vic.city[ind].geometry.type!="MultiPolygon"){

            currentlocation = transit(testlist)
            drawArea(map,currentlocation,c)

        }else{

            testlist = vic.city[ind].geometry.coordinates;

            if(testlist.length!=1){
                var location =new Array;
                for(var inde = 0; inde<testlist.length;inde++){
                    if(testlist[inde].length!=1){

                        location = transit(testlist[inde])

                    }else{

                        if (testlist[inde][0].length!=1){
                            location = transit(testlist[inde][0])
                                            
                        }else{
                            location = transit(testlist[inde][0][0])}
                    }  
                    drawArea(map,location,c)
                }
            }
        }
    }
}

function drawArea(map,currentlocation,color){
    var bermudaTriangle = new google.maps.Polygon({
        paths: currentlocation,
        strokeColor: color,
        strokeOpacity: 0.8,
        strokeWeight: 2,
        fillColor: color,
        fillOpacity: 0.5
      });
      bermudaTriangle.setMap(map);
}

function transit(list){
    if(list.length!=1){
        var currentlocation=new Array();
        for (var i = 0, n = list.length; i < n; i++) {

            
            currentlocation[i]={lat: list[i][1], lng: list[i][0]};
//            console.log(list[0]);
        }
    }   
    return currentlocation
}

var color = {one:'#87CEFA',
            two:'#00BFFF',
             three:'#4682B4',
             four:'#0000FF',
             five:'#191970'
            }

