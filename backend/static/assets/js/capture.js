
$(document).ready(function(){
var stream = document.getElementById("stream");
var capture = document.getElementById("capture");
var snapshot = document.getElementById("snapshot");

var cameraStream = null;
    $("#startCamera").on('click', function(){
        var mediaSupport = 'mediaDevices' in navigator;
        if( mediaSupport && null == cameraStream ) {
            navigator.mediaDevices.getUserMedia( { video: true } )
            .then(function(mediaStream) {
                cameraStream = mediaStream;
                stream.srcObject = mediaStream;
                stream.play();
            })
            .catch(function(err) {
                console.log( "Unable to access camera: " + err );
            });
        }
        else {
    
            alert('Your browser does not support media devices.');
            return;
        }
    })

    $("#stopCamera").on('click', function(){
        if( null != cameraStream ) {
            var track = cameraStream.getTracks()[ 0 ];
            track.stop();
            stream.load();
            cameraStream = null;
        }
    })

    $("#captureCamera").on('click', function(){
        if( null != cameraStream ) {
            var ctx = capture.getContext( '2d' );
            var img = new Image();
            ctx.drawImage(stream, 0, 0, capture.width, capture.height );
            img.src		= capture.toDataURL( "image/png" );
            img.width	= 240;
            snapshot.innerHTML = '';
            snapshot.appendChild( img );
        }
    })
});

// Stop Streaming