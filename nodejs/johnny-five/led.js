var raspi 	= require('raspi-io');
var five 	= require('johnny-five');
var board 	= new five.Board({
 	io: new raspi()
});

board.on('ready', function() {
	// Create an Led on pin 7 on P1 (GPIO4)
	// and strobe it on/off
	var led = new five.Led('P1-7');
	console.log(led);
	led.strobe(500);
});