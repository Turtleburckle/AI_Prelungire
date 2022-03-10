import pygame
from pygame.locals import *


class DroneClass:

    def __init__(self, x, y, directions):
        self.x = x
        self.y = y
        self.directions = directions
        self.stack = [(self.x, self.y)]
        self.blocks_passed = []
        self.current_index = 0

    def move(self, detectedMap):
        pressed_keys = pygame.key.get_pressed()
        if self.x > 0:
            if pressed_keys[K_UP] and detectedMap.surface[self.x - 1][self.y] == 0:
                self.x = self.x - 1
        if self.x < 19:
            if pressed_keys[K_DOWN] and detectedMap.surface[self.x + 1][self.y] == 0:
                self.x = self.x + 1

        if self.y > 0:
            if pressed_keys[K_LEFT] and detectedMap.surface[self.x][self.y - 1] == 0:
                self.y = self.y - 1
        if self.y < 19:
            if pressed_keys[K_RIGHT] and detectedMap.surface[self.x][self.y + 1] == 0:
                self.y = self.y + 1

    def moveDSF(self, detectedMap, environment):
        # TODO:: rewrite this function in such a way that you perform an automatic & mapping with DFS
        dead_end = True
        # Step 1 : takes the last element added to the list (mimics a stack)
        if len(self.stack) != 0 :
            current_block = self.stack[0]
        else: return None
        #print(current_block)
        # Step 2 : adds the element to the passed blocks list
        self.blocks_passed.append(current_block)
        # Step 3 : reads the UDM Sensor for this element
        reading = environment.readUDMSensors(current_block[0], current_block[1])
        # Step 4 : Checks if the element it's in a dead end
        if reading[self.directions.get_up()] > 0:
            coordinates = (current_block[0] - 1, current_block[1])
            if not (coordinates in self.blocks_passed) and not (coordinates in self.stack):
                self.stack.insert(0, coordinates)
                dead_end = False
        if reading[self.directions.get_down()] > 0 and dead_end:
            coordinates = (current_block[0] + 1, current_block[1])
            if not (coordinates in self.blocks_passed) and not (coordinates in self.stack):
                self.stack.insert(0, coordinates)
                dead_end = False
        if reading[self.directions.get_left()] > 0 and dead_end:
            coordinates = (current_block[0], current_block[1] - 1)
            if not (coordinates in self.blocks_passed) and not (coordinates in self.stack):
                self.stack.insert(0, coordinates)
                dead_end = False
        if reading[self.directions.get_right()] > 0 and dead_end:
            coordinates = (current_block[0], current_block[1] + 1)
            if not (coordinates in self.blocks_passed) and not (coordinates in self.stack):
                self.stack.insert(0, coordinates)
                dead_end = False
        if dead_end:
            self.stack.pop(0)
        return current_block
