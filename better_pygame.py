# Collect Blocks
# Author:
# Date:

import random

import pygame

# make the 2 pipes appear in level 5, let them stay
# in opposite corners
# when mario collieds with the pipe, he gets tranported to the other pipe
# (to escape mushrooms cornering)




# COLOURS - (R, G, B)
# CONSTANTS ALL HAVE CAPS FOR THEIR NAMES
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED   = (255,   0,   0)
GREEN = (  0, 255,   0)
BLUE  = (  0,   0, 255)
GREY  = (128, 128, 128)

# background
background_image = pygame.image.load("assets/mario background.jpg")
background_image = pygame.transform.scale(background_image, (1565, 730))

class Block(pygame.sprite.Sprite):
    def __init__(self):
        """A blue block"""
        super().__init__()

        self.image = pygame.image.load("assets/moneymoney.png")
        self.image = pygame.transform.scale_by(self.image, 0.1)

        # rect represents the hitbox of our sprite
        # the hitbox gives information about:
        #    - location of the sprite x, y
        #    - the size of the sprite width, height
        self.rect = self.image.get_rect()
        # change the location of our hitbox
        self.rect.centerx = 100
        self.rect.centery = 100


        self.point_value = 1

# in the bottomm of block class
    def level_up(self, val: int):
        """Incr point value"""
        self.point_value *= 1.5

class Mario(pygame.sprite.Sprite):
    def __init__(self):
        """Player sprite"""
        super().__init__()

        # Two copies of image: right-facing and left-facing
        self.image_right = pygame.image.load("assets/mario-snes.png")
        self.image_right = pygame.transform.scale_by(self.image_right, 0.5)
        self.image_left = pygame.transform.flip(self.image_right, True, False)
        self.image = self.image_right

        self.rect = self.image.get_rect()

        # Keep track of last x-coord
        self.last_x = 0

        # Mario's "Life"
        self.health = 100
        self.points = 0

    def decrease_health(self, mag: int) -> int:
        """Decrease player's health by magnitude.
        Returns:
            current health that Mario has after the change
        """
        self.health -= mag
        return self.health

    def increase_health(self, mag: int) -> int:
        """Increase the health of the player
        return current health after changhe"""
        self.health += mag
        return self.health


    def increase_score(self, amt: int):
        self.points += amt

    def show_health_percentage(self) -> int:
        return self.health / 100

    def update(self):
        """Have Mario follow the mouse.
        Set the "right" Mario image based on where he's facing."""
        self.rect.center = pygame.mouse.get_pos()

        # Mario faces right if and only if the previous x
        # is less than the current x
        if self.last_x < self.rect.x:
            self.image = self.image_right
        elif self.last_x > self.rect.x:
            self.image = self.image_left

        # Update the last_x
        self.last_x = self.rect.x

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        """Goomba"""
        super().__init__()

        self.image = pygame.image.load("assets/goomba-nes.png")
        self.rect = self.image.get_rect()
        # No initial location -> (0, 0)

        # Velocity of the Enemy
        self.vel_x = 0
        self.vel_y = 0

        self.damage = 1

    def level_up(self):
        # increase damage
        self.damage *= 2


    def update(self):
        # movement in the x- and y-axis
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        # TODO: randomize movement

class Mushroom(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/pixel_art.png")
        self.image = pygame.transform.scale_by(self.image, 2.5)
        self.rect = self.image.get_rect()

        # Velocity of mushroom
        self.vel_x = 0
        self.vel_y = 0
        self.heal = 10

    """a thing that restores marios health"""
    def increase_health():
        self.health += mag
        return self.health

    def update(self):
        # movement in the x- and y-axis
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

class HealthBar(pygame.Surface):
    def __init__(self):
        super().__init__((300, 10))
        self.fill(RED)

    def set_health(self, percentage: float):
        self.fill(RED)
        pygame.draw.rect(self, GREEN, (0, 0, (300 * percentage), 10))

class pipes(pygame.sprite.Sprite):
    def __init__(self):
        """A pipe"""
        super().__init__()
        self.image = pygame.image.load("assets/pipe.png")
        self.image = pygame.transform.scale_by(self.image, 0.3)


def spawn_mushrooms(num_mushrooms: int, scrn_height: int, all_sprites: pygame.sprite.Group, mush_sprites: pygame.sprite.Group):
    """Spawns mushrooms and adds to group"""
    for _ in range(num_mushrooms):
        mushroom = Mushroom()
        random_x = random.randrange(20, 100)
        random_y = random.randrange(scrn_height-100, scrn_height-20)
        mushroom.rect.center = random_x, random_y
        mushroom.vel_x = 1
        mushroom.vel_y = 1

        all_sprites.add(mushroom)
        mush_sprites.add(mushroom)

#def spawn_pipe(num_mushrooms: int, scrn_height: int, all_sprites: pygame.sprite.Group, pipe_sprites: pygame.sprite.Group):
    #for _ in range(2)
    #pipes = Pipes()
 #   x = 100
#    y = 500

def game():
    pygame.init()

    # CONSTANTS
    WIDTH = 800
    HEIGHT = 600
    SIZE = (WIDTH, HEIGHT)

    # Creating the Screen
    screen = pygame.display.set_mode(SIZE)
    pygame.display.set_caption("Collect Blocks")
    pygame.mouse.set_visible(False)

    # Variables
    done = False
    clock = pygame.time.Clock()
    num_enemies = 3
    num_blocks = 100
    healthbar = HealthBar()
    level = 1
    spawned_mushrooms = False
    num_mushrooms = 1
    points_rn = 0

    # Create a sprite group
    all_sprites_group = pygame.sprite.Group()
    block_sprites_group = pygame.sprite.Group()
    enemy_sprites_group = pygame.sprite.Group()
    mushroom_sprites_group = pygame.sprite.Group()

    # Create player sprite
    player = Mario()
    # Place Mario in the middle of the screen
    player.rect.centerx = WIDTH / 2
    player.rect.centery = HEIGHT / 2
    all_sprites_group.add(player)

    # Create Enemies
    for _ in range(num_enemies):
        enemy_one = Enemy()
        # Randomize position at bottom-left
        random_x = random.randrange(20, 100)
        random_y = random.randrange(HEIGHT-100, HEIGHT-20)
        enemy_one.rect.center = random_x, random_y
        # Randomize velocity
        enemy_one.vel_x = random.choice([ -1, 1, 2, 3, 4, 5])
        enemy_one.vel_y = random.choice([-1, 1, 2, 3, 4, 5])

        all_sprites_group.add(enemy_one)
        enemy_sprites_group.add(enemy_one)

    # Create a super mushroom
    spawn_mushrooms(num_mushrooms, HEIGHT, all_sprites_group, mushroom_sprites_group)

    # Create 100 blocks
    for _ in range(num_blocks):
        block = Block()
        # randomize their location
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
        healthbar.set_health(player.show_health_percentage())

        # If at level 3, start mushroom spawning every 2 levels
        if level > 2 and (level % 2 == 1) and not spawned_mushrooms:
            # Spawn num_mushrooms
            spawn_mushrooms(num_mushrooms, HEIGHT, all_sprites_group, mushroom_sprites_group)
            # increase the number by 1
            num_mushrooms += 1
            spawned_mushrooms = True
        if level % 2 == 0:
            spawned_mushrooms = False


        # Keep the enemies inside the screen
        for enemy in enemy_sprites_group:
            # x-axis and y-axis bounce
            if enemy.rect.left < 0 or enemy.rect.right > WIDTH:
                enemy.vel_x = -enemy.vel_x
            if enemy.rect.top < 0 or enemy.rect.bottom > HEIGHT:
                enemy.vel_y = -enemy.vel_y

        # keep in the mushroom
        for mushroom in mushroom_sprites_group:
            if mushroom.rect.left < 0 or mushroom.rect.right > WIDTH:
                mushroom.vel_x = -mushroom.vel_x
            if mushroom.rect.top < 0 or mushroom.rect.bottom > HEIGHT:
                mushroom.vel_y = -mushroom.vel_y

        # Check if Mario collides with a block
        blocks_collided = pygame.sprite.spritecollide(player, block_sprites_group, True)
        for block in blocks_collided:
            player.increase_score(block.point_value)

        # Check if mario collides with a mushroom
        mushroom_collided = pygame.sprite.spritecollide(player, mushroom_sprites_group, True)
        for mushroom in mushroom_collided:
            # increase marios health
            player.increase_health(mushroom.heal)

        # Check if Mario collides with enemies
        enemies_collided = pygame.sprite.spritecollide(player, enemy_sprites_group, False)
        for enemy in enemies_collided:
            # Decrease Mario's life by some number
            player.decrease_health(enemy.damage)


        points_rn+= 100
        # LEVEL UP if the player gets more than 100 points in level 1
        # Refill blocks
        # Increase enemy damage
        # Increase block point value
        if not block_sprites_group :
            level += 1

            for _ in range(num_blocks):
                block = Block()
                block.rect.center = random.randrange(0, WIDTH), random.randrange(0, HEIGHT)

                block.level_up(level)

                all_sprites_group.add(block)
                block_sprites_group.add(block)

            enemy = Enemy()
            enemy.vel_x, enemy.vel_y = random.choice([-5, -3, -1, 1, 3, 5]), random.choice([-5, -3, -1, 1, 3, 5])
            enemy.rect.center = (WIDTH/2, HEIGHT/2)
            all_sprites_group.add(enemy)
            enemy_sprites_group.add(enemy)


            for enemy in enemy_sprites_group:
                enemy.level_up()

        # End Game
        if player.health <= 0:
            done = True

        # ------ DRAWING TO SCREEN
        screen.blit(background_image, (0,0))

        # Draw all the sprites
        all_sprites_group.draw(screen)
        screen.blit(healthbar, (5, 5))

        # Update screen
        pygame.display.flip()

        # ------ CLOCK TICK
        clock.tick(60) # 60 fps


    # Display final score:
    print("Thanks for playing!")
    print("Final score is:", player.points)

    pygame.quit()

if __name__ == "__main__":
    game()
