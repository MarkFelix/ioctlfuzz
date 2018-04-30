
A crude fuzzer that generates all possible IOCTL Function Codes and fuzzes the hackSysExtremeVulnerableDriver kernel driver.
Allthough, this could be used to fuzz any kernel driver, this would just need a couple of minor changes.
Ioctl codes are made up of 4 things, FUNCTION code, DEVICE code, ACCESS code and BUFFER METHOD. In this case, this script
tagets specifically the "FUNCTION" IOCTL code which is fuzzed through all possibilities. 
At times, it may be neccesary to change the other 3 codes as well but this seems to be rare.

The following device, access and buffer method codes are static and will need to be changed manually if neccesarry.

DEVICE: unknown 0x22
ACCESS: FILE_ANY_ACCESS 0x00
BUFFER METHOD: METHOD_NEITHER 0x03


M$ Macro for resolving/generating IOCTL's:
hex((0x00000022 << 16) | (0x00000000 << 14) | (0x802 << 2) | 0x00000003)

Credit to https://rootkits.xyz/blog/ whose kernel exploit tutorials have shown me the way of using the windows API using 
ctypes in python.