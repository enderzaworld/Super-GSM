import os
import sys

pid = str(os.getpid())
pidfile = "/tmp/mydaemon.pid"

if os.path.isfile(pidfile):
    print ("%s already exists, exiting" % pidfile)
    sys.exit()
file(pidfile, 'w').write(pid)
#try:
#    # Do some actual work here
#finally:
os.unlink(pidfile)
