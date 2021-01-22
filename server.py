from flask import Flask, request, abort
import time

app = Flask(__name__)

db = [
    {
        'time': time.time(),
        'name': 'Bob',
        'text': 'Hi everybody!'
    },
    {
        'time': time.time() + 100,
        'name': 'Alice',
        'text': 'Hello there!'
    }
]


@app.route('/')
def index():
    return 'hello world'


@app.route('/send', methods=['POST'])
def send_message():
    name = request.json.get('name')
    text = request.json.get('text')

    if not (isinstance(name, str) and isinstance(text, str) and name and text):
        abort(400)

    message = {
        'name': name,
        'text': text,
        'time': time.time()
    }
    db.append(message)
    return {'ok': True}


@app.route('/messages')
def get_messages():
    try:
        after = float(request.args.get('after', 0))
    except ValueError:
        return abort(400)
    messages = []
    for message in db:
        if message['time'] > after:
            messages.append(message)
    return {'messages': messages}


if __name__ == '__main__':
    app.run()
