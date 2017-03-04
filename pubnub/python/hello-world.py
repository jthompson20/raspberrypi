import sys
from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
 
pnconfig = PNConfiguration()
 
pnconfig.subscribe_key  = 'sub-c-17b7db8a-3915-11e4-9868-02ee2ddab7fe'
pnconfig.publish_key    = 'pub-c-561a7378-fa06-4c50-a331-5c0056d0163c'
 
pubnub = PubNub(pnconfig)
 
 
def my_publish_callback(envelope, status):
    # Check whether request successfully completed or not
    if not status.is_error():
        print("successfully published")
        pass  # Message successfully published to specified channel.
    else:
        print("error")
        print(status)
        print('')
        pass  # Handle message publish error. Check 'category' property to find out possible issue
        # because of which request did fail.
        # Request can be resent using: [status retry];
 
 
class MySubscribeCallback(SubscribeCallback):
    def presence(self, pubnub, presence):
        print('incoming presence data')
        print(pubnub)
        print(presence)
        print('')
        pass  # handle incoming presence data
 
    def status(self, pubnub, status):
        if status.category == PNStatusCategory.PNUnexpectedDisconnectCategory:
            print('connectivity lost')
            pass  # This event happens when radio / connectivity is lost
 
        elif status.category == PNStatusCategory.PNConnectedCategory:
            # Connect event. You can do stuff like publish, and know you'll get it.
            # Or just use the connected event to confirm you are subscribed for
            # UI / internal notifications, etc
            pubnub.publish().channel("awesomeChannel").message("hello!!").async(my_publish_callback)
            print('published')
        elif status.category == PNStatusCategory.PNReconnectedCategory:
            print('connectivity lost again')
            pass
            # Happens as part of our regular operation. This event happens when
            # radio / connectivity is lost, then regained.
        elif status.category == PNStatusCategory.PNDecryptionErrorCategory:
            print('encryption error')
            pass
            # Handle message decryption error. Probably client configured to
            # encrypt messages and on live data feed it received plain text.
 
    def message(self, pubnub, message):
        print('new message')
        print(message)
        print('')
        pass  # Handle new message stored in message.message
 
 
try:
    pubnub.add_listener(MySubscribeCallback())
    pubnub.subscribe().channels('awesomeChannel').execute()
except KeyboardInterrupt:
    sys.exit()
finally:
    sys.exit()

