#	BloodLights Relay Controllers
#	Utility Functions
#	By Kjatar Tavishen and Natasha L.
#	github.com/kjatar | github.com/lupinia | www.lupinia.net

from data import command_delay

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
def relay_command(port, command1, command2, serial_obj=False, delay=command_delay):
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

# Check whether the data for a specified relay exists in the data source
# Returns True if relay exists and has valid data, False otherwise
# Parameters:
#	id:  The ID of the relay to check.  Should cast to an integer, and correspond to a list index that exists in the data parameter
#	data:  The data source to check.  Should ideally be a list containing dictionaries or other objects with named fields (should hypothetically work with a Django queryset too).
def check_relay(id, data):
	try:
		# Step 1:  id is probably a string, so let's find out if it's a valid integer
		id_int = int(id)
		
		# Step 2:  Find out if id is a valid list index, and grab the data item if possible
		data_item = data[id_int]
		
		# Step 3:  Check whether the important fields exist
		check_port = data['port']
		check_cmd1 = data['command1']
		check_cmd2 = data['command2']
		
		# Step 4:  Validation of data fields can go here; for now, we're done unless there was an exception.
		
		# If we're here, there were no exceptions thrown, which means this is a valid id and data set.
		return True
	
	except (ValueError, TypeError, KeyError, IndexError) as e:
		# The prior steps in this function throw intentional exceptions
		# If any of them are thrown, return False, because the parameters are invalid for the other functions
		return False

# Shortcut to extract and standardize the required data fields
def get_relay_fields(data_item):
	data_name = data_item.get('name', 'Relay %i' % id_int)
	data_port = data_item.get('port', False)
	data_cmd1 = data_item.get('command1', False)
	data_cmd2 = data_item.get('command2', False)
	data_delay = data_item.get('delay', command_delay)
	
	return (data_name, data_port, data_cmd1, data_cmd2, data_delay)

# Get the relevant fields of a specified relay in the data source
# This function assumes you have already run check_relay(), or are otherwise confident that the data is valid
def get_relay(id, data):
	id_int = int(id)
	data_item = data[id_int]
	
	return get_relay_fields(data_item)



