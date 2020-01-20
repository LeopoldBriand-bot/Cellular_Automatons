from Vector import *
from kivy.uix.widget import Widget
from kivy.lang import Builder
Builder.load_file('./Boids.kv')

class Boid(Widget):
    def __init__(self, position=Vector(0,0),velocity=Vector(0,0), **kwargs):
        super(Boid, self).__init__(**kwargs)
        self.position = position
        self.velocity = velocity
        self.nearBoids = []

    def searchForNearBoids(self, boids, distanceMax, enabled):
        if enabled:
            for boid in boids:
                distance = sqrt(pow(boid.position[0]-self.position[0])+pow(boid.position[1]-self.position[1]))
                if distance < distanceMax and boid != self:
                    self.nearBoids.append(boid)
        else:
            self.nearBoids = boids