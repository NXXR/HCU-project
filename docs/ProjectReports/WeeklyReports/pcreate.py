# pcreate.py

import sys
import os
import glob

if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        if os.path.isfile(arg):
            os.system("pandoc -t slidy -s " + arg + " -o " + arg[:-3] + ".html --self-contained --metadata pagetitle=\"" + arg[:-3] + "\"")
        elif len(arg) == 2:
            file = glob.glob("Week" + arg + "*.md")
            os.system("pandoc -t slidy -s " + file[0] + " -o " + file[0][:-3] + ".html --self-contained --metadata pagetitle=\"" + file[0][:-3] + "\"")
        else:
            print("invalid argument \"" + arg + "\" skipping...")
else:
    number = input("Week Number (2 digits): ")
    if len(number) == 2 and number.isdigit():
        file = glob.glob("Week" + number + "*.md")
        os.system("pandoc -t slidy -s " + file[0] + " -o " + file[0][:-3] + ".html --self-contained --metadata pagetitle=\""+file[0][:-3]+"\"")