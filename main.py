from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()

PapkaButton = QPushButtom("Папка")
LeftButton = QPushButton("Вліво")
RightButton = QPushButton("Вправо")
MirorButton = QPushButton("Дзеркало")
SharpnessButton = QPushButton("Різкість")
WhiteAndBlackButton = QPushButton("Ч/Б")
PapkaList = QListWidget()


window.show()
app.exec()