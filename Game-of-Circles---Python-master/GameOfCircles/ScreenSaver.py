from Sprite import Sprite
class ScreenSaver(Sprite):
    
    speedX = 8
    speedY = 4
    diameter = 50
    c = color(255,0,105)
    
    def __init__(self, x, y, team):
        self.x = x
        self.y = y
        self.team = team
        
    def move(self):
        self.x += self.speedX
        self.y += self.speedY
        if self.x < 0 or self.x > width:
            self.speedX *= -1
        if self.y < 0 or self.y > width:
            self.speedY *= -1
        
    def display(self):
        fill(self.c)
        ellipse(self.x, self.y, self.diameter, self.diameter)
        
    def animate(self):
        self.move()
        self.display()
