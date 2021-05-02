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
        self.image1_box.currentTextChanged.connect(self.select_component)
        self.comp2_slider.valueChanged.connect(self.mixer)


    def Importbutton(self):
        filename = QFileDialog.getOpenFileName(None, 'Load Signal', "*.png;;")
        self.path = filename[0]
        self.Open(self.path)
    
    def Open(self,path):
        if path:
            if self.Labels[0].pixmap() is None : 
                self.image = cv2.imread(path)
                self.image = self.image/np.max(self.image)
                self.image1 = Image(self.image)
                plt.imsave('input.png' , self.image)
                self.Labels[0].setPixmap(QPixmap('input.png'))
            else:
                self.Labels[1].setPixmap(QPixmap(path))

    def select_component(self,Image_component):
        for i in range(2):
            selected_component = self.image1_box.currentIndex()
            display_component = self.image1.Image_component[selected_component]
            dis_imag = np.real(np.fft.ifft2(display_component))
            dis_imag=dis_imag/ np.max(dis_imag)
            
            plt.imsave('component.png', abs(dis_imag)) 
            self.Labels[2].setPixmap(QPixmap('component.png'))
         
    def mixer(self,Image_component):
        ratio=[0,0]
        sliders=[self.comp1_slider,self.comp2_slider]
        for i in range(2):
            ratio[i]= (sliders[i].value())/100
        print(ratio)  
    
        mixmag=(self.image1.Image_component[0]) 
        mixphase= (self.image1.Image_component[1]) 
        combine= np.multiply(mixphase , mixmag)
        imgmix= np.real(np.fft.ifft2(combine))
        imgmix= imgmix/ np.max(imgmix)
        plt.imsave('mixed.png',abs( imgmix) )
        self.output1_img.setPixmap(QPixmap('mixed.png'))

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
