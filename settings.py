#	BloodLights Relay Controllers
#	Configuration Values
#	By Kjatar Tavishen and Natasha L.
#	github.com/kjatar | github.com/lupinia | www.lupinia.net
#	=================

from serial import EIGHTBITS, PARITY_NONE, STOPBITS_ONE

#	Default delay between commands
command_delay = 0.25

#	PySerial configuration values
serial_baudrate = 9600
serial_bytesize = EIGHTBITS		#number of bits per bytes
serial_parity = PARITY_NONE		#set parity check: no parity
serial_stopbits = STOPBITS_ONE	#number of stop bits
serial_timeout = 2				#timeout block read
serial_xonxoff = False			#disable software flow control
serial_rtscts = False			#disable hardware (RTS/CTS) flow control
serial_dsrdtr = False			#disable hardware (DSR/DTR) flow control
serial_writeTimeout = 2			#timeout for write
