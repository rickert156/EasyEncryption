#!/usr/bin/python3

import os

def writeFile(file, translate):
    with open(file, 'w') as newfile:
        newfile.write(translate)


def enc(r, file):
    translate = ''
    i=len(r)-1
    while i>=0:
        translate+=r[i]
        i-=1
    print(translate)
    writeFile(file, translate)


def readFile(file):
    with open(file, 'r') as filer:
        r = filer.read()
        print(r)
        enc(r, file)

def searchFile():
    for file in os.listdir():
        print(file)
        readFile(file)
        
searchFile()

