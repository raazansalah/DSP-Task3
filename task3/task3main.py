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
        self.image2_box.currentTextChanged.connect(self.select_component)
        self.comp2_slider.valueChanged.connect(self.mixer)
        self.comp1_slider.valueChanged.connect(self.mixer)

    
    def Importbutton(self):
        filename = QFileDialog.getOpenFileName(None, 'Load Signal', "*.png;;")
        self.path = filename[0]
        self.Open(self.path)



    def Open(self,path):
        
        if self.Labels[0].pixmap() is None :
            self.image = cv2.imread(path)
            self.image = self.image/np.max(self.image)
            self.image1 = Image(self.image)
            if self.Labels[0].pixmap() is None : 
                plt.imsave('input1.png',self.image)
                self.Labels[0].setPixmap(QPixmap('input1.png'))
        else:
            self.image = cv2.imread(path)
            self.image = self.image/np.max(self.image)
            self.image2 = Image(self.image)
            if self.Labels[1].pixmap() is None : 
                plt.imsave('input2.png',self.image)
                self.Labels[1].setPixmap(QPixmap('input2.png'))



    def select_component(self,Image_component):
            
            selected_component1 = self.image1_box.currentIndex()
            selected_component2 = self.image2_box.currentIndex()

            dis_imag1 = self.image1.Image_component[selected_component1]
            dis_imag1 = np.real(np.fft.ifft2(dis_imag1))
            dis_imag1 = abs(dis_imag1)
            dis_imag1=dis_imag1/ np.max(dis_imag1)
            dis_imag2 = np.real(np.fft.ifft2(self.image2.Image_component[selected_component2]))
            dis_imag2 = abs(dis_imag2)
            dis_imag2=dis_imag2/ np.max(dis_imag2)
            
            plt.imsave('component1.png', abs(dis_imag1)) 
            self.Labels[2].setPixmap(QPixmap('component1.png'))
                        
            plt.imsave('component2.png', abs(dis_imag2)) 
            self.Labels[3].setPixmap(QPixmap('component2.png'))
            print(self.image2.Image_component[0][1][3])
            print(self.image1.Image_component[0][1][3])

    def mixer(self,Image_component):
        
        ratio=[0,0]
        sliders=[self.comp1_slider,self.comp2_slider]
        for i in range(2):
            ratio[i]= (sliders[i].value())/100
        print(ratio)
        mixing=[self.image1,self.image2]
        combo2=[['Phase','Uniphase'],['Magnitude','Unimag'],['Imaginary'],['Real'],['Phase','UniPhase'],['Magnitude','Unimag']]
        
        for i in range(2):
            if self.comp1_box1.currentIndex()==i:
                mix1=mixing[i]
            for i in range(6):
                if self.comp1_box2.currentIndex()==i:
                    global comp1
                    comp1=mix1.Image_component[i]
                    
                    self.comp2_box2.clear()
                    self.comp2_box2.addItems(combo2[i])
                for i in range( 2):
                    if self.comp1_box1.currentIndex()==i:
                        mix2=mixing[i]
                    for i in range(self.comp2_box2.count()):
                        if self.comp2_box2.currentIndex()==i:
                            global comp2
                            comp2 = mix2.Image_component[i]
        for i in range(4):
            listofcomp=['Magnitude','Phase','Unimag','UniPhase']
            if self.comp1_box2.currentText() in listofcomp:
                resmix1= (comp1*ratio[0]) + ((mix2.Image_component[self.comp2_box2.currentIndex()])*(1-ratio[0]))
                resmix2= (comp2*ratio[1]) + ((mix1.Image_component[self.comp1_box2.currentIndex()])*(1-ratio[1]))
            else  :
                resmix1= (comp1*ratio[0]) + ((mix2.Image_component[self.comp2_box2.currentIndex()])*(1-ratio[0]))
                resmix2= (comp2*ratio[1]) + ((mix1.Image_component[self.comp1_box2.currentIndex()])*(1-ratio[1]))  
            combine= np.multiply(resmix1 , resmix2)
            imgmix= np.real(np.fft.ifft2(combine))
            imgmix= imgmix/ np.max(imgmix)
            plt.imsave('mixed.png',abs( imgmix) )
            self.output1_img.setPixmap(QPixmap('mixed.png'))
                                


        # mixmag=((self.image1.Image_component[0]) * ratio[0]) +((1-ratio[0]) *(self.image2.Image_component[0]) )
        # mixphase= ((self.image2.Image_component[1]) * ratio[1]) +((1-ratio[1]) *(self.image1.Image_component[1]) )
        # combine= np.multiply(mixphase , mixmag)
        # imgmix= np.real(np.fft.ifft2(combine))
        # imgmix= imgmix/ np.max(imgmix)
        # plt.imsave('mixed.png',abs( imgmix) )
        # self.output1_img.setPixmap(QPixmap('mixed.png'))

class Image():
    def __init__(self,image=[]):
         self.image = image
         self.im_fft = fftpack.fft2(self.image) 
         self.magnitude= np.abs(self.im_fft)
         self.phase =  np.exp(1j*np.angle(self.im_fft))
         self.real = np.real(self.im_fft)
         self.imaginary = 1j*np.imag(self.im_fft)
         self.unimag = np.ones(np.shape(self.magnitude))
         self.uniphase = np.zeros(np.shape(self.phase))
         self.Image_component=[self.magnitude,self.phase ,self.real,self.imaginary,self.unimag,self.uniphase]


    



app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = ApplicationWindow(MainWindow)
MainWindow.show()
app.exec_()
