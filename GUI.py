import sys
import os
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class filedialogdemo(QWidget):

    def __init__(self, parent=None):
        super(filedialogdemo, self).__init__(parent)
        layout = QVBoxLayout()
        self.resize(300, 450)

        self.btn = QPushButton()
        self.btn.clicked.connect(self.loadFile)
        self.btn.setText("选择一张你喜欢的图片吧！")
        layout.addWidget(self.btn)
        self.btn_2 = QPushButton()
        self.btn_2.clicked.connect(self.on_click)
        self.btn_2.setText("猜猜它们是什么？")
        layout.addWidget(self.btn_2)

        self.label = QLabel()
        layout.addWidget(self.label)
        self.label_2 = QLabel()
        layout.addWidget(self.label_2)

        self.setWindowTitle("看图说话")

        self.setLayout(layout)

    def loadFile(self):
        print("load--file")
        global fname, _
        fname, _ = QFileDialog.getOpenFileName(self, '选择图片', './png/', 'Image files(*.jpg *.gif *.png)')
        pic = QPixmap(fname)
        self.label.setPixmap(pic)
        self.label.setScaledContents(True)



    def on_click(self):
        zname = str(fname)
        res = os.popen("python ./sample.py --image=" + zname).read()
        self.label_2.setText(str(res))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    fileload = filedialogdemo()
    fileload.show()
    sys.exit(app.exec_())
