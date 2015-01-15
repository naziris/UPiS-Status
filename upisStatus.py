#!/usr/bin/python
# Kyriakos Naziris / University of Portsmouth / kyriakos@naziris.co.uk

import smbus
i2c = smbus.SMBus(1)

def pwr_mode():
	row = i2c.read_word_data(0x6a, 0x00)
	row = "%02x "%(row,)
	output = (row[-2:]).strip()
	if (output == '1'):
		return "External Cable Powering (EPR)"
	elif (output == '2'):
		return "USB Cable Powering"
	elif (output == '3'):
		return "Raspberry Pi Powering"
	elif (output == '4'):
		return "Battery Powering"
	elif (output == '5'):
		return "Battery Low Powering"
	elif (output == '6'):
		return "CPR Mode"
	elif (output =='7'):
		return "BPR Mode"
	else:
		return "Reading Error"

def bat_level():
	row = i2c.read_word_data(0x6a, 0x01)
	row = "%02x "%(row,)
	return (float(row) / 100)

def rpi_level():
	row = i2c.read_word_data(0x6a, 0x03)
	row = "%02x "%(row,)
	return (float(row) / 100)

def usb_level():
	row = i2c.read_word_data(0x6a, 0x05)
	row = "%02x "%(row,)
	return (float(row) / 100)

def epr_level():
	row = i2c.read_word_data(0x6a, 0x07)
	row = "%02x "%(row,)
	return (float(row) / 100)

def crn_level():
	row = i2c.read_word_data(0x6a, 0x09)
	row = "%02x "%(row,)
	return row

def version():
	row = i2c.read_word_data(0x6b, 0x00)
	row = "%02x "%(row,)
	return float(int(row, 16)) / 100 # int(row,16) is converting the hex string into an integer

print "***********************************"
print "*","Powering Mode:",pwr_mode(),"*"
print "*","Battery Voltage:", bat_level(),"V", "        *"
print "*","RPi Voltage:" , rpi_level(),"V","            *"
print "*","USB Voltage:" , usb_level(),"V","            *"
print "*","EPR Voltage:" , epr_level(),"V", "            *"
print "*","Current:", crn_level(),"mA", "               *"
print "*","UPiS Firmware:",version(),"            *"
print "***********************************"