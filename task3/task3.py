# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'task3.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1359, 830)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.image2_label = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.image2_label.setFont(font)
        self.image2_label.setObjectName("image2_label")
        self.gridLayout_4.addWidget(self.image2_label, 0, 0, 1, 1)
        self.image2_after = QtWidgets.QLabel(self.frame_3)
        self.image2_after.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.image2_after.setText("")
        self.image2_after.setScaledContents(True)
        self.image2_after.setObjectName("image2_after")
        self.gridLayout_4.addWidget(self.image2_after, 1, 1, 1, 1)
        self.image2_before = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.image2_before.setFont(font)
        self.image2_before.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.image2_before.setScaledContents(True)
        self.image2_before.setAlignment(QtCore.Qt.AlignCenter)
        self.image2_before.setObjectName("image2_before")
        self.gridLayout_4.addWidget(self.image2_before, 1, 0, 1, 1)
        self.image2_box = QtWidgets.QComboBox(self.frame_3)
        self.image2_box.setObjectName("image2_box")
        self.image2_box.addItem("")
        self.image2_box.addItem("")
        self.image2_box.addItem("")
        self.image2_box.addItem("")
        self.gridLayout_4.addWidget(self.image2_box, 0, 1, 1, 1)
        self.gridLayout.addWidget(self.frame_3, 1, 0, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.image1_label = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.image1_label.setFont(font)
        self.image1_label.setObjectName("image1_label")
        self.gridLayout_2.addWidget(self.image1_label, 0, 0, 1, 1)
        self.image1_after = QtWidgets.QLabel(self.frame_2)
        self.image1_after.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.image1_after.setText("")
        self.image1_after.setScaledContents(True)
        self.image1_after.setObjectName("image1_after")
        self.gridLayout_2.addWidget(self.image1_after, 1, 1, 1, 1)
        self.image1_box = QtWidgets.QComboBox(self.frame_2)
        self.image1_box.setMaximumSize(QtCore.QSize(600, 16777215))
        self.image1_box.setObjectName("image1_box")
        self.image1_box.addItem("")
        self.image1_box.addItem("")
        self.image1_box.addItem("")
        self.image1_box.addItem("")
        self.gridLayout_2.addWidget(self.image1_box, 0, 1, 1, 1)
        self.image1_before = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.image1_before.setFont(font)
        self.image1_before.setAutoFillBackground(False)
        self.image1_before.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.image1_before.setScaledContents(True)
        self.image1_before.setAlignment(QtCore.Qt.AlignCenter)
        self.image1_before.setObjectName("image1_before")
        self.gridLayout_2.addWidget(self.image1_before, 1, 0, 1, 1)
        self.gridLayout.addWidget(self.frame_2, 0, 0, 1, 1)
        self.frame_4 = QtWidgets.QFrame(self.centralwidget)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.output1_label = QtWidgets.QLabel(self.frame_4)
        self.output1_label.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.output1_label.setFont(font)
        self.output1_label.setAlignment(QtCore.Qt.AlignCenter)
        self.output1_label.setObjectName("output1_label")
        self.gridLayout_5.addWidget(self.output1_label, 0, 0, 1, 1)
        self.output2_label = QtWidgets.QLabel(self.frame_4)
        self.output2_label.setMaximumSize(QtCore.QSize(16777215, 22))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.output2_label.setFont(font)
        self.output2_label.setAutoFillBackground(False)
        self.output2_label.setAlignment(QtCore.Qt.AlignCenter)
        self.output2_label.setObjectName("output2_label")
        self.gridLayout_5.addWidget(self.output2_label, 0, 1, 1, 1)
        self.output1_img = QtWidgets.QLabel(self.frame_4)
        self.output1_img.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.output1_img.setText("")
        self.output1_img.setScaledContents(True)
        self.output1_img.setObjectName("output1_img")
        self.gridLayout_5.addWidget(self.output1_img, 1, 0, 1, 1)
        self.output2_img = QtWidgets.QLabel(self.frame_4)
        self.output2_img.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.output2_img.setText("")
        self.output2_img.setScaledContents(True)
        self.output2_img.setObjectName("output2_img")
        self.gridLayout_5.addWidget(self.output2_img, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.frame_4, 1, 1, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.comp2_box1 = QtWidgets.QComboBox(self.frame)
        self.comp2_box1.setObjectName("comp2_box1")
        self.comp2_box1.addItem("")
        self.comp2_box1.addItem("")
        self.gridLayout_3.addWidget(self.comp2_box1, 3, 1, 1, 1)
        self.component1_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.component1_label.setFont(font)
        self.component1_label.setAutoFillBackground(False)
        self.component1_label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.component1_label.setObjectName("component1_label")
        self.gridLayout_3.addWidget(self.component1_label, 1, 0, 1, 1)
        self.comp1_box2 = QtWidgets.QComboBox(self.frame)
        self.comp1_box2.setObjectName("comp1_box2")
        self.comp1_box2.addItem("")
        self.comp1_box2.addItem("")
        self.comp1_box2.addItem("")
        self.comp1_box2.addItem("")
        self.comp1_box2.addItem("")
        self.comp1_box2.addItem("")
        self.gridLayout_3.addWidget(self.comp1_box2, 2, 1, 1, 1)
        self.comp1_box1 = QtWidgets.QComboBox(self.frame)
        self.comp1_box1.setObjectName("comp1_box1")
        self.comp1_box1.addItem("")
        self.comp1_box1.addItem("")
        self.gridLayout_3.addWidget(self.comp1_box1, 1, 1, 1, 1)
        self.mixer_box = QtWidgets.QComboBox(self.frame)
        self.mixer_box.setObjectName("mixer_box")
        self.mixer_box.addItem("")
        self.mixer_box.addItem("")
        self.gridLayout_3.addWidget(self.mixer_box, 0, 1, 1, 1)
        self.component2_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.component2_label.setFont(font)
        self.component2_label.setObjectName("component2_label")
        self.gridLayout_3.addWidget(self.component2_label, 3, 0, 1, 1)
        self.comp2_box2 = QtWidgets.QComboBox(self.frame)
        self.comp2_box2.setObjectName("comp2_box2")
        self.comp2_box2.addItem("")
        self.comp2_box2.addItem("")
        self.comp2_box2.addItem("")
        self.comp2_box2.addItem("")
        self.comp2_box2.addItem("")
        self.comp2_box2.addItem("")
        self.gridLayout_3.addWidget(self.comp2_box2, 4, 1, 1, 1)
        self.mixer_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.mixer_label.setFont(font)
        self.mixer_label.setObjectName("mixer_label")
        self.gridLayout_3.addWidget(self.mixer_label, 0, 0, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.frame)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        
        self.comp1_slider = QtWidgets.QSlider(self.frame_5)
        self.comp1_slider.setGeometry(QtCore.QRect(9, 0, 301, 22))
        self.comp1_slider.setMaximumSize(QtCore.QSize(301, 22))
        self.comp1_slider.setMaximum(100)
        self.comp1_slider.setProperty("value", 0)
        self.comp1_slider.setOrientation(QtCore.Qt.Horizontal)
        self.comp1_slider.setInvertedAppearance(False)
        self.comp1_slider.setInvertedControls(False)
        self.comp1_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.comp1_slider.setTickInterval(3)
        self.comp1_slider.setObjectName("comp1_slider")
        self.gridLayout_3.addWidget(self.frame_5, 2, 0, 1, 1)
        self.frame_6 = QtWidgets.QFrame(self.frame)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.comp2_slider = QtWidgets.QSlider(self.frame_6)
        self.comp2_slider.setGeometry(QtCore.QRect(9, 0, 301, 22))
        self.comp2_slider.setMaximumSize(QtCore.QSize(301, 22))
        self.comp2_slider.setMaximum(100)
        self.comp2_slider.setOrientation(QtCore.Qt.Horizontal)
        self.comp2_slider.setTickPosition(QtWidgets.QSlider.TicksAbove)
        self.comp2_slider.setTickInterval(3)
        self.comp2_slider.setObjectName("comp2_slider")
        self.gridLayout_3.addWidget(self.frame_6, 4, 0, 1, 1)
        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1359, 26))
        self.menubar.setObjectName("menubar")
        self.menuOpen = QtWidgets.QMenu(self.menubar)
        self.menuOpen.setObjectName("menuOpen")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionImport = QtWidgets.QAction(MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.menuOpen.addAction(self.actionImport)
        self.menubar.addAction(self.menuOpen.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.image2_label.setText(_translate("MainWindow", "Image 2"))
        #self.image2_before.setText(_translate("MainWindow", "Image 2"))
        self.image2_box.setItemText(0, _translate("MainWindow", "Magnitude"))
        self.image2_box.setItemText(1, _translate("MainWindow", "Phase"))
        self.image2_box.setItemText(2, _translate("MainWindow", "Real"))
        self.image2_box.setItemText(3, _translate("MainWindow", "Imaginary"))
        self.image1_label.setText(_translate("MainWindow", "Image 1"))
        self.image1_box.setItemText(0, _translate("MainWindow", "Magnitude"))
        self.image1_box.setItemText(1, _translate("MainWindow", "Phase"))
        self.image1_box.setItemText(2, _translate("MainWindow", "Real"))
        self.image1_box.setItemText(3, _translate("MainWindow", "Imaginary"))
        #self.image1_before.setText(_translate("MainWindow", "Image 1"))
        self.output1_label.setText(_translate("MainWindow", "Output 1"))
        self.output2_label.setText(_translate("MainWindow", "Output 2"))
        self.comp2_box1.setItemText(0, _translate("MainWindow", "Image 1"))
        self.comp2_box1.setItemText(1, _translate("MainWindow", "Image 2"))
        self.component1_label.setText(_translate("MainWindow", "Component 1:"))
        self.comp1_box2.setItemText(0, _translate("MainWindow", "Magnitude "))
        self.comp1_box2.setItemText(1, _translate("MainWindow", "Phase"))
        self.comp1_box2.setItemText(2, _translate("MainWindow", "Real"))
        self.comp1_box2.setItemText(3, _translate("MainWindow", "Imaginary"))
        self.comp1_box2.setItemText(4, _translate("MainWindow", "UniMagnitude"))
        self.comp1_box2.setItemText(5, _translate("MainWindow", "UniPhase"))
        self.comp1_box1.setItemText(0, _translate("MainWindow", "Image 1"))
        self.comp1_box1.setItemText(1, _translate("MainWindow", "Image 2"))
        self.mixer_box.setItemText(0, _translate("MainWindow", "Output 1"))
        self.mixer_box.setItemText(1, _translate("MainWindow", "Output 2"))
        self.component2_label.setText(_translate("MainWindow", "Component 2 :"))
        self.comp2_box2.setItemText(0, _translate("MainWindow", "Magnitude"))
        self.comp2_box2.setItemText(1, _translate("MainWindow", "Phase"))
        self.comp2_box2.setItemText(2, _translate("MainWindow", "Real"))
        self.comp2_box2.setItemText(3, _translate("MainWindow", "Imaginary"))
        self.comp2_box2.setItemText(4, _translate("MainWindow", "UniMagnitude"))
        self.comp2_box2.setItemText(5, _translate("MainWindow", "UniPhase"))
        self.mixer_label.setText(_translate("MainWindow", "Mixer Output To :"))
        self.menuOpen.setTitle(_translate("MainWindow", "Open"))
        self.actionImport.setText(_translate("MainWindow", "Import"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
