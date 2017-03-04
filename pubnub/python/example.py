## ---------------------------------------------------
##
## YOU MUST HAVE A PUBNUB ACCOUNT TO USE THE API.
## http://www.pubnub.com/account
##
## ----------------------------------------------------

## --------------------------------------------------
## PubNub 3.0 Web Data Push Cloud-hosted API - PYTHON
## --------------------------------------------------
##
## www.pubnub.com - PubNub Web Data Push Service in the Cloud. 
## http://github.com/pubnub/pubnub-api/tree/master/python/
##
## PubNub is a Massively Scalable Data Push Service for Web and Mobile Games.
## This is a cloud-based service for broadcasting messages
## to thousands of web and mobile clients simultaneously.

## ---------------
## Python Push API
## ---------------
pubnub = Pubnub()

# -------
# PUBLISH
# -------
# Send Message
info = pubnub.publish({
    'channel' : 'hello_world',
    'message' : {
        'some_text' : 'Hello my World'
    }
})
print('info')
print(info)
print('')

# ---------
# SUBSCRIBE
# ---------
# Listen for Messages *BLOCKING*
def receive(message) :
    print(message)
    return True

pubnub.subscribe({
    'channel'  : 'hello_world',
    'callback' : receive 
})

# ------------------
## Channel Analytics
# ------------------
analytics = pubnub.analytics({
    'channel'  : 'hello_world', ## Leave blank for all channels
    'limit'    : 100,                 ## aggregation range
    'ago'      : 0,                   ## minutes ago to look backward
    'duration' : 100                  ## minutes offset
})
print('analytics')
print(analytics)
print('')

# -------
# HISTORY
# -------
# Load Previously Published Messages
history = pubnub.history({
    'channel' : 'hello_world',
    'limit'   : 1
})
print('history')
print(history)
print('')