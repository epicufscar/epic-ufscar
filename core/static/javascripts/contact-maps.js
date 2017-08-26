$(document).ready(function () {
    //Set Map
    function initialize() {
        var myLatlng = new google.maps.LatLng(-21.979656, -47.880628);
        var mapOptions = {
            zoom: 15,
            center: myLatlng,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        }

        var map = new google.maps.Map(document.getElementById('map'), mapOptions);
        var contentString = '<div class="iw-container">\n    <div class="iw-title"><b>ESCOLA PILOTO DE COMPUTAÇÃO</b></div>\n    <div class="iw-content">\n        <b>Departamento de Computação</b><br>\n        Rod. Washington Luís, Km 235<br>\n        13565-905, São Carlos-SP<br>\n    </div>\n</div>';
        var infowindow = new google.maps.InfoWindow({
            content: contentString,
        });

        //Add Marker
        var marker = new google.maps.Marker({
            position: myLatlng,
            map: map,
            visible: false,
        });

        infowindow.open(map, marker);

        //Resize Function
        google.maps.event.addDomListener(window, "resize", function () {
            var center = map.getCenter();
            google.maps.event.trigger(map, "resize");
            map.setCenter(center);
        });
    }

    google.maps.event.addDomListener(window, 'load', initialize);
});
