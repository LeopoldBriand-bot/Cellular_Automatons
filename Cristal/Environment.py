from Cell import *
from Utils import randomColor
import random

class Environment(Widget):
    def __init__(self, **kwargs):
        super(Environment, self).__init__(**kwargs)
        self.sizeOfMap = 2
        self.numberOfType = 3
        self.typesOfCells = []
        self.initNewMap()
        self.state = "pause"
        
    def sizeMap(self, instance, value):
        self.sizeOfMap = value
    
    def changeNumberOfType(self, instance, value):
        self.numberOfType = value

    def initNewMap(self):
        self.setNewTypes()
        self.grille = GridLayout(cols=self.sizeOfMap, size_hint=(1, 1))
        for i in range(0,self.sizeOfMap ** 2):
            tempType = random.choice(self.typesOfCells)
            self.grille.add_widget(Cell(typeOfCell=tempType[0], color=tempType[1]))
    
    def setNewTypes(self):
        self.typesOfCells = []
        for i in range(0, self.numberOfType):
            self.typesOfCells.append([i, randomColor()])


