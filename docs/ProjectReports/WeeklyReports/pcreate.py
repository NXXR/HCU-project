# pcreate.py

import sys
import os
import glob

if len(sys.argv) > 1:
    for arg in sys.argv[1:]:
        if os.path.isfile(sys.argv[1]):
            os.system("pandoc -t slidy -s " + sys.argv[1] + " -o " + sys.argv[1][:-3] + ".html --self-contained --metadata pagetitle=\""+sys.argv[1][:-3]+"\"")
        elif len(sys.argv[1]) == 2:
            number = sys.argv[1]
            file = glob.glob("Week" + sys.argv[1] + "*.md")
            os.system("pandoc -t slidy -s " + file[0] + " -o " + file[0][:-3] + ".html --self-contained --metadata pagetitle=\""+file[0][:-3]+"\"")
        else:
            print("invalid argument \""+arg+"\" skipping...")
else:
    number = input("Week Number (2 digits): ")
    if len(number) == 2 and number.isdigit():
        file = glob.glob("Week" + sys.argv[1] + "*.md")
        os.system("pandoc -t slidy -s " + file[0] + " -o " + file[0][:-3] + ".html --self-contained --metadata pagetitle=\""+file[0][:-3]+"\"")