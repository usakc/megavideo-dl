# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_ui.ui'
#
# Created: Sat Jan 22 23:06:50 2011
#      by: PyQt4 UI code generator 4.7.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.setEnabled(True)
        main.resize(561, 466)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(main.sizePolicy().hasHeightForWidth())
        main.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(main)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setEnabled(False)
        self.groupBox.setGeometry(QtCore.QRect(0, 30, 561, 441))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtGui.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 20, 561, 391))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label = QtGui.QLabel(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 0, 1, 1)
        self.label_3 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 3, 0, 1, 1)
        self.label_4 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 4, 0, 1, 1)
        self.label_5 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 5, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 6, 0, 1, 1)
        self.label_7 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 7, 0, 1, 1)
        self.label_8 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 8, 0, 1, 1)
        self.label_9 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 9, 0, 1, 1)
        self.label_10 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 10, 0, 1, 1)
        self.label_11 = QtGui.QLabel(self.gridLayoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 11, 0, 1, 1)
        self.durLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.durLabel.setText("")
        self.durLabel.setObjectName("durLabel")
        self.gridLayout.addWidget(self.durLabel, 3, 1, 1, 2)
        self.titleLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.titleLabel.setText("")
        self.titleLabel.setObjectName("titleLabel")
        self.gridLayout.addWidget(self.titleLabel, 4, 1, 1, 2)
        self.descLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.descLabel.setText("")
        self.descLabel.setObjectName("descLabel")
        self.gridLayout.addWidget(self.descLabel, 5, 1, 1, 2)
        self.dateLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.dateLabel.setText("")
        self.dateLabel.setObjectName("dateLabel")
        self.gridLayout.addWidget(self.dateLabel, 6, 1, 1, 2)
        self.commLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.commLabel.setText("")
        self.commLabel.setObjectName("commLabel")
        self.gridLayout.addWidget(self.commLabel, 8, 1, 1, 2)
        self.catLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.catLabel.setText("")
        self.catLabel.setObjectName("catLabel")
        self.gridLayout.addWidget(self.catLabel, 9, 1, 1, 2)
        self.tagsLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.tagsLabel.setText("")
        self.tagsLabel.setObjectName("tagsLabel")
        self.gridLayout.addWidget(self.tagsLabel, 10, 1, 1, 2)
        self.ratLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.ratLabel.setText("")
        self.ratLabel.setObjectName("ratLabel")
        self.gridLayout.addWidget(self.ratLabel, 11, 1, 1, 2)
        self.downVideoB = QtGui.QPushButton(self.gridLayoutWidget)
        self.downVideoB.setObjectName("downVideoB")
        self.gridLayout.addWidget(self.downVideoB, 0, 2, 1, 1)
        self.copyUrlB = QtGui.QPushButton(self.gridLayoutWidget)
        self.copyUrlB.setObjectName("copyUrlB")
        self.gridLayout.addWidget(self.copyUrlB, 0, 1, 1, 1)
        self.sizeLabel = QtGui.QLabel(self.gridLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.sizeLabel.sizePolicy().hasHeightForWidth())
        self.sizeLabel.setSizePolicy(sizePolicy)
        self.sizeLabel.setText("")
        self.sizeLabel.setObjectName("sizeLabel")
        self.gridLayout.addWidget(self.sizeLabel, 2, 1, 1, 2)
        self.favLabel = QtGui.QLabel(self.gridLayoutWidget)
        self.favLabel.setText("")
        self.favLabel.setObjectName("favLabel")
        self.gridLayout.addWidget(self.favLabel, 7, 1, 1, 2)
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 561, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_12 = QtGui.QLabel(self.horizontalLayoutWidget)
        self.label_12.setObjectName("label_12")
        self.horizontalLayout.addWidget(self.label_12)
        self.urlInput = QtGui.QLineEdit(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.urlInput.sizePolicy().hasHeightForWidth())
        self.urlInput.setSizePolicy(sizePolicy)
        self.urlInput.setToolTip("")
        self.urlInput.setText("")
        #self.urlInput.setPlaceholderText("None")
        self.urlInput.setObjectName("urlInput")
        self.horizontalLayout.addWidget(self.urlInput)
        self.showInfoB = QtGui.QPushButton(self.horizontalLayoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showInfoB.sizePolicy().hasHeightForWidth())
        self.showInfoB.setSizePolicy(sizePolicy)
        self.showInfoB.setObjectName("showInfoB")
        self.horizontalLayout.addWidget(self.showInfoB)
        main.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(main)
        self.statusbar.setObjectName("statusbar")
        main.setStatusBar(self.statusbar)

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        main.setWindowTitle(QtGui.QApplication.translate("main", "megavideo-dl", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setStatusTip(QtGui.QApplication.translate("main", "Video info", None, QtGui.QApplication.UnicodeUTF8))
        self.groupBox.setTitle(QtGui.QApplication.translate("main", "Video information", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("main", "URL", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("main", "Size", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("main", "Duration", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("main", "Title", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("main", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("main", "Publication date", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("main", "Favourites by users number", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("main", "Number of comments", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("main", "Category", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("main", "Tags", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("main", "Rating", None, QtGui.QApplication.UnicodeUTF8))
        self.downVideoB.setText(QtGui.QApplication.translate("main", "Download video", None, QtGui.QApplication.UnicodeUTF8))
        self.copyUrlB.setText(QtGui.QApplication.translate("main", "Copy url", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("main", "Megavideo url", None, QtGui.QApplication.UnicodeUTF8))
        self.urlInput.setStatusTip(QtGui.QApplication.translate("main", "Example: http://www.megavideo.com/?v=HPJB0RWP", None, QtGui.QApplication.UnicodeUTF8))
        self.showInfoB.setText(QtGui.QApplication.translate("main", "Show video info", None, QtGui.QApplication.UnicodeUTF8))

