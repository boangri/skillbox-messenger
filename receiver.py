from time import sleep

import requests
from datetime import datetime


def print_message(mess):
    time_ = datetime.fromtimestamp(mess['time'])
    time_ = time_.strftime('%Y/%m/%d %H:%M')
    print(time_, mess['name'])
    print(mess['text'])
    print()


after = 0
while True:
    response = requests.get('http://localhost:5000/messages',
                            params={'after': after})
    data = response.json()
    for message in data['messages']:
        print_message(message)
        after = message['time']

    sleep(1)
