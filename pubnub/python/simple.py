import pubnub#pubnub==4.0.2
import time
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub

pnconf = PNConfiguration()
pnconf.subscribe_key 	= "sub-c-17b7db8a-3915-11e4-9868-02ee2ddab7fe"
pnconf.publish_key 		= "pub-c-561a7378-fa06-4c50-a331-5c0056d0163c"
pubnub = PubNub(pnconf)

def show(msg, stat):
    if msg and stat: print( msg.timetoken, stat.status_code )
    else           : print( "Error", stat and stat.status_code )

while True:
    pubnub.publish().channel("eon-sensor-lsm9ds0").message(0).async(show)
    time.sleep(2)