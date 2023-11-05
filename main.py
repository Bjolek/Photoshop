from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()
window.resize(800, 500)
mainLine = QHBoxLayout()
app.setStyleSheet("""
        QWidget {
            background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0.14 red, stop: 0.62 yellow,stop: 0.90 green);
        }
        QPushButton
        {
            background: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0.14 red, stop: 0.62 yellow,stop: 0.90 green);
            border-style: inset;
            font-family: Impact;
            min-width: 6em;
            padding: 6px;
        }
        
        QPushButton:hover {
            background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0.14 blue, stop: 0.62 purple,stop: 0.90 gold);
        }
        QTextEdit
        {
            background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0.14 red, stop: 0.62 yellow,stop: 0.90 green);

        }
        QTextEdit:hover {
            background-color: qlineargradient(x1: 0, y1: 0, x2: 1, y2: 1,stop: 0.14 blue, stop: 0.62 purple,stop: 0.90 gold);
        }
        
        
        
""")





Non = QHBoxLayout()
windows1 = QLabel("Папка")
windows2 = QLabel("Вліво")
windows3 = QLabel("Вправо")
windows4 = QLabel("Дзеркало")
windows5 = QLabel("Різкість")
windows6 = QLabel("Ч/Б")
windows7 = QLabel("Photo")

mono1 = QPushButton("Папка")
mono2 = QPushButton("Вліво")
mono3 = QPushButton("Вправо")
mono4 = QPushButton("Дзеркало")
mono5 = QPushButton("Різкість")
mono6 = QPushButton("Ч/Б")
text = QTextEdit()

Mon = QVBoxLayout()
Mon.addWidget(mono1)
Mon.addWidget(text)
mainLine.addLayout(Mon)
Mon1 = QVBoxLayout()
Mon1.addWidget(windows7)
Non = QHBoxLayout()
Non.addWidget(mono2)
Non.addWidget(mono3)
Non.addWidget(mono4)
Non.addWidget(mono5)
Non.addWidget(mono6)
Mon1.addLayout(Non)
mainLine.addLayout(Mon1)

window.setLayout(mainLine)

window.show()
app.exec()