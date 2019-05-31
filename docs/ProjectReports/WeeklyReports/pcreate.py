# pcreate.py

import sys
import os
import glob

if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        if os.path.isfile(arg):
            os.system("pandoc -t slidy -s " + arg + " -o " + arg[:-3] + ".html --self-contained --metadata pagetitle=\"" + arg[:-3] + "\"")
        elif len(arg) == 2 and arg.isdigit():
            file = glob.glob("Week" + arg + "*.md")
            os.system("pandoc -t slidy -s " + file[0] + " -o " + file[0][:-3] + ".html --self-contained --metadata pagetitle=\"" + file[0][:-3] + "\"")
        else:
            print("invalid argument \"" + arg + "\" skipping...")
else:
    number = input("Week Number (2 digits or x to cancel): ")
    numlist = number.split()
    for item in numlist:
        if len(item) == 2 and item.isdigit():
            file = glob.glob("Week" + item + "*.md")
            print("creating slides for Week " + item)
            os.system("pandoc -t slidy -s " + file[0] + " -o " + file[0][:-3] + ".html --self-contained --metadata pagetitle=\"" + file[0][:-3] + "\"")
            print("DONE")
        else:
            print("invalid argument \"" + item + "\" skipping...")
