/**
 * Produce a stream of random data on the channel: random1
 */
var PubNub = require('pubnub');

var pubnub = new PubNub({
    publishKey   : "pub-c-561a7378-fa06-4c50-a331-5c0056d0163c",
    subscribeKey : "sub-c-17b7db8a-3915-11e4-9868-02ee2ddab7fe"
});

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