#NOTE: CANNOT ENTER A BLOCK DEPTH LESS THAN 8.

import pygame
from classes import Rectangle, Ball, Block
from easy import block_create_easy, BLOCK_WIDTH, BLOCK_DEPTH
pygame.init()

#Note: I usually update the screen as soon as I move my object, to reduce stutter

MAX_WIDTH = 480
MAX_DEPTH = 356

#Colours
red = (255,0,0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255,255,255)
black = (0,0,0)

#Bounce check is a variable which makes sure the ball only bounces on the rectangle once
#It resets to 0 if it bounces on another object.
bounce_check = 0

win = pygame.display.set_mode((MAX_WIDTH,MAX_DEPTH))

pygame.display.set_caption("Lateres")

clock = pygame.time.Clock()

running = True

#Setting up the rectangle sprite
rect_sprites = pygame.sprite.Group()
rectangle = Rectangle(red)
rect_sprites.add(rectangle)
#Setting the starting sprites of the rectangle
rect_sprites.draw(win)
pygame.display.flip()

#Setting up the ball sprite
ball_sprites = pygame.sprite.Group()
ball = Ball(white)
ball_sprites.add(ball)
#Setting the starting sprites of the ball
ball_sprites.draw(win)
pygame.display.flip()

#Setting up the blocks for easy mode.
block_sprites = pygame.sprite.Group()
block_sprites = block_create_easy(block_sprites)
#Setting the starting sprites of the blocks.
block_sprites.draw(win)
pygame.display.flip()


#Main loop
while running:
    clock.tick(70)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        rectangle.move_right(MAX_WIDTH, win, black, rect_sprites)
    if keys[pygame.K_LEFT]:
        rectangle.move_left(MAX_WIDTH, win, black, rect_sprites)

    #Below is to update the position of the ball.
    ball.update_ball(win, ball_sprites)
    ball_sprites.draw(win)
    pygame.display.flip()

    #Below is to update the velocity of the ball if it reaches the rectangle.
    if bounce_check == 0:
        if pygame.sprite.spritecollide(ball, rect_sprites, False):
            x_centre = ball.rect.x + ball.radius - rectangle.rect.x
            fraction_of_rect = x_centre/rectangle.width
            ball.rebound_rectangle(fraction_of_rect)
            bounce_check = 1
    #Below is for if the ball hits the rectangle, and we need to reset the colour
    if ball.rect.y + 2*ball.radius >= MAX_DEPTH - rectangle.height:
        rectangle.update_rect(win, red, rect_sprites)

    #Below is for if we rebound off the left wall.
    if ball.rect.x <= 0:
        ball.rebound_left_wall()
        bounce_check = 0
    #Below is for if we rebound off the right wall.
    if ball.rect.x + 2*ball.radius >= MAX_WIDTH:
        ball.rebound_right_wall()
        bounce_check = 0
    #Below is for if we rebound off the ceiling.
    if ball.rect.y <= 0:
        ball.rebound_ceiling()
        bounce_check = 0
    #Below is if we hit the ground (fail)
    if ball.rect.y >= MAX_DEPTH:
        running = False

    #Below is to check if the ball hit the blocks
    collision_list = pygame.sprite.spritecollide(ball, block_sprites, False)
    #if collision_list:
        #This is where I calculate the rebound direction.
        #Below is for if the ball hits on the left side of the block
    for i in collision_list:
        #Make the below an elif. if it doesn't hit the bottom

        if ball.rect.y <= i.rect.y + i.height and ball.rect.y >= i.rect.y + i.height - ball.radius:
            ball.rebound_ceiling()
        #Below elif is for if the ball bounces on top of a block.
        elif ball.rect.y + 2*ball.radius <= i.rect.y and ball.rect.y + ball.radius >= i.rect.y:
            ball.rebound_horizontal()
        elif ball.rect.x + 2*ball.radius >= i.rect.x and ball.rect.x + ball.radius <= i.rect.x:
            ball.rebound_right_wall()
        elif ball.rect.x <= i.rect.x + i.width and ball.rect.x + ball.radius >= i.rect.x + i.width:
            ball.rebound_left_wall()
        bounce_check = 0
        i.delete_blocks(win, black, i.rect.x, i.rect.y)
        pygame.sprite.Sprite.kill(i)

    block_sprites.draw(win)
    pygame.display.flip()

ball_sprites.empty()
block_sprites.empty()
rect_sprites.empty()
win.fill(black)

gameover = pygame.image.load('gameover.jpg')
win.blit(gameover, (75, 60))
pygame.display.update()
pygame.time.wait(1000)


#FUTURE GOALS:
    #Set up an enemy that tries to stop you... If they shoot you, you can't move
    #For a couple seconds. Or prevents user input for a bit. #pygame.get.time.ticks? 
    #while loop that repeats until seconds are over?
