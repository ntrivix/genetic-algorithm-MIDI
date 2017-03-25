# -*- coding: utf-8 -*-
"""
Created on Sat Mar 25 20:02:16 2017

@author: Nikol
"""


import mido

from mido import MidiFile

file = input("File name: ")
channelNum = input("Channel number: ")
trackNum = input("Track number: ")

mid = MidiFile("songs/"+file)
              
track = mid.tracks[int(trackNum)]
events = []
startedEvents = {}
startTime = 0;
for msg in track:
    if msg.type in ["note_on", "note_off"] and msg.channel == int(channelNum):
        startTime += msg.time
        if (msg.type == "note_off"):
            if msg.note in startedEvents:
                time = startedEvents[msg.note][1]
                startedEvents[msg.note].append(startTime-time)
                events.append(startedEvents[msg.note])
                startedEvents.pop(msg.note)
        else:
            startedEvents[msg.note] = [msg, startTime]

events = sorted(events,key=lambda x : x[1])

print(events)
        
        