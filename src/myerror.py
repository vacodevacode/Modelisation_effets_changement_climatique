#!/usr/bin/env python3

import sys
class FuncError():

    def allerror(self, argv):
        
            if len(sys.argv) != 2:
                exit(84)
            if sys.argv[1] == "-h":
                exit(0)
    
    def needHelp(self, argv):

        if "-h" in argv or "--help" in argv:
            return 1
        return 0