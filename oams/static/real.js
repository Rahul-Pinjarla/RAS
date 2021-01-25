// The buttons to start & stop stream and to capture the image
var btnStart = document.getElementById( "btn-start" );
var btnStop = document.getElementById( "btn-stop" );
var btnCapture = document.getElementById( "btn-capture" );

// The stream & capture
var stream = document.getElementById( "stream" );
var capture = document.getElementById( "capture" );
var snapshot = document.getElementById( "snapshot" );

// The video stream
var cameraStream = null;

// Attach listeners
btnStart.addEventListener( "click", startStreaming );
btnStop.addEventListener( "click", stopStreaming );

// Start Streaming
function startStreaming() {

	var mediaSupport = 'mediaDevices' in navigator;

	if( mediaSupport && null == cameraStream ) {

		navigator.mediaDevices.getUserMedia( { video: true } )
		.then( function( mediaStream ) {

			cameraStream = mediaStream;

			stream.srcObject = mediaStream;

			stream.play();
		})
		.catch( function( err ) {

			console.log( "Unable to access camera: " + err );
		});
	}
	else {

		alert( 'Your browser does not support media devices.' );

		return;
	}
}

// Stop Streaming
function stopStreaming() {

	if( null != cameraStream ) {

		var track = cameraStream.getTracks()[ 0 ];

		track.stop();
		stream.load();

		cameraStream = null;
	}
}

btnCapture.addEventListener( "click", captureSnapshot );

var script = document.createElement('script');
script.src = 'https://code.jquery.com/jquery-3.4.1.min.js';
script.type = 'text/javascript';
document.getElementsByTagName('head')[0].appendChild(script);

window.setInterval(captureSnapshot, 5000)

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function captureSnapshot() {

	if( null != cameraStream ) {

		var ctx = capture.getContext( '2d' );
		var img = new Image();

		ctx.drawImage( stream, 0, 0, capture.width, capture.height );

		img.src		= capture.toDataURL( "image/png" );
		img.width	= 240;

		snapshot.innerHTML = '';

		snapshot.appendChild( img );
		console.log(img)
		formdata = new FormData();	

		const csrftoken = getCookie('csrftoken');

		console.log(csrftoken)
		if (formdata) {
			formdata.append("face", img.src);
			formdata.append("csrfmiddlewaretoken", csrftoken)
			$.ajax({
				url: "facecam",
				type: "POST",
				data: formdata,
				processData: false,
				contentType: false,
				success:function(){
					console.log('success')	
				}
			});
		}	
	}
}


function dataURItoBlob( dataURI ) {

	var byteString = atob( dataURI.split( ',' )[ 1 ] );
	var mimeString = dataURI.split( ',' )[ 0 ].split( ':' )[ 1 ].split( ';' )[ 0 ];
	
	var buffer	= new ArrayBuffer( byteString.length );
	var data	= new DataView( buffer );
	
	for( var i = 0; i < byteString.length; i++ ) {
	
		data.setUint8( i, byteString.charCodeAt( i ) );
	}
	
	return new Blob( [ buffer ], { type: mimeString } );
}


// var request = new XMLHttpRequest();

// request.open( "POST", "/upload/url", true );

// var data	= new FormData();
// var dataURI	= snapshot.firstChild.getAttribute( "src" );
// var imageData   = dataURItoBlob( dataURI );

// data.append( "image", imageData, "myimage" );

// request.send( data );


// $.noConflict();	
// formdata = new FormData();		
// $("#image_to_upload").on("change", function() {
// 	var file = this.files[0];
// 	if (formdata) {
// 		formdata.append("image", file);
// 		$.ajax({
// 			url: "/student-attendence",
// 			type: "POST",
// 			data: formdata,
// 			processData: false,
// 			contentType: false,
// 			success:function(){}
// 		});
// 	}						
// });	