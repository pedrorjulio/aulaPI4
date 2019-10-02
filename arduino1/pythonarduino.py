import serial                                 # add Serial library for Serial c$

Arduino_Serial = serial.Serial('/dev/ttyACM0',9600)  #Create Serial port object$

while 1:

	input_data = raw_input()                  #waits until user enters data
	print "you entered", input_data           #prints the data for confirmation

	if (input_data == '1'):                   #if the entered data is 1 
		Arduino_Serial.write('1')             #send 1 to arduino
		print ("LED ON")

	if (input_data == '2'):
		Arduino_Serial.write('2')
		print ("LED OFF")        
