from model import Colony

class RepositoryClass:
    # args[0] -dMap
    # args[1] - drone
    def __init__(self, args):
        self.dMap = args[0]
        self.drone = args[1]
        self.sensor_number = 3
        self.sensors = [(6, 11), (5, 5), (16, 4)]
        self.colony = self.initiate_colony()

    def initiate_colony(self):
        colony_args = [self.get_pheromone_map(), 100, self.drone.get_position(), self.sensor_number, self.drone.get_energy(), self.sensors]
        return Colony.ColonyClass(colony_args)

    def set_colony(self):
        self.colony = self.initiate_colony()

    def get_colony(self):
        return self.colony

    def set_drone_position(self, position):
        self.drone.set_position(position)

    def set_drone_energy(self, energy):
        self.drone.set_energy(energy)

    def set_sensors(self, sensor_list):
        self.sensors.clear()
        self.sensors = sensor_list

    def get_sensors(self):
        return self.sensors

    def hit_wall(self, point):
        return self.dMap.hit_wall(point)

    def get_map(self):
        return self.dMap

    def get_pheromone_map(self):
        return self.dMap.pheromone_map

    def get_drone_position(self):
        return self.drone.get_position()

    def load_map(self, file_name):
        if file_name == "" or file_name == '':
            self.dMap.load_map("test.map")
        else:
            self.dMap.load_map(file_name)
        self.initialize_pheromone_map()

    def random_map(self, file_name):
        self.dMap.random_map()
        if file_name == "" or file_name == '':
            self.dMap.save_map()
        else:
            self.dMap.save_map(file_name)
        self.initialize_pheromone_map()

    def initialize_pheromone_map(self):
        self.dMap.init_pheromone_map(self.drone.get_position(), self.sensors)
