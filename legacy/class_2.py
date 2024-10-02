import pygame
import sys

#Start PyGame
#Most Window Settings are Stored Here
class Game: 
    #Here all the PyGame Variables are Stored
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Your Game Name")
        self.screen = pygame.display.set_mode((640,480))
        self.clock = pygame.time.Clock()
        self.img = pygame.image.load("data/images/clouds/cloud_1.png")
        self.img_pos = [160, 260]
        self.movement = [False,False]
        #Replace Pure Black with Transparent
        self.img.set_colorkey((0,0,0))
        #Collision Area
        self.collision_area = pygame.Rect(50, 50, 300, 50)
    #This is where the GameLoop and Event Handling will Take place
    def run(self):
        running = True
        while running:
            #fill screen to prevent drawing
            self.screen.fill((14, 219, 248))


            #Create a rectangle which is the same size as the image (player in this case)
            img_r = pygame.Rect(self.img_pos[0], self.img_pos[1], self.img.get_width(), self.img.get_height())
            #Actual Collision testing
            if img_r.colliderect(self.collision_area):
                pygame.draw.rect(self.screen, (0,100,255), self.collision_area)
            else:
                pygame.draw.rect(self.screen, (0,100,15), self.collision_area)
           
            self.img_pos[1] += (self.movement[1] - self.movement[0])*5
            self.screen.blit(self.img, self.img_pos)
            
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
                    if event.key == pygame.K_UP:
                        self.movement[0] = True
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_UP:
                        self.movement[0] = False
                    if event.key == pygame.K_DOWN:
                        self.movement[1] = False
                        
            #Keep this at the end
            pygame.display.update()
            self.clock.tick(60)

Game().run()