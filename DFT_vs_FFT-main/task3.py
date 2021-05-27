import ctypes
import numpy as np
import time
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from pyqtgraph import PlotWidget
from typing import DefaultDict
from PyQt5 import QtWidgets, QtCore, uic, QtGui, QtPrintSupport
from pyqtgraph import PlotWidget, plot
from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import *   
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from os import path
library = ctypes.CDLL('./libfft.so')


MAIN_WINDOW,_=loadUiType(path.join(path.dirname(__file__),"task3.ui"))

class MainApp(QMainWindow,MAIN_WINDOW):
    def __init__(self,parent=None):
        super(MainApp,self).__init__(parent)
        QMainWindow.__init__(self)
        self.setupUi(self)
        
        # doublesArray === double [4];
        # arr2 = doublesArray.from_address(np_array) ---- arr2 is double arr[4] in C
        
        self.N = np.array([1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024], dtype=np.int)
        # self.N = np.array([16, 32, 64, 128, 256, 512, 1024, 2048 , 4096 , 8192 , 16384], dtype=np.int)

        self.i_real = np.arange((1024), dtype=np.double)
        self.i_imag = np.arange((1024), dtype=np.double)

        self.dftTime = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=np.double)
        self.fftTime = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], dtype=np.double)


        self.DFT.clicked.connect(lambda: self.plotting(index = 1))
        self.FFT.clicked.connect(lambda: self.plotting(index = 2))
        self.clear.clicked.connect(lambda: self.plotting(index = 3))
        self.error.clicked.connect(self.plot_error)
        
        self.widgets_array = [self.widget , self.widget_2]

        for i in range (2):
            self.widgets_array[i].plotItem.addLegend(size=(1,2))
            self.widgets_array[i].plotItem.showGrid(True, True, alpha = 0.5)
            self.widgets_array[i].plotItem.setLabel('bottom', "Number of samples")

        self.widget.plotItem.setLabel('left', "Computation time", units = "s")
        self.widget_2.plotItem.setLabel('left', "error")
        self.widget_2.setYRange(-2,2)

# g++ -fPIC -shared -o libfft.so fft.cpp && python run.py

    def plotting(self, index):
        global i_size
        global i_real_C
        size = len(self.N)
        for i in range (size):
            start_time = time.time()
            self.i_real_iteration = self.i_real[0: self.N[i]]
            self.i_imag_iteration = self.i_imag[0: self.N[i]]
            i_size = len(self.i_real_iteration)
            doublesArray = ctypes.c_double * self.N[i]
            i_real_C = doublesArray.from_address(self.i_real_iteration.ctypes.data)
            i_imag_C = doublesArray.from_address(self.i_imag_iteration.ctypes.data)
            o_real_ptr = ctypes.POINTER(ctypes.c_double)()
            o_imag_ptr = ctypes.POINTER(ctypes.c_double)()
            o_size = ctypes.c_int()

            if ( index == 1):
       
                library.C_dft(i_real_C, i_imag_C, i_size, ctypes.byref(o_real_ptr), ctypes.byref(o_imag_ptr), ctypes.byref(o_size))
                self.dftTime[i] = (time.time() - start_time)
                

            if (index == 2):
                library.C_fft(i_real_C, i_imag_C, i_size, ctypes.byref(o_real_ptr), ctypes.byref(o_imag_ptr), ctypes.byref(o_size))
                
                self.fftTime[i] = (time.time() - start_time)
                
        
        if (index == 1):
            self.widget.plot(self.N, self.dftTime, name = "DFT", pen = "r")
            
        
        if (index == 2):
            self.widget.plot(self.N, self.fftTime, name = "FFT", pen = "b")

        if (index == 3):
            self.widget.clear()
            self.widget_2.clear()
            

    def plot_error (self):
        self.i_size = len(self.i_real)

        doublesArray = ctypes.c_double *self.i_size
        i_real_C = doublesArray.from_address(self.i_real.ctypes.data)
        i_imag_C = doublesArray.from_address(self.i_imag.ctypes.data)

        o_real_ptr = ctypes.POINTER(ctypes.c_double)()
        o_imag_ptr = ctypes.POINTER(ctypes.c_double)()
        o_size = ctypes.c_int()

        library.C_fft(i_real_C, i_imag_C, self.i_size, ctypes.byref(o_real_ptr), ctypes.byref(o_imag_ptr), ctypes.byref(o_size))


        fft_o_real = o_real_ptr[:o_size.value]
        fft_o_imag = o_imag_ptr[:o_size.value]

        

        library.C_dft(i_real_C, i_imag_C, self.i_size, ctypes.byref(o_real_ptr), ctypes.byref(o_imag_ptr), ctypes.byref(o_size))
        
        dft_o_real = o_real_ptr[:o_size.value]
        dft_o_imag = o_imag_ptr[:o_size.value]

        error_real =  np.subtract(dft_o_real ,fft_o_real)
        error_imag =  np.subtract(dft_o_imag ,fft_o_imag)
        error = np.multiply(error_real, error_imag)
        self.error_array = error[0:11]

        print("error :",self.error_array)
        self.widget_2.plot(self.N, self.error_array, name = "error", pen = "r")
                
def main():
        app = QApplication(sys.argv)
        window = MainApp()
        window.show()
        sys.exit(app.exec_())


if __name__ == '__main__':
    main()

    
