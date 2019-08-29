import requests
import json

class Photo:
    def __init__(self,d):
        self.__dict__ = d
    def __str__(self):
        result = ""
        for k,v in self.__dict__.items():
            result += f'{k} - {v}\n'
        return result


def getPhoto(photoID):
    resp = requests.get('http://jsonplaceholder.typicode.com/photos/' + str(photoID))
    if resp.status_code == 404:
        return "No picture at that ID"
    return Photo(json.loads(resp.content))

a = getPhoto(input('Enter a photo ID to retrieve: '))
print (a)
