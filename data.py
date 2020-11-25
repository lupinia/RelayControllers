#	BloodLights Relay Controllers
#	Static Relay Data
#	By Kjatar Tavishen and Natasha L.
#	github.com/kjatar | github.com/lupinia | www.lupinia.net

#	Default delay between commands
command_delay = 0.25

#	List of dictionaries, in lieu of a database source
#	Reference using the list index, starting with 1
#		Example:  relays[1].get('port', False)
#	Always use the dictionary's .get() method to retrieve these values
#	(Zero is intentionally left blank, for backward compatibility)
#	Format:
#		name:  String, optional, mainly for convenience
#		port:  String, serial port address
#		command1:  String, the first command to send, before the delay
#		command2:  String, the second command to send, after the delay
#		delay:  Float, optional; if present, this will override the default delay between command1 and command2.
relays = [{'name':'INVALID RELAY'},
	{ #1
		'name':'Relay 1',
		'port':'/dev/ttyUSB0',
		'command1':'3A 46 45 30 35 30 30 30 30 46 46 30 30 46 45 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 30 30 30 30 30 46 44 0D 0A',
	},
	{ #2
		'name':'Relay 2',
		'port':'/dev/ttyUSB0',
		'command1':'3A 46 45 30 35 30 30 30 31 46 46 30 30 46 44 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 31 30 30 30 30 46 43 0D 0A',
	},
	{ #3
		'name':'Relay 3',
		'port':'/dev/ttyUSB0',
		'command1':'3A 46 45 30 35 30 30 30 32 46 46 30 30 46 43 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 32 30 30 30 30 46 42 0D 0A',
	},
	{ #4
		'name':'Relay 4',
		'port':'/dev/ttyUSB0',
		'command1':'3A 46 45 30 35 30 30 30 33 46 46 30 30 46 42 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 33 30 30 30 30 46 41 0D 0A',
	},
	{ #5
		'name':'Relay 5',
		'port':'/dev/ttyUSB0',
		'command1':'3A 46 45 30 35 30 30 30 34 46 46 30 30 46 41 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 34 30 30 30 30 46 39 0D 0A',
	},
	{ #6
		'name':'Relay 6',
		'port':'/dev/ttyUSB0',
		'command1':'3A 46 45 30 35 30 30 30 35 46 46 30 30 46 39 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 35 30 30 30 30 46 38 0D 0A',
	},
	{ #7
		'name':'Relay 7',
		'port':'/dev/ttyUSB0',
		'command1':'3A 46 45 30 35 30 30 30 36 46 46 30 30 46 38 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 36 30 30 30 30 46 37 0D 0A',
	},
	{ #8
		'name':'Relay 8',
		'port':'/dev/ttyUSB0',
		'command1':'3A 46 45 30 35 30 30 30 37 46 46 30 30 46 37 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 37 30 30 30 30 46 36 0D 0A',
	},
	{ #9
		'name':'Relay 9',
		'port':'/dev/ttyUSB0',
		'command1':'3A 46 45 30 35 30 30 30 38 46 46 30 30 46 36 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 38 30 30 30 30 46 35 0D 0A',
	},
	{ #10
		'name':'Relay 10',
		'port':'/dev/ttyUSB0',
		'command1':'3A 46 45 30 35 30 30 30 39 46 46 30 30 46 35 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 39 30 30 30 30 46 34 0D 0A',
	},
	{ #11
		'name':'Relay 11',
		'port':'/dev/ttyUSB0',
		'command1':'3A 46 45 30 35 30 30 30 41 46 46 30 30 46 34 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 41 30 30 30 30 46 33 0D 0A',
	},
	{ #12
		'name':'Relay 12',
		'port':'/dev/ttyUSB0',
		'command1':'3A 46 45 30 35 30 30 30 42 46 46 30 30 46 33 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 42 30 30 30 30 46 32 0D 0A',
	},
	{ #13
		'name':'Relay 13',
		'port':'/dev/ttyUSB0',
		'command1':'3A 46 45 30 35 30 30 30 43 46 46 30 30 46 32 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 43 30 30 30 30 46 31 0D 0A',
	},
	{ #14
		'name':'Relay 14',
		'port':'/dev/ttyUSB0',
		'command1':'3A 46 45 30 35 30 30 30 44 46 46 30 30 46 31 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 44 30 30 30 30 46 30 0D 0A',
	},
	{ #15
		'name':'Relay 15',
		'port':'/dev/ttyUSB0',
		'command1':'3A 46 45 30 35 30 30 30 45 46 46 30 30 46 30 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 45 30 30 30 30 46 46 0D 0A',
	},
	{ #16
		'name':'Relay 16',
		'port':'/dev/ttyUSB0',
		'command1':'3A 46 45 30 35 30 30 30 46 46 46 30 30 46 46 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 46 30 30 30 30 46 45 0D 0A',
	},
	
	{ #17
		'name':'Relay 17',
		'port':'/dev/ttyUSB1',
		'command1':'3A 46 45 30 35 30 30 30 30 46 46 30 30 46 45 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 30 30 30 30 30 46 44 0D 0A',
	},
	{ #18
		'name':'Relay 18',
		'port':'/dev/ttyUSB1',
		'command1':'3A 46 45 30 35 30 30 30 31 46 46 30 30 46 44 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 31 30 30 30 30 46 43 0D 0A',
	},
	{ #19
		'name':'Relay 19',
		'port':'/dev/ttyUSB1',
		'command1':'3A 46 45 30 35 30 30 30 32 46 46 30 30 46 43 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 32 30 30 30 30 46 42 0D 0A',
	},
	{ #20
		'name':'Relay 20',
		'port':'/dev/ttyUSB1',
		'command1':'3A 46 45 30 35 30 30 30 33 46 46 30 30 46 42 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 33 30 30 30 30 46 41 0D 0A',
	},
	{ #21
		'name':'Relay 21',
		'port':'/dev/ttyUSB1',
		'command1':'3A 46 45 30 35 30 30 30 34 46 46 30 30 46 41 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 34 30 30 30 30 46 39 0D 0A',
	},
	{ #22
		'name':'Relay 22',
		'port':'/dev/ttyUSB1',
		'command1':'3A 46 45 30 35 30 30 30 35 46 46 30 30 46 39 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 35 30 30 30 30 46 38 0D 0A',
	},
	{ #23
		'name':'Relay 23',
		'port':'/dev/ttyUSB1',
		'command1':'3A 46 45 30 35 30 30 30 36 46 46 30 30 46 38 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 36 30 30 30 30 46 37 0D 0A',
	},
	{ #24
		'name':'Relay 24',
		'port':'/dev/ttyUSB1',
		'command1':'3A 46 45 30 35 30 30 30 37 46 46 30 30 46 37 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 37 30 30 30 30 46 36 0D 0A',
	},
	{ #25
		'name':'Relay 25',
		'port':'/dev/ttyUSB1',
		'command1':'3A 46 45 30 35 30 30 30 38 46 46 30 30 46 36 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 38 30 30 30 30 46 35 0D 0A',
	},
	{ #26
		'name':'Relay 26',
		'port':'/dev/ttyUSB1',
		'command1':'3A 46 45 30 35 30 30 30 39 46 46 30 30 46 35 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 39 30 30 30 30 46 34 0D 0A',
	},
	{ #27
		'name':'Relay 27',
		'port':'/dev/ttyUSB1',
		'command1':'3A 46 45 30 35 30 30 30 41 46 46 30 30 46 34 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 41 30 30 30 30 46 33 0D 0A',
	},
	{ #28
		'name':'Relay 28',
		'port':'/dev/ttyUSB1',
		'command1':'3A 46 45 30 35 30 30 30 42 46 46 30 30 46 33 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 42 30 30 30 30 46 32 0D 0A',
	},
	{ #29
		'name':'Relay 29',
		'port':'/dev/ttyUSB1',
		'command1':'3A 46 45 30 35 30 30 30 43 46 46 30 30 46 32 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 43 30 30 30 30 46 31 0D 0A',
	},
	{ #30
		'name':'Relay 30',
		'port':'/dev/ttyUSB1',
		'command1':'3A 46 45 30 35 30 30 30 44 46 46 30 30 46 31 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 44 30 30 30 30 46 30 0D 0A',
	},
	{ #31
		'name':'Relay 31',
		'port':'/dev/ttyUSB1',
		'command1':'3A 46 45 30 35 30 30 30 45 46 46 30 30 46 30 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 45 30 30 30 30 46 46 0D 0A',
	},
	{ #32
		'name':'Relay 32',
		'port':'/dev/ttyUSB1',
		'command1':'3A 46 45 30 35 30 30 30 46 46 46 30 30 46 46 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 46 30 30 30 30 46 45 0D 0A',
	},
	
	{ #33
		'name':'Relay 33',
		'port':'/dev/ttyUSB2',
		'command1':'3A 46 45 30 35 30 30 30 30 46 46 30 30 46 45 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 30 30 30 30 30 46 44 0D 0A',
	},
	{ #34
		'name':'Relay 34',
		'port':'/dev/ttyUSB2',
		'command1':'3A 46 45 30 35 30 30 30 31 46 46 30 30 46 44 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 31 30 30 30 30 46 43 0D 0A',
	},
	{ #35
		'name':'Relay 35',
		'port':'/dev/ttyUSB2',
		'command1':'3A 46 45 30 35 30 30 30 32 46 46 30 30 46 43 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 32 30 30 30 30 46 42 0D 0A',
	},
	{ #36
		'name':'Relay 36',
		'port':'/dev/ttyUSB2',
		'command1':'3A 46 45 30 35 30 30 30 33 46 46 30 30 46 42 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 33 30 30 30 30 46 41 0D 0A',
	},
	{ #37
		'name':'Relay 37',
		'port':'/dev/ttyUSB2',
		'command1':'3A 46 45 30 35 30 30 30 34 46 46 30 30 46 41 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 34 30 30 30 30 46 39 0D 0A',
	},
	{ #38
		'name':'Relay 38',
		'port':'/dev/ttyUSB2',
		'command1':'3A 46 45 30 35 30 30 30 35 46 46 30 30 46 39 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 35 30 30 30 30 46 38 0D 0A',
	},
	{ #39
		'name':'Relay 39',
		'port':'/dev/ttyUSB2',
		'command1':'3A 46 45 30 35 30 30 30 36 46 46 30 30 46 38 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 36 30 30 30 30 46 37 0D 0A',
	},
	{ #40
		'name':'Relay 40',
		'port':'/dev/ttyUSB2',
		'command1':'3A 46 45 30 35 30 30 30 37 46 46 30 30 46 37 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 37 30 30 30 30 46 36 0D 0A',
	},
	{ #41
		'name':'Relay 41',
		'port':'/dev/ttyUSB2',
		'command1':'3A 46 45 30 35 30 30 30 38 46 46 30 30 46 36 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 38 30 30 30 30 46 35 0D 0A',
	},
	{ #42
		'name':'Relay 42',
		'port':'/dev/ttyUSB2',
		'command1':'3A 46 45 30 35 30 30 30 39 46 46 30 30 46 35 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 39 30 30 30 30 46 34 0D 0A',
	},
	{ #43
		'name':'Relay 43',
		'port':'/dev/ttyUSB2',
		'command1':'3A 46 45 30 35 30 30 30 41 46 46 30 30 46 34 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 41 30 30 30 30 46 33 0D 0A',
	},
	{ #44
		'name':'Relay 44',
		'port':'/dev/ttyUSB2',
		'command1':'3A 46 45 30 35 30 30 30 42 46 46 30 30 46 33 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 42 30 30 30 30 46 32 0D 0A',
	},
	{ #45
		'name':'Relay 45',
		'port':'/dev/ttyUSB2',
		'command1':'3A 46 45 30 35 30 30 30 43 46 46 30 30 46 32 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 43 30 30 30 30 46 31 0D 0A',
	},
	{ #46
		'name':'Relay 46',
		'port':'/dev/ttyUSB2',
		'command1':'3A 46 45 30 35 30 30 30 44 46 46 30 30 46 31 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 44 30 30 30 30 46 30 0D 0A',
	},
	{ #47
		'name':'Relay 47',
		'port':'/dev/ttyUSB2',
		'command1':'3A 46 45 30 35 30 30 30 45 46 46 30 30 46 30 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 45 30 30 30 30 46 46 0D 0A',
	},
	{ #48
		'name':'Relay 48',
		'port':'/dev/ttyUSB2',
		'command1':'3A 46 45 30 35 30 30 30 46 46 46 30 30 46 46 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 46 30 30 30 30 46 45 0D 0A',
	},
	
	{ #49
		'name':'Relay 49',
		'port':'/dev/ttyUSB3',
		'command1':'3A 46 45 30 35 30 30 30 30 46 46 30 30 46 45 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 30 30 30 30 30 46 44 0D 0A',
	},
	{ #50
		'name':'Relay 50',
		'port':'/dev/ttyUSB3',
		'command1':'3A 46 45 30 35 30 30 30 31 46 46 30 30 46 44 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 31 30 30 30 30 46 43 0D 0A',
	},
	{ #51
		'name':'Relay 51',
		'port':'/dev/ttyUSB3',
		'command1':'3A 46 45 30 35 30 30 30 32 46 46 30 30 46 43 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 32 30 30 30 30 46 42 0D 0A',
	},
	{ #52
		'name':'Relay 52',
		'port':'/dev/ttyUSB3',
		'command1':'3A 46 45 30 35 30 30 30 33 46 46 30 30 46 42 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 33 30 30 30 30 46 41 0D 0A',
	},
	{ #53
		'name':'Relay 53',
		'port':'/dev/ttyUSB3',
		'command1':'3A 46 45 30 35 30 30 30 34 46 46 30 30 46 41 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 34 30 30 30 30 46 39 0D 0A',
	},
	{ #54
		'name':'Relay 54',
		'port':'/dev/ttyUSB3',
		'command1':'3A 46 45 30 35 30 30 30 35 46 46 30 30 46 39 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 35 30 30 30 30 46 38 0D 0A',
	},
	{ #55
		'name':'Relay 55',
		'port':'/dev/ttyUSB3',
		'command1':'3A 46 45 30 35 30 30 30 36 46 46 30 30 46 38 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 36 30 30 30 30 46 37 0D 0A',
	},
	{ #56
		'name':'Relay 56',
		'port':'/dev/ttyUSB3',
		'command1':'3A 46 45 30 35 30 30 30 37 46 46 30 30 46 37 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 37 30 30 30 30 46 36 0D 0A',
	},
	{ #57
		'name':'Relay 57',
		'port':'/dev/ttyUSB3',
		'command1':'3A 46 45 30 35 30 30 30 38 46 46 30 30 46 36 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 38 30 30 30 30 46 35 0D 0A',
	},
	{ #58
		'name':'Relay 58',
		'port':'/dev/ttyUSB3',
		'command1':'3A 46 45 30 35 30 30 30 39 46 46 30 30 46 35 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 39 30 30 30 30 46 34 0D 0A',
	},
	{ #59
		'name':'Relay 59',
		'port':'/dev/ttyUSB3',
		'command1':'3A 46 45 30 35 30 30 30 41 46 46 30 30 46 34 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 41 30 30 30 30 46 33 0D 0A',
	},
	{ #60
		'name':'Relay 60',
		'port':'/dev/ttyUSB3',
		'command1':'3A 46 45 30 35 30 30 30 42 46 46 30 30 46 33 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 42 30 30 30 30 46 32 0D 0A',
	},
	{ #61
		'name':'Relay 61',
		'port':'/dev/ttyUSB3',
		'command1':'3A 46 45 30 35 30 30 30 43 46 46 30 30 46 32 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 43 30 30 30 30 46 31 0D 0A',
	},
	{ #62
		'name':'Relay 62',
		'port':'/dev/ttyUSB3',
		'command1':'3A 46 45 30 35 30 30 30 44 46 46 30 30 46 31 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 44 30 30 30 30 46 30 0D 0A',
	},
	{ #63
		'name':'Relay 63',
		'port':'/dev/ttyUSB3',
		'command1':'3A 46 45 30 35 30 30 30 45 46 46 30 30 46 30 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 45 30 30 30 30 46 46 0D 0A',
	},
	{ #64
		'name':'Relay 64',
		'port':'/dev/ttyUSB3',
		'command1':'3A 46 45 30 35 30 30 30 46 46 46 30 30 46 46 0D 0A',
		'command2':'3A 46 45 30 35 30 30 30 46 30 30 30 30 46 45 0D 0A',
	},
]
