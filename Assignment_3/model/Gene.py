import random


class GeneClass:

    def __init__(self, directions, previous_step):
        self.directions = directions
        self.gene = self.random_gene(previous_step)

    def get_gene(self):
        return self.gene

    def random_gene(self, previous_step):
        current_point = previous_step
        direction = random.randint(1, 4)
        if direction == self.directions.get_up():
            current_point = [current_point[0] - 1, current_point[1]]
        if direction == self.directions.get_down():
            current_point = [current_point[0] + 1, current_point[1]]
        if direction == self.directions.get_right():
            current_point = [current_point[0], current_point[1] + 1]
        if direction == self.directions.get_left():
            current_point = [current_point[0], current_point[1] - 1]
        return current_point

    def set_gene(self, gene):
        self.gene = gene

    def equals(self, other):
        if self.gene[0] == other[0] and self.gene[1] == other[1]:
            return True
        return False
