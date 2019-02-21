# HOTSPOT MODULE
# utility script containing all the hotspot related functions

from app.utils.log import Log
import subprocess
from os.path import isfile
import time

class Hotspot():
	def __init__(self,interface,ssid,key_mgmt,pswd):
		self.log=Log()
		self._interface=interface
		self._ssid=ssid
		self._key_mgmt=key_mgmt
		self._pswd=pswd
		self._hostapd='/etc/hostapd/hostapd.conf'
		self._dnsmasq='/etc/dnsmasq.conf'

	def create(self):
		try:
			self.log.print("Creating Hotspot: "+self._ssid+"...","OK")

			return True
		except Exception as e:
			return False

	def destroy(self):
		try:
			self.log.print("Destorying Hotspot: "+self._ssid+"...","OK")
			return True
		except Exception as e:
			return False