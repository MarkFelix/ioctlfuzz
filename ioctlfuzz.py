#################################################################################################################################
#
# A crude fuzzer that generates all possible IOCTL Function Codes and fuzzes the hackSysExtremeVulnerableDriver kernel driver.
# Allthough, this could be used to fuzz any kernel driver, this would just need a couple of minor changes.
# Ioctl codes are made up of 4 things, FUNCTION code, DEVICE code, ACCESS code and BUFFER METHOD. In this case, this script
# tagets specifically the "FUNCTION" IOCTL code which is fuzzed through all possibilities. 
# At times, it may be neccesary to change the other 3 codes as well but this seems to be rare.
#
# The following device, access and buffer method codes are static and will need to be changed manually if neccesarry.
#
# DEVICE: unknown 0x22
# ACCESS: FILE_ANY_ACCESS 0x00
# BUFFER METHOD: METHOD_NEITHER 0x03
#
#
# M$ Macro for resolving/generating IOCTL's:
# hex((0x00000022 << 16) | (0x00000000 << 14) | (0x802 << 2) | 0x00000003)
#
# Credit to rootkits.xyz whos kernel exploit tutorials have shown me the way of using the windows API using ctypes in python.
#
#################################################################################################################################

import ctypes, sys
from ctypes import *
from time import sleep

# Generate all possible Function codes	
for i in range(0x0, 0xFFF):
	func = ((i << 2) | 0x00000003)
	dev = (0x00000022 << 16) | (0x00000000 << 14)
	code = dev | func
	
	kernel32 = windll.kernel32
	hevDevice = kernel32.CreateFileA("\\\\.\\HackSysExtremeVulnerableDriver", 0xC0000000, 0, None, 0x3, 0, None)
 
	if not hevDevice or hevDevice == -1:
		print "Couldn't get a handle."
		sys.exit(0)
 
	buf = "A"*1000
	bufLength = len(buf)
 
	kernel32.DeviceIoControl(hevDevice, code, buf, bufLength, None, 0, byref(c_ulong()), None)
	print hex(dev)
	print hex(func)
	print hex(code)
	sleep(1)