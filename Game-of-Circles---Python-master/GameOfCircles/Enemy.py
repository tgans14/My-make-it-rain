from Sprite import Sprite
from Bullet import Bullet

import SpriteManager

mark = 0
wait = 1000
go = True


class Enemy(Sprite):
    
    speed = 8
    diameter = 50
    c = color(0,0,255)
    
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team
        
    def move(self):
        self.x += self.speed
        if self.x < 0 or self.x > width:
            self.speed *= -1
        
    def aim(self,target):
        xComp = target.x - self.x
        yComp = target.y - self.y
        d = ((self.x - target.x))
