from PyQt5 import QtWidgets, QtCore
import clientui
import requests
from datetime import datetime


class Messenger(QtWidgets.QMainWindow, clientui.Ui_Dialog):
    def __init__(self, server_host):
        super().__init__()
        self.setupUi(self)
        self.server_host = server_host

        self.pushButton.pressed.connect(self.send_message)
        self.after = 0.
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.get_messages)
        self.timer.start(1000)

    def get_messages(self):
        try:
            response = requests.get(self.server_host + '/messages', params={'after': self.after})
        except:
            return

        messages = response.json()['messages']
        for message in messages:
            self.print_message(message)
            self.after = message['time']

    def print_message(self, message):
        time_ = datetime.fromtimestamp(message['time'])
        time_ = time_.strftime('%Y/%m/%d %H:%M')
        self.textBrowser.append(time_ + ' ' + message['name'])
        self.textBrowser.append(message['text'])
        self.textBrowser.append('')

    def send_message(self):
        name = self.lineEdit.text()
        text = self.textEdit.toPlainText()
        try:
            response = requests.post(self.server_host + '/send', json={
                'name': name,
                'text': text
            })
        except:
            self.textBrowser.append('Server is unreachable, try again later')
            self.textBrowser.append('')
            return
        if response.status_code != 200:
            self.textBrowser.append('Error while sending.')
            self.textBrowser.append('')
            return

        self.textEdit.setText('')



app = QtWidgets.QApplication([])
window = Messenger(server_host='http://localhost:8080')
window.show()
app.exec()