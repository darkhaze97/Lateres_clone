#This file will set up the class objects of the ball, rectangle and blocks
import pygame
import math

class Rectangle(pygame.sprite.Sprite):
    #Starting attributes of the rectangle.
    x = 220
    y = 352
    width = 64
    height = 4
    vel = 4
    #Constructing the rectangle sprite.
    def __init__(self, colour):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    def move_right(self, MAX_WIDTH, win, colour, rect_sprites):
        if self.rect.x < MAX_WIDTH - self.width:
            win.fill(colour, self.rect)
            self.rect.x += self.vel
            rect_sprites.draw(win)
            pygame.display.flip()
    def move_left(self, MAX_WIDTH, win, colour, rect_sprites):
        if self.rect.x > 0:
            win.fill(colour, self.rect)
            self.rect.x -= self.vel
            rect_sprites.draw(win)
            pygame.display.flip()
    def update_rect(self, win, colour, rect_sprites):
        win.fill(colour, self.rect)
        rect_sprites.draw(win)
        pygame.display.flip()

class Ball(pygame.sprite.Sprite):
    #Starting attributes of the ball.
    x = 252.0
    y = 100.0
    radius = 4
    velocity = 4.0
    direction = 270.0
    #The sprite of the ball will be black, so I can place a ball over it.
    def __init__(self, colour):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((2*self.radius, 2*self.radius))
        self.rect = self.image.get_rect()
        self.rect.x = self.x - self.radius
        self.rect.y = self.y - self.radius
        pygame.draw.circle(self.image, (0,255,0), (4,4), 4)
    def update_ball(self, win, ball_sprites):
        direction_radians = math.radians(self.direction)
        pygame.draw.circle(win, (0,0,0), (self.rect.x + self.radius, self.rect.y + self.radius), 4)
        self.rect.y = self.rect.y - self.velocity * math.sin(direction_radians)
        self.rect.x = self.rect.x + self.velocity * math.cos(direction_radians)
        pygame.draw.circle(self.image, (0,255,0), (4, 4), 4)
    def rebound_horizontal(self):
        #The % 360 deals with the negative degrees.
        self.direction = (self.direction - 180.0) % 360
    def rebound_rectangle(self, fraction):
        self.direction = 145.0 - (110.0 * fraction)
        if int(self.velocity * math.cos(math.radians(self.direction))) == 0 and fraction != 1/2:
            self.direction = 75.5
    def rebound_left_wall(self):
        if self.direction > 180 and self.direction < 270:
            self.direction = 360 - (self.direction - 180)
            if int(self.velocity * math.cos(math.radians(self.direction))) == 0:
                self.direction = 284.5
                print("Cool")
        elif self.direction > 90 and self.direction < 180:
            self.direction = 180 - self.direction
            if int(self.velocity * math.cos(math.radians(self.direction))) == 0:
                self.direction = 75.5
                print("Cool")
    def rebound_right_wall(self):
        if self.direction > 270 and self.direction < 360:
            self.direction = 180 + (360 - self.direction)
        elif self.direction > 0 and self.direction < 90:
            self.direction = 180 - self.direction
    def rebound_ceiling(self):
        if self.direction > 0 and self.direction < 90:
            self.direction = 360 - self.direction
        elif self.direction > 90 and self.direction < 180:
            self.direction = 180 + (180 - self.direction)
        elif self.direction == 90:
            self.rebound_horizontal()

class Block(pygame.sprite.Sprite):
    width = 0
    height = 0
    n_blocks = 30
    def __init__(self, colour, x_pos, y_pos, BLOCK_WIDTH, BLOCK_DEPTH):
        pygame.sprite.Sprite.__init__(self)
        self.width = BLOCK_WIDTH
        self.height = BLOCK_DEPTH
        self.image = pygame.Surface((self.width, self.height))
        self.image.fill(colour)
        self.rect = self.image.get_rect()
        self.rect.x = x_pos
        self.rect.y = y_pos
    def delete_blocks(self, win, colour, x_pos, y_pos):
        win.fill(colour, (x_pos, y_pos, self.width, self.height))

    