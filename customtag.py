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

class Main(QWidget):
    print("[INFO] 만약에 이 메세지가 보인다면, 현재 디버그용 .exe 를 사용하고 있습니다.\n[WARN] 이 프로젝트를 이용해서 개발을 할려는 목적이 아니라면, 'customtag-user.zip' 를 받아주세요.")

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
            print("[SUCCESS] Initallized.")
        except:
            print("ERROR Occurred!\nidk why it happend. sry about that :(")
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
            #self.scoreModuleStrictLevel = QLabel("판정", self)
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

            # set clicked event
            self.saveBtn.clicked.connect(self.saveFile)
            #self.loadBtn.clicked.connect(self.loadFile)
            self.mainLabel1.mouseDoubleClickEvent = self.showCopyright
            self.mainLabel2.mouseDoubleClickEvent = self.showCopyright
            self.module_acc.clicked.connect(self.changeAcc)
            print("[SUCCESS] Success.")
        except:
            self.close()
            print("[ERROR] An Error occurred while trying to load widgets.")
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print("[ERROR] Error type: ", exc_type, "Error File: " ,fname, "Error Line: " ,exc_tb.tb_lineno)

            errLoadWidget = QMessageBox.critical(self, '오류가 발생하였습니다.', '위젯을 설정 중에 오류가 발생하였습니다.\n보통 프로그램이 꼬였거나, 저장된 위치에 한글이 들어있으면 안되는 경우가 있습니다.\n만약 이 오류가 계속 발생할시에는 개발자에게 DM을 주십시오.')
            self.setWindowTitle("Overlayer CustomTag Generator - 불안정함")

    def saveFile(self):
        print("[INFO] Saving...")
        try:
            print(bool(toggled_Acc), toggled_Crb, toggled_Prgs, toggled_Rkps, toggled_StartedPrgs, toggled_Tb, toggled_Xacc)
            saveFile = QFileDialog.getSaveFileName(self, '저장될 위치 선택', './customtag.js', 'JavaScript (*.js)')

            if saveFile[0] != "":
                with open(saveFile[0], 'w', encoding="UTF-8") as svcustom:
                    # i know that this code is pretty weird :(
                    # def = svcustom.write("function ctg() {\n return `지정된 태그가 없습니다, 프로그램에서 지정후 저장해주세요.`;\n}\nRegisterTag('customTag', ctg, true);")

                    # acc
                    if toggled_Acc == True and toggled_Crb == False and toggled_Prgs == False and toggled_Rkps == False and toggled_StartedPrgs == False and toggled_Tb == False and toggled_Xacc == False:
                        svcustom.write("function ctg() {\nreturn `정확도: ${Accuracy()}%`\n}\nRegisterTag('customTag', ctg, true);")
                        print("[SUCCESS] Successfully saved file.")
                        print(f"[INFO] Saved file location: {saveFile}")
                    # progress
                    elif toggled_Acc == False and toggled_Crb == False and toggled_Prgs == True and toggled_Rkps == False and toggled_StartedPrgs == False and toggled_Tb == False and toggled_Xacc == False:
                        svcustom.write("function ctg() {\nreturn `진행도: ${Progress()}%`\n}\nRegisterTag('customTag', ctg, true);")
                        print("[SUCCESS] Successfully saved file.")
                        print(f"[INFO] Saved file location: {saveFile}")
                    # xacc
                    elif toggled_Acc == False and toggled_Crb == False and toggled_Prgs == False and toggled_Rkps == False and toggled_StartedPrgs == False and toggled_Tb == False and toggled_Xacc == True:
                        svcustom.write("function ctg() {\nreturn `절대 정확도: ${XAccuracy()}%`\n}\nRegisterTag('customTag', ctg, true);")
                        print("[SUCCESS] Successfully saved file.")
                        print(f"[INFO] Saved file location: {saveFile}")
                    # crb
                    elif toggled_Acc == False and toggled_Crb == True and toggled_Prgs == False and toggled_Rkps == False and toggled_StartedPrgs == False and toggled_Tb == False and toggled_Xacc == False:
                        svcustom.write("function ctg() {\nreturn `체감 BPM: ${CurBpm()}%`\n}\nRegisterTag('customTag', ctg, true);")
                        print("[SUCCESS] Successfully saved file.")
                        print(f"[INFO] Saved file location: {saveFile}")
                    else:
                        svcustom.write("function ctg() {\n return `지정된 태그가 없습니다, 프로그램에서 지정후 저장해주세요.`;\n}\nRegisterTag('customTag', ctg, true);")
                        print("[SUCCESS] Successfully saved file.")
                        print("[WARN] No module has been found. return with normal text.")
                        print(f"[INFO] Saved file location: {saveFile}")
                    successSaveFile = QMessageBox.information(self, '저장 완료', '태그가 저장되었습니다,\n오버레이어 설정에서 텍스트를 {customTag} 로 지정해주세요.')
        except:
            print("ERROR Occurred!\nidk why it happend. sry about that :(")
            errSaveFile = QMessageBox.critical(self, '오류가 발생하였습니다.', '파일을 저장하는 중에 오류가 발생하였습니다.\n보통 프로그램이 꼬였거나, 저장된 위치에 한글이 들어있으면 안되는 경우가 있습니다.\n만약 이 오류가 계속 발생할시에는 개발자에게 DM을 주십시오.')
            self.setWindowTitle("Overlayer CustomTag Generator - 불안정함")

    def loadFile(self):
        print("loading...")
        try:
            loadCustomTagfILE = QFileDialog.getOpenFileName(self, '태그 불러오기', './')
            warnLoadJSFormatVersion = QMessageBox.warning(self, '포맷 확인', '불려올려는 파일의 포맷이 2.0.0 이상의 버전보다 더 낮은 포맷을 사용하고 있습니다.\n이러한 포맷은 현재 불러올수가 없습니다.')
        except:
            print("ERROR Occurred!\nidk why it happend. sry about that :(")
            errLoadFile = QMessageBox.critical(self, '오류가 발생하였습니다.', '파일을 불러오는 중에 오류가 발생하였습니다.\n보통 프로그램이 꼬였거나, 저장된 위치에 한글이 들어있으면 안되는 경우가 있습니다.\n만약 이 오류가 계속 발생할시에는 개발자에게 DM을 주십시오.')
            self.setWindowTitle("Overlayer CustomTag Generator - 불안정함")

    def changeAcc(self):
        if self.module_acc.isChecked():
            toggled_Acc = not False
            self.previewText.setText = "정확도: 100%"
            print("[INFO] Acc module toggled.")
            print(f"[INFO] {toggled_Acc}")
        else:
            toggled_Acc = not True
            self.previewText.setText = "기본 텍스트"
            print("[INFO] Acc module deactivated.")
            print(f"[INFO] {toggled_Acc}")

    def showCopyright(self, event):
        showInfoWindow = infoWindow()
        showInfoWindow.show()

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
        
# run
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # load main window
    win = Main()
    win.setWidgets()
    win.show()
    app.exec()