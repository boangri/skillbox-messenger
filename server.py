from flask import Flask, request, abort
import time
import os

app = Flask(__name__)

db = []


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
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
