#!/usr/bin/python
import os
import sys

charset ={'a' : ['a','A','4','@'],'b' : ['b','B'], 'c' : ['c','C'],'d' : ['d','D'], 'e' : ['e','E','3'], 'f' : ['f', 'F'], 'g' : ['g','G'], 'h': ['h','H'], 'i':['i','I','1','!'], 'j': ['j','J'], 'k': ['k','K'], 'l':['l','L', '1','!'], 'm':['m','M'], 'n':['n','N'], 'o':['o','O','0'], 'p':['p','P'], 'q':['q','Q'],'r':['r','R'], 's':['s','S','5','$'], 't': ['t','T','7'], 'u': ['u','U'], 'v':['v','V'], 'w' : ['w','W'], 'x' : ['x','X'],'y':['y','Y'], 'z': ['z','Z']}

if len(sys.argv) < 2:
    print("usage: %s <password>" %(sys.argv[0]))
    sys.exit(0)
def permutations(string):
    string = string.lower()
    
    i = 1
    for c in string:
        i *= len(charset[c])
    
    return i




def makePerm(string):
    string = string.lower()
    passList = []
    wholeList =[]
    for i in range(permutations(string)):
        passList.append("")
        for i2 in range(len(string)):
            if i2 == 0:
                passList[i] += charset[string[0]][i%len(charset[string[0]])]
            else:
                passList[i] += charset[string[i2]][calculateIndex(i,permutations(string[0:i2]))%len(charset[string[i2]])]


    for i in range(len(passList)):
        wholeList.append(passList[i])
        wholeList.append(passList[i]+"!")
        wholeList.append(passList[i]+"!!")
    return wholeList
def calculateIndex(i,i2):
    if i < i2:
        return 0
    
    i3 = int(i/i2)
    return i3

passList = makePerm(sys.argv[1])
for passu in passList:
    print(passu)
