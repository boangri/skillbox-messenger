import requests

name = input('Enter your name: ')

while True:
    text = input()
    requests.post('http://docker-yc.xland.ru:5001/send', json={
        'name': name,
        'text': text
    })
