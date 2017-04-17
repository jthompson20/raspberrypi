$(document).ready(function () {

  // new patient
  $('.patient').on('click',function(){
    phyZeo.patient.username   = $(this).data('username');
    phyZeo.patient.first      = $(this).data('first');
    phyZeo.patient.last       = $(this).data('last');

    $('#messageList').html('');
    doit();
  })


  function doit(){

    // init vars
    var chatChannel   = 'chat-' + phyZeo.patient.username + '-' + phyZeo.provider.username;

    // Initialize the PubNub API connection.
    var pubnub = PUBNUB.init({
      publish_key: 'pub-c-eec0c945-bc5d-4ec5-8531-e9bfeae4a6a4',
      subscribe_key: 'sub-c-4702e662-ad4b-11e6-b0d5-0619f8945a4f'
    });

    // Grab references for all of our elements.
    var messageContent = $('#messageContent'),
        sendMessageButton = $('#sendMessageButton'),
        messageList = $('#messageList');
   
    // Handles all the messages coming in from pubnub.subscribe.
    function handleMessage(message) {
      var messageEl = $("<li class='message'>"
          + "<span class='username'>" + message.username + ": </span>"
          + message.text
          + "</li>");
      messageEl.prependTo(messageList);
      //messageList.listview('refresh');
   
      // Scroll to bottom of page
      $("html, body").animate({ scrollTop: $(document).height() - $(window).height() }, 'slow');
    };
   
    // Compose and send a message when the user clicks our send message button.
    sendMessageButton.click(function (event) {
      var message = messageContent.val();
   
      if (message != '') {
        pubnub.publish({
          channel: chatChannel,
          message: {
            username: phyZeo.first + ' ' + phyZeo.last,
            text: message
          }
        });
   
        messageContent.val("");
      }
    });
   
    // Also send a message when the user hits the enter button in the text area.
    messageContent.bind('keydown', function (event) {
      if((event.keyCode || event.charCode) !== 13) return true;
      sendMessageButton.click();
      return false;
    });
   
    // Subscribe to messages coming in from the channel.
    pubnub.subscribe({
      channel: chatChannel,
      message: handleMessage
    });

    // see if anybody is here
    pubnub.here_now(
        {
            channel: [chatChannel],
            includeUUIDs: true,
            includeState: true
        }, 
        function (status) {
            // handle state setting response

            
        }
    );

    pubnub.history({
      channel: chatChannel,
      limit: 100
    }, function (messages) {
      messages = messages[0];
      messages = messages || [];

      for(var i = 0; i < messages.length; i++) {
        handleMessage(messages[i]);
      }

      $(document).scrollTop($(document).height());
    });

  }

  doit();
 
});