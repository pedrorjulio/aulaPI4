import serial
import time
                                 # add Serial library for Serial c$

Arduino_Serial = serial.Serial('/dev/ttyACM0',9600)  #Create Serial port object$

while 1:
	time.sleep(1)
	Arduino_Serial.write('1')             #send 1 to arduino
	print ("LED ON")
	time.sleep(1)
	Arduino_Serial.write('2')
	print ("LED OFF")        
