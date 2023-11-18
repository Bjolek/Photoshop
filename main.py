from PIL import Image, ImageFilter
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import *
import os

app = QApplication([])
window = QWidget()
window.resize(800, 500)
mainLine = QHBoxLayout()

def pil2pixmap(im):
    if im.mode == "RGB":
        r, g, b = im.split()
        im = Image.merge("RGB", (b, g, r))
    elif im.mode == "RGBA":
        r, g, b, a = im.split()
        im = Image.merge("RGBA", (b, g, r, a))
    elif im.mode == "L":
        im = im.convert("RGBA")
    im2 = im.convert("RGBA")
    data = im2.tobytes("raw", "RGBA")
    qim = QImage(data, im.size[0], im.size[1], QImage.Format_ARGB32)
    pixmap = QPixmap.fromImage(qim)
    return pixmap

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
text = QListWidget()

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

class WorkPhoto:
    def __init__(self):
        self.image = None
        self.folder = None
        self.filename = None

    def load(self):
        imagePath = os.path.join(self.folder, self.filename)
        self.image = Image.open(imagePath)

    def showImage(self):
        pixel = pil2pixmap(self.image)
        pixel = pixel.scaled(800,600, Qt.KeepAspectRatio)
        windows7.setPixmap(pixel)

    def rotate_left(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        self.showImage()

    def rotate_right(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        self.showImage()

    def mirror(self):
        if self.image:
            self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
            self.showImage()

    def apply_sharpness(self):
        if self.image:
            factor = 2.0
            self.image = self.image.filter(ImageFilter.SHARPEN(factor))
            self.showImage()

    def convert_to_bw(self):
        if self.image:
            self.image = self.image.convert("L").convert("RGBA")
            self.showImage()




workwithphoto = WorkPhoto()


def open_folder():
    workwithphoto.folder=QFileDialog.getExistingDirectory()
    files = os.listdir(workwithphoto.folder)
    text.clear()
    text.addItems(files)

def showChosenImage():
    workwithphoto.filename = text.currentItem().text()
    workwithphoto.load()
    workwithphoto.showImage()

text.currentRowChanged.connect(showChosenImage)

mono1.clicked.connect(open_folder)
mono2.clicked.connect(workwithphoto.rotate_left)
mono3.clicked.connect(workwithphoto.rotate_right)
mono4.clicked.connect(workwithphoto.mirror)
mono5.clicked.connect(workwithphoto.apply_sharpness)
mono6.clicked.connect(workwithphoto.convert_to_bw)


window.setLayout(mainLine)

window.setLayout(mainLine)

window.show()
app.exec()