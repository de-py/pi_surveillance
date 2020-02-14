from picamera import PiCamera
from time import sleep, strftime
import requests
from sec import token
import os

def take_picture():
    #Create file name for date and time
    file_name = strftime("%m-%d-%Y-%H-%-M-%S.jpg")
    camera = PiCamera()
    camera.resolution = (1024, 768)
    camera.start_preview()
    # Camera warm-up time
    sleep(2)
    camera.capture('./photos/%s' % file_name)
    return file_name

def upload_file(file_name):
    url = "https://content.dropboxapi.com/2/files/upload"
    headers = {
        'Authorization': 'Bearer ' + token,
        'Dropbox-API-Arg': (
            '{"path": "/%s",'
            '"mode": "add",'
            '"autorename": true,'
            '"mute": false,'
            '"strict_conflict": false'
            '}'
        % file_name),
        'Content-Type': 'application/octet-stream'

    }

    data = open('./photos/%s' % file_name, 'rb').read()


    # print(headers['Dropbox-API-Arg'])
    r = requests.post(url, headers=headers, data=data)

    print(r.text)

def delete_file(file_name):
    os.remove('./photos/%s' % file_name)

if __name__ == "__main__":
    file_name = take_picture()
    upload_file(file_name)    
    delete_file(file_name)