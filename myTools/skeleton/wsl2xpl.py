from pwn import *
import sys

# first run this command below to get core files and move binary + exploit script to /home/robyn/gdb-workspace
# sudo sysctl -w kernel.core_pattern=/home/robyn/gdb-workspace
context.terminal = ['cmd.exe','/c','start','wsl.exe','--cd','/home/robyn/gdb-workspace']

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
