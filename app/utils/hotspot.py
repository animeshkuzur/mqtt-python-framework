from app.utils.log import Log

class Hotspot():
	def __init__(self,ssid,key_mgmt,pswd):
		self.log=Log()
		self._ssid=ssid
		self._key_mgmt=key_mgmt
		self._pswd=pswd

	def create(self):
		try:
			self.log.print("Creating Hotspot: "+self._ssid+"...","OK")
		except Exception as e:
			pass

	def destroy(self):
		try:
			self.log.print("Destorying Hotspot: "+self._ssid+"...","OK")
		except Exception as e:
			pass