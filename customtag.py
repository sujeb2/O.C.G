from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QRadioButton, QCheckBox, QMessageBox, QFileDialog, QLineEdit
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import Qt
from PyQt5 import QtCore
import os, sys, json;

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

# asdf
temp_loc = './src/template/default.js'
lowver = '2.0.0'
overlayer_loc = ''

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
            self.setWindowFlags(QtCore.Qt.WindowType.WindowCloseButtonHint | QtCore.Qt.WindowType.WindowMinimizeButtonHint)
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
            self.mainVersion = QLabel("v0.1.3", self)
            self.moduleListLabel = QLabel("모듈 목록", self)
            #self.scoreModuleStrictLevel = QLabel("판정", self)
            self.previewImage = QLabel("미리보기", self)
            self.deftextlabel = QLabel("텍스트 변경", self)
            self.previewText = QLabel("기본 텍스트", self)
            self.featureListLabel = QLabel("기능", self)

            # img label
            self.imglabelpreview = QLabel(self)

            # button
            self.saveBtn = QPushButton("저장하기", self)
            self.loadBtn = QPushButton("불러오기", self)

            # toggle
            self.module_acc = QCheckBox("정확도", self)
            self.module_xacc = QCheckBox("절대 정확도", self)
            self.module_progress = QCheckBox("진행도", self)
            self.module_startprgs = QCheckBox("시작 진행도", self)
            self.module_crb = QCheckBox("체감 BPM", self)
            self.module_tilebpm = QCheckBox("타일 BPM", self)
            self.module_reckps = QCheckBox("체감 KPS", self)
            self.module_score = QCheckBox("점수", self)
            self.randomPercentText = QCheckBox("랜덤한 확률로 텍스트 변경하기", self)

            # image
            self.previewImagePixmapTemplate = QPixmap('./src/img/preview/preview-text-template')

            # def img
            self.imglabelpreview.setPixmap(QPixmap(self.previewImagePixmapTemplate))
            
            # text edit
            self.deftext = QLineEdit(self)

            # reset btn/label position
            self.mainLabel1.move(15, 20)
            self.mainLabel2.move(15, 50)
            self.mainVersion.move(325, 50)
            self.moduleListLabel.move(15, 127)
            self.previewImage.move(510, 45)
            self.imglabelpreview.move(510, 75)
            self.deftextlabel.move(510, 305)
            self.previewText.move(520, 350)
            self.featureListLabel.move(15, 330)

            self.saveBtn.move(15, 90)
            self.loadBtn.move(95, 90)

            self.module_acc.move(15, 160)
            self.module_xacc.move(15, 180)
            self.module_crb.move(15, 200)
            self.module_progress.move(15, 220)
            self.module_reckps.move(15, 240)
            self.module_startprgs.move(15, 260)
            self.module_tilebpm.move(15, 280)
            self.module_score.move(15, 300)

            self.randomPercentText.move(15, 360)

            self.deftext.move(510, 325)
            
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

            featureListLabelFont = self.featureListLabel.font()
            featureListLabelFont.setFamily('Pretendard JP')
            featureListLabelFont.setPointSize(17)
            featureListLabelFont.setBold(True)

            versionLabelFont = self.mainVersion.font()
            versionLabelFont.setFamily('Pretendard JP')
            versionLabelFont.setPointSize(10)
            versionLabelFont.setBold(True)

            previewImageLabelFont = self.previewImage.font()
            previewImageLabelFont.setFamily('Pretendard JP')
            previewImageLabelFont.setPointSize(15)

            deftextlabelFont = self.deftextlabel.font()
            deftextlabelFont.setFamily('Pretendard JP')
            deftextlabelFont.setPointSize(12)

            previewTextFont = self.previewText.font()
            previewTextFont.setFamily('godoMaum')
            previewTextFont.setPointSize(30)

            savebtnFont = self.saveBtn.font()
            savebtnFont.setFamily('Pretendard JP')

            loadbtnFont = self.loadBtn.font()
            loadbtnFont.setFamily('Pretendard JP')

            # default font size = 13
            moduleToggleFont1 = self.module_acc.font()
            moduleToggleFont1.setFamily('Pretendard JP')
            moduleToggleFont1.setPointSize(13)

            moduleToggleFont2 = self.module_crb.font()
            moduleToggleFont2.setFamily('Pretendard JP')
            moduleToggleFont2.setPointSize(13)
            
            moduleToggleFont3 = self.module_progress.font()
            moduleToggleFont3.setFamily('Pretendard JP')
            moduleToggleFont3.setPointSize(13)

            moduleToggleFont4 = self.module_reckps.font()
            moduleToggleFont4.setFamily('Pretendard JP')
            moduleToggleFont4.setPointSize(13)

            moduleToggleFont5 = self.module_xacc.font()
            moduleToggleFont5.setFamily('Pretendard JP')
            moduleToggleFont5.setPointSize(13)

            moduleToggleFont6 = self.module_startprgs.font()
            moduleToggleFont6.setFamily('Pretendard JP')
            moduleToggleFont6.setPointSize(13)

            moduleToggleFont7 = self.module_tilebpm.font()
            moduleToggleFont7.setFamily('Pretendard JP')
            moduleToggleFont7.setPointSize(13)

            moduleToggleFont8 = self.module_score.font()
            moduleToggleFont8.setFamily('Pretendard JP')
            moduleToggleFont8.setPointSize(13)

            feature_randomPerText = self.randomPercentText.font()
            feature_randomPerText.setFamily('Pretendard JP')
            feature_randomPerText.setPointSize(12)

            # set font
            self.mainLabel1.setFont(mainLabelFont1)
            self.mainLabel2.setFont(mainLabelFont2)
            self.mainVersion.setFont(versionLabelFont)
            self.moduleListLabel.setFont(moduleListLabelFont)
            self.featureListLabel.setFont(featureListLabelFont)
            self.module_crb.setFont(moduleToggleFont2)
            self.module_acc.setFont(moduleToggleFont1)
            self.module_progress.setFont(moduleToggleFont3)
            self.module_reckps.setFont(moduleToggleFont4)
            self.module_xacc.setFont(moduleToggleFont5)
            self.module_startprgs.setFont(moduleToggleFont6)
            self.module_tilebpm.setFont(moduleToggleFont7)
            self.module_score.setFont(moduleToggleFont8)
            self.previewImage.setFont(previewImageLabelFont)
            self.deftextlabel.setFont(deftextlabelFont)
            self.previewText.setFont(previewTextFont)
            self.loadBtn.setFont(loadbtnFont)
            self.saveBtn.setFont(savebtnFont)
            self.randomPercentText.setFont(feature_randomPerText)

            # set clicked event
            self.saveBtn.clicked.connect(self.saveFile)
            self.loadBtn.clicked.connect(self.loadFile)
            self.module_acc.stateChanged.connect(self.changePreviewImgOnlyAcc)
            self.module_xacc.stateChanged.connect(self.changePreviewImgOnlyXAcc)
            self.deftext.textChanged.connect(self.textChange)
        except:
            self.close()
            print("[ERROR] An Error occurred while trying to load widgets.")
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print("[ERROR] Error type: ", exc_type, "Error File: " ,fname, "Error Line: " ,exc_tb.tb_lineno)

            errLoadWidget = QMessageBox.critical(self, '오류가 발생하였습니다.', '위젯을 설정 중에 오류가 발생하였습니다.\n보통 프로그램이 꼬였거나, 저장된 위치에 한글이 들어있으면 안되는 경우가 있습니다.\n만약 이 오류가 계속 발생할시에는 개발자에게 DM을 주십시오.', QMessageBox.Yes)
            self.setWindowTitle("Overlayer CustomTag Generator - 불안정함")

            if errLoadWidget == QMessageBox.Yes:
                self.close()

    def saveFile(self):
        print("saving...")
        #try:
        print(TOGGLED_ACC, TOGGLED_CRB, TOGGLED_PRGS, TOGGLED_RKPS, TOGGLED_STARTPRGS, TOGGLED_TB, TOGGLED_XACC)
        print("Checking Overlayer Version...")
        overCheckVer = QFileDialog.getOpenFileName(self, '오버레이어 파일 선택', './')

        if overCheckVer[0]:
            f = open(overCheckVer[0])

            with f:
                overlayer_loc = f.read()
                print(overlayer_loc)
            
            # uhhhhhhhhhhh

        with open(overlayer_loc) as overlayer_version:
            json_data = overlayer_version.read()

        overlayer_ver = json_data['Version']
        print(overlayer_ver)

        if(overlayer_ver < '2.0.0'):
            warnOverlayerVersion = QMessageBox.warning(self, '버전 확인', '현재 오버레이어 버전이 2.0.0 버전보다 더 낮은 버전을 사용하고 있습니다.\n이 프로그램은 오직 v2.0.0 버전 이상만 사용가능하며, 그 미만은 사용이 불가능 합니다', QMessageBox.Yes)
        else:
            saveFile = QFileDialog.getSaveFileName(self, '저장될 위치 선택', './')
        #except:
        #    print("ERROR Occurred!\nidk why it happend. sry about that :(")
        #    errSaveFile = QMessageBox.critical(self, '오류가 발생하였습니다.', '파일을 저장하는 중에 오류가 발생하였습니다.\n보통 프로그램이 꼬였거나, 저장된 위치에 한글이 들어있으면 안되는 경우가 있습니다.\n만약 이 오류가 계속 발생할시에는 개발자에게 DM을 주십시오.', QMessageBox.y)
        #    self.setWindowTitle("Overlayer CustomTag Generator - 불안정함")
        #    if errSaveFile == QMessageBox.Yes:
        #        self.close()

    def loadFile(self):
        print("loading...")
        try:
            warnLoadJSFormatVersion = QMessageBox.warning(self, '포맷 확인', '불려올려는 파일의 포맷이 2.0.0 이상의 버전보다 더 낮은 포맷을 사용하고 있습니다.\n이러한 포맷은 현재 불러올수가 없습니다.', QMessageBox.Yes)
        except:
            print("ERROR Occurred!\nidk why it happend. sry about that :(")
            errLoadFile = QMessageBox.critical(self, '오류가 발생하였습니다.', '파일을 불러오는 중에 오류가 발생하였습니다.\n보통 프로그램이 꼬였거나, 저장된 위치에 한글이 들어있으면 안되는 경우가 있습니다.\n만약 이 오류가 계속 발생할시에는 개발자에게 DM을 주십시오.', QMessageBox.y)
            self.setWindowTitle("Overlayer CustomTag Generator - 불안정함")
            if errLoadFile == QMessageBox.Yes:
                self.close()

    def changePreviewImgOnlyAcc(self, state):
        if state == Qt.Checked:
            self.imglabelpreview.setPixmap(QPixmap(self.previewImagePixmapOnlyAcc))
            TOGGLED_ACC = True
        else:
            print("toggled")

    def changePreviewImgOnlyXAcc(self, state):
        print("toggled")

    def changePreviewImgAccWXAcc(self, state):
        print("toggled")

    def checkOverlayerVersion(self):
        print("Checking...")

    def textChange(self):
        self.previewText.setText(str(self.deftext.text))

# run
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # load main window
    win = Main()
    win.setWidgets()
    win.show()
    app.exec_()