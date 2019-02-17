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
		self.check_wifi()

	def check_wifi(self):
		wifi=Wifi(CONFIG['wifi_ssid'],CONFIG['wifi_key_mgmt'],CONFIG['wifi_password'])
		if(wifi.check()):
			app=App(CONFIG['app_name'],CONFIG['app_key'],CONFIG['app_version'])
			app.start()
		else:
			if(wifi.connect()):
				pass
			

