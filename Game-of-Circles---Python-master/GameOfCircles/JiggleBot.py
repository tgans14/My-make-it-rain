
from Sprite import Sprite
class JiggleBot(Sprite):
    
    speed = 8
    diameter = 50
    c = color(20,255,125)
    
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team
        
    def move(self):
        self.y += random(-self.speed,self.speed)
        self.x += random(-self.speed,self.speed)
        
    def display(self):
        fill(self.c)
        ellipse(self.x, self.y, self.diameter, self.diameter)
        if( self.y >= 525):
            self.y = 0
