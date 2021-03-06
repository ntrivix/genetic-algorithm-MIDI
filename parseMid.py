# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 20:02:16 2017

@author: Nikol
"""


import sys

from mido import MidiFile


def printNote(note, leng):
    notes=["C","C#","D","D#","E","F","F#","G","G#","A","A#","H"]
    if (note == 0):
        return "P(" + str(leng) + ")"
    return notes[note%12] + str(note//12-1) + "(" + str(leng) + ")" 


"""
=oktava, nota, vreme pocetka, skalirana duzina
"""
def parseMidi(file, channelNum, trackNum):
    mid = MidiFile("songs/"+file)
    track = mid.tracks[int(trackNum)]
    events = []
    startedEvents = {}
    startTime = 0;
    
    maxLen = 0;
    minLen = sys.maxsize
    
    for msg in track:
        if msg.type in ["note_on", "note_off"] and msg.channel == int(channelNum):
            startTime += msg.time
            if (msg.type == "note_off"):
                if msg.note in startedEvents:
                    time = startedEvents[msg.note][1]
                    l = startTime-time
                    maxLen = max(l, maxLen)
                    minLen = min(l, minLen)
                    startedEvents[msg.note].append(l)
                    events.append(startedEvents[msg.note])
                    startedEvents.pop(msg.note)
            else:
                startedEvents[msg.note] = [msg, startTime]
    
    events = sorted(events,key=lambda x : (x[1], -x[2]))
    finalEvents = []
    
    prevEnd = 0
    lastStart = 0
    p = 0
    for event in events:
        if event[1] != lastStart:
            time = event[1] - prevEnd
            if time > 0:
                #ima pauza
                #print("pauza "+str(prevEnd)+" "+str(time))
                
                for i in range(time//maxLen):
                    finalEvents.append([0, prevEnd, maxLen])
                if (time%maxLen > 0):
                    finalEvents.append([0, prevEnd, time%maxLen])
                    if (time < maxLen and p):
                        minLen = min(minLen, time%maxLen)
                    p = 1
            prevEnd = max(event[1]+event[2], prevEnd)
            lastStart = event[1]
        #print("event "+str(event[1])+" "+str(event[2]))
        #note = printNote(event[0].note)
        finalEvents.append([event[0].note, event[1], event[2]])
        
    for event in finalEvents:
        event[2] = round(event[2]/minLen)
        #print(event)
    return finalEvents, minLen, maxLen
    #print(finalEvents)
    #print(str(minLen)+" "+str(maxLen))    



