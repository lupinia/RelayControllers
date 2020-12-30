#	BloodLights Relay Controllers
#	Utility Functions
#	By Kjatar Tavishen and Natasha L.
#	github.com/kjatar | github.com/lupinia | www.lupinia.net

import settings

import serial
import sys

from time import sleep

# Initialize the serial port interface
# Returns a serial.Serial() object after the settings have been applied
def get_serial_interface():
	ser = serial.Serial()
	ser.baudrate = settings.baudrate
	ser.bytesize = settings.bytesize			#number of bits per bytes
	ser.parity = settings.parity				#set parity check: no parity
	ser.stopbits = settings.stopbits			#number of stop bits
	ser.timeout = settings.timeout				#timeout block read
	ser.xonxoff = settings.xonxoff				#disable software flow control
	ser.rtscts = settings.rtscts				#disable hardware (RTS/CTS) flow control
	ser.dsrdtr = settings.dsrdtr				#disable hardware (DSR/DTR) flow control
	ser.writeTimeout = settings.writeTimeout	#timeout for write
	
	return ser

# Send a pair of serial commands
# Parameters:
#	port:  The hardware address for the port to use (example:  /dev/ttyUSB0)
#	command1:  The first command to send, before the delay
#	command2:  The second command to send, after the delay
#	serial_obj:  If the serial port is already open (such as for bulk operations), pass it here to avoid reinitialization
#	delay:  Use this parameter to override the default delay between command1 and command2
def relay_command(port, command1, command2, serial_obj=False, delay=settings.command_delay):
	success = False		# Primary return value; True if everything worked
	error = ''			# Secondary return value, provide info if success == False
	close_when_complete = False
	
	# If you want to validate the port, command1, and command2 inputs, do it here
	
	try:
		if not serial_obj:
			# If there's already a serial interface in use, it can be passed to this function
			# If not, we'll create our own
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
	data_delay = data_item.get('delay', settings.command_delay)
	
	return (data_name, data_port, data_cmd1, data_cmd2, data_delay)

# Get the relevant fields of a specified relay in the data source
# This function assumes you have already run check_relay(), or are otherwise confident that the data is valid
def get_relay(id, data):
	id_int = int(id)
	data_item = data[id_int]
	
	return get_relay_fields(data_item)

# Cycle through all known relays and toggle them
# Parameters:
#	test_delay:  Amount of time to wait before proceeding to the next relay.  Uses the system default if not specified
#	live_status:  If True, print the name of each relay as it comes up in the test
def test_all_relays(live_status=True, test_delay=settings.command_delay):
	from data import relays
	test_output('Beginning test of all relays...', live_status)
	
	if len(relays) > 0:
		test_output('%i relays in list, beginning test...' % len(relays), live_status)
		
		# Open the serial interface here for greater efficiency
		ser = get_serial_interface()
		test_output('Serial interface created.', live_status)
		
		for relay in relays:
			# Step 1:  Grab all the fields we'll need for this relay
			# Storing the bulk of them in a dictionary means we can use my favorite notation later :)
			relay_params = {}
			cur_relay_name, relay_params['port'], relay_params['command1'], relay_params['command2'], relay_params['delay'] = get_relay_fields(relay)
			
			# Step 2:  Make sure the fields we need actually exist
			if relay_params['port'] and relay_params['command1'] and relay_params['command2']:
				test_output('Testing %s...' % cur_relay_name, live_status)
				
				# Time to actually do the commands!
				# Double-asterisk to send a dictionary as if it were function parameters is one of my favorite things about Python.
				# I'm not really sure why, it's just so neat!  ^.^
				relay_command(serial_obj=ser, **relay_params)
				
				# Wait a sec before going to the next one
				# Or a fraction of a sec
				# Or a bunch of secs
				# It's actually entirely up to you, I have no idea what you'll set this value to
				# You could've set it to an entire day between relay tests for all I know!
				# I mean, I don't know why you'd WANT to do that, but you COULD!
				sleep(test_delay)
			
			else:
				# Uh oh!  The important fields were blank!  Skipping this one.
				test_output('Skipping %s due to missing fields' % cur_relay_name, live_status)
	
	else:
		test_output('No relays available in list, nothing to test.', live_status)
	
	test_output('Relay test complete!', live_status)

# Saving myself from having to write "if live_status:" a million times in the previous function
def test_output(message='', live_status=True):
	if live_status and message:
		print message

