from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QRadioButton, QCheckBox, QMessageBox
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

# template loc
temp_loc = './src/template/default.js'

class Main(QWidget):
    def __init__(self):
        try:
            super().__init__()

            self.top = 200
            self.left = 500
            self.width = 1000
            self.height = 500

            # reset
            self.setWindowTitle("Overlayer CustomTag Generator")
            self.setWindowIcon(QIcon('./src/icon_normal.png'))
            self.setGeometry(self.left, self.top, self.width, self.height)
            self.resetWindow()
        except:
            print("ERROR Occurred!\nidk why it happend. sry about that :(")
            errInit = QMessageBox.critical(self, '오류가 발생하였습니다.', '재설정을 하는 중에 오류가 발생했습니다.\n보통 프로그램이 꼬였거나, 저장된 위치에 한글이 들어있으면 안되는 경우가 있습니다.\n만약 이 오류가 계속 발생할시에는 개발자에게 DM을 주십시오.', QMessageBox.y)
            self.setWindowTitle("Overlayer CustomTag Generator - 불안정함")
            if errInit == QMessageBox.Yes:
                self.close()

    def resetWindow(self):
        self.show

    def setWidgets(self):
        try:
            # label
            self.mainLabel1 = QLabel("OverLayer", self)
            self.mainLabel2 = QLabel("CustomTag Generator", self)
            self.mainVersion = QLabel("v0.1.2", self)
            self.moduleListLabel = QLabel("모듈 목록", self)

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
            
            # reset btn/label position
            self.mainLabel1.move(15, 20)
            self.mainLabel2.move(15, 50)
            self.mainVersion.move(325, 50)
            self.moduleListLabel.move(15, 127)

            self.saveBtn.move(15, 90)
            self.loadBtn.move(95, 90)

            module_acc.move(15, 160)
            module_xacc.move(15, 180)
            module_crb.move(15, 200)
            module_progress.move(15, 220)
            module_reckps.move(15, 240)
            module_startprgs.move(15, 260)
            module_tilebpm.move(15, 280)
            
            # font reset
            mainLabelFont1 = self.mainLabel1.font()
            mainLabelFont1.setPointSize(20)
            mainLabelFont1.setFamily('Pretendard Variable')

            mainLabelFont2 = self.mainLabel2.font()
            mainLabelFont2.setPointSize(23)
            mainLabelFont2.setFamily('Pretendard Variable')

            moduleListLabelFont = self.moduleListLabel.font()
            moduleListLabelFont.setFamily('Pretendard JP')
            moduleListLabelFont.setPointSize(17)
            moduleListLabelFont.setBold(True)

            versionLabelFont = self.mainVersion.font()
            versionLabelFont.setFamily('Pretendard JP')
            versionLabelFont.setPointSize(10)
            versionLabelFont.setBold(True)

            # default font size = 13
            moduleToggleFont1 = module_acc.font()
            moduleToggleFont1.setFamily('Pretendard JP')
            moduleToggleFont1.setPointSize(13)

            moduleToggleFont2 = module_crb.font()
            moduleToggleFont2.setFamily('Pretendard JP')
            moduleToggleFont2.setPointSize(13)
            
            moduleToggleFont3 = module_progress.font()
            moduleToggleFont3.setFamily('Pretendard JP')
            moduleToggleFont3.setPointSize(13)

            moduleToggleFont4 = module_reckps.font()
            moduleToggleFont4.setFamily('Pretendard JP')
            moduleToggleFont4.setPointSize(13)

            moduleToggleFont5 = module_xacc.font()
            moduleToggleFont5.setFamily('Pretendard JP')
            moduleToggleFont5.setPointSize(13)

            moduleToggleFont6 = module_startprgs.font()
            moduleToggleFont6.setFamily('Pretendard JP')
            moduleToggleFont6.setPointSize(13)

            moduleToggleFont7 = module_tilebpm.font()
            moduleToggleFont7.setFamily('Pretendard JP')
            moduleToggleFont7.setPointSize(13)

            # set font
            self.mainLabel1.setFont(mainLabelFont1)
            self.mainLabel2.setFont(mainLabelFont2)
            self.mainVersion.setFont(versionLabelFont)
            self.moduleListLabel.setFont(moduleListLabelFont)
            module_crb.setFont(moduleToggleFont2)
            module_acc.setFont(moduleToggleFont1)
            module_progress.setFont(moduleToggleFont3)
            module_reckps.setFont(moduleToggleFont4)
            module_xacc.setFont(moduleToggleFont5)
            module_startprgs.setFont(moduleToggleFont6)
            module_tilebpm.setFont(moduleToggleFont7)

            # set clicked event
            self.saveBtn.clicked.connect(self.saveFile)
            self.loadBtn.clicked.connect(self.loadFile)
        except:
            self.close()
            print("ERROR Occurred!\nidk why it happend. sry about that :(")
            errLoadWidget = QMessageBox.critical(self, '오류가 발생하였습니다.', '위젯을 설정 중에 오류가 발생하였습니다.\n보통 프로그램이 꼬였거나, 저장된 위치에 한글이 들어있으면 안되는 경우가 있습니다.\n만약 이 오류가 계속 발생할시에는 개발자에게 DM을 주십시오.', QMessageBox.Yes)
            self.setWindowTitle("Overlayer CustomTag Generator - 불안정함")

            if errLoadWidget == QMessageBox.Yes:
                self.close()

    def saveFile(self):
        print("saving...")
        try:
            print("hi")
        except:
            print("ERROR Occurred!\nidk why it happend. sry about that :(")
            errSaveFile = QMessageBox.critical(self, '오류가 발생하였습니다.', '파일을 저장하는 중에 오류가 발생하였습니다.\n보통 프로그램이 꼬였거나, 저장된 위치에 한글이 들어있으면 안되는 경우가 있습니다.\n만약 이 오류가 계속 발생할시에는 개발자에게 DM을 주십시오.', QMessageBox.y)
            self.setWindowTitle("Overlayer CustomTag Generator - 불안정함")
            if errSaveFile == QMessageBox.Yes:
                self.close()

    def loadFile(self):
        print("loading...")
        print("ERROR Occurred!\nidk why it happend. sry about that :(")
        errLoadFile = QMessageBox.critical(self, '오류가 발생하였습니다.', '파일을 불러오는 중에 오류가 발생하였습니다.\n보통 프로그램이 꼬였거나, 저장된 위치에 한글이 들어있으면 안되는 경우가 있습니다.\n만약 이 오류가 계속 발생할시에는 개발자에게 DM을 주십시오.', QMessageBox.y)
        self.setWindowTitle("Overlayer CustomTag Generator - 불안정함")
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