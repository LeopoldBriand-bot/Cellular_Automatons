#!/usr/bin/env python3
from random import random
from Boid import Boid 
from tkinter import *

class Page():
    def __init__(self, master, nbBoid):
        self.master = master
        self.flock = []
        self.setup()
        for i in range(nbBoid):
            self.addBoid()
        self.draw()
    def setup(self):
        self.canvas = Canvas(self.master, width=1000, height=1000, background='black')
        self.canvas.pack()
    def draw(self):
        for boid in self.flock :
            boid.update(self)
    def addBoid(self):
        self.flock.append(Boid(random()*1000,random()*1000, self))
        #self.flock[-1].update(self)