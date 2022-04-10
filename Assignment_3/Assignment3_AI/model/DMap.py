import numpy as np
import random
import pickle


class DMapClass:

    def __init__(self, n=20, m=20):
        self.n = n
        self.m = m
        self.surface = np.zeros((self.n, self.m))

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
        if not self.outside_table(point):
            if self.surface[point[0]][point[1]] == 1:
                return True
            return False
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
