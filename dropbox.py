import requests
from sec import token

url = "https://content.dropboxapi.com/2/files/upload"
headers = {
    'Authorization': 'Bearer ' + token,
    'Dropbox-API-Arg': (
        '{"path": "/test.jpg",'
        '"mode": "add",'
        '"autorename": true,'
        '"mute": false,'
        '"strict_conflict": false'
        '}'
    ),
    'Content-Type': 'application/octet-stream'

}

data = open('foo.jpg', 'rb').read()


# print(headers['Dropbox-API-Arg'])
r = requests.post(url, headers=headers, data=data)

print(r.text)
