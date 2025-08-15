from pygame import *
# from pygame import *
# pyame.init()
path = 'C:/Data Scientist/Algonova/Courses/Python Pro I/Modul 6/L3/pacman.png'

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        sprite.Sprite.__init__(self)  # super().__init__() 
        self.image = transform.scale(image.load(player_image), (size_x, size_y))

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):  # Ini akan menempel gambar yang kita pasang pada koordinat tertentu
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed, player_y_speed):
        GameSprite.__init__(self, player_image, player_x, player_y,size_x, size_y) 
        self.x_speed = player_x_speed
        self.y_speed = player_y_speed

    # tambahan untuk pertemuan 2
    def update(self):
        if (packman.rect.x <= win_width-80 and packman.x_speed > 0) or (packman.rect.x >= 0 and packman.x_speed < 0):
            self.rect.x += self.x_speed
    
        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.x_speed > 0: 
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left) 
                
        elif self.x_speed < 0: 
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right) 

        if packman.rect.y <= win_height-80 and packman.y_speed > 0 or packman.rect.y >= 0 and packman.y_speed < 0:
            self.rect.y += self.y_speed

        platforms_touched = sprite.spritecollide(self, barriers, False)
        if self.y_speed > 0: 
            for p in platforms_touched:
                self.rect.bottom = min(self.rect.bottom, p.rect.top)

        elif self.y_speed < 0: 
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom) 

#Creating a window
win_width = 700
win_height = 500
display.set_caption("Maze")
window = display.set_mode((win_width, win_height))
background_color = (0.15*255, 0.15*255, 0.15*255)
# clock = time.Clock

barriers = sprite.Group()

w1 = GameSprite('C:/Data Scientist/Algonova/Courses/Python Pro I/Modul 6/L3/platform2.png',win_width / 2 - win_width / 3, win_height / 2, 300, 50)
w2 = GameSprite('C:/Data Scientist/Algonova/Courses/Python Pro I/Modul 6/L3/platform2_v.png', 370, 100, 50, 400)

barriers.add(w1)
barriers.add(w2)

packman = Player('C:/Data Scientist/Algonova/Courses/Python Pro I/Modul 6/L3/pacman.png', 5, win_height - 80, 80, 80, 0, 0)
# enemy = Player('C:/Data Scientist/Algonova/Courses/Python Pro I/Modul 6/L3/enemy.png', win_width - 80, 180, 80, 80, 0, 0)

# tambahan untuk pertemuan 2
monster = GameSprite('C:/Data Scientist/Algonova/Courses/Python Pro I/Modul 6/L3/enemy.png', win_width - 80, 180, 80, 80)
final_sprite = GameSprite('C:/Data Scientist/Algonova/Courses/Python Pro I/Modul 6/L3/final.png', win_width - 85, win_height - 100, 80, 100)

finish = False
run = True
while run:
    # ini untuk run frame game di dalam milisekon
    time.delay(50)
    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_LEFT:
                packman.x_speed = -100
            elif e.key == K_RIGHT:
                packman.x_speed = 100
            elif e.key == K_UP :
                packman.y_speed = -100
            elif e.key == K_DOWN :
                packman.y_speed = 100
        elif e.type == KEYUP:
            if e.key == K_LEFT :
                packman.x_speed = 0
            elif e.key == K_RIGHT:
                packman.x_speed = 0
            elif e.key == K_UP:
                packman.y_speed = 0
            elif e.key == K_DOWN:
                packman.y_speed = 0
    if not finish:
        window.fill(background_color)

    w1.reset()
    w2.reset()

    # tambahan pertemuan 2
    barriers.draw(window)
    
    monster.reset()
    final_sprite.reset()
    packman.reset()

    # tambahan part 2
    packman.update()

    # tambahan part 2 ini mekanisme game ketika menang atau kalah
    if sprite.collide_rect(packman, monster):
        finish = True
        img = image.load('C:/Data Scientist/Algonova/Courses/Python Pro I/Modul 6/L3/game-over_1.png')
        d = img.get_width() // img.get_height()
        window.fill((255, 255, 255))
        lose = transform.scale(img, (win_height * d, win_height))
        window.blit(lose, (90, 0))

    if sprite.collide_rect(packman, final_sprite):
        finish = True
        img = image.load('C:/Data Scientist/Algonova/Courses/Python Pro I/Modul 6/L3/Wisuda.jpg')
        window.fill((255, 255, 255))
        window.blit(transform.scale(img, (win_width, win_height)), (0, 0))
        

    display.update()
