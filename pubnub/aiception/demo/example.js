<script src="https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js"></script>
<script>
$(document).ready(function(){
    // token
    token = ''

    img_url = 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Taylor_Swift_GMA_2012.jpg/330px-Taylor_Swift_GMA_2012.jpg'

    // 2. Let's find the approximate age of Taylor Swift from this image
    $.ajax({
        headers: {
            "Authorization": "Basic " + btoa(token + ":" + 'password is ignored')
        },
        type: "POST",
        url: "https://aiception.com/api/v2.1/face_age",
        contentType : 'application/json',
        dataType: 'json',
        // use stringify or else jquery will urlencode the data
        data: JSON.stringify({"image_url": img_url}),
        success: function(task_created, textStatus, jqXHR){

            // 2b. We receive a JSON response from aiception
            console.log("created task: ", task_created)

            // 3. Use the Location field to GET the age task
            age_task_url = task_created['Location'];

            // wait 2 seconds for aiception to complete the task
            setTimeout(function(){
                $.ajax({
                    headers: {
                        "Authorization": "Basic " + btoa(token + ":" + 'password is ignored')
                    },
                    type: "GET",
                    url: age_task_url,
                    contentType : 'application/json; charset=utf-8',
                    dataType: 'json',
                    success: function(task){

                        // 3b. We now have an answer with the age of Taylor Swift
                        alert(JSON.stringify(task));
                    }
                });
            }, 2000);
        }
    });
});
</script>