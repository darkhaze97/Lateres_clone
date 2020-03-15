#This file will contain functions that update the screen.
import pygame

BLOCK_WIDTH = 48
BLOCK_HEIGHT = 8
start = 1

#Below creates the blocks
def block_creator():
    blocks = []
    block_creation_iterator = 0
    while block_creation_iterator < 30:
        blocks.append({'is_alive': 1, 'y_pos': y_position, 'x_pos': x_position})
        block_creation_iterator += 1
    TOTAL_BLOCKS = 30
    return (blocks, TOTAL_BLOCKS)

def y_number(index):
    if index < 10:
        return 0
    elif index < 20:
        return 8
    elif index < 30:
        return 16

def column_number(index):
    if index < 10:
        return index*48
    elif index < 20:
        index -= 10
        return index*48
    elif index < 30:
        index -= 20
        return index*48


#Update fill screen simply fills the screen with black.
def update_fill_rectangle_row(win, rectangle):
    win.fill((0,0,0), (rectangle['x'], rectangle['y'], rectangle['width'], rectangle['height']))
    pass

#Update rectangle needs the window, relative location, height and depth.
def update_rectangle(win, x, y, width, height):
    pygame.draw.rect(win, (255, 0 ,0), (x, y, width, height))
    pygame.display.update()
    pass

#Update blocks needs the window, list of dic of the blocks. We will use a dictionary to store the value of whether
#The block has been destroyed yet.
def update_blocks(win, blocks):
    i = 0
    for m in blocks:
        if m['is_alive'] == 1:
            block_calculation(i, win)
        i += 1
    #Below is to erase all blocks so that it could be filled with new ones
    pygame.display.update()
    pass

def block_fill(i, win):
    if i >= 0 and i < 10:
        x = i * 48
        y = 0
    if i >= 10 and i < 20:
        i -= 10
        x = i * 48
        y = 8
    if i >= 20 and i < 30:
        i -= 20
        x = i * 48
        y = 16
    win.fill((0,0,0), (x, y, BLOCK_WIDTH, BLOCK_HEIGHT))


#Block calculation will calculate the positions for the blocks and draws them.
def block_calculation(i, win):
    #tmp will be used to calculate the colour.
    tmp = i
    #Calculates position
    if i >= 0 and i < 10:
        x = i*48
        y = 0
    if i >= 10 and i < 20:
        i -= 10
        x = i*48
        y = 8
    elif i >= 20 and i < 30:
        i -= 20
        x = i*48
        y = 16

    #Below is to calculate colour
    if tmp % 3 == 0:
        pygame.draw.rect(win, (255, 0, 0), (x, y, BLOCK_WIDTH, BLOCK_HEIGHT))
    elif (tmp - 1) % 3 == 0:
        pygame.draw.rect(win, (0, 255, 0), (x, y, BLOCK_WIDTH, BLOCK_HEIGHT))
    elif (tmp - 2) % 3 == 0:
        pygame.draw.rect(win, (0, 0, 255), (x, y, BLOCK_WIDTH, BLOCK_HEIGHT))
    pass

def update_ball(win, ball, blocks, rectangle, MAX_WIDTH, MAX_DEPTH):
    if start == 1:
        pygame.draw.circle(win, (255, 255, 255), (ball['x'], ball['y']), ball['radius'])
        pass
    #We want to check the position first --> whether it hits the rectangle or not.
    x_pos = ball['x']
    y_pos = ball['y']

    #Below is to find the number of rows
    rows = 0
    while rows < len(blocks):
        rows += 1
    rows += 1
    rows = rows/10 #10 is how many blocks are in a row. i will then equal to the number of rows.
    #Below is to check where my x alue is when it hits the rectangle.
    if y_pos == 348:
        if x_pos % 4 != 0:
            print("Dead")
    #If statement below determines if the ball is in the value range of the rectangle.
    if (x_pos >= rectangle['x'] and x_pos <= rectangle['x'] + rectangle['width']) and (y_pos + ball['radius'] == rectangle['y']):
        ball['y_velocity'] = -1 * ball['y_velocity']
        #The if statements below test how the ball will bounce off.
        if x_pos >= rectangle['x'] and x_pos < rectangle['x'] + 16:
            ball['x_velocity'] = -1*ball['velocity_reference']
        elif x_pos >= rectangle['x'] + 16 and x_pos < rectangle['x'] + 32:
            ball['x_velocity'] = int(-1/2 * ball['velocity_reference'])
        elif x_pos == rectangle['x'] + 32:
            ball['x_velocity'] = 0 * ball['velocity_reference']
        elif x_pos > rectangle['x'] + 32 and x_pos < rectangle['x'] + 48:
            ball['x_velocity'] = int(1/2 * ball['velocity_reference'])
        elif x_pos >= rectangle['x'] + 48 and x_pos <= rectangle['x'] + 64:
            ball['x_velocity'] = 1 * ball['velocity_reference']

    #If statement below determines if the ball is in the value range of the blocks.
    if y_pos - ball['radius'] == 24 and ball['y_velocity'] < 0:
        block_number = 20 + int(x_pos/48)
        if blocks[block_number].get('is_alive') == 1:
            ball['y_velocity'] = -1 * ball['y_velocity']
            blocks[block_number]['is_alive'] = 0
            block_fill(block_number, win)
            #Below if statement determines whether the ball hits the boundary of two blocks.
            if x_pos % 48 == 0:
                previous_block_number = block_number - 1
                blocks[previous_block_number]['is_alive'] = 0
                block_fill(previous_block_number, win)
    elif y_pos - ball['radius'] == 16 and ball['y_velocity'] < 0:
        block_number = 10 + int(x_pos/48)
        if blocks[block_number].get('is_alive') == 1:
            ball['y_velocity'] = -1 * ball['y_velocity']
            blocks[block_number]['is_alive'] = 0
            block_fill(block_number, win)
            #Below if statement determines whether the ball hits the boundary of two blocks
            if x_pos % 48 == 0:
                previous_block_number = block_number - 1
                blocks[previous_block_number]['is_alive'] = 0
                block_fill(previous_block_number, win)
    elif y_pos - ball['radius'] == 8 and ball['y_velocity'] < 0:
        block_number = int(x_pos/48)
        if blocks[block_number].get('is_alive') == 1:
            ball['y_velocity'] = -1 * ball['y_velocity']
            blocks[block_number]['is_alive'] = 0
            block_fill(block_number, win)
            if x_pos % 48 == 0:
                previous_block_number = block_number - 1
                blocks[previous_block_number]['is_alive'] = 0
                block_fill(previous_block_number, win)
    #The next 2 if statements are for when the ball hits the blocks from above
    elif y_pos + ball['radius'] == 16 and ball['y_velocity'] > 0:
        block_number = 20 + int(x_pos/48)
        if blocks[block_number].get('is_alive') == 1:
            ball['y_velocity'] = -1 * ball['y_velocity']
            blocks[block_number]['is_alive'] = 0
            block_fill(block_number, win)
    elif y_pos + ball['radius'] == 8 and ball['y_velocity'] > 0:
        block_number = 10 + int(x_pos/48)
        if blocks[block_number].get('is_alive') == 1:
            ball['y_velocity'] = -1 * ball['y_velocity']
            blocks[block_number]['is_alive'] = 0
            block_fill(block_number, win)
    #The next 2 if statements are for when the ball hits the boundary.
    #Note: Since the y_velocity of the ball is always 5 or -5, we don't need to worry about it hitting half way of the block's height
    #Below is for when the ball hits on the right side.
    """
    if y_pos == 16 and (x_pos - ball['radius']) % 48 == 0:
        ball['x_velocity'] = -1 * ball['x_velocity']
        block_number = 20 + int(x_pos/48)
        previous_block_number = block_number - 1
        #above_block_number = previous_block_number - 10
        blocks[previous_block_number]['is_alive'] = 0
        block_fill(previous_block_number, win)
        #blocks[above_block_number]['is_alive'] = 0
        #block_fill(above_block_number, win)
    if y_pos == 8 and (x_pos - ball['radius']) % 48 == 0:
        ball['x_velocity'] = -1 * ball['x_velocity']
        block_number = 10 + int(x_pos/48)
        previous_block_number = block_number - 1
        #above_block_number = previous_block_number - 10
        blocks[previous_block_number]['is_alive'] = 0
        block_fill(previous_block_number, win)
        #blocks[above_block_number]['is_alive'] = 0
        #block_fill(above_block_number, win)
    #Below is for hitting on the right
    if y_pos == 16 and (x_pos + ball['radius']) % 48 == 0:
        ball['x_velocity'] = -1 * ball['x_velocity']
        block_number = 20 + int(x_pos/48)
        #previous_block_number = block_number - 1
        #above_block_number = previous_block_number - 10
        blocks[block_number]['is_alive'] = 0
        block_fill(block_number , win)
        #blocks[above_block_number]['is_alive'] = 0
        #block_fill(above_block_number, win)
    if y_pos == 8 and (x_pos + ball['radius']) % 48 == 0:
        ball['x_velocity'] = -1 * ball['x_velocity']
        block_number = 10 + int(x_pos/48)
        #previous_block_number = block_number - 1
       # above_block_number = previous_block_number - 10
        blocks[block_number]['is_alive'] = 0
        block_fill(block_number, win)
        #blocks[above_block_number]['is_alive'] = 0
        #block_fill(above_block_number, win)"""
    #Below is if we hit from the left. 

    if y_pos == 4 and (((x_pos + ball['radius']) % 48 == 0 or (x_pos + ball['radius']) % 48 == 2) or x_pos % 48 == 0):
        #If we hit the left side, our block number will give us the number of the block we hit.
        block_number = int(x_pos/48)
        if blocks[block_number].get('is_alive'):
            ball['x_velocity'] = -1 * ball['x_velocity']
            blocks[block_number]['is_alive'] = 0
            block_fill(block_number, win)
    elif y_pos == 12 and (((x_pos + ball['radius']) % 48 == 0 or (x_pos + ball['radius']) % 48 == 2) or x_pos % 48 == 0):
        block_number = 10 + int(x_pos/48)
        if blocks[block_number].get('is_alive'):
            ball['x_velocity'] = -1 * ball['x_velocity']
            blocks[block_number]['is_alive'] = 0
            block_fill(block_number, win)
    elif y_pos == 20 and (((x_pos + ball['radius']) % 48 == 0 or (x_pos + ball['radius']) % 48 == 2) or x_pos % 48 == 0):
        block_number = 20 + int(x_pos/48)
        if blocks[block_number].get('is_alive'):
            ball['x_velocity'] = -1 * ball['x_velocity']
            blocks[block_number]['is_alive'] = 0
            block_fill(block_number, win)
        #Bug with hitting from right, where we need to calculate the PREV block.
    elif y_pos == 4 and (((x_pos - ball['radius']) % 48 == 0 or (x_pos - ball['radius']) % 48 == 2) or x_pos % 48 == 0):
        block_number = int(x_pos/48) - 1
        if blocks[block_number].get('is_alive'):
            ball['x_velocity'] = -1 * ball['x_velocity']
            blocks[block_number]['is_alive'] = 0
            block_fill(block_number, win)
    elif y_pos == 12 and (((x_pos - ball['radius']) % 48 == 0 or (x_pos - ball['radius']) % 48 == 2) or x_pos % 48 == 0):
        block_number = 10 + int(x_pos/48) - 1
        if blocks[block_number].get('is_alive'):
            ball['x_velocity'] = -1 * ball['x_velocity']
            blocks[block_number]['is_alive'] = 0
            block_fill(block_number, win)
    elif y_pos == 20 and (((x_pos - ball['radius']) % 48 == 0 or (x_pos - ball['radius']) % 48 == 2) or x_pos % 48 == 0):
        block_number = 20 + int(x_pos/48) - 1
        if blocks[block_number].get('is_alive'):
            ball['x_velocity'] = -1 * ball['x_velocity']
            blocks[block_number]['is_alive'] = 0
            block_fill(block_number, win)
    if y_pos == 4:
        print(f"y = 4, {x_pos}")
    elif y_pos == 12:
        print(f"y = 12, {x_pos}")
    elif y_pos == 20:
        print(f"y == 20, {x_pos}")




    #If statements below determines if the ball hits the walls.
    #Checking left wall first.
    if x_pos - ball['radius'] <= 0:
        ball['x_velocity'] = -1*ball['x_velocity']
    #Checking right wall next.
    elif x_pos + ball['radius'] >= 480:
        ball['x_velocity'] = -1*ball['x_velocity']

    #If statement for if the ball hits the ceiling.
    if y_pos - ball['radius'] <= 0:
        ball['y_velocity'] = -1 * ball['y_velocity']

    #If statement below checks if you lose the game.
    if y_pos + ball['radius'] == 356:
        ball['y_velocity'] = -1 * ball['y_velocity'] #(Will change later)
        win.fill((0,0,0), (ball['x'] - ball['radius'], ball['y'] - ball['radius'], 2*ball['radius'], 2*ball['radius']))

    #Below is to fill the previous instance of the ball black.
    pygame.draw.circle(win, (0,0,0), (ball['x'], ball['y']), ball['radius'])

    prev_y_pos = ball['y']
    prev_x_pos = ball['x']

    #Below is to show the next position of the ball.
    ball['y'] += ball['y_velocity']
    ball['x'] += ball['x_velocity']

    #Then, we draw the ball
    if ball['y'] <= 15:
        pygame.draw.circle(win, (0,0,0), (prev_x_pos, prev_y_pos), ball['radius'])
    win.fill((0,0,0), (ball['x']-ball['radius'], ball['y']-ball['radius'],0,rows*BLOCK_HEIGHT))
    pygame.draw.circle(win, (255, 255, 255), (ball['x'], ball['y']), ball['radius'])

    pygame.display.update()
    return (ball, blocks)

#We need to return a tuple of ball and blocks
#We want to check if the ball hits anything if it's radius and centre enter the x <= 500 and y <= 10 range.

def update_ball(win, ball, blocks, rectangle, MAX_WIDTH, MAX_DEPTH):
