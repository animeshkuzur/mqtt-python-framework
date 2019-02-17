import json
from os.path import abspath, isfile
import sys

json_path = abspath("./config.json")

try:
	if(isfile(json_path)!=True):
		print('File not found: config.json')
		sys.exit()
	with open(json_path) as json_data:
		data = json.load(json_data)
except Exception as e:
	print('Failed to read file: config.json')
	print('Invalid json')
	print(e)
	sys.exit()

try:
	APP_NAME = data['app']['name']
	APP_DEBUG = data['app']['debug'].upper()
	APP_KEY = data['app']['key']
	APP_VERSION = data['app']['version']

	MYSQL_HOST = data['mysql']['host']
	MYSQL_USER = data['mysql']['user']
	MYSQL_PASSWORD = data['mysql']['password']
	MYSQL_DB = data['mysql']['database']

	WIFI_SSID = data['wifi']['ssid']
	WIFI_KEY_MGMT = data['wifi']['key_mgmt'].upper()
	WIFI_PASSWORD = None
	if(WIFI_KEY_MGMT=='TRUE'):
		WIFI_PASSWORD = data['wifi']['password']

	HOTSPOT_SSID = data['hotspot']['ssid']
	HOTSPOT_KEY_MGMT = data['hotspot']['key_mgmt'].upper()
	HOTSPOT_PASSWORD = None
	if(HOTSPOT_KEY_MGMT=='TRUE'):
		HOTSPOT_PASSWORD = data['hotspot']['password']

	BROKER_HOST = data['mqtt_broker']['host']
	BROKER_PORT = data['mqtt_broker']['port']
	BROKER_KEY_MGMT = data['mqtt_broker']['key_mgmt']
	BROKER_USERNAME = None
	BROKER_PASSWORD = None
	if(BROKER_KEY_MGMT=='TRUE'):
		BROKER_USERNAME = data['mqtt_broker']['username']
		BROKER_PASSWORD = data['mqtt_broker']['password']

	CONFIG={
		'app_name':APP_NAME,
		'app_debug':APP_DEBUG,
		'app_key':APP_KEY,
		'app_version':APP_VERSION,

		'mysql_host':MYSQL_HOST,
		'mysql_user':MYSQL_USER,
		'mysql_password':MYSQL_PASSWORD,
		'mysql_db':MYSQL_DB,

		'wifi_ssid':WIFI_SSID,
		'wifi_key_mgmt':WIFI_KEY_MGMT,
		'wifi_password':WIFI_PASSWORD,

		'hotspot_ssid':HOTSPOT_SSID,
		'hotspot_key_mgmt':HOTSPOT_KEY_MGMT,
		'hotspot_password':HOTSPOT_PASSWORD,

		'broker_host':BROKER_HOST,
		'broker_port':BROKER_PORT,
		'broker_key_mgmt':BROKER_KEY_MGMT,
		'broker_username':BROKER_USERNAME,
		'broker_password':BROKER_PASSWORD
	}
except Exception as e:
	print('Failed to read file: config.json')
	print('Invalid config')
	print(e)
	sys.exit()