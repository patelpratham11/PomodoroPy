from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
import sys


app = QApplication(sys.argv)
win = QMainWindow()
win.setGeometry(200, 200, 400, 400)
win.setWindowTitle("Test")
box = QCheckBox()
box.setCheckState(Qt.Checked)
box.stateChanged.connect(app.show_state)
app.setCentralWidget(box)

win.show()
sys.exit(app.exec_())
