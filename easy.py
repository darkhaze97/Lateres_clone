#This file will set up the blocks.
from classes import Block

#Block attributes
BLOCK_WIDTH = 48
BLOCK_DEPTH = 16

#Colours
red = (255,0,0)
green = (0, 255, 0)
blue = (0, 0, 255)

def block_create_easy(block_sprites):
    i = 0
    N_BLOCKS = 30
    block_y_pos = 0
    while i < N_BLOCKS:
        if i >= 0 and i < 10:
            block_x_pos = i * BLOCK_WIDTH
        if i >= 10 and i < 20:
            block_y_pos = BLOCK_DEPTH
            block_x_pos = (i - 10) * BLOCK_WIDTH
        if i >= 20 and i < 30:
            block_y_pos = 2*BLOCK_DEPTH
            block_x_pos = (i - 20) * BLOCK_WIDTH
        if i % 3 == 0:
            colour = red
        elif (i - 1) % 3 == 0:
            colour = green
        elif (i - 2) % 3 == 0:
            colour = blue
        block = Block(colour, block_x_pos, block_y_pos, BLOCK_WIDTH, BLOCK_DEPTH)
        block_sprites.add(block)

        i += 1
    return block_sprites