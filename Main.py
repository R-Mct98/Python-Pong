#Import the pygame library
import pygame
from paddle import Paddle
from ball import Ball

pygame.init()

#Define some colours
BLACK = (0,0,0)
WHITE = (255,255,255)
#Open a new window
size = (500, 500)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Python Pong")

paddleA = Paddle(WHITE, 10, 100)
paddleA.rect.x = 20
paddleA.rect.y = 200

paddleB = Paddle(WHITE, 10, 100)
paddleB.rect.x = 670
paddleB.rect.y = 200

ball = Ball(WHITE,10,10)
ball.rect.x = 345
ball.rect.y = 195

#list that contains all sprites
all_sprites_list = pygame.sprite.Group()
#add paddles to list of sprites
all_sprites_list.add(paddleA)
all_sprites_list.add(paddleB)
all_sprites_list.add(ball)

#loop will carry on until player exits
carryOn = True
#clock used to control updates
clock = pygame.time.Clock()

#Initialise player scores
scoreA = 0
scoreB = 0

#Main program loop
while carryOn:
#main event loop
for event in pygame.event.get():
if event.type == pygame.QUIT:
carryOn = False
elif event.type==pygame.KEYDOWN:
if event.key==pygame.K_x:
carryOn=False

#Moving the paddles using Arrow keys
keys = pygame.key.get_pressed()
if keys[pygame.K_w]:
paddleA.moveUp(5)
if keys[pygame.K_s]:
paddleA.moveDown(5)
if keys[pygame.K_UP]:
paddleB.moveUp(5)
if keys[pygame.K_DOWN]:
paddleB.moveDown(5)

#Game Logic here
all_sprites_list.update()

#Check if the ball is bouncing against any of the 4 walls:
    if ball.rect.x>=690:
        scoreA+=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.x<=0:
        scoreB+=1
        ball.velocity[0] = -ball.velocity[0]
    if ball.rect.y>490:
        ball.velocity[1] = -ball.velocity[1]
    if ball.rect.y<0:
        ball.velocity[1] = -ball.velocity[1]

#Detect collisions between the ball and the paddles
if pygame.sprite.collide_mask(ball, paddleA) or pygame.sprite.collide_mask(ball, paddleB):
ball.bounce()

#Drawing Code
#clear screen to black
screen.fill(BLACK)
#Draw the net
pygame.draw.line(screen, WHITE, [349, 0], [349, 500], 5)

#Draw sprites in one go
all_sprites_list.draw(screen)

#Display scores:
    font = pygame.font.Font(None, 74)
    text = font.render(str(scoreA), 1, WHITE)
    screen.blit(text, (250,10))
    text = font.render(str(scoreB), 1, WHITE)
    screen.blit(text, (420,10))

#Update the screen
pygame.display.flip()
#Limit frames per second
clock.tick(60)
#Stopping the loop once exited
pygame.quit()
