#!/usr/bin/env python3
from math import *
import random as rand

class Vector():
    def __init__(self, *args):
        if len(args)==0: 
            self.x, self.y = (0,0)
        else: 
            self.x, self.y = args
    
    def __add__(self, other):
        return Vector(self.x+other.x,self.y+other.y)
    
    def __sub__(self, other):
        return Vector(self.x-other.x,self.y-other.y)
    
    def __mul__(self,other):
        if isinstance(other, (float, int)):
            return Vector(self.x*other, self.y*other)
        if type(other) == type(self):
            return Vector(self.x*other.x, self.y*other.y)

    def len(self):
        return sqrt(pow(self.x)+pow(self.y))
