class Paddle(pygame.sprite.Sprite):
#Class represents a car

def __init__(self, color, width, height):
#Call the parent class constructor
super().__init__()

#Pass in the color, position, width and height
#Set the background color and set it to transparent
self.image = pygame.Surface([width, height])
self.image.fill(BLACK)
self.image.set_colorkey(BLACK)

#Draw the paddle
pygame.draw.rect(self.image, color, [0, 0, width, height])
#fetch the object
self.rect = self.image.get_rect()

def moveUP(self, pixels):
self.rect.y -= pixels
#Check that your not going too far off the screen
if self.rect.y < 0:
self.rect.y = 0

def moveDown(self, pixels):
self.rect.y += pixels
if self.rect.y > 400:
self.rect.y = 400
