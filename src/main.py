#!/usr/bin/env python3

from src.Simulation import mainn, pa
import sys
from sys import argv
from src.myerror import FuncError
from src.my import manualhelp

def main_function():
    mygeterro = pa
    if mygeterro.py(sys.argv) == 84:
        exit(84)
    
    mygeterror = FuncError()

    if mygeterror.needHelp(sys.argv):
        manualhelp()
    elif mygeterror.allerror(sys.argv) == 84:
        exit(84)
    else:
        simulation = mainn()
        simulation.start()

if __name__ == '__main__':
    main_function()