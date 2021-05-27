from typing import DefaultDict
from PyQt5 import QtWidgets, QtCore, uic, QtGui, QtPrintSupport
from pyqtgraph import PlotWidget, plot
from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import *   
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from os import path
import pandas as pd
import numpy as np
import sys
import os
import matplotlib.pyplot as plot
import librosa 
from pydub import AudioSegment
from tempfile import mktemp
import librosa.display
import numpy as np
from PIL import Image
import imagehash

import pylab


MAIN_WINDOW,_=loadUiType(path.join(path.dirname(__file__),"main.ui"))

class MainApp(QMainWindow,MAIN_WINDOW):
  
    def __init__(self,parent=None):
        super(MainApp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Buttons= [self.Browse1 , self.Browse2 , self.Identify]
        self.Buttons[2].setDisabled(True) 
        self.Table= [self.song_1,self.song_2,self.song_3,self.song_4,self.song_5,self.song_6,self.song_7,self.song_8,self.song_9,self.song_10]
        self.songs= [None,None]
        self.outMix= None
        self.Buttons[0].clicked.connect(lambda : self.readSong(1) )
        self.Buttons[1].clicked.connect(lambda : self.readSong(2) )
        self.Buttons[2].clicked.connect(self.songMixer)

    def readSong(self,songNumber):
      fileName= QFileDialog.getOpenFileName( self, 'choose the signal', os.getenv('HOME') ,"mp3(*.mp3)" ) 
      self.path = fileName[0] 

      if self.path =="" :
          return
      modifiedAudio = AudioSegment.from_file( self.path , format="mp3")[:60000]  # read mp3
      wname = mktemp('.wav')  # use temporary file
      modifiedAudio.export(wname, format="wav")  # convert to wav

      if songNumber == 1:
        self.firstSongName.setText(os.path.splitext(os.path.basename(self.path))[0])
        self.song1Data,self.samplingFrequency1 =librosa.load(wname)
        self.songs[0]= self.song1Data
        self.Buttons[2].setDisabled(False) 
        print("Song1 read ")

      elif songNumber == 2 :
        self.secondSongName.setText(os.path.splitext(os.path.basename(self.path))[0])
        self.song2Data,self.samplingFrequency2 =librosa.load(wname)
        self.songs[1]= self.song2Data
        self.Buttons[2].setDisabled(False) 
        print("song2 read")

        for i in range (10):
            self.Table[i].clear()
        
    def songMixer(self) :
        sliderRatio = self.mixerSlider.value()/100

        if (self.songs[0] is not None) and (self.songs[1] is not None):
            self.outMix = self.songs[0] * sliderRatio + self.songs[1] * (1-sliderRatio)
        
        else:
            if self.songs[0] is not None : self.outMix = self.songs[0]
            if self.songs[1] is not None: self.outMix = self.songs[1]
           
        self.spectrogram()

    def spectrogram (self):
        
        Spectro_Path = 'mixSpectrogram.png'
        pylab.axis('off')  # no axis
        pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[])  # Remove the white edge
        D = librosa.amplitude_to_db(np.abs(librosa.stft(self.outMix)), ref=np.max)
        librosa.display.specshow(D, y_axis='linear')
        pylab.savefig(Spectro_Path, bbox_inches=None, pad_inches=0)
        pylab.close()
        self.features()

    def features (self): 
      
      #mfcc 
      pylab.axis('off')  
      pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[])
      SavePath = 'mfcc.png'
      feature1= librosa.feature.mfcc(y=self.outMix, sr=self.samplingFrequency1)
      Image1=Image.fromarray(feature1)
      Hash1=imagehash.phash(Image1)
      f = open('hash1.txt','a')
      f.write(str(Hash1)+"\n")
      f.close()
      librosa.display.specshow(feature1.T,sr=self.samplingFrequency1 )
      pylab.savefig(SavePath, bbox_inches=None, pad_inches=0)
      pylab.close()

      #melspectrogram
      pylab.axis('off') 
      pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[]) 
      SavePath ='melspectrogram.png'
      feature2= librosa.feature.melspectrogram(y=self.outMix, sr=self.samplingFrequency1)
      Image2=Image.fromarray(feature2)
      Hash2=imagehash.phash(Image2)
      f = open('hash2.txt','a')
      f.write(str(Hash2)+"\n")
      f.close()
      print(Hash2)
      librosa.display.specshow(feature2.T,sr=self.samplingFrequency1 )
      pylab.savefig(SavePath, bbox_inches=None, pad_inches=0)
      pylab.close()

    #spectral_zero_crossing_rate
      pylab.axis('off') 
      pylab.axes([0., 0., 1., 1.], frameon=False, xticks=[], yticks=[]) 
      SavePath ='feature_zero_crossing_rate.png'
      feature3= librosa.feature.zero_crossing_rate(y=self.outMix)
      Image3=Image.fromarray(feature3)
      Hash3=imagehash.phash(Image3)
      f = open('hash3.txt','a')
      f.write(str(Hash3)+"\n")
      f.close()
      librosa.display.specshow(feature3.T,sr=self.samplingFrequency1 )
      pylab.savefig(SavePath, bbox_inches=None, pad_inches=0)
      pylab.close()
    

def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())


if __name__=='__main__':
    main()