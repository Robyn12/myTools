#!/usr/bin/env python

import os, sys


def main(host, port, binary):
  pwd = os.getcwd()
  os.system('cp ~/myTools/skeleton/xpl.py ' + pwd + '/xpl.py')
  os.system("sed -i.bak 's/\[HOST\]/\"" + host + "\"/' xpl.py")
  os.system("sed -i.bak 's/\[PORT\]/" + port + "/' xpl.py")
  os.system("sed -i.bak 's/\[BINARY\]/" + "\".\/" + binary + "\"/' xpl.py")
  os.system("rm ./xpl.py.bak")

if __name__=='__main__':
  if len(sys.argv) < 4:
    print("Usage: skeleton <HOST> <PORT> <BINARY>")
  else:
    main(sys.argv[1], sys.argv[2], sys.argv[3])
