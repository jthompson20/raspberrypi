var v4l2camera = require("v4l2camera");
var cam = new v4l2camera.Camera("/dev/video0");

/*
if (cam.configGet().formatName !== "MJPG") {
  console.log("NOTICE: MJPG camera required");
  process.exit(1);
}
*/

cam.start();
cam.capture(function (success) {
	console.log('capturing..');
	var yuyv 	= cam.toYUYV();
	//console.log(yuyv);
	var frame 	= cam.frameRaw();
	//console.log(frame);
	require("fs").createWriteStream("result.jpg").end(Buffer(frame));
	cam.stop();
});