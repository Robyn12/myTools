#!/usr/bin/env python
from pwn import *
import sys

if len(sys.argv) < 2:
    print("usage %s <length>" % (sys.argv[0]))
print(cyclic(int(sys.argv[1])))
