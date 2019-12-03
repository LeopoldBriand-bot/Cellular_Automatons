#!/usr/bin/env python3
from Vector import *
import math
from random import random

class Boid():

    def __init__(self, x, y, parent):
        self.parent = parent
        self.position = Vector(x, y)
        velVector = ((random() - 0.5)*10,(random() - 0.5)*10)
        accVector = ((random() - 0.5)/2,(random() - 0.5)/2)
        self.velocity = Vector(*velVector)
        self.acceleration = Vector(*accVector)
        self.create()
    
    def create(self):
        self.body = self.parent.canvas.create_oval(self.position.x+3, self.position.y+3,self.position.x-3, self.position.y-3, fill='white')
    
    def update(self,parent):
        self.position += self.velocity
        self.velocity += self.acceleration
        self.parent.canvas.move(self.body,self.position.x,self.position.y)
    
    