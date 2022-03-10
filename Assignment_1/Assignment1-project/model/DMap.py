import numpy as np
import pygame


class MapClass:

    def __init__(self, colors, directions):
        self.colors = colors
        self.directions = directions
        self.__n = 20
        self.__m = 20
        self.surface = np.zeros((self.__n, self.__m))
        self.initialize_surface()
        self.passed_blocks = []

    # initializes the surface with -1
    def initialize_surface(self):
        for i in range(self.__n):
            for j in range(self.__m):
                self.surface[i][j] = -1

    def markDetectedWalls(self, e, x, y):
        # TODO:: mark on this map the walls that you detect
        # walls - [up,left,down,right]
        self.passed_blocks.append((x, y))
        walls = e.readUDMSensors(x, y)

        # UP
        index = 1
        if walls[self.directions.get_up()] > 0:
            while index <= walls[self.directions.get_up()] and (x-index) > 0:
                self.surface[x-index][y] = 0
                index += 1
        if (x - index) >= 0 :
            self.surface[x-index][y] = 1

        # DOWN
        index = 1
        if walls[self.directions.get_down()] > 0:
            while index <= walls[self.directions.get_down()] and (x + index) < self.__n:
                self.surface[x+index][y] = 0
                index += 1
        if (x + index) < self.__n :
            self.surface[x+index][y] = 1

        # LEFT
        index = 1
        if walls[self.directions.get_left()] > 0:
            while index <= walls[self.directions.get_left()] and (y-index) > 0:
                self.surface[x][y-index] = 0
                index += 1
        if (y-index) >= 0:
            self.surface[x][y-index] = 1

        # RIGHT
        index = 1
        if walls[self.directions.get_right()] > 0:
            while index <= walls[self.directions.get_right()] and (y+index) < self.__m:
                self.surface[x][y+index] = 0
                index += 1
        if (y + index) < self.__m:
            self.surface[x][y+index] = 1

        return None

    def image(self, x, y):
        imagine = pygame.Surface((420, 420))
        brick = pygame.Surface((20, 20))
        empty = pygame.Surface((20, 20))
        passed = pygame.Surface((20, 20))
        empty.fill(self.colors.get_white_color())
        brick.fill(self.colors.get_black_color())
        passed.fill(self.colors.get_red_color())
        imagine.fill(self.colors.get_gray_blue_color())

        for i in range(self.__n):
            for j in range(self.__m):
                if self.surface[i][j] == 1:
                    imagine.blit(brick, (j * 20, i * 20))
                elif self.surface[i][j] == 0:
                    imagine.blit(empty, (j * 20, i * 20))
        for index in range(len(self.passed_blocks)):
            imagine.blit(passed, (self.passed_blocks[index][1] * 20, self.passed_blocks[index][0] * 20))
        drona = pygame.image.load("drona.png")
        imagine.blit(drona, (y * 20, x * 20))
        return imagine
