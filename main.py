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
              
for i, track in enumerate(mid.tracks):
    print('Track {}: {}'.format(i, track.name))
    for msg in track:
        print(msg)