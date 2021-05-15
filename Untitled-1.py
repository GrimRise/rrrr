from pygame import *

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
        if keys_pressed[K_DOWN] and self.rect.y  < 500 - 80:
            self.rect.y += self.speed
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -=self.speed
        if keys_pressed[K_s] and self.rect.y  < 500 - 80:
            self.rect.y +=self.speed






sprite1 = GameSprite('ball.png', 250, 300,50 ,50, 5)
sprite2 = Player('sprite2.png', 680, 200,20,100, 5)
sprite3 = Player('sprite2.png', 0, 200,20,100, 5)







clock = time.Clock()
FPS = 60
game = True
while game:
    keys_pressed = key.get_pressed()
    window.blit(background,(0,0))
    window.blit(sprite1, (250, 300))
    window.blit(sprite2, (680, 200))
    window.blit(sprite3, (0, 200))
    sprite2.update_r()
    sprite3.update_l()
    sprite2.reset()
    sprite3.reset()
    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(FPS)