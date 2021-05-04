from task3 import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtGui import QPixmap
import matplotlib.pyplot as plt
import numpy as np
from scipy import fftpack,fft
import cv2
from numpy.fft import fft2, ifft2, fftfreq, fftshift


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
        self.comp1_box1.currentTextChanged.connect(self.mixer)
        self.comp1_box2.currentTextChanged.connect(self.mixer)
        self.comp2_box1.currentTextChanged.connect(self.mixer)
        self.comp2_box2.currentTextChanged.connect(self.mixer)


    def Importbutton(self):
        filename = QFileDialog.getOpenFileName(None, 'Load Signal', "*.png;;")
        self.path = filename[0]
        self.Open(self.path)



    def Open(self,path):
        
        if self.Labels[0].pixmap() is None :
            self.image = cv2.imread(path,flags=cv2.IMREAD_GRAYSCALE)
            #self.image = self.image/np.max(self.image)
            self.image1 = Image(self.image)
            if self.Labels[0].pixmap() is None : 
                plt.imsave('input1.png',self.image)
                self.Labels[0].setPixmap(QPixmap('input1.png'))
        else:
            self.image = cv2.imread(path,flags=cv2.IMREAD_GRAYSCALE)
            #self.image = self.image/np.max(self.image)
            self.image2 = Image(self.image)
            if self.Labels[1].pixmap() is None : 
                plt.imsave('input2.png',self.image)
                self.Labels[1].setPixmap(QPixmap('input2.png'))



    def select_component(self,Image_component):
            selectors=[self.image1_box,self.image2_box]
            images=[self.image1 ,self.image2]
            sel_comp=[self.image1 , self.image2]
            show=[self.image1_after , self.image2_after]
            for i in range(2):
                for k in range(1,5):
                    if selectors[i].currentIndex()==k:
                        sel_comp[i]= images[i].Image_component2[k-1]
                        #sel_comp[i]= np.real(np.fft.ifft2(sel_comp[i]))
                        #sel_comp[i]= abs(sel_comp[i])
                        #sel_comp[i]= sel_comp[i]/ np.max(sel_comp[i])
                        name= 'component' + str(i) + '.png'
                        plt.imsave( name, sel_comp[i]) 
                        self.Labels[i+2].setPixmap(QPixmap( name))
                        break

                        


            """ selected_component1 = self.image1_box.currentIndex()
            selected_component2 = self.image2_box.currentIndex()

            dis_imag1 = self.image1.Image_component[selected_component1]
            dis_imag1 = np.real(np.fft.ifft2(dis_imag1))
            dis_imag1 = abs(dis_imag1)
            dis_imag1=dis_imag1/ np.max(dis_imag1)
            dis_imag2 = np.real(np.fft.ifft2(self.image2.Image_component[selected_component2]))
            dis_imag2 = abs(dis_imag2)
            dis_imag2=dis_imag2/ np.max(dis_imag2) """
            
            """ plt.imsave('component1.png', abs(sel_comp[0])) 
            self.Labels[2].setPixmap(QPixmap('component1.png'))
                        
            plt.imsave('component2.png', abs(sel_comp[1])) 
            self.Labels[3].setPixmap(QPixmap('component2.png')) """
 

    def mixer(self,Image_component):
        
        ratio=[0,0]
        sliders=[self.comp1_slider,self.comp2_slider]
        for i in range(2):
            ratio[i]= (sliders[i].value())/100
        #print(ratio)
        mixing=[self.image1,self.image2]
        combo2=[['Phase','UniPhase'],['Magnitude','UniMagnitude'],['Imaginary'],['Real'],['Phase','UniPhase'],['Magnitude','UniMagnitude']]
        lookup= {
            'Magnitude' : 0,
            'Phase':1,
            'Real':2,
            'Imaginary':3,
            'UniMagnitude':4,
            'UniPhase':5    
            }
        ## update combobox2
        """ for i in range(6):
            if self.comp1_box2.currentIndex()==i:
                self.comp2_box2.clear()
                self.comp2_box2.addItems(combo2[i])

                #print(self.comp2_box2.count()) """
        ## choose mixed images
        for i in range(2):
            global mix11,mix22,mix21,mix12
            if self.comp1_box1.currentIndex()==i:
                mix11= mixing[i]
                mix22 = mixing[i]
                
            if self.comp2_box1.currentIndex()==i:
                mix21=mixing[i]
                mix12=mixing[i]
                
        ##choose mixed components
        for i in range(6):
            global m1 ,m2 ,m3,m4,resmix1,resmix2
            if self.comp1_box2.currentIndex()==i:
                m1= mix11.Image_component[i]
                m2= mix12.Image_component[i]
                # print(m1[0][0][0])
                # print(m2[0][0][0])
              
        for i in range(self.comp2_box2.count()):
            

            if self.comp2_box2.currentIndex()==i:
                global x
                x=lookup.get(self.comp2_box2.currentText())
                
                m3= mix21.Image_component[x]
                m4= mix22.Image_component[x]
                    
                resmix1= (m1*ratio[0]) + (m2 *(1-ratio[0]))
                resmix2= (m3*ratio[1]) + (m4 *(1-ratio[1])) 

            xx=[0,1,4,5]
            if x in xx:
                
                combine= np.multiply(resmix1 , resmix2)
            else:
                combine= np.add(resmix1 , resmix2)    

            imgmix= np.real(np.fft.ifft2(combine))
            #imgmix= imgmix/ np.max(imgmix)
            
            out=[self.output1_img , self.output2_img]
            for i in range(2):
                if self.mixer_box.currentIndex()==i:
                    plt.imsave('mixed.png', imgmix )
                    out[i].setPixmap(QPixmap('mixed.png')) 
        

class Image():
    def __init__(self,image=[]):
         self.image = image
         self.im_fft = fft2(self.image) 
         self.im_fft_shifted=np.fft.fftshift(self.im_fft)
         self.magnitude= np.abs(self.im_fft)
         self.magnitude_spectrum=20*np.log(np.abs(self.im_fft_shifted))
         self.phase =  np.angle(self.im_fft)
         self.real = np.real(self.im_fft)
         self.real_spectrum=20*np.log(np.real(self.im_fft_shifted))
         self.imaginary = np.imag(self.im_fft)
         self.unimag = np.ones(np.shape(self.magnitude))
         self.uniphase = np.zeros(np.shape(self.phase))
         self.Image_component=[self.magnitude,self.phase ,self.real,self.imaginary,self.unimag,self.uniphase]
         self.Image_component2=[self.magnitude_spectrum,self.phase,self.real_spectrum,self.imaginary]

    



app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()

ui = ApplicationWindow(MainWindow)
MainWindow.show()
app.exec_()
