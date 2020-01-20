########################################################################################
#   Import local modules
########################################################################################
import Boid
import Vector

########################################################################################
#   Import Maths modules
########################################################################################
from math import sqrt, pow

########################################################################################
#   Import kivy relative modules
########################################################################################

from kivy.uix.widget import Widget
from kivy.lang import Builder
Builder.load_file('./Environment.kv')


class Environment(Widget):
    def __init__(self, **kwargs):
        super(Environment, self).__init__(**kwargs)
        self.boids = []
        self.size_hint =(.7, 1)
        self.params  = {"nearBoidsDistanceEnabled": False, 
                        "nearBoidsDistance": 50, 
                        "cohesionEnabled": False, 
                        "cohesionCoef": 100, 
                        "separationEnabled": False,
                        "separationDistanceMax":5,
                        "alignmentEnabled": False,
                        "alignmentCoef": 8}

    def addBoids(self, x, y):
        self.boids.append(Boid(position=Vector(x,y)))

    def cohesion(self, boid, coef):
        mouvement = Vector(0,0)
        for nearBoid in boid.nearBoids:
            mouvement += nearBoid.position
        return (mouvement - boid.position)/coef

    def separation(self, boid, distanceMax):
        mouvement = Vector(0,0)
        for nearBoid in boid.nearBoids:
            distance = sqrt(pow(boid.position[0]-nearBoid.position[0])+pow(boid.position[1]-nearBoid.position[1]))
            if distance < distanceMax :
                mouvement -= (boid.position - nearBoids.position)
        return mouvement 
    
    def alignment(self, boid, coef):
        velocity = Vector(0,0)
        for nearBoid in boid.nearBoids:
            velocity += nearBoid.velocity
        return velocity/coef

    def moveAllBoids(self):
        for boid in self.boids:
            boid.searchForNearBoids(self.boids, self.params["nearBoidsDistance"], self.params["nearBoidsDistanceEnabled"])
            if self.params["cohesionEnabled"]:
                v1 = cohesion(boid, self.params["cohesionCoef"])
            else:
                v1 = 0
            if self.params["separationEnabled"]:
                v2 = separation(boid, self.params["separationDistanceMax"])
            else:
                v2 = 0
            if self.params["alignmentEnabled"]:
                v3 = alignment(boid, self.params["alignmentCoef"])
            else:
                v3 = 0
            boid.velocity += (v1+v2+v3)
            boid.position += boid.velocity

    def drawBoids(self, boid):
        print(boid.position)
