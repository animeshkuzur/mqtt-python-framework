from app.utils.log import Log
import subprocess

class Wifi():
	def __init__(self,ssid,key_mgmt,pswd):
		self.log=Log()
		self._ssid=ssid
		self._key_mgmt=key_mgmt
		self._pswd=pswd

	def connect(self):
		try:
			self.log.print("Connecting to "+self._ssid+"...","OK")
			if(self._key_mgmt=='TURE'):
				pass
			else:
				pass
			return True
		except Exception as e:
			self.log.print("Unable to connect...",e)
			return False

	def disconnect(self):
		try:
			pass
		except Exception as e:
			pass

	def check(self):
		try:
			self.log.print("Checking for wifi...","OK")
			ps = subprocess.Popen(['iwconfig'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
			output = subprocess.check_output(('grep', self._ssid), stdin=ps.stdout)
			self.log.print("Wifi SSID: "+self._ssid+" found...",format(output))
			return True
		except subprocess.CalledProcessError as e:
			self.log.print("Unable to find: "+self._ssid+"...",format(e))
			return False
		except Exception as e:
			self.log.print("Unable to find: "+self._ssid+"...",e)
			return False
