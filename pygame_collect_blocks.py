# Your Title Here
# Author: Rachel Y
# Date: Jan 7, 2026

import random

import pygame

# COLOURS - (R, G, B)
# CONSTANTS ALL HAVE CAPS FOR THEIR NAMES
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
GREY = (128, 128, 128)


class Block(pygame.sprite.Sprite):
    def __init__(self):
        """A blue block"""
        super().__init__()

        self.image = pygame.Surface((30, 20))
        # change the colour of our image to blue
        self.image.fill(BLUE)

        # rect reresents the hitbox of our sprite
        # the hitox give infrmation about:
        # - location of the sprite
        # - the size of the sprt width, height
        self.rect = self.image.get_rect()
        # change the location of our hitbox
        self.rect.centerx = 100
        self.rect.centery = 100

        # (x, y width height)


class Mario(pygame.sprite.Sprite):

    def __init__(self):
        """Player sprite"""
        super().__init__()
        self.image_right = pygame.image.load("assets/mario-snes.png")
        self.image_right = pygame.transform.scale_by(self.image_right, 0.5)
        self.image_left = pygame.transform.flip(self.image_right, True, False)
        self.image = self.image_right
        # scale image down to one-half
        self.rect = self.image.get_rect()

        # keep track of x coordinate
        self.last_x = 0
        self.mario_facing = "right"
        # mario facing direction


    def update(self):
        """Have Mario follow the mouse"""
        self.rect.center = pygame.mouse.get_pos()

        if self.last_x > self.rect.x:
            self.image = self.image_right
        else:
            self.image = self.image_left

        # Update the last x
        self.last_x = self.rect.x

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("assets/goomba-nes.png")
        self.rect = self.image.get_rect()

        # No initial location -> (0, 0)
        self.vel_x = 0
        self.vel_y = 0

    def update(self):
        #movement in x axis
        self.rect.x += self.vel_x
        #  movement in y axis
        self.rect.y += self.vel_y


def game():
    pygame.init()

    # CONSTANTS
    WIDTH = 800
    HEIGHT = 600
    SIZE = (WIDTH, HEIGHT)

    # Creating the Screen
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Mushroom world")

    # Variables
    done = False
    clock = pygame.time.Clock()

    # Create a sprite group
    all_sprites_group = pygame.sprite.Group()
    block_sprites_group = pygame.sprite.Group()
    enemy_sprites_group = pygame.sprite.Group()

    # Create player sprite
    player = Mario()

    # place mario in the middle of the screen
    player.rect.centerx = WIDTH / 2
    player.rect.centery = HEIGHT / 2
    all_sprites_group.add(player)

    # TODO: check colision with enemies


    # Create 3 enemies
    for _ in range(3):
        enemy_one = Enemy()
        random_x = random.randrange(20, 100)
        random_y = random.randrange(HEIGHT - 120, HEIGHT - 20)

        enemy_one.rect.centerx = random_x
        enemy_one.rect.centery = random_y
        #Randomize velocity
        enemy_one.vel_x = random.choice([-3, -2, -1, 1, 2, 3])
        enemy_one.vel_y = random.choice([-3, -2, -1, 1, 2, 3])

        all_sprites_group.add(enemy_one)
        enemy_sprites_group.add(enemy_one)




    # Create 100 blocks
    for _ in range(100):
        block = Block()
        # randomize their locations
        block.rect.centerx = random.randrange(0, WIDTH)
        block.rect.centery = random.randrange(0, HEIGHT)
        # add them to the sprite group
        all_sprites_group.add(block)
        block_sprites_group.add(block)

    # ------------ MAIN GAME LOOP
    while not done:
        # ------ MAIN EVENT LISTENER
        # when the user does something
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ------ GAME LOGIC
        all_sprites_group.update()

        # Keep the enemies inside the screen
        # X axis bounce
        for enemy in enemy_sprites_group:
            if enemy.rect.left< 0 or enemy.rect.right >WIDTH:
                enemy.vel_x = -enemy.vel_x

        for enemy in enemy_sprites_group:
            if enemy.rect.top< 0 or enemy.rect.bottom >HEIGHT:
                enemy.vel_y = -enemy.vel_y



        # TODO: Check if Mario collides with a block
        enemies_collide = pygame.sprite.spritecollide(player, enemy_sprites_group, False)
        # If mario collides wiht a block, print out
        # MARIO HAS COLLIDED WITH A BLOCK
        blocks_collided = pygame.sprite.spritecollide(player, block_sprites_group, True)
        if blocks_collided:
            print("---")
            print("KABOOM! Mario collided with a block")
            print(blocks_collided)

        # ------ DRAWING TO SCREEN
        screen.fill(WHITE)
        # Draw all the sprites
        all_sprites_group.draw(screen)

        # Update screen
        pygame.display.flip()

        # ------ CLOCK TICK
        clock.tick(60)  # 60 fps

    pygame.quit()


if __name__ == "__main__":
    game()
