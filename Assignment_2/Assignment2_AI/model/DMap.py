import random
import pickle
import pygame
import numpy as np


class MapClass:
    def __init__(self, n, m, colors):
        self.n = n
        self.m = m
        self.colors = colors
        self.surface = np.zeros((self.n, self.m))
        self.distances = self.initialize_distances()
        self.previous = self.initialize_previous()

    def initialize_previous(self):
        dictionary = {}
        for index1 in range(self.n):
            for index2 in range(self.m):
                dictionary[index1, index2] = []
        return dictionary

    def initialize_distances(self):
        matrix = np.zeros((self.n, self.m))
        for index1 in range(self.n):
            for index2 in range(self.m):
                if self.surface[index1][index2] == -1:
                    matrix[index1][index2] = -2
                else:
                    matrix[index1][index2] = -1
        return matrix

    def randomMap(self, fill=0.2):
        for i in range(self.n):
            for j in range(self.m):
                if random.randint(-2, 10) <= fill:
                    self.surface[i][j] = 1

    def __str__(self):
        string = ""
        for i in range(self.n):
            for j in range(self.m):
                string = string + str(int(self.surface[i][j]))
            string = string + "\n"
        return string

    def saveMap(self, numFile="test.map"):
        with open(numFile, 'wb') as f:
            pickle.dump(self, f)
            f.close()

    def loadMap(self, numfile):
        with open(numfile, "rb") as f:
            dummy = pickle.load(f)
            self.n = dummy.n
            self.m = dummy.m
            self.surface = dummy.surface
            f.close()

    def image(self):
        imagine = pygame.Surface((400, 400))
        brick = pygame.Surface((20, 20))
        brick.fill(self.colors.get_blue_color())
        imagine.fill(self.colors.get_white_color())
        for i in range(self.n):
            for j in range(self.m):
                if self.surface[i][j] == 1:
                    imagine.blit(brick, (j * 20, i * 20))
        return imagine
