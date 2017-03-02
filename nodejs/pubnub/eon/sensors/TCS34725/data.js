var PubNub = require('pubnub');
var rgbLib = require('TCS34725');

// init pubnub
var pubnub = new PubNub({
    publishKey   : "pub-c-561a7378-fa06-4c50-a331-5c0056d0163c",
    subscribeKey : "sub-c-17b7db8a-3915-11e4-9868-02ee2ddab7fe"
});

// init RGB class
var rgb = rgbLib.use({ 
  "bus"     : "/dev/i2c-1", 
  //"led_pin" : "P8_14", 
  //"irq_pin" : "P8_26",
  "module_id" : 0x29
});

rgb.on('ready', function() {
  
  setInterval(function() {
    rgb.getRawData(function(err, colors) {
      
      if (err) throw err;

      console.log('RED:', colors.red);
      console.log('GREEN:', colors.green);
      console.log('BLUE:', colors.blue);
      console.log('CLEAR:', colors.clear);
    });
    
  }, 1000);



/*
var number = 100;
function publish() {
    number += (Math.random() - 0.5);
    var message = { eon: {"value" : number} };
    console.log("sending",message);
    pubnub.publish({
        channel   : 'example-eon',
        message   : message,
    });
}
setInterval(publish,3*1000); //every three seconds
*/