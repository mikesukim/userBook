import sys, os
INTERP = "/home/mikesungunkim/venv/bin/python2.7"
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())

sys.path.append('userBookFlask')
from userBookFlask.app import app as application
