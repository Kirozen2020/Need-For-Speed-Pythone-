from pygame import*
import pygame
import random
import time
import os

init()
screen = display.set_mode((640, 480))
display.set_caption('Need For Speed')

mixer.music.load('background.mod')
mixer.music.play(-1)

class Sprite:
    def __init__(self, xpos, ypos, filename):
        self.x = xpos
        self.y = ypos
        self.bitmap = image.load(filename)
    def render(self):
        screen.blit(self.bitmap, (self.x, self.y))

def Intersect(s1_x, s1_y, s2_x, s2_y):
    if (s1_x > s2_x - 40) and (s1_x < s2_x + 40) and (s1_y > s2_y - 100) and (s1_y < s2_y + 100):
        return 1
    else:
        return 0

playercar = Sprite(20, 400, 'car_player.png')
enemycar = Sprite(random.randrange(100, 500), 0, 'car_enemy.png')
enemycar1 = Sprite(random.randrange(100, 500), 0, 'police1.png')
enemycar2 = Sprite(random.randrange(100, 500), 0, 'police2.png')
enemycar3 = Sprite(random.randrange(100, 500), 0, 'police3.png')
tree1 = Sprite(10, 0, 'tree.png')
tree2 = Sprite(550, 240, 'tree.png')
whiteline1 = Sprite(315, 0, 'whiteline.png')
whiteline2 = Sprite(315, 240, 'whiteline.png')
scorefont = font.Font(None, 60)
crasheffect = mixer.Sound('crash.wav')
score = 0
maxscore = 0
quit1 = 0



while quit1 == 0:
    screen.fill((0,200,0))
    screen.fill((200,200,200), ((100, 0), (440, 480)))
    tree1.render()
    tree1.y += 10
    if (tree1.y > 480):
        tree1.y = -110

    tree2.render()
    tree2.y += 10
    if (tree2.y > 480):
        tree2.y = -110

    whiteline1.render()
    whiteline1.y += 10
    if (whiteline1.y > 480):
        whiteline1.y = -80

    whiteline2.render()
    whiteline2.y += 10
    if (whiteline2.y > 480):
        whiteline2.y = -80

    enemycar.render()
    enemycar.y += 15
    if (enemycar.y > 480):
        enemycar.y = -100
        enemycar.x = random.randrange(100, 200)

    enemycar1.render()
    enemycar1.y += 15
    if (enemycar1.y > 480):
        enemycar1.y = -100
        enemycar1.x = random.randrange(200, 300)

    enemycar2.render()
    enemycar2.y += 15
    if (enemycar2.y > 480):
        enemycar2.y = -100
        enemycar2.x = random.randrange(300, 400)

    enemycar3.render()
    enemycar3.y += 15
    if (enemycar3.y > 480):
        enemycar3.y = -100
        enemycar3.x = random.randrange(400, 500)

    x, y = mouse.get_pos()
    if (x < 100):
        x = 100
    if (x > 500):
        x = 500
    playercar.x = x
    playercar.render()

    scoretext = scorefont.render('Score: ' + str(score), True, (255, 255, 255), (0,0,0))
    screen.blit(scoretext, (5,5))

    if (Intersect(playercar.x, playercar.y, enemycar.x, enemycar.y)):
        mixer.Sound.play(crasheffect)
        if (score > maxscore):
            maxscore = score
        score = 0

    if (Intersect(playercar.x, playercar.y, enemycar1.x, enemycar1.y)):
        mixer.Sound.play(crasheffect)
        if (score > maxscore):
            maxscore = score
        score = 0

    if (Intersect(playercar.x, playercar.y, enemycar2.x, enemycar2.y)):
        mixer.Sound.play(crasheffect)
        if (score > maxscore):
            maxscore = score
        score = 0

    if (Intersect(playercar.x, playercar.y, enemycar3.x, enemycar3.y)):
        mixer.Sound.play(crasheffect)
        if (score > maxscore):
            maxscore = score
        score = 0

    for ourevent in event.get():
        if ourevent == QUIT:
            quit1 = 1
            pygame.quit()
            sys.exit()

    display.update()
    time.sleep(0.02)

    score += 1

print('Yout maximum score was:' + str(maxscore))