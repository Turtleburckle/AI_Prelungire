import numpy as np
import random
import pickle


class DMapClass:
    def __init__(self, size_map):
        self.n = size_map[0]
        self.m = size_map[1]
        self.surface = np.zeros((self.n, self.m))
        self.pheromone_map = np.zeros((self.n, self.m))

    def init_pheromone_map(self, drone, sensors):
        for i in range(self.n):
            for j in range(self.m):
                if self.surface[i][j] == 1:
                    self.pheromone_map[i][j] = -1

        self.pheromone_map[drone[1]][drone[0]] = -2
        for sensor in sensors:
            self.pheromone_map[sensor[1]][sensor[0]] = -3


    def random_map(self, fill=0.2):
        for i in range(self.n):
            for j in range(self.m):
                if random.randint(-2, 10) <= fill:
                    self.surface[i][j] = 1

    def save_map(self, numFile="test.map"):
        with open(numFile, 'wb') as f:
            pickle.dump(self, f)
            f.close()

    def load_map(self, numfile):
        with open(numfile, "rb") as f:
            dummy = pickle.load(f)
            self.n = dummy.n
            self.m = dummy.m
            self.surface = dummy.surface
            f.close()

    def hit_wall(self, point):
        if self.surface[point[0]][point[1]] == 1:
            return True
        return False

    def outside_table(self, point):
        if point[0] >= self.m or point[0] < 0:
            return True
        if point[1] >= self.n or point[1] < 0:
            return True
        return False

    def __str__(self):
        string = ""
        for i in range(self.n):
            for j in range(self.m):
                string = string + str(int(self.surface[i][j]))
            string = string + "\n"
        return string
