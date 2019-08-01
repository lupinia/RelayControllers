#!/usr/bin/Python
import serial
import sys
from time import sleep
import os

ser = serial.Serial()
ser.baudrate = 9600
ser.bytesize = serial.EIGHTBITS #number of bits per bytes
ser.parity = serial.PARITY_NONE #set parity check: no parity
ser.stopbits = serial.STOPBITS_ONE #number of stop bits
ser.timeout = 2            #timeout block read
ser.xonxoff = False     #disable software flow control
ser.rtscts = False     #disable hardware (RTS/CTS) flow control
ser.dsrdtr = False       #disable hardware (DSR/DTR) flow control
ser.writeTimeout = 2     #timeout for write


if len(sys.argv) != 2:
    print "Usage: python MyRelays.py <relay #>"
    sys.exit()

if sys.argv[1] == "TEST":
    for i in range(1, 65):
        os.system("python MyRelays.py "+str(i))


if sys.argv[1] == "1":
    ser.port = "/dev/ttyUSB0"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 30 46 46 30 30 46 45 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 30 30 30 30 30 46 44 0D 0A"))

if sys.argv[1] == "2":
    ser.port = "/dev/ttyUSB0"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 31 46 46 30 30 46 44 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 31 30 30 30 30 46 43 0D 0A"))

if sys.argv[1] == "3":
    ser.port = "/dev/ttyUSB0"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 32 46 46 30 30 46 43 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 32 30 30 30 30 46 42 0D 0A"))

if sys.argv[1] == "4":
    ser.port = "/dev/ttyUSB0"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 33 46 46 30 30 46 42 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 33 30 30 30 30 46 41 0D 0A"))

if sys.argv[1] == "5":
    ser.port = "/dev/ttyUSB0"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 34 46 46 30 30 46 41 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 34 30 30 30 30 46 39 0D 0A"))

if sys.argv[1] == "6":
    ser.port = "/dev/ttyUSB0"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 35 46 46 30 30 46 39 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 35 30 30 30 30 46 38 0D 0A"))

if sys.argv[1] == "7":
    ser.port = "/dev/ttyUSB0"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 36 46 46 30 30 46 38 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 36 30 30 30 30 46 37 0D 0A"))

if sys.argv[1] == "8":
    ser.port = "/dev/ttyUSB0"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 37 46 46 30 30 46 37 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 37 30 30 30 30 46 36 0D 0A"))

if sys.argv[1] == "9":
    ser.port = "/dev/ttyUSB0"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 38 46 46 30 30 46 36 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 38 30 30 30 30 46 35 0D 0A"))

if sys.argv[1] == "10":
    ser.port = "/dev/ttyUSB0"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 39 46 46 30 30 46 35 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 39 30 30 30 30 46 34 0D 0A"))

if sys.argv[1] == "11":
    ser.port = "/dev/ttyUSB0"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 41 46 46 30 30 46 34 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 41 30 30 30 30 46 33 0D 0A"))

if sys.argv[1] == "12":
    ser.port = "/dev/ttyUSB0"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 42 46 46 30 30 46 33 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 42 30 30 30 30 46 32 0D 0A"))

if sys.argv[1] == "13":
    ser.port = "/dev/ttyUSB0"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 43 46 46 30 30 46 32 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 43 30 30 30 30 46 31 0D 0A"))

if sys.argv[1] == "14":
    ser.port = "/dev/ttyUSB0"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 44 46 46 30 30 46 31 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 44 30 30 30 30 46 30 0D 0A"))

if sys.argv[1] == "15":
    ser.port = "/dev/ttyUSB0"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 45 46 46 30 30 46 30 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 45 30 30 30 30 46 46 0D 0A"))

if sys.argv[1] == "16":
    ser.port = "/dev/ttyUSB0"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 46 46 46 30 30 46 46 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 46 30 30 30 30 46 45 0D 0A"))

if sys.argv[1] == "17":
    ser.port = "/dev/ttyUSB1"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 30 46 46 30 30 46 45 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 30 30 30 30 30 46 44 0D 0A"))

if sys.argv[1] == "18":
    ser.port = "/dev/ttyUSB1"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 31 46 46 30 30 46 44 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 31 30 30 30 30 46 43 0D 0A"))

if sys.argv[1] == "19":
    ser.port = "/dev/ttyUSB1"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 32 46 46 30 30 46 43 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 32 30 30 30 30 46 42 0D 0A"))

if sys.argv[1] == "20":
    ser.port = "/dev/ttyUSB1"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 33 46 46 30 30 46 42 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 33 30 30 30 30 46 41 0D 0A"))

if sys.argv[1] == "21":
    ser.port = "/dev/ttyUSB1"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 34 46 46 30 30 46 41 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 34 30 30 30 30 46 39 0D 0A"))

if sys.argv[1] == "22":
    ser.port = "/dev/ttyUSB1"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 35 46 46 30 30 46 39 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 35 30 30 30 30 46 38 0D 0A"))

if sys.argv[1] == "23":
    ser.port = "/dev/ttyUSB1"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 36 46 46 30 30 46 38 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 36 30 30 30 30 46 37 0D 0A"))

if sys.argv[1] == "24":
    ser.port = "/dev/ttyUSB1"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 37 46 46 30 30 46 37 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 37 30 30 30 30 46 36 0D 0A"))

if sys.argv[1] == "25":
    ser.port = "/dev/ttyUSB1"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 38 46 46 30 30 46 36 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 38 30 30 30 30 46 35 0D 0A"))

if sys.argv[1] == "26":
    ser.port = "/dev/ttyUSB1"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 39 46 46 30 30 46 35 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 39 30 30 30 30 46 34 0D 0A"))

if sys.argv[1] == "27":
    ser.port = "/dev/ttyUSB1"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 41 46 46 30 30 46 34 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 41 30 30 30 30 46 33 0D 0A"))

if sys.argv[1] == "28":
    ser.port = "/dev/ttyUSB1"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 42 46 46 30 30 46 33 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 42 30 30 30 30 46 32 0D 0A"))

if sys.argv[1] == "29":
    ser.port = "/dev/ttyUSB1"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 43 46 46 30 30 46 32 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 43 30 30 30 30 46 31 0D 0A"))

if sys.argv[1] == "30":
    ser.port = "/dev/ttyUSB1"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 44 46 46 30 30 46 31 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 44 30 30 30 30 46 30 0D 0A"))

if sys.argv[1] == "31":
    ser.port = "/dev/ttyUSB1"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 45 46 46 30 30 46 30 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 45 30 30 30 30 46 46 0D 0A"))

if sys.argv[1] == "32":
    ser.port = "/dev/ttyUSB1"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 46 46 46 30 30 46 46 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 46 30 30 30 30 46 45 0D 0A"))


if sys.argv[1] == "33":
    ser.port = "/dev/ttyUSB2"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 30 46 46 30 30 46 45 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 30 30 30 30 30 46 44 0D 0A"))

if sys.argv[1] == "34":
    ser.port = "/dev/ttyUSB2"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 31 46 46 30 30 46 44 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 31 30 30 30 30 46 43 0D 0A"))

if sys.argv[1] == "35":
    ser.port = "/dev/ttyUSB2"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 32 46 46 30 30 46 43 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 32 30 30 30 30 46 42 0D 0A"))

if sys.argv[1] == "36":
    ser.port = "/dev/ttyUSB2"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 33 46 46 30 30 46 42 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 33 30 30 30 30 46 41 0D 0A"))

if sys.argv[1] == "37":
    ser.port = "/dev/ttyUSB2"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 34 46 46 30 30 46 41 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 34 30 30 30 30 46 39 0D 0A"))

if sys.argv[1] == "38":
    ser.port = "/dev/ttyUSB2"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 35 46 46 30 30 46 39 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 35 30 30 30 30 46 38 0D 0A"))

if sys.argv[1] == "39":
    ser.port = "/dev/ttyUSB2"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 36 46 46 30 30 46 38 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 36 30 30 30 30 46 37 0D 0A"))

if sys.argv[1] == "40":
    ser.port = "/dev/ttyUSB2"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 37 46 46 30 30 46 37 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 37 30 30 30 30 46 36 0D 0A"))

if sys.argv[1] == "41":
    ser.port = "/dev/ttyUSB2"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 38 46 46 30 30 46 36 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 38 30 30 30 30 46 35 0D 0A"))

if sys.argv[1] == "42":
    ser.port = "/dev/ttyUSB2"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 39 46 46 30 30 46 35 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 39 30 30 30 30 46 34 0D 0A"))

if sys.argv[1] == "43":
    ser.port = "/dev/ttyUSB2"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 41 46 46 30 30 46 34 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 41 30 30 30 30 46 33 0D 0A"))

if sys.argv[1] == "44":
    ser.port = "/dev/ttyUSB2"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 42 46 46 30 30 46 33 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 42 30 30 30 30 46 32 0D 0A"))

if sys.argv[1] == "45":
    ser.port = "/dev/ttyUSB2"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 43 46 46 30 30 46 32 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 43 30 30 30 30 46 31 0D 0A"))

if sys.argv[1] == "46":
    ser.port = "/dev/ttyUSB2"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 44 46 46 30 30 46 31 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 44 30 30 30 30 46 30 0D 0A"))

if sys.argv[1] == "47":
    ser.port = "/dev/ttyUSB2"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 45 46 46 30 30 46 30 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 45 30 30 30 30 46 46 0D 0A"))

if sys.argv[1] == "48":
    ser.port = "/dev/ttyUSB2"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 46 46 46 30 30 46 46 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 46 30 30 30 30 46 45 0D 0A"))


if sys.argv[1] == "49":
    ser.port = "/dev/ttyUSB3"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 30 46 46 30 30 46 45 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 30 30 30 30 30 46 44 0D 0A"))

if sys.argv[1] == "50":
    ser.port = "/dev/ttyUSB3"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 31 46 46 30 30 46 44 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 31 30 30 30 30 46 43 0D 0A"))

if sys.argv[1] == "51":
    ser.port = "/dev/ttyUSB3"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 32 46 46 30 30 46 43 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 32 30 30 30 30 46 42 0D 0A"))

if sys.argv[1] == "52":
    ser.port = "/dev/ttyUSB3"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 33 46 46 30 30 46 42 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 33 30 30 30 30 46 41 0D 0A"))

if sys.argv[1] == "53":
    ser.port = "/dev/ttyUSB3"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 34 46 46 30 30 46 41 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 34 30 30 30 30 46 39 0D 0A"))

if sys.argv[1] == "54":
    ser.port = "/dev/ttyUSB3"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 35 46 46 30 30 46 39 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 35 30 30 30 30 46 38 0D 0A"))

if sys.argv[1] == "55":
    ser.port = "/dev/ttyUSB3"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 36 46 46 30 30 46 38 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 36 30 30 30 30 46 37 0D 0A"))

if sys.argv[1] == "56":
    ser.port = "/dev/ttyUSB3"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 37 46 46 30 30 46 37 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 37 30 30 30 30 46 36 0D 0A"))

if sys.argv[1] == "57":
    ser.port = "/dev/ttyUSB3"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 38 46 46 30 30 46 36 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 38 30 30 30 30 46 35 0D 0A"))

if sys.argv[1] == "58":
    ser.port = "/dev/ttyUSB3"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 39 46 46 30 30 46 35 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 39 30 30 30 30 46 34 0D 0A"))

if sys.argv[1] == "59":
    ser.port = "/dev/ttyUSB3"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 41 46 46 30 30 46 34 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 41 30 30 30 30 46 33 0D 0A"))

if sys.argv[1] == "60":
    ser.port = "/dev/ttyUSB3"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 42 46 46 30 30 46 33 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 42 30 30 30 30 46 32 0D 0A"))

if sys.argv[1] == "61":
    ser.port = "/dev/ttyUSB3"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 43 46 46 30 30 46 32 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 43 30 30 30 30 46 31 0D 0A"))

if sys.argv[1] == "62":
    ser.port = "/dev/ttyUSB3"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 44 46 46 30 30 46 31 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 44 30 30 30 30 46 30 0D 0A"))

if sys.argv[1] == "63":
    ser.port = "/dev/ttyUSB3"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 45 46 46 30 30 46 30 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 45 30 30 30 30 46 46 0D 0A"))

if sys.argv[1] == "64":
    ser.port = "/dev/ttyUSB3"
    ser.open()
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 46 46 46 30 30 46 46 0D 0A"))
    sleep(0.25)
    ser.write(bytearray.fromhex("3A 46 45 30 35 30 30 30 46 30 30 30 30 46 45 0D 0A"))
