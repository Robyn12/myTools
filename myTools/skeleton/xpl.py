#!/usr/bin/env python

from pwn import *
import sys

HOST = [HOST]
PORT = [PORT]

global r, e

e = ELF([BINARY])

def exploit():
  r.interactive()



if __name__== "__main__":
  if len(sys.argv) > 1:
    r = remote(HOST, PORT)
    exploit()
  else:
    r = process([e.path])
    gdb.attach(r)
    pause()
    exploit()

