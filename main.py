# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 20:02:16 2017

@author: Nikol
"""


import parseMid
import lenga

midiData,minLen,maxLen = parseMidi("pesma1.mid",6,6)

normalizeTime = []
scaleFactor = 511/round(maxLen/minLen)
#print(scaleFactor)
notes = []
for i in range(len(midiData)):
    normalizeTime.append(round(midiData[i][2]*scaleFactor))
    notes.append(midiData[i][0])

#print(findLen([511, 511, 511, 511, 511, 511, 511, 511, 511, 511]))

#print(normalizeTime)
#print(len(normalizeTime))
BIT_NUM = 9
MAX_VAL = 511
pom = 1 if len(midiData)%10<0 else 0
l = len(midiData)//10 + pom
       
resDataLen = []
for i in range(l):
    #print(findLen(normalizeTime[i*10:min((i+1)*10,len(midiData))]))
    resDataLen += findLen(normalizeTime[i*10:min((i+1)*10,len(midiData))])
    
BIT_NUM = 7
MAX_VAL = 127
print("---------------------------------")

resDataNote = []
for i in range(l):
    resDataNote += findLen(notes[i*10:min((i+1)*10,len(midiData))])


#print(normalizeTime)
#print(resDataLen)
#print()

#print(notes)
#print(resDataNote)
#print()

before = []
after = []
for i in range(len(resDataNote)):
    before.append(printNote(notes[i], round(normalizeTime[i]/scaleFactor)))
    after.append(printNote(resDataNote[i], round(resDataLen[i]/scaleFactor)))
print(before)
print()
print(after)




#print(fitness([1,2,5,8,3],[1,2,5,511,3]))