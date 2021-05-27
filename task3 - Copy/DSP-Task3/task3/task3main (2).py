from numpy.core.fromnumeric import partition
from task3 import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QFileDialog,QMessageBox
from PyQt5.QtGui import QPixmap
import matplotlib.pyplot as plt
import numpy as np
from scipy import fftpack,fft
import cv2
from numpy.fft import fft2, ifft2, fftfreq, fftshift
import logging
import os
combo2=[['Phase','UniPhase'],['Magnitude','UniMagnitude'],['Imaginary'],['Real'],['Phase','UniPhase'],['Magnitude','UniMagnitude']]
lookup= {'Magnitude' : 0,'Phase':1,'Real':2,'Imaginary':3,'UniMagnitude':4, 'UniPhase':5 }
update=[[1,5] ,[0,4] ,[3] ,[2] ,[1,5] ,[0,4]]

logging.basicConfig(level=logging.DEBUG,
                    filename="app.log",
                    format='%(lineno)s - %(levelname)s - %(message)s',
                    filemode='w')


logger = logging.getLogger()

class ApplicationWindow(Ui_MainWindow):
    def __init__(self,window):
        self.setupUi(window)
        self.array_of_images_class=[]
        self.array_of_images=[]
        self.Labels = [self.image1_before,self.image2_before,self.image1_after,self.image2_after]
        self.combobox=[self.image1_box,self.image2_box]
        self.content=self.image1_box.currentText()
        self.actionImport.triggered.connect(self.Importbutton)
        self.image1_box.currentTextChanged.connect(self.select_component)
        self.image2_box.currentTextChanged.connect(self.select_component)
        self.comp2_slider.valueChanged.connect(self.mixercomp)
        self.comp1_slider.valueChanged.connect(self.mixercomp)
        self.mixer_box.currentTextChanged.connect(self.mixercomp)
        #self.comp1_box1.currentTextChanged.connect(self.mixercomp)
        self.comp1_box2.currentTextChanged.connect(self.update_combo)
        #self.comp2_box1.currentTextChanged.connect(self.mixercomp)
        #self.comp2_box2.currentTextChanged.connect(self.mixercomp)
        logger.info("The Application started successfully")
## IMPORT and OPEN

    def Importbutton(self):
        logger.info("Browsing the files")
        filename = QFileDialog.getOpenFileNames(None, 'Select image', os.getenv('HOME'), "Images (*.png)")
        if len(filename[0]) != 2:
            # Showing number of images warning msg and return
            self.warning_msg(
                "Error in selected Images ", "You must select two images at once!")
            logger.info("The user didn't select exactly 2 images")
            return self.Importbutton()
        self.array_of_images=[]
        for file in filename[0]:
            self.array_of_images.append(cv2.imread(file)) 
        if self.array_of_images[0].shape != self.array_of_images[1].shape:
            self.warning_msg(
                "Error in Image Size", "The 2 images must have the same size!")
            logger.info("The user selected 2 images with different sizes")
            return self.Importbutton()
        else:
            self.image1, self.image2 = [Image(self.array_of_images[i]/np.max(self.array_of_images[i])) for i in range(2)] 
            for i in range (2):
                cv2.imwrite('input'+str(i)+'.png',self.array_of_images[i])
                self.Labels[i].setPixmap(QPixmap('input'+str(i)+'.png'))
            logger.info("Images browsed sucsuccessfully")
        
        
    ## SELECT COMPONENTS
    def select_component(self,Image_component):
            selectors=[self.image1_box,self.image2_box]
            images=[self.image1,self.image2]
            sel_comp=[self.image1,self.image2]
            
            show=[self.image1_after , self.image2_after]
            for i in range(2):
                for k in range(1,5):
                    if selectors[i].currentIndex()==k:
                        sel_comp[i]= images[i].Image_component2[k-1]
                        logger.info("Components have been returned successfully")
                        sel_comp[i]= abs(sel_comp[i])
                        if k != 3:
                            sel_comp[i]= sel_comp[i]/ np.max(sel_comp[i])
                        name= 'component' + str(i) + '.png'
                        plt.imsave( name, abs(sel_comp[i])) 
                        self.Labels[i+2].setPixmap(QPixmap( name))
                        break
            logger.info("Components have been drawn successfully")
    def update_combo(self):
        for i in range(1,7):
            if self.comp1_box2.currentIndex()==i:
                self.comp2_box2.clear()
                self.comp2_box2.addItems(combo2[i-1])

    def mixercomp(self):
        global m1 ,m2 ,m3 ,m4
        y=self.comp1_box2.currentIndex()
        ratio =[0,0]
        mixing=[self.image1,self.image2]
        out=[self.output1_img , self.output2_img]
        sliders=[self.comp1_slider,self.comp2_slider]
        for i in range(2):
            ratio[i]= (sliders[i].value())/100

        ##Select Mixed Images
        miximg=[]
        for i in range(2):
            if self.comp1_box1.currentIndex()==i:
                mix11= mixing[i]
                mix22 = mixing[i]
            if self.comp2_box1.currentIndex()==i:
                mix21=mixing[i]
                mix12=mixing[i]
        logger.info("MIXED images was selected")
        ##choose mixed components
        for i in range(1,7):
             
            if self.comp1_box2.currentIndex()==i:
                m1= mix11.Image_component[i-1]
                m2= mix12.Image_component[i-1]
        logger.info("First mixer component was selected ")    
        for i in range(self.comp2_box2.count()):
            if self.comp2_box2.currentIndex()==i:
                global x
                x=lookup.get(self.comp2_box2.currentText())
                m3= mix21.Image_component[x]
                m4= mix22.Image_component[x]
               
        Image.mixer= classmethod(Image.mixer)
        mixeeed= Image.mixer(x,m1,m2 ,m3,m4,ratio)
        #mixeeed= mixeeed/ (np.max(mixeeed))
        mixeeed = cv2.convertScaleAbs(mixeeed, alpha=(255.0))
        cv2.imwrite('mixed.png', mixeeed)
        i= self.mixer_box.currentIndex()
        out[i-1].setPixmap(QPixmap('mixed.png'))

    #WARNING MESSAGES 
    def warning_msg(self, title, text):
        msg = QMessageBox()
        msg.setWindowTitle(title)
        msg.setText(text)
        msg.setIcon(QMessageBox.Warning)
        return msg.exec_()

class Image():
    def __init__(self,image=[]):
        ##IMAGE COMPONENTS
         self.image = image
         self.im_fft = fft2(self.image) 
         self.im_fft_shifted=np.fft.fftshift(self.im_fft)
         self.magnitude= np.abs(self.im_fft)
         self.magnitude_spectrum=20*np.log(np.abs(self.im_fft_shifted))
         self.phase =  np.exp(1j*np.angle(self.im_fft))
         self.real = np.real(self.im_fft)
         self.real_spectrum=20*np.log(np.real(self.im_fft_shifted))
         self.imaginary = 1j*np.imag(self.im_fft)
         self.unimag = np.ones(np.shape(self.magnitude))
         self.uniphase = np.zeros(np.shape(self.phase))
         self.Image_component=[self.magnitude,self.phase ,self.real,self.imaginary,self.unimag,self.uniphase]
         self.Image_component2=[self.magnitude_spectrum,np.real(self.phase),self.real_spectrum,self.imaginary]
    ##FUNCTION TO MIX 
    def mixer(self , x , m1 ,m2 ,m3 ,m4, ratio):
        xx=[0,1,4,5]
        resmix1=(m1*ratio[0]) + (m2 *(1-ratio[0]))
        resmix2= (m3*ratio[1]) + (m4 *(1-ratio[1])) 
        if x in xx:
                
                combine= np.multiply(resmix1 , resmix2)
        else:
                combine= np.add(resmix1 , resmix2)    

        imgmix= np.real(np.fft.ifft2(combine))

        return imgmix
        

app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = ApplicationWindow(MainWindow)
MainWindow.show()
app.exec_()
