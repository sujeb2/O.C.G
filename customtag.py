import typing
from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QCheckBox, QMessageBox, QFileDialog
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6 import QtCore
import os, sys;

# accuracy
toggled_Acc = False
toggled_Xacc = False

# bpm
toggled_Crb = False
toggled_Tb = False
toggled_Rkps = False

# progrss
toggled_Prgs = False
toggled_StartedPrgs = False

class infoWindow(QWidget):
    # why tf this wont work
    def __init__(self, parent=None):
        super(infoWindow, self).__init__(parent)

        self.l = 200
        self.t = 500
        self.w = 500
        self.h = 300

        self.setWindowTitle("정보")
        self.setWindowFlags(QtCore.Qt.WindowType.WindowCloseButtonHint)
        self.setWindowIcon(QIcon('./src/icon_normal.png'))
        self.setGeometry(self.l, self.t, self.w, self.h)
        self.showNormal()
        self.show()

class randomTextEditWindow(QWidget):
    def __init__(self):
        try:
            super().__init__()

            self.l = 200
            self.t = 500
            self.w = 300
            self.h = 100

            self.setWindowTitle("랜덤 확률 수정")
            self.setWindowFlags(QtCore.Qt.WindowType.WindowCloseButtonHint)
            self.setWindowIcon(QIcon('./src/icon_normal.png'))
            self.setGeometry(self.l, self.t, self.w, self.h)
        except:
            print("ERROR Occurred!\nidk why it happend. sry about that :(")
            errShowrandTextEditWindowShow = QMessageBox.critical(self, '오류가 발생하였습니다.', '확률 수정 화면을 불러오는중에 오류가 발생했습니다.\n\n보통 프로그램이 꼬였거나, 저장된 위치에 한글이 있거나, 버그로 인해 안되는 경우가 있습니다.\n 계속 이러한 경우가 발생하는경우 Issue를 열어주세요.')
            self.setWindowTitle("Overlayer CustomTag Generator - 불안정함")

# color
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Main(QWidget):
    print(f"{bcolors.ENDC}[INFO] 만약에 이 메세지가 보인다면, 현재 디버그용 .exe 를 사용하고 있습니다.\n{bcolors.WARNING}[WARN] 이 프로젝트를 이용해서 개발을 할려는 목적이 아니라면, 'customtag-user.zip' 를 받아주세요.{bcolors.ENDC}")

    def __init__(self):
        print("[INFO] Initallizing...")
        try:
            super().__init__()

            self.top = 200
            self.left = 500
            self.width = 960
            self.height = 450

            # reset
            self.setWindowTitle("Overlayer CustomTag Generator")
            self.setWindowIcon(QIcon('./src/icon_normal.png'))
            self.setGeometry(self.left, self.top, self.width, self.height)
            self.resetWindow()
            self.setWindowFlags(QtCore.Qt.WindowType.WindowCloseButtonHint | QtCore.Qt.WindowType.WindowMinimizeButtonHint)
            print(f"{bcolors.OKCYAN}[SUCCESS] Initallized.{bcolors.ENDC}")
        except:
            print(F"{bcolors.FAIL}ERROR Occurred!\nidk why it happend. sry about that :({bcolors.ENDC}")
            errInit = QMessageBox.critical(self, '오류가 발생하였습니다.', '재설정을 하는 중에 오류가 발생했습니다.\n보통 프로그램이 꼬였거나, 저장된 위치에 한글이 들어있으면 안되는 경우가 있습니다.\n만약 이 오류가 계속 발생할시에는 개발자에게 DM을 주십시오.')
            self.setWindowTitle("Overlayer CustomTag Generator - 불안정함")

    def resetWindow(self):
        self.show

    def setWidgets(self):
        print("[INFO] Loading Widgets...")
        try:
            # label
            self.mainLabel1 = QLabel("OverLayer", self)
            self.mainLabel2 = QLabel("CustomTag Generator", self)
            self.mainVersion = QLabel("v0.2.5", self)
            self.moduleListLabel = QLabel("모듈 목록", self)
            self.previewImage = QLabel("미리보기", self)
            self.previewText = QLabel("기본 텍스트", self)
            self.featureListLabel = QLabel("기능", self)

            self.est = QLabel("와샌즈!", self)

            # img label
            self.imglabelpreview = QLabel(self)

            # button
            self.saveBtn = QPushButton("저장하기", self)
            #self.loadBtn = QPushButton("불러오기", self)

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
            self.setColorOnCertainPercent = QCheckBox("특정 지점에서 텍스트 색상 변경하기", self)

            if self.module_acc.text == "":
                self.module_acc.text == "ctg.module.acc"
            elif self.module_crb.text == "":
                self.module_crb.text == "ctg.module.crb"
            elif self.module_progress.text == "":
                self.module_progress.text == "ctg.module.progress"
            elif self.module_reckps.text == "":
                self.module_reckps.text == "ctg.module.module_reckps"
            elif self.module_score.text == "":
                self.module_score.text == "ctg.module.score"
            elif self.module_startprgs.text == "":
                self.module_startprgs.text == "ctg.module.startprgs"
            elif self.module_tilebpm.text == "":
                self.module_tilebpm.text == "ctg.module.tilebpm"
            elif self.module_xacc.text == "":
                self.module_startprgs.text == "ctg.module.xacc"
            elif self.randomPercentText.text == "":
                self.module_tilebpm.text == "ctg.feature.randomPercentText"

            self.previewText.raise_()
            self.previewText.setStyleSheet("Color : white")

            # image
            self.previewImagePixmapTemplate = QPixmap('./src/img/preview/preview-text-template')

            # def img
            self.imglabelpreview.setPixmap(QPixmap(self.previewImagePixmapTemplate))

            # reset btn/label position
            self.mainLabel1.move(15, 20)
            self.mainLabel2.move(15, 50)
            self.mainVersion.move(325, 50)
            self.moduleListLabel.move(15, 127)
            self.previewImage.move(510, 45)
            self.imglabelpreview.move(510, 75)
            self.previewText.move(520, 83)
            self.featureListLabel.move(15, 330)

            self.saveBtn.move(15, 90)
            #self.loadBtn.move(95, 90)

            self.est.move(100, 550)

            self.module_acc.move(15, 160)
            self.module_xacc.move(15, 180)
            self.module_crb.move(15, 200)
            self.module_progress.move(15, 220)
            self.module_reckps.move(15, 240)
            self.module_startprgs.move(15, 260)
            self.module_tilebpm.move(15, 280)
            self.module_score.move(15, 300)

            self.randomPercentText.move(15, 360)
            self.setColorOnCertainPercent.move(15, 380)
            
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

            previewTextFont = self.previewText.font()
            previewTextFont.setFamily('godoMaum')
            previewTextFont.setPointSize(30)

            savebtnFont = self.saveBtn.font()
            savebtnFont.setFamily('Pretendard JP')

            #loadbtnFont = self.loadBtn.font()
            #loadbtnFont.setFamily('Pretendard JP')

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
            
            feature_setColorOnCertainPercent = self.setColorOnCertainPercent.font()
            feature_setColorOnCertainPercent.setFamily('Pretendard JP')
            feature_setColorOnCertainPercent.setPointSize(12)

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
            self.previewText.setFont(previewTextFont)
            #self.loadBtn.setFont(loadbtnFont)
            self.saveBtn.setFont(savebtnFont)
            self.randomPercentText.setFont(feature_randomPerText)
            self.setColorOnCertainPercent.setFont(feature_setColorOnCertainPercent)

            # set clicked event
            self.saveBtn.clicked.connect(self.saveFile)
            #self.loadBtn.clicked.connect(self.loadFile)
            self.mainLabel1.mouseDoubleClickEvent = self.showCopyright
            self.mainLabel2.mouseDoubleClickEvent = self.showCopyright
            self.module_acc.clicked.connect(self.changeAcc)
            self.randomPercentText.clicked.connect(self.setRandom)
            print(f"{bcolors.OKCYAN}[SUCCESS] Success.{bcolors.ENDC}")
        except:
            self.close()
            print(f"{bcolors.FAIL}[ERROR] An Error occurred while trying to load widgets.{bcolors.ENDC}")
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(f"{bcolors.FAIL}[ERROR] Error type: ", exc_type, "Error File: " ,fname, "Error Line: " ,exc_tb.tb_lineno, f"{bcolors.ENDC}")

            errLoadWidget = QMessageBox.critical(self, '오류가 발생하였습니다.', '위젯을 설정 중에 오류가 발생하였습니다.\n보통 프로그램이 꼬였거나, 저장된 위치에 한글이 들어있으면 안되는 경우가 있습니다.\n만약 이 오류가 계속 발생할시에는 개발자에게 DM을 주십시오.')
            self.setWindowTitle("Overlayer CustomTag Generator - 불안정함")

    def saveFile(self):
        print("[INFO] Saving...")
        try:
            

            print(self.module_acc.isChecked(), self.module_crb.isChecked(), self.module_progress.isChecked(), self.module_reckps.isChecked(), self.module_progress.isChecked(), self.module_score.isChecked(), self.module_startprgs.isChecked(), self.module_xacc.isChecked())
            saveFile = QFileDialog.getSaveFileName(self, '저장될 위치 선택', './customtag.js', 'JavaScript (*.js)')

            if saveFile[0] != "":
                with open(saveFile[0], 'w', encoding="UTF-8") as svcustom:
                    # i know that this code is pretty weird :(
                    # def = svcustom.write("function ctg() {\n return `지정된 태그가 없습니다, 프로그램에서 지정후 저장해주세요.`;\n}\nRegisterTag('customTag', ctg, true);")

                    # acc
                    if self.module_acc.isChecked() == True and self.module_crb.isChecked() == False and self.module_progress.isChecked() == False and self.module_reckps.isChecked() == False and self.module_score.isChecked() == False and self.module_startprgs.isChecked() == False and self.module_tilebpm.isChecked() == False and self.module_xacc.isChecked() == False:
                        svcustom.write("function ctg() {\nreturn `정확도: ${Accuracy()}%`\n}\nRegisterTag('customTag', ctg, true);")
                        print(f"{bcolors.OKCYAN}[SUCCESS] Successfully saved file.{bcolors.ENDC}")
                        print(f"[INFO] Saved file location: {saveFile}")
                    # progress
                    elif self.module_acc.isChecked() == False and self.module_crb.isChecked() == False and self.module_progress.isChecked() == True and self.module_reckps.isChecked() == False and self.module_score.isChecked() == False and self.module_startprgs.isChecked() == False and self.module_tilebpm.isChecked() == False and self.module_xacc.isChecked() == False:
                        svcustom.write("function ctg() {\nreturn `진행도: ${Progress()}%`\n}\nRegisterTag('customTag', ctg, true);")
                        print(f"{bcolors.OKCYAN}[SUCCESS] Successfully saved file.{bcolors.ENDC}")
                        print(f"[INFO] Saved file location: {saveFile}")
                    # xacc
                    elif self.module_acc.isChecked() == False and self.module_crb.isChecked() == False and self.module_progress.isChecked() == False and self.module_reckps.isChecked() == False and self.module_score.isChecked() == False and self.module_startprgs.isChecked() == False and self.module_tilebpm.isChecked() == False and self.module_xacc.isChecked() == True:
                        svcustom.write("function ctg() {\nreturn `절대 정확도: ${XAccuracy()}%`\n}\nRegisterTag('customTag', ctg, true);")
                        print(f"{bcolors.OKCYAN}[SUCCESS] Successfully saved file.{bcolors.ENDC}")
                        print(f"[INFO] Saved file location: {saveFile}")
                    # crb
                    elif self.module_acc.isChecked() == False and self.module_crb.isChecked() == True and self.module_progress.isChecked() == False and self.module_reckps.isChecked() == False and self.module_score.isChecked() == False and self.module_startprgs.isChecked() == False and self.module_tilebpm.isChecked() == False and self.module_xacc.isChecked() == False:
                        svcustom.write("function ctg() {\nreturn `체감 BPM: ${CurBpm()}%`\n}\nRegisterTag('customTag', ctg, true);")
                        print(f"{bcolors.OKCYAN}[SUCCESS] Successfully saved file.{bcolors.ENDC}")
                        print(f"[INFO] Saved file location: {saveFile}")
                    elif self.module_acc.isChecked() == False and self.module_crb.isChecked() == False and self.module_progress.isChecked() == False and self.module_reckps.isChecked() == False and self.module_score.isChecked() == True and self.module_startprgs.isChecked() == False and self.module_tilebpm.isChecked() == False and self.module_xacc.isChecked() == False:
                        svcustom.write("function ctg() {\nreturn `점수: ${Score()}%`\n}\nRegisterTag('customTag', ctg, true);")
                        print(f"[{bcolors.OKCYAN}SUCCESS] Successfully saved file.{bcolors.ENDC}")
                        print(f"[INFO] Saved file location: {saveFile}")
                    elif self.module_acc.isChecked() == True and self.module_crb.isChecked() == True and self.module_progress.isChecked() == True and self.module_reckps.isChecked() == True and self.module_score.isChecked() == True and self.module_startprgs.isChecked() == True and self.module_tilebpm.isChecked() == True and self.module_xacc.isChecked() == True:
                        svcustom.write("function ctg() {\nreturn `정확도: ${Accuracy()}%\n진행도: ${Progress()}%\n절대 정확도: ${XAccuracy()}%\n체감 BPM: ${CurBpm()}%\n점수: ${Score()}%\n시작 진행도`\n}\nRegisterTag('customTag', ctg, true);")
                        print(f"{bcolors.OKCYAN}[SUCCESS] Successfully saved file.{bcolors.ENDC}")
                        print(f"[INFO] Saved file location: {saveFile}")
                    # default
                    else:
                        svcustom.write("function ctg() {\n return `지정된 태그가 없습니다, 프로그램에서 지정후 저장해주세요.`;\n}\nRegisterTag('customTag', ctg, true);")
                        print(f"{bcolors.OKCYAN}[SUCCESS] Successfully saved file.{bcolors.ENDC}")
                        print(f"{bcolors.WARNING}[WARN] No module has been found. return with normal text.{bcolors.ENDC}")
                        print(f"[INFO] Saved file location: {saveFile}")
                    successSaveFile = QMessageBox.information(self, '저장 완료', '태그가 저장되었습니다,\n오버레이어 설정에서 텍스트를 {customTag} 로 지정해주세요.')
        except:
            print(f"{bcolors.FAIL}ERROR Occurred!\nidk why it happend. sry about that :({bcolors.ENDC}")
            errSaveFile = QMessageBox.critical(self, '오류가 발생하였습니다.', '파일을 저장하는 중에 오류가 발생하였습니다.\n보통 프로그램이 꼬였거나, 저장된 위치에 한글이 들어있으면 안되는 경우가 있습니다.\n만약 이 오류가 계속 발생할시에는 개발자에게 DM을 주십시오.')
            self.setWindowTitle("Overlayer CustomTag Generator - 불안정함")

    def loadFile(self):
        print("loading...")
        try:
            loadCustomTagFile = QFileDialog.getOpenFileName(self, '태그 불러오기', './')
            warnLoadJSFormatVersion = QMessageBox.warning(self, '포맷 확인', '불려올려는 파일의 포맷이 2.0.0 이상의 버전보다 더 낮은 포맷을 사용하고 있습니다.\n이러한 포맷은 현재 불러올수가 없습니다.')
        except:
            print(f"{bcolors.FAIL}ERROR Occurred!\nidk why it happend. sry about that :({bcolors.ENDC}")
            errLoadFile = QMessageBox.critical(self, '오류가 발생하였습니다.', '파일을 불러오는 중에 오류가 발생하였습니다.\n보통 프로그램이 꼬였거나, 저장된 위치에 한글이 들어있으면 안되는 경우가 있습니다.\n만약 이 오류가 계속 발생할시에는 개발자에게 DM을 주십시오.')
            self.setWindowTitle("Overlayer CustomTag Generator - 불안정함")

    def changeAcc(self):
        if self.module_acc.isChecked():
            self.previewText.setText = "정확도: 100%"
        else:
            self.previewText.setText = "기본 텍스트"

    def showCopyright(self, event):
        showInfoWindow = infoWindow()
        showInfoWindow.show()

    def setRandom(self):
        showRandomPerEditWindow = randomTextEditWindow()
        showRandomPerEditWindow.show()
        return showRandomPerEditWindow
        
# run
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # load main window
    win = Main()
    win.setWidgets()
    win.show()
    app.exec()