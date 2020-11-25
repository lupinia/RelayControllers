#	BloodLights Relay Controllers
#	Utility Functions
#	By Kjatar Tavishen and Natasha L.
#	github.com/kjatar | github.com/lupinia | www.lupinia.net

import os
import serial
import sys

from time import sleep

# Initialize the serial port interface
# Returns a serial.Serial() object after the settings have been applied
def get_serial_interface():
	ser = serial.Serial()
	ser.baudrate = 9600
	ser.bytesize = serial.EIGHTBITS #number of bits per bytes
	ser.parity = serial.PARITY_NONE #set parity check: no parity
	ser.stopbits = serial.STOPBITS_ONE #number of stop bits
	ser.timeout = 2            #timeout block read
	ser.xonxoff = False     #disable software flow control
	ser.rtscts = False     #disable hardware (RTS/CTS) flow control
	ser.dsrdtr = False       #disable hardware (DSR/DTR) flow control
	ser.writeTimeout = 2 #timeout for write
	
	return ser

# Send a pair of serial commands
# Parameters:
#	port:  The hardware address for the port to use (example:  /dev/ttyUSB0)
#	command1:  The first command to send, before the delay
#	command2:  The second command to send, after the delay
#	serial_obj:  If the serial port is already open (such as for bulk operations), pass it here to avoid reinitialization
#	delay:  Use this parameter to override the default delay between command1 and command2
def relay_command(port, command1, command2, serial_obj=False, delay=0.25):
	success = False		# Primary return value; True if everything worked
	error = ''			# Secondary return value, provide info if success == False
	close_when_complete = False
	
	# If you want to validate the port, command1, and command2 inputs, do it here
	
	try:
		if not serial_obj:
			# If there's already a serial interface in use, it can be passed to this function
			# If not, we'll create our own
			# NOTE: If the serial interface needs to be closed manually, add a variable to do that!
			serial_obj = get_serial_interface()
			close_when_complete = True
		
		# Open the port
		if(serial_obj.port != port):
			serial_obj.port = port
		
		if not serial_obj.is_open:
			serial_obj.open()
		
		# Send the commands!
		serial_obj.write(bytearray.fromhex(command1))
		sleep(delay)
		serial_obj.write(bytearray.fromhex(command2))
		
		# If this isn't a bulk operation, let's clean things up by closing the port when we're done
		if close_when_complete:
			serial_obj.close()
		
		# All done!
		success = True
	
	except Exception as e:
		exc_type, value, traceback = sys.exc_info()
		error = "%s error:  %s" % (exc_type, value)
	
	return (success, error)





