import requests

name = input('Enter your name: ')

while True:
    text = input()
    requests.post('http://localhost:5000/send', json={
        'name': name,
        'text': text
    })
