# STARTUP SCRIPT
# to check root privileges and initialize boot process

from bootloader.boot import Boot
import os
import sys

def run():
	if(os.geteuid()!=0):
		print('Root privileges required!')
		print('Run this app as root or with sudo')
		sys.exit(0)
	boot=Boot()
	boot.start()
	return 0

if __name__ == "__main__":
	run()