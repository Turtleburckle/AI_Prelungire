import statistics
from model import Population


class RepositoryClass:

    def __init__(self, dMap, start_point):
        self.dMap = dMap
        self.start_point = start_point
        self.battery_level = 10
        self.iterations = 10
        self.__population_size = 6
        self.__individual_size = 10
        self.__mutation_probability = 0.04
        self.__crossover_probability = 0.8
        self.__populations = []
        self.average = []

    def create_population(self):
        args = [self.__population_size, self.__individual_size, self.dMap, self.start_point, self.battery_level,
                self.__mutation_probability, self.__crossover_probability]
        return Population.PopulationClass(args)

    # Calculates the mean value (average) of the population's fitness & adds it to the list
    def add_to_statistics(self, population):
        population_fitness = []
        for individual in population:
            population_fitness.append(individual.fitness())
        self.average.append(statistics.mean(population_fitness))

    def get_fittest_individual(self, individuals):
        evaluated_population = []
        my_list = []
        index = 0
        for individual in individuals:
            fitness = individual.fitness()
            evaluated_population.append((fitness, index))
            print(individual)
            my_list.append(individual)
            index += 1
        evaluated_population.sort(reverse=True)
        print(evaluated_population[0])
        return my_list[evaluated_population[0][1]]

    def get_average_fitness(self):
        return self.average

    def set_battery_level(self, new_value):
        self.battery_level = new_value

    def get_battery_level(self):
        return self.battery_level

    def get_battery_level_string(self):
        return "Current Battery Level : " + str(self.battery_level)

    def set_population_size(self, new_value):
        self.__population_size = new_value

    def get_population_size(self):
        return self.__population_size

    def get_population_size_string(self):
        return "Current Population Size : " + str(self.__population_size)

    def set_iterations(self, new_value):
        self.iterations = new_value

    def get_iterations(self):
        return self.iterations

    def get_iterations_string(self):
        return "Current Number of Iterations : " + str(self.iterations)

    def set_individual_size(self, new_value):
        self.__individual_size = new_value

    def get_individual_size(self):
        return self.__individual_size

    def get_individual_size_string(self):
        return "Current Individual Size : " + str(self.__individual_size)

    def set_mutation_probability(self, new_value):
        self.__mutation_probability = new_value

    def get_mutation_probability(self):
        return self.__mutation_probability

    def get_mutation_probability_string(self):
        return "Current Mutation Probability : " + str(self.__mutation_probability)

    def set_crossover_probability(self, new_value):
        self.__crossover_probability = new_value

    def get_crossover_probability(self):
        return self.__crossover_probability

    def get_crossover_probability_string(self):
        return "Current Crossover Probability : " + str(self.__crossover_probability)
