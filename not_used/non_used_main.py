import pygame
#from display import update_rectangle, update_fill_rectangle_row, update_blocks, update_ball, block_creator
from classes import Rectangle
pygame.init()

MAX_WIDTH = 480
MAX_DEPTH = 356

#Colours
red = (255,0,0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255,255,255)
black = (0,0,0)

win = pygame.display.set_mode((MAX_WIDTH,MAX_DEPTH))

pygame.display.set_caption("Lateres")

clock = pygame.time.Clock()

running = True
"""
#Below is to set up the rectangle
rectangle = {
    #Starting position
    'x': 220,
    'y': 352,
    #Rectangle dimensions
    'width': 64,
    'height': 4,
    'vel': 4
}

#Below is to set up the ball
ball = {
    'x': 252,
    'y': 100,
    'radius': 4,
    #Velocity reference is to help change x_velocity.
    'velocity_reference': 4,
    'x_velocity': 0,
    #Y velocity is +- 4
    'y_velocity': 4,
}

#Below is to set up the blocks
block_convert = block_creator()
blocks = block_convert[0]
TOTAL_BLOCKS = block_convert[1]"""

rect_sprites = pygame.sprite.Group()

rectangle = Rectangle(red)
rect_sprites.add(rectangle)



#To set the starting sprites
pygame.display.flip()

#Main loop
while running:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()

    if keys[pygame.K_RIGHT]:
        rectangle.move_right(MAX_WIDTH, win, black, rect_sprites)
    if keys[pygame.K_LEFT]:
        rectangle.move_left(MAX_WIDTH, win, black, rect_sprites)

    """
    if keys[pygame.K_RIGHT] and rectangle['x'] < MAX_WIDTH - rectangle['width']:
        update_fill_rectangle_row(win, rectangle)
        rectangle['x'] = rectangle['x'] + rectangle['vel']
    if keys[pygame.K_LEFT] and rectangle['x'] > 0:
        update_fill_rectangle_row(win, rectangle)
        rectangle['x'] = rectangle['x'] - rectangle['vel']

    update_rectangle(win, rectangle['x'], rectangle['y'], rectangle['width'], rectangle['height'])

    #Update ball function should return list dic of blocks and dic of ball as a tuple.
    ball_block_info = update_ball(win, ball, blocks, rectangle, MAX_WIDTH, MAX_DEPTH)

    #Below is to update the ball info.
    ball_to_update = ball_block_info[0]
    ball = ball_to_update
   
    #Below is to update the block info.
    block_to_update = ball_block_info[1]
    i = 0
    while i < TOTAL_BLOCKS:
        blocks[i]['is_alive'] = block_to_update[i]['is_alive']
        i += 1

    update_blocks(win, blocks)"""

  


pygame.quit()

#To make a ball, I will make it so that if it hits any of the boundary of the rectangle, it will rebound in a specific way (will think later)
#I will call it after we move our rectangle.
#It will have a specific velocity
#Depending on where the ball hits, it will rebound in a specific way. E.g. if it hits midway between the edge and middle,
#The y velocity remains the same (always constant), but the x velocity will be 1/2 of normal velocity, etc.
#When the ball bounces on any other surface, it's rebound velocity will depend on the surface. e.g. if it hits the right boundary,
#it's x velocity becomes the opposite.

#FILL SCREEN ONLY IF SOMETHING CHANGES AND ONLY FOR THE THING THAT CHANGES

#NEXT GOAL:
    #CHANGE THE MOVEMENTS OF THE BALL DEPENDENT ON LANDING.Convert the position of the ball.
    #CHANGE EVERYTHING TO BE IN REFERENCE OF VELOCITY = 4
    #THE BALL'S TRAVEL IS NOT IN EXACT MULTIPLES OF 4. THEREFORE, TO CHECK WHERE IT HITS THE SIDES, WE MUST ALLOW FOR +3 ROOM. I.E.
    #E.G. (x_pos + ball['radius']) % 48 == 0: OR OR == 2 --> need to calculate if this is the case or not.
    #Fix the hitboxes: Allow balls to hit the tip of the block


    #CHANGE THE BLOCK DICTIONARY SO THAT IT CONTAINS THE X AND Y VALUE OF WHERE IT BEGINS.



#NEXT GOAL: 
    #USE SPRITES... SET UP THE CLASSES, DO THE CALCUALTIONS, ETC. TO SET UP BALL, BLOCKS AND RECTANGLE. MAYBE ALSO SET UP THE VELOCITY OF THE BALL.
