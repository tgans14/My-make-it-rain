import platform
import SpriteManager

from Bullet import Bullet
from Enemy import Enemy
from Player import Player
from SpriteManager import sprites
from Raindrop import Raindrop
from JiggleBot import JiggleBot
from ScreenSaver import ScreenSaver

def setup():
    print "Built with Processing Python version " + platform.python_version()
    
    global player, sprites
    size(500, 500)
    playerTeam = 1
    enemyTeam = 2
    player = Player(width/2, height/2, playerTeam)
    SpriteManager.setPlayer(player)
    SpriteManager.spawn(JiggleBot(200,50,2))
    SpriteManager.span(Enemy
    #sprites.append(player)
    #sprites.append(Enemy(150, 150, enemyTeam))
    #sprites.append(Raindrop(400,100, enemyTeam)) 
    #sprites.append(ScreenSaver(10,200, enemyTeam))  
    #sprites.append(JiggleBot(100,100, enemyTeam)) 
    
def draw():
    noStroke()
    global player, sprites
    background(0)    
    SpriteManager.animate()
def keyPressed():
    global player
    player.keyDown()    
def keyReleased():
    global player
    player.keyUp()
