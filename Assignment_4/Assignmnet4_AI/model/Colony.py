from model import Ant

class ColonyClass:
    # args[0] - pheromone_map,
    # args[1] - number_of_ants,
    # args[2] - start_point,
    # args[3] - number_of_sensors,
    # args[4] - max_steps.
    def __init__(self, args):
        self.pheromone_map = args[0]
        self.number_of_ants = args[1]
        self.start_point = args[2]
        self.colony = [Ant.AntClass(args) for x in range(self.number_of_ants)]

    def send_colony(self):
        previous_map = []
        for ant in self.colony:
            if len(previous_map) == 0:
                ant.generate_path()
            else:
                ant.set_pheromone_map(previous_map)
                ant.generate_path()
            previous_map = ant.get_pheromone_map()

    def evaluate_colony(self):
        evaluated_population = []
        ants = []
        index = 0
        for ant in self.colony:
            fitness = ant.evaluate()
            evaluated_population.append((fitness, index))
            ants.append(ant)
            index += 1
        evaluated_population.sort(reverse=False)
        return evaluated_population, ants

    def get_best_path(self):
        evaluated_population, ants = self.evaluate_colony()
        return ants[evaluated_population[0][1]].get_path()

