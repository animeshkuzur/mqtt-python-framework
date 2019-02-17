from bootloader.boot import Boot

def run():
	boot=Boot()
	boot.start()
	return 0

if __name__ == "__main__":
	run()