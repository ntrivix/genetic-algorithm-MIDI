# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 20:02:16 2017

@author: Nikola
"""


import parseMid
import lenga
import datetime
import threading

"""
parseMidi(file, channelNum, trackNum)
"""
midiData,minLen,maxLen = parseMidi("pesma1.mid",5,5)

normalizeTime = []
scaleFactor = 511/round(maxLen/minLen)

notes = []
for i in range(len(midiData)):
    normalizeTime.append(round(midiData[i][2]*scaleFactor))
    notes.append(midiData[i][0])
    
resDataLen = []
resDataNote = []

BIT_NUM = 9
MAX_VAL = 511
LEN_POPULATION_SIZE = 200
l = len(normalizeTime)//10
       
startTime = datetime.datetime.now()
       

for i in range(l):
    resDataLen += findLen(normalizeTime[i*10:(i+1)*10])
    
i+=1
if (i*10<len(normalizeTime)):
    resDataLen+= findLen(normalizeTime[i*10:len(normalizeTime)])

    
BIT_NUM = 7
MAX_VAL = 127
LEN_POPULATION_SIZE = 200
print("---------------------------------")


for i in range(l):
    resDataNote += findLen(notes[i*10:(i+1)*10])

i+=1
if (i*10<len(notes)):
    resDataNote+= findLen(notes[i*10:len(notes)])
    
endTime = datetime.datetime.now()

before = []
after = []
for i in range(len(resDataNote)):
    before.append(printNote(notes[i], round(normalizeTime[i]/scaleFactor)))
    after.append(printNote(resDataNote[i], round(resDataLen[i]/scaleFactor)))

print("Original notes")
print(before)
print("Result notes")
print(after)

print("Track length: ",len(resDataNote))
print("Elapsed time:",endTime-startTime)
