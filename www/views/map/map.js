var map;
initMap()
function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: -37.2744, lng: 144.7852},
        zoom: 7
    });
    var marker = new google.maps.Marker({
        position: {lat: -37.2744, lng: 144.7751},
        map: map
    });
}
