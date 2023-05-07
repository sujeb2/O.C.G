from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QCheckBox, QMessageBox, QFileDialog, QLineEdit
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6 import QtCore
import os, sys;

# j
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

VER = '0.2.8==dev'

class InfoWindow(QWidget):
    def __init__(self):
        print("[INFO] Initallizing infoWindow...")
        try:
            super().__init__()

            self.top = 200
            self.left = 500
            self.width = 400
            self.height = 200

            self.setWindowTitle("정보")
            self.setWindowIcon(QIcon('./src/icon_normal.png'))
            self.setGeometry(self.left, self.top, self.width, self.height)
            self.setWindowFlags(QtCore.Qt.WindowType.WindowCloseButtonHint | QtCore.Qt.WindowType.WindowMinimizeButtonHint)
            self.setWidgets()
            print(f"{bcolors.OKCYAN}[SUCCESS] Initallized.{bcolors.ENDC}")
        except:
            print(F"{bcolors.FAIL}ERROR Occurred!\nidk why it happend. sry about that :({bcolors.ENDC}")
            errInfoWinInit = QMessageBox.critical(self, '오류가 발생하였습니다.', '재설정을 하는 중에 오류가 발생했습니다.\n보통 프로그램이 꼬였거나, 저장된 위치에 한글이 들어있으면 안되는 경우가 있습니다.\n만약 이 오류가 계속 발생할시에는 개발자에게 DM을 주십시오.')
            self.setWindowTitle("정보 - 불안정함")

    def setWidgets(self):
        print("[INFO] Loading Widgets...")
        try:
            overlayerUrlLink="<a href=\"https://overlayer.notion.site/overlayer/Overlayer-Knowledge-Base-a06a2947f8bd44e098189a9d3c28ac49\">Overlayer Knowledge Base</a>"
            csharpdiscord="<a href=\"https://discord.gg/duwPWhFcxx\">C## Discord Server (Not me!)</a>"

            # info label
            self.infoMainLabel = QLabel("OverLayer", self)
            self.infoMainLabel2 = QLabel("CustomTag Generator", self)

            self.madebysans = QLabel("Made by. songro_", self)

            self.ctgLogo = QLabel(self)

            self.infoOverlayerKnowledgeLabel = QLabel(overlayerUrlLink, self)
            #self.infoCSharpSharpDiscordLabel = QLabel(csharpdiscord, self)

            self.ctgLogoPixmap = QPixmap('./src/icon_normal-resized')

            # move/set font
            self.infoMainLabel.move(70, 40)
            self.infoMainLabel2.move(70, 75)
            self.infoOverlayerKnowledgeLabel.move(70, 145)
            #self.infoCSharpSharpDiscordLabel.move(70, 165)
            self.madebysans.move(70, 115)
            self.ctgLogo.move(10, 65)

            infoLabelFont1 = self.infoMainLabel.font()
            infoLabelFont1.setFamily('Pretendard Variable')
            infoLabelFont1.setPointSize(20)

            infoLabelFont2 = self.infoMainLabel2.font()
            infoLabelFont2.setFamily('Pretendard Variable')
            infoLabelFont2.setPointSize(23)

            infoOverLayerLinkFont = self.infoOverlayerKnowledgeLabel.font()
            infoOverLayerLinkFont.setFamily('Pretendard Variable')
            infoOverLayerLinkFont.setPointSize(10)

            #infoCSharpDiscordLinkFont = self.infoCSharpSharpDiscordLabel.font()
            #infoCSharpDiscordLinkFont.setFamily('Pretendard Variable')

            madebysansfont = self.madebysans.font()
            madebysansfont.setFamily('Pretendard Variable')
            madebysansfont.setPointSize(13)

            ctgLogoFont = self.ctgLogo.font()
            ctgLogoFont.setPointSize(10)

            self.infoMainLabel.setFont(infoLabelFont1)
            self.infoMainLabel2.setFont(infoLabelFont2)
            #self.infoCSharpSharpDiscordLabel.setFont(infoCSharpDiscordLinkFont)
            self.infoOverlayerKnowledgeLabel.setFont(infoOverLayerLinkFont)
            self.madebysans.setFont(madebysansfont)
            self.ctgLogo.setFont(ctgLogoFont)

            self.infoOverlayerKnowledgeLabel.setOpenExternalLinks(True)
            #self.infoCSharpSharpDiscordLabel.setOpenExternalLinks(True)

            self.ctgLogo.setPixmap(self.ctgLogoPixmap)

        except:
            self.close()
            print(f"{bcolors.FAIL}[ERROR] An Error occurred while trying to load widgets.{bcolors.ENDC}")
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(f"{bcolors.FAIL}[ERROR] Error type: ", exc_type, "Error File: " ,fname, "Error Line: " ,exc_tb.tb_lineno, f"{bcolors.ENDC}")

            errLoadWidget = QMessageBox.critical(self, '오류가 발생하였습니다.', '위젯을 설정 중에 오류가 발생하였습니다.\n보통 프로그램이 꼬였거나, 저장된 위치에 한글이 들어있으면 안되는 경우가 있습니다.\n만약 이 오류가 계속 발생할시에는 개발자에게 DM을 주십시오.')
            self.setWindowTitle("Overlayer CustomTag Generator - 불안정함")
        print(f"[INFO] Current Window Width {self.width}, Height {self.height}")

class EditRandomPercent(QWidget):
    def __init__(self):
        print("[INFO] Initallizing EditWindow...")
        try:
            super().__init__()

            self.top = 200
            self.left = 500
            self.width = 300
            self.height = 125

            self.setWindowTitle("확률 수정")
            self.setWindowIcon(QIcon('./src/icon_edit.png'))
            self.setGeometry(self.left, self.top, self.width, self.height)
            self.setWindowFlags(QtCore.Qt.WindowType.WindowCloseButtonHint | QtCore.Qt.WindowType.WindowMinimizeButtonHint)
            self.setWidgets()
            print(f"{bcolors.OKCYAN}[SUCCESS] Initallized.{bcolors.ENDC}")
        except:
            print(F"{bcolors.FAIL}ERROR Occurred!\nidk why it happend. sry about that :({bcolors.ENDC}")
            errInitWin2 = QMessageBox.critical(self, '오류가 발생하였습니다.', '재설정을 하는 중에 오류가 발생했습니다.\n보통 프로그램이 꼬였거나, 저장된 위치에 한글이 들어있으면 안되는 경우가 있습니다.\n만약 이 오류가 계속 발생할시에는 개발자에게 DM을 주십시오.')
            self.setWindowTitle("확률 수정 - 불안정함")

    def setWidgets(self):
        print("[INFO] Loading Widgets...")
        try:
            self.editTitle = QLabel("확률 수정", self)
            
            self.activatePercent = QLineEdit("", self)
            self.startText = QLineEdit("", self)
            self.customText1 = QLineEdit("", self)
            self.customText2 = QLineEdit("", self)

            self.doneBtn = QPushButton("확인", self)

            self.editTitle.move(15, 5)

            self.activatePercent.move(15, 45)
            self.startText.move(156, 45)
            self.customText1.move(15, 72)
            self.customText2.move(156, 72)
            self.doneBtn.move(215, 97)

            editTitleFont = self.editTitle.font()
            editTitleFont.setFamily('Pretendard Variable')
            editTitleFont.setPointSize(20)

            self.editTitle.setFont(editTitleFont)

            self.doneBtn.clicked.connect(self.done)

            self.activatePercent.setPlaceholderText("100")
            self.startText.setPlaceholderText("시작 텍스트")
            self.customText1.setPlaceholderText("텍스트 1")
            self.customText2.setPlaceholderText("텍스트 2")
            print(f"{bcolors.OKCYAN}[SUCCESS] Loaded.{bcolors.ENDC}")
        except:
            print(F"{bcolors.FAIL}ERROR Occurred!\nidk why it happend. sry about that :({bcolors.ENDC}")
            errWidgetSetupWin2 = QMessageBox.critical(self, '오류가 발생하였습니다.', '위젯을 설정 중에 오류가 발생하였습니다.\n보통 프로그램이 꼬였거나, 저장된 위치에 한글이 들어있으면 안되는 경우가 있습니다.\n만약 이 오류가 계속 발생할시에는 개발자에게 DM을 주십시오.')
            self.setWindowTitle("확률 수정 - 불안정함")

    def done(self):
        print("[INFO] Saving info..")
        try:
            self.activatePer = self.activatePercent.text()
            self.startTxt = self.startText.text()
            self.text1 = self.customText1.text()
            self.text2 = self.customText2.text()
            print(f"{bcolors.OKCYAN}[SUCCESS] Saved.{bcolors.ENDC}")
            print(f"[INFO] {self.activatePer}, {self.startTxt}, {self.text1}, {self.text2}")
        except:
            print(F"{bcolors.FAIL}ERROR Occurred!\nidk why it happend. sry about that :({bcolors.ENDC}")
            errWidgetSetupWin2 = QMessageBox.critical(self, '오류가 발생하였습니다.', '설정을 저장하는중에 오류가 발생하였습니다.\n보통 프로그램이 꼬였거나, 저장된 위치에 한글이 들어있으면 안되는 경우가 있습니다.\n만약 이 오류가 계속 발생할시에는 개발자에게 DM을 주십시오.')
            self.setWindowTitle("확률 수정 - 불안정함")
        self.close()

class Main(QWidget):
    print(f"{bcolors.ENDC}[INFO] 만약에 이 메세지가 보인다면, 현재 디버그용 .exe 를 사용하고 있습니다.\n{bcolors.WARNING}[WARN] 이 프로젝트를 이용해서 개발을 할려는 목적이 아니라면, 'customtag-user.zip' 를 받아주세요.{bcolors.ENDC}")

    def __init__(self):
        print("[INFO] Initallizing...")
        try:
            super().__init__()
            # u
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
            self.mainVersion = QLabel('v' + VER, self)
            self.moduleListLabel = QLabel("모듈 목록", self)
            self.previewImage = QLabel("미리보기", self)
            self.previewText = QLabel("기본 텍스트", self)
            self.featureListLabel = QLabel("기능", self)

            self.est = QLabel("와샌즈!", self)

            # img label
            self.imglabelpreview = QLabel(self)

            # button
            self.saveBtn = QPushButton("저장하기", self)
            self.infoBtn = QPushButton("정보", self)
            self.showEditWin = QPushButton("수정", self)

            # toggle
            self.module_acc = QCheckBox("정확도", self)
            self.module_xacc = QCheckBox("절대 정확도", self)
            self.module_progress = QCheckBox("진행도", self)
            self.module_startprgs = QCheckBox("시작 진행도", self)
            self.module_crb = QCheckBox("체감 BPM", self)
            self.module_tilebpm = QCheckBox("타일 BPM", self)
            self.module_reckps = QCheckBox("체감 KPS", self)
            self.module_score = QCheckBox("점수", self)
            self.randomPercentText = QCheckBox("특정 확률로 텍스트 변경하기", self)
            self.setColorOnCertainPercent = QCheckBox("특정 지점에서 텍스트 색상 변경하기", self)
            #self.dummy = QCheckBox("", self)

            if self.module_acc.text == "":
                self.module_acc.setText == "ctg.module.acc"
            elif self.module_crb.text == "":
                self.module_crb.setText == "ctg.module.crb"
            elif self.module_progress.text == "":
                self.module_progress.setText == "ctg.module.progress"
            elif self.module_reckps.text == "":
                self.module_reckps.setText == "ctg.module.module_reckps"
            elif self.module_score.text == "":
                self.module_score.setText == "ctg.module.score"
            elif self.module_startprgs.text == "":
                self.module_startprgs.setText == "ctg.module.startprgs"
            elif self.module_tilebpm.text == "":
                self.module_tilebpm.setText == "ctg.module.tilebpm"
            elif self.module_xacc.text == "":
                self.module_startprgs.setText == "ctg.module.xacc"
            elif self.randomPercentText.text == "":
                self.module_tilebpm.setText == "ctg.feature.randomPercentText"

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
            self.showEditWin.move(220, 360)

            self.saveBtn.move(15, 90)
            self.infoBtn.move(95, 90)

            self.est.move(100, 550)
            # s
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

            # t
            # set clicked event
            self.saveBtn.clicked.connect(self.saveFile)
            self.infoBtn.clicked.connect(self.showInfoWindow)
            self.module_acc.clicked.connect(self.changeAcc)
            self.showEditWin.clicked.connect(self.showEditTextWindow)
            self.randomPercentText.clicked.connect(self.showEditBtn)
            print(f"{bcolors.OKCYAN}[SUCCESS] Loaded.{bcolors.ENDC}")
        except:
            self.close()
            print(f"{bcolors.FAIL}[ERROR] An Error occurred while trying to load widgets.{bcolors.ENDC}")
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(f"{bcolors.FAIL}[ERROR] Error type: ", exc_type, "Error File: " ,fname, "Error Line: " ,exc_tb.tb_lineno, f"{bcolors.ENDC}")

            errLoadWidget = QMessageBox.critical(self, '오류가 발생하였습니다.', '위젯을 설정 중에 오류가 발생하였습니다.\n보통 프로그램이 꼬였거나, 저장된 위치에 한글이 들어있으면 안되는 경우가 있습니다.\n만약 이 오류가 계속 발생할시에는 개발자에게 DM을 주십시오.')
            self.setWindowTitle("Overlayer CustomTag Generator - 불안정함")
        print(f"[INFO] Current Window Width {self.width}, Height {self.height}")

    def saveFile(self):
        print("[INFO] Saving...")
       #try:
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
                    # score
                elif self.module_acc.isChecked() == False and self.module_crb.isChecked() == False and self.module_progress.isChecked() == False and self.module_reckps.isChecked() == False and self.module_score.isChecked() == True and self.module_startprgs.isChecked() == False and self.module_tilebpm.isChecked() == False and self.module_xacc.isChecked() == False:
                        svcustom.write("function ctg() {\nreturn `점수: ${Score()}%`\n}\nRegisterTag('customTag', ctg, true);")
                        print(f"[{bcolors.OKCYAN}SUCCESS] Successfully saved file.{bcolors.ENDC}")
                        print(f"[INFO] Saved file location: {saveFile}")
                    # acc + progress
                if self.module_acc.isChecked() == True and self.module_crb.isChecked() == False and self.module_progress.isChecked() == True and self.module_reckps.isChecked() == False and self.module_score.isChecked() == False and self.module_startprgs.isChecked() == False and self.module_tilebpm.isChecked() == False and self.module_xacc.isChecked() == False:
                        svcustom.write("function ctg() {\nreturn `정확도: ${Accuracy()}%\n진행도: ${Progress()}`\n}\nRegisterTag('customTag', ctg, true);")
                        print(f"{bcolors.OKCYAN}[SUCCESS] Successfully saved file.{bcolors.ENDC}")
                        print(f"[INFO] Saved file location: {saveFile}")
                    # acc + crb
                if self.module_acc.isChecked() == True and self.module_crb.isChecked() == True and self.module_progress.isChecked() == False and self.module_reckps.isChecked() == False and self.module_score.isChecked() == False and self.module_startprgs.isChecked() == False and self.module_tilebpm.isChecked() == False and self.module_xacc.isChecked() == False:
                        svcustom.write("function ctg() {\nreturn `정확도: ${Accuracy()}%\n체감 BPM: ${CurBPM()}`\n}\nRegisterTag('customTag', ctg, true);")
                        print(f"{bcolors.OKCYAN}[SUCCESS] Successfully saved file.{bcolors.ENDC}")
                        print(f"[INFO] Saved file location: {saveFile}")
                    # acc + reckps
                if self.module_acc.isChecked() == True and self.module_crb.isChecked() == False and self.module_progress.isChecked() == False and self.module_reckps.isChecked() == True and self.module_score.isChecked() == False and self.module_startprgs.isChecked() == False and self.module_tilebpm.isChecked() == False and self.module_xacc.isChecked() == False:
                        svcustom.write("function ctg() {\nreturn `정확도: ${Accuracy()}%\n진행도: ${Progress()}`\n}\nRegisterTag('customTag', ctg, true);")
                        print(f"{bcolors.OKCYAN}[SUCCESS] Successfully saved file.{bcolors.ENDC}")
                        print(f"[INFO] Saved file location: {saveFile}")
                    # acc + score
                if self.module_acc.isChecked() == True and self.module_crb.isChecked() == False and self.module_progress.isChecked() == False and self.module_reckps.isChecked() == False and self.module_score.isChecked() == True and self.module_startprgs.isChecked() == False and self.module_tilebpm.isChecked() == False and self.module_xacc.isChecked() == False:
                        svcustom.write("function ctg() {\nreturn `정확도: ${Accuracy()}%\n점수: ${Score()}`\n}\nRegisterTag('customTag', ctg, true);")
                        print(f"{bcolors.OKCYAN}[SUCCESS] Successfully saved file.{bcolors.ENDC}")
                        print(f"[INFO] Saved file location: {saveFile}")
                    # acc + startprgs
                if self.module_acc.isChecked() == True and self.module_crb.isChecked() == False and self.module_progress.isChecked() == False and self.module_reckps.isChecked() == False and self.module_score.isChecked() == False and self.module_startprgs.isChecked() == True and self.module_tilebpm.isChecked() == False and self.module_xacc.isChecked() == False:
                        svcustom.write("function ctg() {\nreturn `정확도: ${Accuracy()}%\시작 진행도: ${StartProgress()}`\n}\nRegisterTag('customTag', ctg, true);")
                        print(f"{bcolors.OKCYAN}[SUCCESS] Successfully saved file.{bcolors.ENDC}")
                        print(f"[INFO] Saved file location: {saveFile}")
                    # acc + tilebpm
                if self.module_acc.isChecked() == True and self.module_crb.isChecked() == False and self.module_progress.isChecked() == True and self.module_reckps.isChecked() == False and self.module_score.isChecked() == False and self.module_startprgs.isChecked() == False and self.module_tilebpm.isChecked() == True and self.module_xacc.isChecked() == False:
                        svcustom.write("function ctg() {\nreturn `정확도: ${Accuracy()}%\n타일 BPM: ${TileBPM()}`\n}\nRegisterTag('customTag', ctg, true);")
                        print(f"{bcolors.OKCYAN}[SUCCESS] Successfully saved file.{bcolors.ENDC}")
                        print(f"[INFO] Saved file location: {saveFile}")
                    # d
                    # acc + xacc
                if self.module_acc.isChecked() == True and self.module_crb.isChecked() == False and self.module_progress.isChecked() == False and self.module_reckps.isChecked() == False and self.module_score.isChecked() == False and self.module_startprgs.isChecked() == False and self.module_tilebpm.isChecked() == False and self.module_xacc.isChecked() == True:
                        svcustom.write("function ctg() {\nreturn `정확도: ${Accuracy()}%\n진행도: ${Progress()}`\n}\nRegisterTag('customTag', ctg, true);")
                        print(f"{bcolors.OKCYAN}[SUCCESS] Successfully saved file.{bcolors.ENDC}")
                        print(f"[INFO] Saved file location: {saveFile}")
                    # crb + progress
                if self.module_acc.isChecked() == False and self.module_crb.isChecked() == True and self.module_progress.isChecked() == True and self.module_reckps.isChecked() == False and self.module_score.isChecked() == False and self.module_startprgs.isChecked() == False and self.module_tilebpm.isChecked() == False and self.module_xacc.isChecked() == False:
                        svcustom.write("function ctg() {\nreturn `진행도: ${Progress()}\n체감 BPM: ${CurBPM}`\n}\nRegisterTag('customTag', ctg, true);")
                        print(f"{bcolors.OKCYAN}[SUCCESS] Successfully saved file.{bcolors.ENDC}")
                        print(f"[INFO] Saved file location: {saveFile}")

                    # feature
                    ## text from spef per
                # 웨 안됨?
                if self.module_progress.isChecked() == True and self.randomPercentText.isChecked() == True:
                    svcustom.write("function ctg() {\n  let startText = " + f"`{EditRandomPercent().startText}`;\n" + "    let percent = " + f"`{EditRandomPercent().activatePercent.text()}`;\n   let text1 = " + f"`{EditRandomPercent().text1}`;\n     let text2 = " + f"`{EditRandomPercent().text2}`;\n   let finString;\n\n  if(Progress() < percent)" + "{\n        finString = startText;\n        }\n     else if(Progress() > percent) {\n       finString = text1}\n        else if(Progress() == percent) {\n      finString = text2}\nreturn `${finString}`\n}\nRegisterTag('customtag', ctg, true)")

                    # all
                elif self.module_acc.isChecked() == True and self.module_crb.isChecked() == True and self.module_progress.isChecked() == True and self.module_reckps.isChecked() == True and self.module_score.isChecked() == True and self.module_startprgs.isChecked() == True and self.module_tilebpm.isChecked() == True and self.module_xacc.isChecked() == True:
                        svcustom.write("function ctg() {\nreturn `정확도: ${Accuracy()}%\n진행도: ${Progress()}%\n절대 정확도: ${XAccuracy()}%\n체감 BPM: ${CurBpm()}%\n점수: ${Score()}\n시작 진행도: ${StartProgress()}\n체감 KPS: ${RecKps()}\n타일 BPM: ${TileBPM()}`\n}\nRegisterTag('customTag', ctg, true);")
                        print(f"{bcolors.OKCYAN}[SUCCESS] Successfully saved file.{bcolors.ENDC}")
                        print(f"[INFO] Saved file location: {saveFile}")
                    # default
                else:
                        svcustom.write("function ctg() {\n return `지정된 태그가 없습니다, 프로그램에서 지정후 저장해주세요.`;\n}\nRegisterTag('customTag', ctg, true);")
                        print(f"{bcolors.OKCYAN}[SUCCESS] Successfully saved file.{bcolors.ENDC}")
                        print(f"{bcolors.WARNING}[WARN] No module has been found. return with normal text.{bcolors.ENDC}")
                        print(f"[INFO] Saved file location: {saveFile}")
                successSaveFile = QMessageBox.information(self, '저장 완료', '태그가 저장되었습니다,\n오버레이어 설정에서 텍스트를 {customTag} 로 지정해주세요.')
        # i
        #except:
        #    print(f"{bcolors.FAIL}ERROR Occurred!\nidk why it happend. sry about that :({bcolors.ENDC}")
        #    errSaveFile = QMessageBox.critical(self, '오류가 발생하였습니다.', '파일을 저장하는 중에 오류가 발생하였습니다.\n보통 프로그램이 꼬였거나, 저장된 위치에 한글이 들어있으면 안되는 경우가 있습니다.\n만약 이 오류가 계속 발생할시에는 개발자에게 DM을 주십시오.')
        #    self.setWindowTitle("Overlayer CustomTag Generator - 불안정함")

    # e
    def changeAcc(self):
        if self.module_acc.isChecked() == True:
            self.previewText.setText = "정확도: 100%"
        else:
            self.previewText.setText = "기본 텍스트"

    def showInfoWindow(self, checked):
        self.w = InfoWindow()
        self.w.show()

    def showEditTextWindow(self):
        self.w = EditRandomPercent()
        self.w.show()

    def onClose(self, event):
        for window in QApplication.topLevelWidgets():
            window.close()

    def showEditBtn(self):
        print("dummy")
        
# run
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # load main window
    win = Main()
    win.setWidgets()
    win.show()
    app.exec()