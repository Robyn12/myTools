#!/usr/bin/env python
import sys
from pwn import *

offset = ""
if len(sys.argv) < 2:
    print("usage: %s <argument>" % (sys.argv[0]))
    exit()
if str(sys.argv[1][0:2]) == '0x':
    if len(sys.argv[1]) > 10:
        print "use first 4 bytes in little endian\n"
    else:
        offset = p32(int(sys.argv[1], 16))
else:
    offset = sys.argv[1]

print(cyclic_find(offset))
