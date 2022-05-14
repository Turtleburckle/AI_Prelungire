import random


class AntClass:

    def __init__(self, args, probability=0.8):
        self.probability = probability
        self.path = []
        self.pheromone_map = args[0]
        self.start_point = args[2]
        self.number_of_sensors = args[3]
        self.max_steps = args[4]
        self.sensors = args[5]

    def generate_path(self):
        current_point = self.start_point
        steps = 0
        while steps != self.max_steps:
            # UP
            point_up = [current_point[0] - 1, current_point[1]]
            # DOWN
            point_down = [current_point[0] + 1, current_point[1]]
            # LEFT
            point_left = [current_point[0], current_point[1] - 1]
            # RIGHT
            point_right = [current_point[0], current_point[1] + 1]
            if random.random() < self.probability:
                result = self.get_best_choice(point_up, point_down, point_left, point_right)
            else:
                result = self.check(point_up, point_down, point_left, point_right)
            self.pheromone_map[result[0]][result[1]] += 1
            self.path.append(result)
            steps += 1
            current_point = result

    def check(self, up, down, left, right):
        if self.is_not_outside_map(up):
            if self.is_not_wall(up):
                return up
        if self.is_not_outside_map(down):
            if self.is_not_wall(down):
                return down
        if self.is_not_outside_map(left):
            if self.is_not_wall(left):
                return left
        if self.is_not_outside_map(right):
            if self.is_not_wall(right):
                return right

    def get_best_choice(self, up, down, left, right):
        best_choice = []
        # UP
        grade = self.get_grade(up)
        if grade > 0:
            if self.is_pheromoned(up):
                grade += self.pheromone_map[up[0]][up[1]]
            if up not in self.path:
                grade += 10
            best_choice = [up, grade]
        # DOWN
        grade = self.get_grade(down)
        if grade > 0:
            if self.is_pheromoned(down):
                grade += self.pheromone_map[down[0]][down[1]]
            if down not in self.path:
                grade += 10
            if len(best_choice) != 0:
                if best_choice[1] < grade:
                    best_choice.clear()
                    best_choice = [down, grade]
            else:
                best_choice = [down, grade]
        # LEFT
        grade = self.get_grade(left)
        if grade > 0:
            if self.is_pheromoned(left):
                grade += self.pheromone_map[left[0]][left[1]]
            if left not in self.path:
                grade += 10
            if len(best_choice) != 0:
                if best_choice[1] < grade:
                    best_choice.clear()
                    best_choice = [left, grade]
            else:
                best_choice = [left, grade]
        # RIGHT
        grade = self.get_grade(right)
        if grade > 0:
            if self.is_pheromoned(right):
                grade += self.pheromone_map[right[0]][right[1]]
            if right not in self.path:
                grade += 10
            if len(best_choice) != 0:
                if best_choice[1] < grade:
                    best_choice.clear()
                    best_choice = [right, grade]
            else:
                best_choice = [right, grade]
        return best_choice[0]

    def get_grade(self, current_point):
        grade = 0
        if self.is_not_outside_map(current_point):
            grade += 1
            if self.is_not_start_point(current_point):
                grade += 1
                if self.is_not_wall(current_point):
                    grade += 1
                    if self.is_sensor(current_point):
                        grade += 10
        return grade

    def evaluate(self):
        grade = 0
        for step in self.path:
            if self.is_sensor(step):
                grade += 1
            for sensor in self.sensors:
                grade += self.h_function(step, sensor)
        return grade

    def h_function(self, point, sensor):
        return abs(point[0] - sensor[1]) + abs(point[1] - sensor[0])

    def is_pheromoned(self, current_point):
        if self.pheromone_map[current_point[0]][current_point[1]] > 0:
            return True
        return False

    def is_sensor(self, current_point):
        if self.pheromone_map[current_point[0]][current_point[1]] == -3:
            return True
        return False

    def is_not_outside_map(self, current_point):
        if current_point[0] > 19:
            return False
        if current_point[1] > 19:
            return False
        if current_point[0] < 0:
            return False
        if current_point[1] < 0:
            return False
        return True

    def is_not_wall(self, current_point):
        if self.pheromone_map[current_point[0]][current_point[1]] != -1:
            return True
        return False

    def is_not_start_point(self, current_point):
        if self.pheromone_map[current_point[0]][current_point[1]] != -2:
            return True
        return False

    def get_path(self):
        return self.path

    def set_pheromone_map(self, new_map):
        self.pheromone_map = new_map

    def get_pheromone_map(self):
        return self.pheromone_map

    def __str__(self):
        result = "[ "
        for x in self.path:
            result += str(x) + " "
        return result + " ] - " + str(self.evaluate())
