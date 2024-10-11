#!/usr/bin/env python3

from statistics import *
import sys
import math
import random

class pa():

    def py(argv):
            
        if (len(argv) == 1):
            return 84

class mainn:
    def __init__(self):
        self._T = 0
        self._tpp = []
        self._Lastr = 0.0
        self._r = 0.0
        self._g = 0.0
        self._s = 0.0
        self._period = 0
        self._temp = []
    
    def gestionofprogram(self):
        if not sys.argv[1].isdigit():
            exit(84)
        else:
            self._period = int(sys.argv[1])
    
    def myTermin(self, log):
        try:
            input_temp = float(log)
        except ValueError:
            exit(84)
        self._temp.append(input_temp)
        self.myfirstval(input_temp)
        self.mysecondval(input_temp)
        self.mylastval(input_temp)
        self.myshowbrainmsg()


    def myinterface(self):
        while True:
            log = input()
            self.myTermin(log)
    
    def myfirstval(self, log):
        self.myfirstTemperat()
        if (len(self._temp) >= self._period):
          self.mymeteofunc(log)
    
    def mysecondval(self, log):
        self.mysecondTemperat()
        if (len(self._temp) >= self._period):
          self.mymeteofunc(log)

    def mylastval(self, log):
        self.mylastTemperat(log)
        if (len(self._temp) >= self._period):
          self.mymeteofunc(log)
    
    def myfirstTemperat(self):
        if len(self._temp) > self._period:
            self._g = 0
            index = len(self._temp) - self._period
            self.mycheckTemp(index)
        else:
            self._g = "nan"
    
    def mycheckTemp(self, index):
        if len(self._temp) > self._period:
            for i in range(index, len(self._temp)):
                n = self._temp[i] - self._temp[i - 1]
                self._g += n if n > 0 else 0
            if self._period != 0:
                self._g /= self._period
            else:
                self._g = 0
        else: 
            self._g = "nan"

    def mysecondTemperat(self):
        var1 = 0
        if len(self._temp) > self._period:
            self.mychecksecondTemp()
        else:
            self._r = "nan"
    
    def mychecksecondTemp(self):
        if self._r != "nan":
            self._Lastr = self._r
        var1 = self._temp[len(self._temp) - self._period - 1]
        var2 = self._temp[-1]
        self.mysecureTemp(var1, var2)
    
    def mysecureTemp(self, var1, var2):
        if var1 == 0:
            self._r = int(0)
        if var2 == 0:
            self._r = int(0)
        else:
            self._r = int((round((var2-var1)/var1*100)))

    def mylastTemperat(self, log):
        if len(self._temp) >= self._period:
            x = 0
            y = 0
            for temp in self._temp[-self._period:]:
                x += temp
                y += temp ** 2
            self._s = math.sqrt(y / self._period - pow(x / self._period, 2))
        else:
            self._s = "nan"
    
    def myswitch(self):
        if self._r != "nan":
            if self._Lastr < 0 and self._r > 0:
                return 1
            else:
                return self._Lastr > 0 and self._r < 0
        return 0
    
    def mytchektempswi(self):
        if self.myswitch():
            return 1
        else:
            return 0

    def myalltemp(self):
        TempArray = list()
        LastPeriodeValue = len(self._temp) - self._period
        for i in range(LastPeriodeValue, len(self._temp)):
            TempArray.append(self._temp[i])
        TempArray.sort()
        return TempArray
    
    def mymeteofunc(self, log):
        try:
            val = self.myalltemp()
            M = median(val)
            if len(val) % 2 == 0:
                Q1 = median(val[:len(val)//2])
                Q3 = median(val[len(val)//2:])
            else:
                Q1 = median(val[:len(val)//2])
                Q3 = median(val[len(val)//2+1:])
            InterQ = Q3 - Q1
            minimus = InterQ * 0.8
            minimus = Q1 - minimus
            mSup = Q3 + minimus
            self.allo(log, minimus, mSup)
        except:
            print(f"error")

    def allo(self, log, minimus, mSup):
        if (log < minimus or log > mSup):
            self._tpp.append(log)
    
    def brainmsgfunc(self):
        if (self._r != "nan" and self._g != "nan" and self._s != "nan"):
            Weather_message = "g=" + str(round(self._g, 2)) + "\tr=" + str(round(self._r, 2)) + "%\ts=" + ("%.2f" % self._s)
            if (self.mytchektempswi()):
                Weather_message += "\ta switch occurs"
                self._T += 1
            return Weather_message
        else:
            if self._r == "nan" and self._g == "nan" and self._s != "nan":
                return "g=nan\tr=nan\ts=" + "%.2f" % self._s
            else:
                return "g=nan\tr=nan%\ts=nan"
    
    def myshowbrainmsg(self):
        Weather_message = self.brainmsgfunc()
        print(Weather_message)

    def start(self):
        self.gestionofprogram()
        self.myinterface()