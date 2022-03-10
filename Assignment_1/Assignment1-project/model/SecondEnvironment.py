import random
import pickle
import pygame
import numpy as np


class Environment:

    def __init__(self, colors, directions):
        self.__n = 20
        self.__m = 20
        self.__surface = np.zeros((self.__n, self.__m))
        self.colors = colors
        self.directions = directions

    def randomMap(self, fill=0.2):
        for i in range(self.__n):
            for j in range(self.__m):
                if random() <= fill:
                    self.__surface[i][j] = 1

    def existsWallThere(self, x, y):
        if self.__surface[x][y] == 1:
            return True
        else:
            return False

    def readUDMSensors(self, x, y):
        readings = [0, 0, 0, 0]
        # UP
        xf = x - 1
        while (xf >= 0) and (self.__surface[xf][y] == 0):
            xf -= 1
            readings[self.directions.get_up()] += 1
        # DOWN
        xf = x + 1
        while (xf < self.__n) and (self.__surface[xf][y] == 0):
            xf += 1
            readings[self.directions.get_down()] += 1
        # LEFT
        yf = y - 1
        while (yf >= 0) and (self.__surface[x][yf] == 0):
            yf -= 1
            readings[self.directions.get_left()] += 1
        # RIGHT
        yf = y + 1
        while (yf < self.__m) and (self.__surface[x][yf] == 0):
            yf += 1
            readings[self.directions.get_right()] += 1
        return readings

    def saveEnvironment(self, numFile):
        with open(numFile, 'wb') as f:
            pickle.dump(self, f)
            f.close()

    def loadEnvironment(self, numFile):
        with open(numFile, "rb") as f:
            dummy = pickle.load(f)
            self.__n = dummy.__n
            self.__m = dummy.__m
            self.__surface = dummy.__surface
            f.close()

    def image(self):
        imagine = pygame.Surface((420, 420))
        brick = pygame.Surface((20, 20))
        brick.fill(self.colors.get_blue_color())
        imagine.fill(self.colors.get_white_color())
        for i in range(self.__n):
            for j in range(self.__m):
                if self.__surface[i][j] == 1:
                    imagine.blit(brick, (j * 20, i * 20))
        return imagine

    def __str__(self):
        string = ""
        for i in range(self.__n):
            for j in range(self.__m):
                string = string + str(int(self.__surface[i][j]))
            string = string + "\n"
        return string
