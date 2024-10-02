import pygame

class PhysicsEntity:
    def __init__(self, game, e_type, pos, size):
        self.game = game
        self.type = e_type
        # It allows for an easier way to change entity position, tuples are not as easy to change as lists are.
        self.pos = list(pos)
        self.size = size
        # Rate of Change of the position
        self.velocity = [0,0]

    def update(self, movement=(0, 0)):
        frame_movement = (movement[0], + self.velocity[0], movement[1] + self.velocity[1])

        #Update the Movement into separate x and y axis
        self.pos[0] += frame_movement[0]
        self.pos[1] += frame_movement[1]
    
    def render(self, surf):
        surf.blit(self.game.assets["player"], self.pos)