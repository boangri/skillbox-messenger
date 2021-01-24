from PyQt5 import QtWidgets
import clientui


class Messenger(QtWidgets.QMainWindow, clientui.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


app = QtWidgets.QApplication([])
window = Messenger()
window.show()
app.exec()