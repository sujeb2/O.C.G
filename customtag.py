from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QPushButton, QCheckBox, QMessageBox, QFileDialog, QLineEdit
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6 import QtCore
from datetime import date
import os, sys, requests, logging;

VER = 'v0.2.9==dev'
githubLink = requests.get('https://api.github.com/repos/sujeb2/O.C.G/releases/latest')
log = logging
log.basicConfig(filename='./log/debug-log.log', level=logging.INFO, encoding="utf-8")

class InfoWindow(QWidget):
    def __init__(self):
        log.info("Initializing infoWindow...")
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
            log.info(f"Initialized.")
        except:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            log.critical(f"ERROR Occurred!\nLog: {exc_type}, {exc_obj}, {exc_tb}, {fname}")
            errInfoWinInit = QMessageBox.critical(self, '오류가 발생하였습니다.', '재설정을 하는 중에 오류가 발생했습니다.\n보통 프로그램이 꼬였거나, 저장된 위치에 한글이 들어있으면 안되는 경우가 있습니다.\n만약 이 오류가 계속 발생할시에는 개발자에게 DM을 주십시오.')
            self.setWindowTitle("정보 - 불안정함")

    def setWidgets(self):
        log.info("Loading Widgets...")
        try:
            overlayerUrlLink="<a href=\"https://overlayer.notion.site/overlayer/Overlayer-Knowledge-Base-a06a2947f8bd44e098189a9d3c28ac49\">Overlayer Knowledge Base (Notion)</a>"
            csharpdiscord="<a href=\"https://overlayerwiki.github.io/index.html\">Overlayer Knowledge Base (Website)</a>"

            # info label
            self.infoMainLabel = QLabel("OverLayer", self)
            self.infoMainLabel2 = QLabel("CustomTag Generator", self)

            self.madebysans = QLabel("Made by. songro_", self)

            self.ctgLogo = QLabel(self)

            self.infoOverlayerKnowledgeLabel = QLabel(overlayerUrlLink, self)
            self.infoCSharpSharpDiscordLabel = QLabel(csharpdiscord, self)

            self.ctgLogoPixmap = QPixmap('./src/icon_normal-resized')

            # move/set font
            self.infoMainLabel.move(70, 40)
            self.infoMainLabel2.move(70, 75)
            self.infoOverlayerKnowledgeLabel.move(70, 145)
            self.infoCSharpSharpDiscordLabel.move(70, 165)
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

            infoCSharpDiscordLinkFont = self.infoCSharpSharpDiscordLabel.font()
            infoCSharpDiscordLinkFont.setFamily('Pretendard Variable')
            infoCSharpDiscordLinkFont.setPointSize(10)

            madebysansfont = self.madebysans.font()
            madebysansfont.setFamily('Pretendard Variable')
            madebysansfont.setPointSize(13)

            ctgLogoFont = self.ctgLogo.font()
            ctgLogoFont.setPointSize(10)

            self.infoMainLabel.setFont(infoLabelFont1)
            self.infoMainLabel2.setFont(infoLabelFont2)
            self.infoCSharpSharpDiscordLabel.setFont(infoCSharpDiscordLinkFont)
            self.infoOverlayerKnowledgeLabel.setFont(infoOverLayerLinkFont)
            self.madebysans.setFont(madebysansfont)
            self.ctgLogo.setFont(ctgLogoFont)

            self.infoOverlayerKnowledgeLabel.setOpenExternalLinks(True)
            self.infoCSharpSharpDiscordLabel.setOpenExternalLinks(True)

            self.ctgLogo.setPixmap(self.ctgLogoPixmap)

        except:
            self.close()
            log.critical(f"An Error occurred while trying to load widgets.")
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            log.critical(f"Error type: ", exc_type, "Error File: " ,fname, "Error Line: " ,exc_tb.tb_lineno)

            errLoadWidget = QMessageBox.critical(self, '오류가 발생하였습니다.', '위젯을 설정 중에 오류가 발생하였습니다.\n보통 프로그램이 꼬였거나, 저장된 위치에 한글이 들어있으면 안되는 경우가 있습니다.\n만약 이 오류가 계속 발생할시에는 개발자에게 DM을 주십시오.')
            self.setWindowTitle("Overlayer CustomTag Generator - 불안정함")
        log.info(f"Current Window Width {self.width}, Height {self.height}")

class EditRandomPercent(QWidget):
    def __init__(self):
        log.info("Initializing EditWindow...")
        try:
            super().__init__()

            self.top = 200
            self.left = 500
            self.width = 300
            self.height = 125

            self.setWindowTitle("텍스트 변경")
            self.setWindowIcon(QIcon('./src/icon_edit.png'))
            self.setGeometry(self.left, self.top, self.width, self.height)
            self.setWindowFlags(QtCore.Qt.WindowType.WindowCloseButtonHint | QtCore.Qt.WindowType.WindowMinimizeButtonHint)
            self.setWidgets()
            log.info(f"Initialized.")
        except:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            log.critical(f"ERROR Occurred!\n] Log: {exc_type}, {exc_obj}, {exc_tb}, {fname}")
            errInitWin2 = QMessageBox.critical(self, '오류가 발생하였습니다.', '재설정을 하는 중에 오류가 발생했습니다.\n보통 프로그램이 꼬였거나, 저장된 위치에 한글이 들어있으면 안되는 경우가 있습니다.\n만약 이 오류가 계속 발생할시에는 개발자에게 DM을 주십시오.')
            self.setWindowTitle("텍스트 변경 - 불안정함")

    def setWidgets(self):
        log.info("Loading Widgets...")
        try:
            self.editTitle = QLabel("텍스트 변경", self)
            
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
            self.customText2.setPlaceholderText("끝 텍스트")
            log.info(f"Loaded.")
        except:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            log.critical(f"ERROR Occurred!\n Log: {exc_type}, {exc_obj}, {exc_tb}, {fname}")
            errWidgetSetupWin2 = QMessageBox.critical(self, '오류가 발생하였습니다.', '위젯을 설정 중에 오류가 발생하였습니다.\n보통 프로그램이 꼬였거나, 저장된 위치에 한글이 들어있으면 안되는 경우가 있습니다.\n만약 이 오류가 계속 발생할시에는 개발자에게 DM을 주십시오.')
            self.setWindowTitle("텍스트 변경 - 불안정함")

    def done(self):
        log.info("Saving info..")
        try:
            self.activatePer = float(self.activatePercent.text())
            self.startTxt = self.startText.text()
            self.text1 = self.customText1.text()
            self.text2 = self.customText2.text()
            log.info(f"Saved.")
            log.info(f"{self.activatePer}, {self.startTxt}, {self.text1}, {self.text2}")
        except ValueError:
            try:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                log.critical(f"ERROR Occurred!\n] Log: {exc_type}, {exc_obj}, {exc_tb}, {fname}")
                errWidgetSetupWin2 = QMessageBox.information(self, '값 확인', '시작될 퍼센트를 지정하는중에 오류가 발생하였습니다.\n해당 값이 숫자인지 확인해주세요.')
            except:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                log.critical(f"ERROR Occurred!\n Log: {exc_type}, {exc_obj}, {exc_tb}, {fname}")
                errWidgetSetupWin2 = QMessageBox.critical(self, '오류가 발생했습니다', '오류를 표시하는중에 오류가 발생하였습니다.\n보통 프로그램이 꼬였거나, 저장된 위치에 한글이 들어있으면 안되는 경우가 있습니다.\n만약 이 오류가 계속 발생할시에는 개발자에게 DM을 주십시오.')
                self.setWindowTitle("텍스트 변경 - 불안정함")
        self.close()

class Main(QWidget):
    log = logging

    githubLatestVer = githubLink.json()["name"]
    githubLastestDownload = githubLink.json()['assets']
    log.info(githubLastestDownload)
    log.info("Current path: " + os.getcwd())

    log.info(f"만약에 이 메세지가 보인다면, 현재 디버그용 .exe 를 사용하고 있습니다.")
    log.warning("이 프로젝트를 이용해서 개발을 할려는 목적이 아니라면, 'customtag-user.zip' 를 받아주세요.")
    log.info("Current latest version: " + githubLatestVer)
    log.info("Current version: " + VER)
    if(githubLatestVer > VER):
        findUpdateMsg = QMessageBox.question('업데이트 발견', '새로운 버전 ' + githubLatestVer + ' 이 발견되었습니다.')
    elif(githubLatestVer < VER):
        log.warning(f"현재 개발자 버전을 사용하고 있습니다.\n이 버전은 매우 불안정하며, 버그가 자주 발생합니다.")
    elif(githubLatestVer == VER):
        log.info(f"최신버전을 사용하고 있습니다!")

    def __init__(self):
        log.info(" Initializing...")
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
            log.info(f"Initialized.")
        except:
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            log.critical(f"ERROR Occurred!\nLog: {exc_type}, {exc_obj}, {exc_tb}, {fname}")
            errInit = QMessageBox.critical(self, '오류가 발생하였습니다.', '재설정을 하는 중에 오류가 발생했습니다.\n보통 프로그램이 꼬였거나, 저장된 위치에 한글이 들어있으면 안되는 경우가 있습니다.\n만약 이 오류가 계속 발생할시에는 개발자에게 DM을 주십시오.')
            self.setWindowTitle("Overlayer CustomTag Generator - 불안정함")

    def resetWindow(self):
        self.show

    def setWidgets(self):
        log.info(" Loading Widgets...")
        try:
            # label
            self.mainLabel1 = QLabel("OverLayer", self)
            self.mainLabel2 = QLabel("CustomTag Generator", self)
            self.mainVersion = QLabel(VER, self)
            self.moduleListLabel = QLabel("모듈 목록", self)
            self.previewImage = QLabel("미리보기", self)
            self.previewText = QLabel("기본 텍스트", self)
            self.featureListLabel = QLabel("기능", self)

            self.est = QLabel(self)

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
            self.module_combo = QCheckBox("콤보", self)
            self.module_pgrsdeath = QCheckBox("지정한 범위에서 죽은 횟수", self)
            self.module_sngCurMin = QCheckBox("노래 (분)", self)
            self.module_sngCurSec = QCheckBox("노래 (초)", self)
            self.module_sngCurMilliSec = QCheckBox("노래 (밀리초)", self)
            self.module_totMin = QCheckBox("총 노래 길이 (분)", self)
            self.module_totSec = QCheckBox("총 노래 길이 (초)", self)
            self.module_totMilliSec = QCheckBox("총 노래 길이 (밀리초)")

            self.randomPercentText = QCheckBox("특정 지점에서 텍스트 변경하기", self)
            self.setColorOnCertainPercent = QCheckBox("특정 지점에서 텍스트 색상 변경하기", self)
            #self.featureDummy = QCheckBox("", self)

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
            self.estImgNotEndDream = QPixmap('./src/img/easter/not-end-dream')
            self.estImgNoBitches = QPixmap('./src/img/easter/nobitches')

            # def img
            self.imglabelpreview.setPixmap(QPixmap(self.previewImagePixmapTemplate))

            if date.today().strftime('%m-%d') == '04-01':
                self.est.setPixmap(QPixmap(self.estImgNotEndDream))
            elif date.today().strftime('%m-%d') == '02-14':
                self.est.setPixmap(QPixmap(self.estImgNoBitches))
            else:
                self.est.setText('언더테일 아시는구나!\n혹시 모르시는분들에 대해 설명해드립니다\n샌즈랑 언더테일의 세가지 엔딩루트중 몰살엔딩의 최종보스로 진.짜.겁.나.어.렵.습.니.다\n공격은 전부다 회피하고 만피가 92인데 샌즈의 공격은 1초당 60이 다는데다가 독뎀까지 추가로 붙어있습니다..\n하지만 이러면 절대로 게임을 깰 수 가없으니 제작진이 치명적인 약점을 만들었죠.\n샌즈의 치명적인 약점이 바로 지친다는것입니다.\n패턴들을 다 견디고나면 지쳐서 자신의 턴을 유지한채로 잠에듭니다.\n하지만 잠이들었을때 창을옮겨서 공격을 시도하고 샌즈는 1차공격은 피하지만 그 후에 바로날아오는 2차 공격을 맞고 죽습니다.')

            # reset btn/label position
            self.mainLabel1.move(15, 20)
            self.mainLabel2.move(15, 50)
            self.mainVersion.move(325, 50)
            self.moduleListLabel.move(15, 127)
            self.previewImage.move(510, 45)
            self.imglabelpreview.move(510, 75)
            self.previewText.move(520, 83)
            self.featureListLabel.move(15, 330)
            self.showEditWin.move(230, 360)

            self.saveBtn.move(15, 90)
            self.infoBtn.move(95, 90)

            self.est.move(100, 500)

            self.module_acc.move(15, 160)
            self.module_xacc.move(15, 180)
            self.module_crb.move(15, 200)
            self.module_progress.move(15, 220)
            self.module_reckps.move(15, 240)
            self.module_startprgs.move(15, 260)
            self.module_tilebpm.move(15, 280)
            self.module_score.move(15, 300)
            self.module_combo.move(120, 160)
            self.module_pgrsdeath.move(120, 180)
            self.module_sngCurMin.move(120, 201)
            self.module_sngCurSec.move(120, 221)
            self.module_sngCurMilliSec.move(120, 241)
            self.module_totMin.move(120, 261)
            self.module_totSec.move(120, 281)
            self.module_totMilliSec.move(120, 301)

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

            # default font size = 13
            moduleToggleFont1 = self.module_acc.font()
            moduleToggleFont1.setFamily('Pretendard JP')
            moduleToggleFont1.setPointSize(13)

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
            self.module_crb.setFont(moduleToggleFont1)
            self.module_acc.setFont(moduleToggleFont1)
            self.module_progress.setFont(moduleToggleFont1)
            self.module_reckps.setFont(moduleToggleFont1)
            self.module_xacc.setFont(moduleToggleFont1)
            self.module_startprgs.setFont(moduleToggleFont1)
            self.module_tilebpm.setFont(moduleToggleFont1)
            self.module_score.setFont(moduleToggleFont1)
            self.module_combo.setFont(moduleToggleFont1)
            self.module_pgrsdeath.setFont(moduleToggleFont1)
            self.module_sngCurSec.setFont(moduleToggleFont1)
            self.module_sngCurMin.setFont(moduleToggleFont1)
            self.module_sngCurMilliSec.setFont(moduleToggleFont1)
            self.module_totMin.setFont(moduleToggleFont1)
            self.module_totSec.setFont(moduleToggleFont1)
            self.previewImage.setFont(previewImageLabelFont)
            self.previewText.setFont(previewTextFont)
            self.saveBtn.setFont(savebtnFont)
            self.randomPercentText.setFont(feature_randomPerText)
            self.setColorOnCertainPercent.setFont(feature_setColorOnCertainPercent)

            # set clicked event
            self.saveBtn.clicked.connect(self.saveFile)
            self.infoBtn.clicked.connect(self.showInfoWindow)
            self.module_acc.clicked.connect(self.changeAcc)
            self.showEditWin.clicked.connect(self.showEditTextWindow)
            self.randomPercentText.clicked.connect(self.showEditBtn)
            log.info(f"Loaded.")
        except:
            self.close()
            log.critical(f" An Error occurred while trying to load widgets.")
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            log.critical(f" Error type: ",exc_type, "Error File: " ,fname, "Error Line: " ,exc_tb.tb_lineno)

            errLoadWidget = QMessageBox.critical(self, '오류가 발생하였습니다.', '위젯을 설정 중에 오류가 발생하였습니다.\n보통 프로그램이 꼬였거나, 저장된 위치에 한글이 들어있으면 안되는 경우가 있습니다.\n만약 이 오류가 계속 발생할시에는 개발자에게 DM을 주십시오.')
            self.setWindowTitle("Overlayer CustomTag Generator - 불안정함")
        log.info(f"Current Window Width {self.width}, Height {self.height}")

    def saveFile(self):
        log.info("Saving...")
        log.info(f"{self.module_acc.isChecked()}, {self.module_crb.isChecked()}, {self.module_progress.isChecked()}, {self.module_reckps.isChecked()}, {self.module_progress.isChecked()}, {self.module_score.isChecked()}, {self.module_startprgs.isChecked()}, {self.module_xacc.isChecked()}, {self.randomPercentText.isChecked()}, {self.setColorOnCertainPercent.isChecked()}")
        saveFile = QFileDialog.getSaveFileName(self, '저장될 위치 선택', './customtag.js', 'JavaScript (*.js)')
        filenum = [1, 2]
        num = 0

        if saveFile[0] != "":
            try:
                for filenums in filenum:
                    filenum = filenum + 1
                    with open(saveFile[0], 'w+', encoding='UTF-8') as svfirst:
                        svfirst.write("function ctg() {")

                    with open(saveFile[0], 'a+', encoding="UTF-8") as svcustom:
                        # acc
                        if self.module_acc.isChecked() == True:
                            svcustom.writelines("\n  return `정확도: ${Accuracy()}%`;\n")
                            log.info(f"Successfully saved file.")
                            log.info(f"Saved file location: {saveFile}")
                        # xacc
                        elif self.module_xacc.isChecked() == True:
                            svcustom.write("\n  return `절대 정확도: ${XAccuracy()}%`;\n")
                            log.info("Successfully saved file.")
                            log.info(f"Saved file location: {saveFile}")
                        # crb
                        elif self.module_crb.isChecked() == True:
                            svcustom.write("\n  return `체감 BPM: ${CurBpm()}BPM`;\n")
                            log.info(f"Successfully saved file.")
                            log.info(f"Saved file location: {saveFile}")
                        elif self.module_xacc.isChecked() == True:
                            svcustom.write("\n  return `절대 정확도: ${XAccuracy()}%`;\n")
                            log.info("Successfully saved file.")
                            log.info(f"Saved file location: {saveFile}")
                        # score
                        elif self.module_score.isChecked() == True:
                            svcustom.write("\n  return `점수: ${Score()}`;\n")
                            log.info(f"Successfully saved file.")
                            log.info(f"Saved file location: {saveFile}")
                    # all
                        elif self.module_acc.isChecked() == True and self.module_crb.isChecked() == True and self.module_progress.isChecked() == True and self.module_reckps.isChecked() == True and self.module_score.isChecked() == True and self.module_startprgs.isChecked() == True and self.module_tilebpm.isChecked() == True and self.module_xacc.isChecked() == True:
                            svcustom.write("\n  return `정확도: ${Accuracy()}%\n진행도: ${Progress()}%\n절대 정확도: ${XAccuracy()}%\n체감 BPM: ${CurBpm()}%\n점수: ${Score()}\n시작 진행도: ${StartProgress()}\n체감 KPS: ${RecKps()}\n타일 BPM: ${TileBPM()}`\n})")
                            log.info(f"Successfully saved file.")
                            log.info(f"Saved file location: {saveFile}")
                        else:
                        svcustom.write("\n  return `태그 없음`;\n")
                        log.info("Successfully saved file.")
                        log.info(f"Saved file location: {saveFile}")

                    with open(saveFile[0], 'a+', encoding='UTF-8') as svlast:
                        svlast.write("}\nRegisterTag('customTag', ctg, true);")
                    log.info(num)
                
                successSaveFile = QMessageBox.information(self, '저장 완료', '태그가 저장되었습니다,\n오버레이어 설정에서 텍스트를 {customTag} 로 지정해주세요.')
                log.info("Written: " + svfirst.read() + svcustom.read() + svlast.read())
                svfirst.close()
                svcustom.close()
                svlast.close()
            except:
                exc_type, exc_obj, exc_tb = sys.exc_info()
                fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                log.critical(f"Error type: ", exc_type, "Error File: " ,fname, "Error Line: " ,exc_tb.tb_lineno)
                errSaveFile = QMessageBox.critical(self, '오류가 발생하였습니다.', '파일을 저장하는 중에 오류가 발생하였습니다.\n보통 프로그램이 꼬였거나, 저장된 위치에 한글이 들어있으면 안되는 경우가 있습니다.\n만약 이 오류가 계속 발생할시에는 개발자에게 DM을 주십시오.')
                self.setWindowTitle("Overlayer CustomTag Generator - 불안정함")

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
        log.info("to-do")
        
# run
if __name__ == '__main__':
    app = QApplication(sys.argv)
    # load main window
    win = Main()
    win.setWidgets()
    win.show()
    app.exec()