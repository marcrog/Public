import os
import sys

if len(sys.argv) >= 2:
    os.system("pyinstaller " + sys.argv[1] + " --onefile")
    os.system("mv dist/* ./")
    os.system("rm -r __pycache__ build dist *.spec")
    
