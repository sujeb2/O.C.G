from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QRadioButton, QGroupBox, QCheckBox, QMessageBox
from PyQt5.QtGui import QIcon
import os, sys;

# accuracy
TOGGLED_ACC = False
TOGGLED_XACC = False

# bpm
TOGGLED_CRB = False
TOGGLED_TB = False
TOGGLED_RKPS = False

# progrss
TOGGLED_PRGS = False
TOGGLED_STARTPRGS = False

class Main(QWidget):
    def __init__(self):
        super().__init__()

        self.top = 200
        self.left = 500
        self.width = 1000
        self.height = 500

        # reset
        self.setWindowTitle("CustomTag Generator")
        self.setWindowIcon(QIcon('./src/icon.png'))
        self.setGeometry(self.left, self.top, self.width, self.height)
        self.resetWindow()

    def resetWindow(self):
        self.show

    def setWidgets(self):
        try:
            # label
            self.mainLabel1 = QLabel("OverLayer", self)
            self.mainLabel2 = QLabel("CustomTag Generator", self)
            self.mainVersion = QLabel("v1.0", self)

            # button
            self.saveBtn = QPushButton("저장하기", self)
            self.loadBtn = QPushButton("불러오기", self)

            # toggle
            module_acc = QCheckBox("정학도", self)
            module_xacc = QCheckBox("절대 정확도", self)
            module_progress = QCheckBox("진행도", self)
            module_startprgs = QCheckBox("시작 진행도", self)
            module_crb = QCheckBox("체감 BPM", self)
            module_tilebpm = QCheckBox("타일 BPM", self)
            module_reckps = QCheckBox("체감 KPS", self)

            # group
            self.groupTagSelectList = QGroupBox("태그 모듈 목록")
            
            # reset btn/label position
            self.mainLabel1.move(15, 20)
            self.mainLabel2.move(15, 50)
            self.mainVersion.move(340, 50)

            self.saveBtn.move(15, 90)
            self.loadBtn.move(95, 90)
            
            # font reset
            mainLabelFont1 = self.mainLabel1.font()
            mainLabelFont1.setPointSize(20)
            mainLabelFont2 = self.mainLabel2.font()
            mainLabelFont2.setPointSize(23)
            versionLabelFont = self.mainVersion.font()
            versionLabelFont.setBold(True)

            # set font
            self.mainLabel1.setFont(mainLabelFont1)
            self.mainLabel2.setFont(mainLabelFont2)
            self.mainVersion.setFont(versionLabelFont)

            # set clicked event
            self.saveBtn.clicked.connect(self.saveFile)
            self.loadBtn.clicked.connect(self.loadFile)
        except:
            self.close()
            print("ERROR Occurred!\nidk why it happend. sry about that :(")
            errLoadWidget = QMessageBox.critical(self, '오류가 발생하였습니다.', '위젯을 설정 중에 오류가 발생하였습니다.\n\n이 오류가 계속 발생할시에는 개발자에게 DM을 주십시오.', QMessageBox.Yes)

    def saveFile(self):
        print("saving...")
        print("ERROR Occurred!\nidk why it happend. sry about that :(")
        errSaveFile = QMessageBox.critical(self, '오류가 발생하였습니다.', '파일을 저장하는 중에 오류가 발생하였습니다.\n이 오류가 계속 발생할시에는 개발자에게 DM을 주십시오.', QMessageBox.y)
        
        if errSaveFile == QMessageBox.Yes:
            self.close()

    def loadFile(self):
        print("loading...")
        print("ERROR Occurred!\nidk why it happend. sry about that :(")
        errLoadFile = QMessageBox.critical(self, '오류가 발생하였습니다.', '파일을 불러오는 중에 오류가 발생하였습니다.\n이 오류가 계속 발생할시에는 개발자에게 DM을 주십시오.', QMessageBox.y)

        if errLoadFile == QMessageBox.Yes:
            self.close()

# run
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # load main window
    win = Main()
    win.setWidgets()
    win.show()
    app.exec_()