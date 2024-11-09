from pygame import *

window = display.set_mode((700, 500)) 
display.set_caption("Догонялки")
background = transform.scale(image.load("background.jpg"), (700, 500) )



#mixer.init()
#mixer.music.load("jungles.ogg")
#mixer.music.play()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect() # хитбокс
        self.rect.x = player_x
        self.rect.y = player_y
        self.direction = 'left'       

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

    def move(self):
        keys = key.get_pressed()
        if keys[K_LEFT]:
            self.rect.x -= self.speed
        if keys[K_RIGHT]:
            self.rect.x += self.speed
        if keys[K_UP]:
            self.rect.y -= self.speed
        if keys[K_DOWN]:
            self.rect.y += self.speed

    def auto_move(self): 
        if self.rect.x <= 470:
            self.direction = "right"
        if self.rect.x >= 615:
            self.direction = "left"

        if self.direction == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed 
    
class Wall(sprite.Sprite):
    def __init__(self,color1, color2, color3, wallx, wally, widht, height):
        super().__init__()
        self.color1 = color1
        self.color2 = color2
        self.color3 = color3
        self.widht = widht
        self.height = height
        self.image = Surface((self.widht, self.height))
        self.image.fill((color1, color2,color3))
        self.rect = self.image.get_rect()
        self.rect.x = wallx
        self.rect.y = wally

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))    



hero = GameSprite('hero.png', 100, 100, 22)
w1 = Wall(154, 205, 50, 100, 20, 450, 10)
w2 = Wall(250, 100, 0, 100, 480, 350, 10)
w3 = Wall(0, 50, 250, 100, 20, 10, 380)
w4 = Wall(0, 90, 200, 250, 50, 30, 360)

enemy = GameSprite('cyborg.png', 40, 100, 10)

game = True
while game:
    window.blit(background, (0,0))
    hero.move()
    enemy.auto_move()
    hero.reset()
    enemy.reset()

    
    w1.draw()
    w2.draw()
    w3.draw()
    w4.draw()

    for e in event.get():
        if e.type == QUIT:
            game = False



    display.update()
    time.delay(50)