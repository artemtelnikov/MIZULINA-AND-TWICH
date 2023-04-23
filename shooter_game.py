from pygame import *
from random import *

mixer.init()
mixer.music.load('space.ogg')
mixer.music.load('fire.ogg')
#mixer.music.play()
window = display.set_mode((700, 500))
display.set_caption('МИЗУЛИНА АТАКУЕТ САНЯ БЕГИТ')
background = transform.scale(image.load('galaxy.jpg'), (700, 500))
font.init()
font.init()

window.blit(background, (0,0))

x1,y1 = 300, 390
x2,y2 = 250, 250
x3,y3 = 100, 100

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, h,w ,player_speed,):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (h, w))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))



monsters_kill = 0
lostes = 0

game = True


class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, h,w ,player_speed):   
        super().__init__(player_image, player_x, player_y, h,w ,player_speed)
    def update(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
            
        if key_pressed[K_RIGHT] and self.rect.x < 690:
            self.rect.x += self.speed





class Enemy(GameSprite):
    def __init__(self, player_image, player_x, player_y, h,w ,player_speed):   
        super().__init__(player_image, player_x, player_y, h,w ,player_speed)
    def update(self):
        lost = 0
        self.rect.y += 2
        if self.rect.y > 680:
            self.rect.x = randint(80,  680 - 80)
            self.rect.y = 0
            lost = lost + 1


class Bullet(GameSprite):
    def __init__(self, player_image, player_x, player_y, h,w ,player_speed):   
        super().__init__(player_image, player_x, player_y, h,w ,player_speed)
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y > 680:
            bullet.delete()

rocket = Player('rocket.png', 300, 430, 100,65, 5)
sanya = Enemy('ufo.png', 300, 0, 65,65, 5)  

monstres = sprite.Group()
for i in range(10):
    monstres.add(Enemy('ufo.png', randint(0, 680), randint(0, 10), 65, 65,5))    

bullets = sprite.Group()



font1 = font.Font(None, 70)
font2 = font.Font(None, 70)

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    window.blit(background, (0,0))

    rocket.update()
    rocket.reset()
    
    key_pressed = key.get_pressed()

    if key_pressed[K_UP]:
        bullet = Bullet('bullet.png', rocket.rect.centerx, rocket.rect.top, 50,50, 5)
        bullets.add(bullet)

    sprites_list = sprite.groupcollide(monstres, bullets, True, True)
    for i in sprites_list:
        monstres.add(Enemy('ufo.png', randint(0, 680), randint(0, 10), 65, 65,5))        
        monsters_kill += 1

    
    killed = font1.render('УБИТО:'+str(monsters_kill), 1, (200, 200, 200))
    window.blit(killed, (0,0))

    #loster = font2.render('ПРОПУЩЕННО:'+str(lost), 1, (200, 0, 200))
    #window.blit(loster, (0,50))

    bullets.draw(window)
    monstres.draw(window)
    bullets.update()
    monstres.update()

    display.update()
