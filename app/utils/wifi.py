from app.utils.log import Log
import subprocess

class Wifi():
	def __init__(self,interface,ssid,key_mgmt,pswd):
		self.log=Log()
		self._interface=interface
		self._ssid=ssid
		self._key_mgmt=key_mgmt
		self._pswd=pswd

	def connect(self):
		try:
			self.log.print("Connecting to "+self._ssid+"...","OK")
			if(self._key_mgmt=='TRUE'):
				ps = subprocess.Popen([''], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
				#output = subprocess.check_output()

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

	def status(self):
		try:
			flag=False
			self.log.print("Checking for wifi status...","OK")
			ps = subprocess.Popen(['iw',self._interface,'link'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
			for line in ps.stdout:
				row = line.decode()
				row = row.replace('\t','')
				row = row.replace('\n','')
				row = row.split(' ')
				if(row[0]=='Not'):
					self.log.print(self._interface+" not connected to any wifi",row[0]+" "+row[1])
					return -1
				if(row[0]=='Connected'):
					flag=True
					continue
				if(flag):
					flag=False
					if(row[1]==self._ssid):
						self.log.print(self._interface+" connected to...",row[1])
						return 1
					else:
						self.log.print(self._interface+" connected to...",row[1])
						return 0
			#output = subprocess.check_output(('grep', self._ssid), stdin=ps.stdout)
			#self.log.print("Wifi SSID: "+self._ssid+" found...",(output.decode()).replace('\n',''))
			#return True
		except subprocess.CalledProcessError as e:
			self.log.print(self._interface+" not connected to: "+self._ssid+"...",format(e))
			return 0
		except Exception as e:
			self.log.print(self._interface+" not connected to: "+self._ssid+"...",e)
			return 0

	def check(self):
		try:
			self.log.print("Checking the availabilitly of "+self._ssid+"...","OK")
			ps = subprocess.Popen([])
		except subprocess.CalledProcessError as e:
			self.log.print("Unable to find: "+self._ssid+"...",format(e))
			return False
		except Exception as e:
			self.log.print("Unable to find: "+self._ssid+"...",format(e))
			return False
