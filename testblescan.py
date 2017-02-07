# test BLE Scanning software
# jcs 6/8/2014

import blescan   ###uso blescan.py
import sys

import bluetooth._bluetooth as bluez

dev_id = 0
try:
	sock = bluez.hci_open_dev(dev_id)
	print "ble thread started"

except:
	print "error accessing bluetooth device..."
    	sys.exit(1)

blescan.hci_le_set_scan_parameters(sock)
blescan.hci_enable_le_scan(sock)

while True:
	returnedList = blescan.parse_events(sock, 10)
	print "----------"
	for beacon in returnedList:
		print beacon

##PARTE LED
import Adafruit_BBIO.GPIO as GPIO #import GPIO Library
outPin="P9_12"                    #set outPin to "P9_12" barra a sinistra con in alto la porta ethernet
GPIO.setup(outPin,GPIO.OUT)       #make outPin an Output
from time import sleep            #so we can use delays
for i in range(0,5):              #loop 5 times
    GPIO.output(outPin, GPIO.HIGH) # Set outPin HIGH
    sleep(3)                       #Pause
    GPIO.output(outPin, GPIO.LOW) # Set outPin LOW
    sleep(3)                       #Wait
GPIO.cleanup()                     #Release your pins
