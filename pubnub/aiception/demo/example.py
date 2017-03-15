import requests
import time
from pprint import pprint

# 1. Get your API token from https://aiception.com/dashboard
token = 'eyJhbGciOiJIUzI1NiJ9.eyJpZCI6MjIsInRpbWUiOjE0ODk1MjcyNDguOTI4OTg2fQ.XLg6YyejL6U6EftpJwp9FxAoXtLdK2FRpw7A8_3Wwp4'

# 2. Let's find the approximate age of Taylor Swift from this image
r = requests.post('https://aiception.com/api/v2.1/face_age',
                  auth=(token, 'password is ignored'),
                  json={'image_url': 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/8f/Taylor_Swift_GMA_2012.jpg/330px-Taylor_Swift_GMA_2012.jpg'})

# 2b. The Response object r has a JSON response
print('Headers')
pprint(r.headers)

print('Server response to our POST request')
pprint(r.json())
# {'Location': 'https://aiception.com/api/v2.1/face_age/12', 'message': 'age task created'}

# The Location value is both in the headers and in the json body
age_task_url = r.headers['Location']
# age_task_url = r.json()['Location']  # is also fine


# wait 2 seconds for aiception to complete the task
time.sleep(2)

# 3. Use the Location to get the age task
r = requests.get(age_task_url, auth=(token, 'password is ignored'))

# 3b. We now have an answer with the age of Taylor Swift
print('Server response to our GET request')
pprint(r.json())
#{
#  "answer": "{'age': 23}",
#}