import random
import math
import time
from queue import PriorityQueue


class DroneClass:
    def __init__(self, x, y, colors):
        self.start_point = [0, 0]
        self.end_point = [0, 0]
        self.x = x
        self.y = y
        self.colors = colors

    def initialize_points(self, start_point, end_point):
        self.start_point[0] = start_point[0]
        self.start_point[1] = start_point[1]
        self.end_point[0] = end_point[0]
        self.end_point[1] = end_point[1]

    # Manhattan Distance
    # A (Xa, Ya) & B (Xb, Yb) --> h(A,B) = | Xa - Xb | + | Ya - Yb |
    def h_function(self, point):
        return abs(point[0] - self.end_point[0]) + abs(point[1] - self.end_point[1])

    def h_function_2(self, point):
        return math.sqrt(abs(point[0] - self.end_point[0]) ** 2 + abs(point[1] - self.end_point[1]) ** 2)

    def f_function(self, g, h):
        return g + h

    def get_neighbours(self, point, map_surface):
        neighbours_list = []
        x = point[0]
        y = point[1]
        if x + 1 <= 19:
            if map_surface[x + 1][y] != 1:
                neighbours_list.append([x + 1, y])
        if x - 1 >= 0:
            if map_surface[x - 1][y] != 1:
                neighbours_list.append([x - 1, y])
        if y + 1 <= 19:
            if map_surface[x][y + 1] != 1:
                neighbours_list.append([x, y + 1])
        if y - 1 >= 0:
            if map_surface[x][y - 1] != 1:
                neighbours_list.append([x, y - 1])
        return neighbours_list

    def construct_path(self, previous_list):
        path = []
        current_point = self.end_point
        path.append(current_point)
        while current_point != self.start_point:
            new_point = previous_list[current_point[0], current_point[1]]
            current_point = new_point
            path.insert(0, current_point)
        return path

    def searchAStar(self, dMap):
        start = time.perf_counter()
        open_list = PriorityQueue()
        close_list = []
        neighbour_list = []
        checked = []
        distances = dMap.distances
        previous_nodes = dMap.previous
        previous_value = dMap.distances

        open_list.put((self.h_function(self.start_point), self.start_point))
        distances[self.start_point[0]][self.start_point[1]] = 0
        previous_nodes[self.start_point[0],self.start_point[1]] = None
        previous_value[self.start_point[0]][self.start_point[1]] = self.h_function(self.start_point)

        path_found = False

        while not path_found and not open_list.empty():
            open_entry = open_list.get()

            current_node = open_entry[1]

            neighbour_list.clear()
            neighbour_list = self.get_neighbours(current_node, dMap.surface)

            for neighbour in neighbour_list:
                if not(neighbour[0] == self.start_point[0] and neighbour[1] == self.start_point[1]):
                    if neighbour not in checked:
                        distances[neighbour[0]][neighbour[1]] = distances[current_node[0]][current_node[1]]
                        previous_nodes[neighbour[0],neighbour[1]] = current_node
                        f_value = self.f_function(distances[neighbour[0]][neighbour[1]], self.h_function(neighbour))
                        previous_value[neighbour[0]][neighbour[1]] = f_value
                        open_list.put((f_value, neighbour))
                        checked.append(neighbour)
                        if neighbour[0] == self.end_point[0] and neighbour[1] == self.end_point[1]:
                            path_found = True
                    else:
                        current_distance = distances[current_node[0]][current_node[1]] + 1
                        old_value = previous_value[neighbour[0]][neighbour[1]]
                        current_value = self.f_function(distances[neighbour[0]][neighbour[1]], self.h_function(neighbour))
                        if old_value > current_value:
                            distances[neighbour[0]][neighbour[1]] = current_distance
                            previous_nodes[neighbour[0], neighbour[1]] = current_node
            close_list.append(current_node)
        end = time.perf_counter()
        print("Time A Star : " + str(end - start))
        if path_found :
            return self.construct_path(previous_nodes)
        return []

    def searchGreedy(self, dMap):
        #dMap.initialize_distances()
        start = time.perf_counter()
        path = []
        visited = dMap.distances
        pq = PriorityQueue()

        pq.put((0, self.start_point))

        while not pq.empty():
            current_node = pq.get()[1]
            path.append(current_node)
            if current_node[0] == self.end_point[0] and current_node[1] == self.end_point[1]:
                end = time.perf_counter()
                print("Time Greedy : " + str(end - start))
                return path
            neighbours = self.get_neighbours(current_node, dMap.surface)
            for neighbour in neighbours:
                if visited[neighbour[0]][neighbour[1]] == -1:
                    visited[neighbour[0]][neighbour[1]] = 1
                    priority = self.h_function(neighbour)
                    pq.put((priority, neighbour))

        end = time.perf_counter()
        print("Time Greedy : " + str(end - start))
        return []

    def simulatedAnnealing(self, dMap):
        current_node = self.start_point
        checked = dMap.surface
        path = []
        neighbours_list = []
        path_found = False
        while not path_found:
            neighbours_list.clear()
            neighbours_list = self.get_neighbours(current_node,dMap.surface)
            if len(neighbours_list) == 0:
                return []
            random_index = random.randint(0, len(neighbours_list)-1)
            random_neighbour = neighbours_list[random_index]
            if random_neighbour[0] == self.end_point[0] and random_neighbour[1] == self.end_point[1]:
                path.append(random_neighbour)
                path_found = True
            current_node_h = self.h_function(current_node)
            random_node_h = self.h_function(random_neighbour)
            if current_node_h > random_node_h or checked[current_node[0]][current_node[1]] > 10:
                path.append(current_node)
                current_node = random_neighbour
                checked[random_neighbour[0]][random_neighbour[1]] += 1
            else :
                checked[current_node[0]][current_node[1]] += 1
        return path



    def dummysearch(self, ):
        # example of some path in test1.map from [5,7] to [7,11]
        return [[5, 7], [5, 8], [5, 9], [5, 10], [5, 11], [6, 11], [7, 11]]


