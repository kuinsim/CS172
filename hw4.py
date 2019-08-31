#Suin Kim, Section 061
from Text import Text
from Block import Block
from Ball import Ball
from Drawable import Drawable
import pygame
import pygame.freetype
from pygame.locals import *
import math

pygame.init()

def intersect(rect1, rect2):
    if rect1.x < rect2.x + rect2.width and rect1.x + rect1.width > rect2.x and rect1.y < rect2.y + rect2.height and rect1.height + rect1.y > rect2.y:
        return True
    return False

surface = pygame.display.set_mode((500,500))
fpsClock = pygame.time.Clock()
blue = (0,0,255)
xv = 0
yv = 0
dt = 0.1
g = 6.67
R = 0.7
eta = 0.5
mult = 1

drawables = []
drawables.append(Block(0, 400, True, 500, 1,(0,0,0)))
drawables.append(Ball(20, 400, True))
drawables.append(Text(0, 0, True, 0))
drawables.append(Block(380,380,True,20,20,blue))
drawables.append(Block(400,380,True,20,20,blue))
drawables.append(Block(420,380,True,20,20,blue))
drawables.append(Block(380,360,True,20,20,blue))
drawables.append(Block(400,360,True,20,20,blue))
drawables.append(Block(420,360,True,20,20,blue))
drawables.append(Block(380,340,True,20,20,blue))
drawables.append(Block(400,340,True,20,20,blue))
drawables.append(Block(420,340,True,20,20,blue))

while True:
    surface.fill((255,255,255))
    for drawable in drawables[3::]:
        if drawable.getVisible():
            if intersect(drawables[1].getRect(), drawable.getRect()):
                drawable.setVisible(False)
                drawables[2].updateScore()
    for drawable in drawables:
        if drawable.getVisible():
            drawable.draw(surface)
    for event in pygame.event.get():
        if event.type == pygame.locals.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            initPos = pygame.mouse.get_pos()
        elif event.type == pygame.MOUSEBUTTONUP:
            finPos = pygame.mouse.get_pos()
            xv = finPos[0] - initPos[0]
            yv = -1 * (finPos[1] - initPos[1])
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            xv = 0
            yv = 0
            drawables[1].setLoc([20,400])
            drawables[2].resetScore()
            for drawable in drawables[3::]:
                drawable.setVisible(True)
    if math.fabs(xv) > 0 and math.fabs(yv) > 0:
        ballX, ballY = drawables[1].getLoc()
        if ballY > 400:
            yv = -R*yv
            xv = eta*xv
        else:
                yv = yv - g*dt
        drawables[1].setLoc([ballX+mult*dt*xv, ballY-dt*yv])
    pygame.display.update()
    fpsClock.tick(120)