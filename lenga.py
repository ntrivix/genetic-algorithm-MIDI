# -*- coding: utf-8 -*-
"""
Created on Mon Mar 27 20:24:59 2017

@author: Nikol
"""

import gautils
import random
import math

from itertools import zip_longest

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)

#LEN_POPULATION_SIZE = 200
#BIT_NUM = 9
#MAX_VAL = 511

def generateHromozome(len):
    arr = [random.randint(0,MAX_VAL) for r in range(len-1)]
    arr.append(0)
   # arr.append(MAX_VAL)

    return arr

def fitness(hromosome, target):
    sum = 0
    for i in range(len(hromosome)):
        #print(bin(hromosome[i]))
        #print(bin(target[i]))
        #print(bin( ((hromosome[i] & target[i]) + ((~hromosome[i] & 0xFF) & (~target[i] & 0xFF))) ))
        sum += bin( ((hromosome[i] & target[i]) + ((~hromosome[i] & 0xFFF) & (~target[i] & 0xFFF))) ).count("1")
        #print( bin( ((hromosome[i] & target[i]) + ((~hromosome[i] & 0xFF) & (~target[i] & 0xFF))) ).count("1"))
        #print("------")
    return sum


def cross(hromosome1, hromosome2):
    length = len(hromosome1)
    if (len(hromosome1)==1):
        br= ((hromosome1[0]<<(BIT_NUM//2))+(hromosome2[0]>>(BIT_NUM//2)))%(1<<BIT_NUM)
        list=[br]
        return list
    if (len(hromosome1)==2):
        return hromosome1[0:1]+hromosome2[1:2]
    p1 = random.randint(1,3*length//5)
    p2 = random.randint(p1+1, length-1)
    return hromosome1[0:p1] + hromosome2[p1:p2] + hromosome1[p2:length]

def mutate(hromosome):
    if random.uniform(0,1) > 0.7:
        numToMute = random.randint(0, 5)
        for i in range(numToMute):
            randNote = random.randint(0,len(hromosome)-1)
            k = random.randint(0,3)
            for j in range(k):
                pos = 1 << random.randint(0,BIT_NUM-1)
                pom = hromosome[randNote] & pos
                if pom == 0:
                    newNote = hromosome[randNote] | pos
                else:
                    newNote = hromosome[randNote] &  (~pos & 0xFFF)
                hromosome[randNote] = newNote
    return hromosome

def findLen(lenArray):
    generation = 0
    maxFitness = 0
    mf = 12*len(lenArray)
    res = None
    
    population = [[generateHromozome(len(lenArray)), 0] for i in range(LEN_POPULATION_SIZE)]
    
    for p in population:
            p[1] = fitness(p[0], lenArray)
    
    #print(len(population))
    for j in range(500):
        population = sorted(population,key=lambda x : (-x[1]))
        
        if ( population[0][1]> maxFitness ):
            maxFitness = population[0][1]
            res = population[0]
            if (maxFitness == mf):
                break
            #print(res)

        newPopulation = population[:len(population)//2]
       # for i in range(len(newPopulation)):
       #     mutate(newPopulation[i][0])
        
        for i in range(LEN_POPULATION_SIZE//2):
            cr = [cross(newPopulation[i][0], newPopulation[i+1][0]),0]
            mutate(cr[0])
            cr[1] = fitness(cr[0],lenArray)
            newPopulation.append(cr)
            
            
        
        population = newPopulation
        generation += 1
    
    #print(j)
    #population = sorted(population,key=lambda x : (-x[1]))
    if (res[1] < 12*len(lenArray)):
        print(lenArray)
        print(res[0])
        print(res[1])
    
    return res[0]
    
    