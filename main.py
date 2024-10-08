import pygame
import sys

from scripts.entities import PhysicsEntity
from scripts.utils import *
#Start PyGame
#Most Window Settings are Stored Here
class Game: 
    #Here all the PyGame Variables are Stored
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Your Game Name")
        self.screen = pygame.display.set_mode((640,480))
        #Display is an alternate name from the actual screen surface which serves to upscale the sprites to make them more visible, pygame.Surface serves to create an image you can render to.
        self.display = pygame.Surface((320,240))
        self.clock = pygame.time.Clock()
        self.img = pygame.image.load("data/images/clouds/cloud_1.png")
        self.movement = [False,False]
        
        self.assets = {
            "player": load_image("entities/player.png")
        }

        self.player = PhysicsEntity(self, "player", (50,50), (8,15))

    #This is where the GameLoop and Event Handling will Take place
    def run(self):
        running = True
        while running:
            #fill screen to prevent drawing
            self.display.fill((14, 219, 248))
            self.player.update((self.movement[1]-self.movement[0], 0))
            self.player.render(self.display)

            for event in pygame.event.get():
                # Handle the quit event
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                    sys.exit()
                # Handle key presses
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = True
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        self.movement[0] = False
                    if event.key == pygame.K_RIGHT:
                        self.movement[1] = False
                        
            self.screen.blit(pygame.transform.scale(self.display, self.screen.get_size()), (0,0))
            #Keep this at the end
            pygame.display.update()
            self.clock.tick(60)

Game().run()