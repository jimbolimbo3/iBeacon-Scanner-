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