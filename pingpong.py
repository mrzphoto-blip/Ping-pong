from pygame import *
black = (200,255,255)
win_width = 680
win_height = 580
win = display.set_mode([win_width,win_height])
display.set_caption('Ping - pong')
win.fill(black)
game = True
clock = time.Clock()
FPS = 60
class GameSprite(sprite.Sprite):
    def __init__(self,player_image,player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        win.blit(self.image,(self.rect.x,self.rect.y))
class Player(GameSprite):
    def update_l(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_s] and self.rect.x1 < win_height:
            self.rect.y += self.speed
    def update_r(self):
        key_pressed = key.get_pressed()
        if key_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if key_pressed[K_DOWN] and self.rect.x1 < win_height:
            self.rect.y += self.speed
player_l =Player('.png',50,400,5)
player_r =Player('.png',50,400,5)
ball = Player('ball.png',50,400,50)
font1 =font.Font("Arial",70)
win1 = font.render('Ура',True,(255,215,0))
lose = font.render('Нет',True,(180,0,0))
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        player_l.update_l()
        player_l.reset()
        player_r.update_r()
        player_r.reset()
        ball.update()
        ball.reset()
    clock.tick(FPS)
win.update()
