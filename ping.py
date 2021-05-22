from pygame import *
finish = False

font.init()
font1 = font.SysFont('Arial', 40)
lose = font1.render("Lose 2", True, (180, 0 ,0))
lose1 = font1.render("Lose 1", True, (180, 0 ,0))
window = display.set_mode((700, 500))
display.set_caption('Теннис')
background = transform.scale(image.load('fon.jpg'), (700, 500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x,size_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (size_x, size_y))
        self.rect = self.image.get_rect()
        self.speed = player_speed
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y  < 420:
            self.rect.y += self.speed
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -=self.speed
        if keys_pressed[K_s] and self.rect.y  < 420:
            self.rect.y +=self.speed


speed_x = 3
speed_y = 3


sprite1 = GameSprite('ball.png', 250,300,50,50,5)
sprite2 = Player('sprite2.jpg', 680, 200,20,100, 5)
sprite3 = Player('sprite2.jpg', 0, 200,20,100, 5)

clock = time.Clock()
FPS = 60
game = True
while game:
    keys_pressed = key.get_pressed()
    window.blit(background, (0,0))
    
  
    sprite2.update_r()
    sprite3.update_l()
    sprite1.reset()
    sprite2.reset()
    sprite3.reset()
    if finish != True:
        sprite1.rect.x += speed_x
        sprite1.rect.y += speed_y
    if sprite.collide_rect(sprite2, sprite1) or sprite.collide_rect(sprite3, sprite1):
        speed_x *= -1
    if sprite1.rect.y > 450 or sprite1.rect.y < 0:
        speed_y *= -1
    if sprite1.rect.x > 700:
        window.blit(lose, (350,250))
    if sprite1.rect.x < 0:
        window.blit(lose1, (350,250))
    
    
    
    
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)