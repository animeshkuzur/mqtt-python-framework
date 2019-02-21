# WIFI MODULE
# utility script containing all the wifi related functions

from app.utils.log import Log
import subprocess
from os.path import isfile
import time

class Wifi():
	def __init__(self,interface,ssid,key_mgmt,pswd):
		self.log=Log()
		self._interface=interface
		self._ssid=ssid
		self._key_mgmt=key_mgmt
		self._pswd=pswd
		self._wpa_supplicant='/etc/wpa_supplicant/wpa_supplicant.conf'

	def connect(self):
		try:
			data=''
			self.log.print("Connecting to "+self._ssid+"...","OK")
			if(self._key_mgmt=='TRUE'):
				dat = subprocess.Popen(['wpa_passphrase',self._ssid,self._pswd], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
				for line in dat.stdout:
					line=line.decode()
					data=data+line
				#data = 'network={\nssid="'+self._ssid+'"\npsk="'+self._pswd+'"\n}\n'
			else:
				data = 'network={\nssid="'+self._ssid+'"\nkey_mgmt=NONE\n}\n'
			if(self.write_config(data)==False):
				self.log.print("Unable to connect to wifi: "+self._ssid+"...","OK")
				return False
			ps = subprocess.Popen(['wpa_supplicant','-q','-B','-i',self._interface,'-D','nl80211,wext','-c',self._wpa_supplicant], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
			time.sleep(15)
			self.log.print("Connection to wifi: "+self._ssid+" successful...","OK")
			return True
		except subprocess.CalledProcessError as e:
			self.log.print("Error Initiating a new connection with: "+self._ssid+"...",format(e))
			return False
		except Exception as e:
			self.log.print("Unable to connect...",e)
			return False

	def disconnect(self):
		try:
			self.log.print("Disconnecting from the current wifi network...","OK")
			ps = subprocess.Popen(['killall','wpa_supplicant'], stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
			time.sleep(5)
			return True
		except Exception as e:
			self.log.print("Unable to disconnect...",e)
			return False

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
					ssid=''
					for r in row:
						if(r=='SSID:'):
							continue
						ssid=ssid+' '+r
					if(ssid[1:]==self._ssid):
						self.log.print(self._interface+" connected to...",ssid[1:])
						return 1
					else:
						self.log.print(self._interface+" connected to...",ssid[1:])
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

	def scan(self):
		try:
			self.log.print("Checking the availabilitly of "+self._ssid+"...","OK")
			ps = subprocess.Popen(['iw',self._interface,'scan'],stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
			for line in ps.stdout:
				#print(line.decode())
				if('command failed: Network is down (-100)' in line.decode()):
					self.log.print("Wireless Interface "+self._interface+" down...","OK")
					pps = subprocess.Popen(['ip','link','set',self._interface,'up'],stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
					time.sleep(5)
					self.log.print("Enabling Wireless Interface "+self._interface+" up...","OK")
					return False
				else:
					break
			output = subprocess.check_output(('grep', 'SSID'), stdin=ps.stdout)
			for line in (output.decode()).split('\n'):
				row = line.replace('\t','')
				row = row.split(': ')
				if(row[1]==self._ssid):
					self.log.print("ESSID "+self._ssid+" found...","OK")
					return True
			return False

		except subprocess.CalledProcessError as e:
			self.log.print("Unable to find: "+self._ssid+"...",format(e))
			return False
		except Exception as e:
			self.log.print("Unable to find: "+self._ssid+"...",format(e))
			return False

	def write_config(self,data):
		try:
			buf=''
			if(isfile(self._wpa_supplicant)):
				with open(self._wpa_supplicant,'r') as cfile:
					for fline in cfile:
						if('network' in fline):
							break
						buf=buf+fline
				with open(self._wpa_supplicant,'w') as conf:
					conf.write(buf+data)
				return True
			else:
				self.log.print("Unable to find: "+self._wpa_supplicant+"...",e)
				return False
			return True
		except Exception as e:
			self.log.print("Unable to write: "+self._wpa_supplicant+"...",format(e))
			return False