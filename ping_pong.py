#Создать класс GameSprite(Shooter)
from pygame import *
class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, speed, width=70, height=70):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (width, height))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
#Cоздать класс Player(Shooter)
class Player(GameSprite):
    def update_l(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 435:
            self.rect.y += self.speed
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 435:
            self.rect.y += self.speed

window = display.set_mode( (708, 500))
#Закрасить фоном
window.fill((130, 100, 200))
#Создать игровой таймер
clock = time.Clock()
    #Создать Обьекты ракеток
racket1 = Player( 'platform_v.png', 25, 150, 3, 15, 50)
racket2 = Player( 'platform_v.png', 650, 150, 3, 15, 50)
     #Создать переменные game, finish
game = True
finish = False
     #Запустить игровой цикл while
while game:
    #Прописать цикл ог для обработки, события нажатия на крестик
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill((130, 100, 200))
        racket1.update_l()
        racket2.update_r()
        racket1.reset ()
        racket2.reset()
        
    display.update()
    clock. tick(60)