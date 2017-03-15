# https://www.aiception.com/dashboard

# 2. Let's find the approximate age of Taylor Swift from this image
$ curl --user $TK: -X POST --data '{"image_url":"https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Taylor_Swift_GMA_2012.jpg/330px-Taylor_Swift_GMA_2012.jpg"}' https://aiception.com/api/v2.1/face_age

# 2b. We receive a JSON response from aiception
{
  "Location": "https://aiception.com/api/v2.1/face_age/12", 
  "message": "age task created"
}

# 3. Use the Location to get the age task
$ curl --user $TK: -X GET https://aiception.com/api/v2.1/face_age/12

# 3b. We now have an answer with the age of Taylor Swift
# (it isn't polite to ask a woman her age)
{
  "answer": "{'age': 23}", 
  ...
}

# 4. Go build an Application that uses the age recognizer and share it with us!