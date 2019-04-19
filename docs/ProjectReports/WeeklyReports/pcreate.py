# pcreate.py

import sys
import os
import glob

file = glob.glob("Week"+sys.argv[1]+"*.md")
os.system("pandoc -t slidy -s "+file[0]+" -o "+file[0][:-3]+".html --self-contained")
