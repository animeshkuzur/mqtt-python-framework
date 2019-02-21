# BOOTLOADER SCRIPT
# configures the wifi and then starts the app

from config.config import CONFIG
from app.utils.log import Log
from app.utils.wifi import Wifi
from app.utils.hotspot import Hotspot
from app.app import App

class Boot():
	def __init__(self):
		self.log=Log()
		self.log.create_log()
		self.log.print("Log file created...","OK")

	def start(self):
		self.log.print("validating wifi credentials...","OK")
		while True:
			if(self.manage_wifi()):
				break
		self.log.print("Configuration complete...","OK")
		self.log.print("Starting new instance of the app...","OK")
		app=App(CONFIG['app_name'],CONFIG['app_key'],CONFIG['app_version'])
		app.start()

	def manage_wifi(self):
		wifi=Wifi(CONFIG['interface'],CONFIG['wifi_ssid'],CONFIG['wifi_key_mgmt'],CONFIG['wifi_password'])
		status=wifi.status()
		if(status>=0):
			if(status==1):
				return True
			if(status==0):
				if(wifi.scan()):
					wifi.disconnect()
					wifi.connect()
					return False
				else:
					self.log.print("Creating a hotstop to configure the device...","OK")
					hotspot=Hotspot(CONFIG['interface'],CONFIG['hotspot_ssid'],CONFIG['hotspot_key_mgmt'],CONFIG['hotspot_password'])
					if(hotspot.create()):
						return True
					else:
						self.log.print("Unable to create the hotspot...","OK")
						return False
		else:
			if(wifi.scan()):
				wifi.disconnect()
				wifi.connect()
				return False
			else:
				self.log.print("Creating a hotstop to configure the device...","OK")
				hotspot=Hotspot(CONFIG['interface'],CONFIG['hotspot_ssid'],CONFIG['hotspot_key_mgmt'],CONFIG['hotspot_password'])
				if(hotspot.create()):
					return True
				else:
					self.log.print("Unable to create the hotspot...","OK")
					return False


