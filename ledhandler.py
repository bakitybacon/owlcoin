import time
import os
import signal
import sys

args = sys.argv
if len(args) != 2:
  print "usage: ledhandler.py signal"

pidfile = open("/home/pi/ledpid","r")
pid = int(pidfile.readline())

#print pid

sig = sys.argv[1]

sig = int(sig)
#print sig

if sig == 0:
  os.kill(pid, signal.SIGUSR1)
#  print "sent to", pid
elif sig == 1:
  os.kill(pid, signal.SIGUSR2)
elif sig == 2:
  os.kill(pid, signal.SIGALRM)

