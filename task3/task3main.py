from task3 import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
import matplotlib.pyplot as plt
import numpy as np
from scipy import fftpack,fft
import cv2


class ApplicationWindow(Ui_MainWindow):
    def __init__(self,window):
        self.setupUi(window)
        self.Labels = [self.image1_before,self.image2_before,self.image1_after,self.image2_after]
        self.combobox=[self.image1_box,self.image2_box]
        self.content=self.image1_box.currentText()
        self.actionImport.triggered.connect(self.Importbutton)
        for i in range(2):
            self.combobox[i].currentTextChanged.connect(self.select_component)


    def Importbutton(self):
        filename = QFileDialog.getOpenFileName(None, 'Load Signal', "*.png;;")
        self.path = filename[0]
        self.Open(self.path)
    
    def Open(self,path):
        if path:
                if self.Labels[0].pixmap() is None : 
                    self.Labels[0].setPixmap(QPixmap(path))
                else:
                    self.Labels[1].setPixmap(QPixmap(path))
        self.image = cv2.imread(path)
        self.image1 = Image(self.image)

    def select_component(self,Image_component):
        for i in range(2):
            selected_component = self.combobox[i].currentIndex()
            display_component = self.image1.Image_component[selected_component]
            dis_imag = np.real(np.fft.ifft2(display_component))
            dis_imag=dis_imag/ np.max(dis_imag)
            if self.Labels[1].pixmap() is None:
                plt.imsave('component1.png', abs(dis_imag)) 
                self.Labels[2].setPixmap(QPixmap('component1.png'))
            else:
                plt.imsave('component2.png', abs(dis_imag)) 
                self.Labels[3].setPixmap(QPixmap('component2.png'))



class Image():
    def __init__(self,image=[]):
         self.image = image
         self.im_fft = fftpack.fft2(self.image) 
         self.magnitude= np.abs(self.im_fft)
         self.phase =  np.exp(1j*np.angle(self.im_fft))
         self.real = np.real(self.im_fft)
         self.imaginary = 1j*np.imag(self.im_fft)
         self.Image_component=[self.magnitude,self.phase ,self.real,self.imaginary]


    



app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = ApplicationWindow(MainWindow)
MainWindow.show()
app.exec_()
