# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledjYYzkH.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLabel,
    QMainWindow, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QVBoxLayout, QWidget)
import img_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(900, 600)
        self.all_market = QWidget(MainWindow)
        self.all_market.setObjectName(u"all_market")
        self.font_market = QFrame(self.all_market)
        self.font_market.setObjectName(u"font_market")
        self.font_market.setGeometry(QRect(0, 0, 900, 700))
        self.font_market.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(217, 217, 217);\n"
"}\n"
"\n"
".QPushButton {\n"
"	background-color: rgb(230, 255, 148);\n"
"	border-radius: 15%;\n"
"	border : 1px solid black\n"
"  }\n"
".QPushButton:hover {\n"
"      ;\n"
"	background-color: rgb(255, 95, 42);\n"
"      transition: 0.7s;\n"
"  }\n"
"")
        self.font_market.setFrameShape(QFrame.StyledPanel)
        self.font_market.setFrameShadow(QFrame.Raised)
        self.market = QFrame(self.font_market)
        self.market.setObjectName(u"market")
        self.market.setGeometry(QRect(20, 15, 371, 521))
        self.market.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.market.setFrameShape(QFrame.StyledPanel)
        self.market.setFrameShadow(QFrame.Raised)
        self.text = QLabel(self.market)
        self.text.setObjectName(u"text")
        self.text.setEnabled(True)
        self.text.setGeometry(QRect(0, 50, 371, 91))
        font = QFont()
        font.setPointSize(15)
        self.text.setFont(font)
        self.text.setAlignment(Qt.AlignCenter)
        self.text.setWordWrap(False)
        self.placeBottle = QFrame(self.market)
        self.placeBottle.setObjectName(u"placeBottle")
        self.placeBottle.setGeometry(QRect(30, 220, 181, 241))
        self.placeBottle.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.placeBottle.setFrameShape(QFrame.StyledPanel)
        self.placeBottle.setFrameShadow(QFrame.Raised)
        self.welcome_label = QFrame(self.market)
        self.welcome_label.setObjectName(u"welcome_label")
        self.welcome_label.setGeometry(QRect(60, 150, 301, 41))
        self.welcome_label.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.welcome_label.setFrameShape(QFrame.StyledPanel)
        self.welcome_label.setFrameShadow(QFrame.Raised)
        self.welcome_text = QLabel(self.welcome_label)
        self.welcome_text.setObjectName(u"welcome_text")
        self.welcome_text.setGeometry(QRect(-2, 10, 301, 20))
        self.welcome_text.setAlignment(Qt.AlignCenter)
        self.info = QFrame(self.market)
        self.info.setObjectName(u"info")
        self.info.setGeometry(QRect(240, 220, 120, 201))
        self.info.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.info.setFrameShape(QFrame.StyledPanel)
        self.info.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.info)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(3, 5, 116, 16))
        self.label_2.setAlignment(Qt.AlignCenter)
        self.pushButton = QPushButton(self.info)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(0, 168, 121, 31))
        self.pushButton.setStyleSheet(u"background-color: rgb(107, 95, 95);\n"
"  border-radius: 15%;\n"
"border : 1px solid black")
        self.menu_water = QFrame(self.info)
        self.menu_water.setObjectName(u"menu_water")
        self.menu_water.setGeometry(QRect(5, 40, 30, 100))
        self.menu_water.setStyleSheet(u"")
        self.menu_water.setFrameShape(QFrame.StyledPanel)
        self.menu_water.setFrameShadow(QFrame.Raised)
        self.water1 = QPushButton(self.menu_water)
        self.water1.setObjectName(u"water1")
        self.water1.setGeometry(QRect(3, 5, 24, 24))
        self.water1.setStyleSheet(u"\n"
"  border-radius: 12%;\n"
"  border: 1px solid red;")
        self.water5 = QPushButton(self.menu_water)
        self.water5.setObjectName(u"water5")
        self.water5.setGeometry(QRect(3, 35, 24, 24))
        self.water5.setStyleSheet(u"\n"
"  border-radius: 12%;\n"
"  border: 1px solid red;")
        self.water19 = QPushButton(self.menu_water)
        self.water19.setObjectName(u"water19")
        self.water19.setGeometry(QRect(3, 65, 24, 24))
        self.water19.setStyleSheet(u"\n"
"  border-radius: 12%;\n"
"  border: 1px solid red;")
        self.label_3 = QLabel(self.info)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(45, 45, 66, 81))
        self.label_3.setStyleSheet(u"color: #000;\n"
"text-align: center;\n"
"font-size: 12px;\n"
"font-family: Alata;\n"
"font-style: normal;\n"
"font-weight: 400;\n"
"line-height: normal;")
        self.get_kard = QFrame(self.market)
        self.get_kard.setObjectName(u"get_kard")
        self.get_kard.setGeometry(QRect(224, 434, 136, 81))
        self.get_kard.setStyleSheet(u"background-color: rgb(217, 217, 217);")
        self.get_kard.setFrameShape(QFrame.StyledPanel)
        self.get_kard.setFrameShadow(QFrame.Raised)
        self.kard_text = QLabel(self.get_kard)
        self.kard_text.setObjectName(u"kard_text")
        self.kard_text.setGeometry(QRect(3, 5, 131, 71))
        self.kard_text.setAlignment(Qt.AlignCenter)
        self.water = QFrame(self.market)
        self.water.setObjectName(u"water")
        self.water.setGeometry(QRect(-1, 0, 376, 71))
        self.water.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.water.setFrameShape(QFrame.StyledPanel)
        self.water.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.water)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(0, -200, 466, 341))
        self.verticalLayoutWidget = QWidget(self.font_market)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(470, 15, 221, 174))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.checkBox = QCheckBox(self.verticalLayoutWidget)
        self.checkBox.setObjectName(u"checkBox")

        self.verticalLayout.addWidget(self.checkBox)

        self.checkBox_2 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_2.setObjectName(u"checkBox_2")

        self.verticalLayout.addWidget(self.checkBox_2)

        self.checkBox_6 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_6.setObjectName(u"checkBox_6")

        self.verticalLayout.addWidget(self.checkBox_6)

        self.checkBox_3 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_3.setObjectName(u"checkBox_3")

        self.verticalLayout.addWidget(self.checkBox_3)

        self.checkBox_4 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_4.setObjectName(u"checkBox_4")

        self.verticalLayout.addWidget(self.checkBox_4)

        self.checkBox_5 = QCheckBox(self.verticalLayoutWidget)
        self.checkBox_5.setObjectName(u"checkBox_5")

        self.verticalLayout.addWidget(self.checkBox_5)

        self.true_card = QPushButton(self.font_market)
        self.true_card.setObjectName(u"true_card")
        self.true_card.setGeometry(QRect(745, 215, 121, 31))
        self.true_card.setStyleSheet(u"")
        self.put_bottle = QPushButton(self.font_market)
        self.put_bottle.setObjectName(u"put_bottle")
        self.put_bottle.setGeometry(QRect(545, 305, 121, 31))
        self.put_bottle.setStyleSheet(u"")
        self.bottle = QLabel(self.font_market)
        self.bottle.setObjectName(u"bottle")
        self.bottle.setGeometry(QRect(405, 285, 261, 266))
        self.card = QLabel(self.font_market)
        self.card.setObjectName(u"card")
        self.card.setGeometry(QRect(745, 250, 126, 111))
        self.false_card = QPushButton(self.font_market)
        self.false_card.setObjectName(u"false_card")
        self.false_card.setGeometry(QRect(750, 385, 121, 31))
        self.false_card.setStyleSheet(u"")
        self.false_card_frame = QFrame(self.font_market)
        self.false_card_frame.setObjectName(u"false_card_frame")
        self.false_card_frame.setGeometry(QRect(745, 440, 120, 80))
        self.false_card_frame.setStyleSheet(u"background-color: rgb(89, 255, 178);")
        self.false_card_frame.setFrameShape(QFrame.StyledPanel)
        self.false_card_frame.setFrameShadow(QFrame.Raised)
        self.pick_up_bottle = QPushButton(self.font_market)
        self.pick_up_bottle.setObjectName(u"pick_up_bottle")
        self.pick_up_bottle.setGeometry(QRect(590, 455, 121, 31))
        self.pick_up_bottle.setStyleSheet(u"")
        self.bottle.raise_()
        self.market.raise_()
        self.verticalLayoutWidget.raise_()
        self.true_card.raise_()
        self.put_bottle.raise_()
        self.card.raise_()
        self.false_card.raise_()
        self.false_card_frame.raise_()
        self.pick_up_bottle.raise_()
        MainWindow.setCentralWidget(self.all_market)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 900, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"1", None))
        self.text.setText(QCoreApplication.translate("MainWindow", u"\u0414\u044b\u0445\u0430\u043d\u0438\u0435 \u0440\u043e\u0434\u043d\u0438\u043a\u0430 \n"
" Water dispanser", None))
        self.welcome_text.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u0433\u043b\u0430\u0448\u0435\u043d\u0438\u0435", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u043f\u0443\u0441\u0442\u043a/\u0441\u0442\u043e\u043f", None))
        self.water1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.water5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.water19.setText(QCoreApplication.translate("MainWindow", u"19", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"1\u043b \u2014 5\u0440\n"
"\n"
"5\u043b \u2014 20\u0440\n"
"\n"
"19\u043b \u2014 40\u0440", None))
        self.kard_text.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043b\u043e\u0436\u0438\u0442\u0435 \u043a\u0430\u0440\u0442\u0443", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/newPrefix/3.png\"/></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u0418\u043d\u0441\u0442\u0440\u0443\u043a\u0446\u0438\u044f", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u043e\u0440 \u043e\u0431\u044a\u0435\u043c\u0430", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0440\u0438\u043b\u043e\u0436\u0438\u0442\u0435 \u043a\u0430\u0440\u0442\u0443", None))
        self.checkBox_6.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0430\u0432\u044c\u0442\u0435 \u0442\u0430\u0440\u0443", None))
        self.checkBox_3.setText(QCoreApplication.translate("MainWindow", u"\u041f\u0443\u0441\u043a (\u043f\u0443\u0441\u043a/\u0441\u0442\u043e\u043f)", None))
        self.checkBox_4.setText(QCoreApplication.translate("MainWindow", u"\u042d\u043a\u0441\u0442\u0440\u0435\u043d\u043d\u043e\u0435 \u0437\u0430\u0432\u0435\u0440\u0448\u0435\u043d\u0438\u0435(\u043f\u0443\u0441\u043a/\u0441\u0442\u043e\u043f)", None))
        self.checkBox_5.setText(QCoreApplication.translate("MainWindow", u"\u0410\u0432\u0442\u043e\u043c\u0430\u0442\u0438\u0447\u0435\u0441\u043a\u043e\u0435 \u0437\u0430\u0432\u0440\u0448\u0435\u043d\u0438\u0435", None))
        self.true_card.setText(QCoreApplication.translate("MainWindow", u"\u043f\u0440\u0438\u043b\u043e\u0436\u0438\u0442\u044c \u043a\u0430\u0440\u0442\u0443", None))
        self.put_bottle.setText(QCoreApplication.translate("MainWindow", u"\u043f\u043e\u0441\u0442\u0430\u0432\u0438\u0442\u044c \u0431\u0443\u0442\u044b\u043b\u043a\u0443", None))
        self.bottle.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/newPrefix/2.png\"/></p></body></html>", None))
        self.card.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/newPrefix/4.png\"/></p></body></html>", None))
        self.false_card.setText(QCoreApplication.translate("MainWindow", u"\u043f\u0440\u0438\u043b\u043e\u0436\u0438\u0442\u044c \u043e\u0431\u043c\u0430\u043d\u043a\u0443", None))
        self.pick_up_bottle.setText(QCoreApplication.translate("MainWindow", u"\u0417\u0430\u0431\u0440\u0430\u0442\u044c \u0442\u0430\u0440\u0443", None))
    # retranslateUi

