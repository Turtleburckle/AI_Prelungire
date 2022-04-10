from model import Individual
from queue import PriorityQueue


class PopulationClass:

    # args[0] - population size
    # args[1] - individual_size
    # args[2] - dMap
    # args[3] - start point
    # args[4] - battery level
    # args[5] - mutation probability
    # args[6] - crossover probability
    def __init__(self, args):
        self.__population_size = args[0]
        self.dMap = args[2]
        self.__population = [Individual.IndividualClass(args) for x in range(self.__population_size)]

    def evaluate(self):
        evaluated_population = []
        individuals = []
        index = 0
        for individual in self.__population:
            fitness = individual.fitness()
            evaluated_population.append((fitness, index))
            individuals.append(individual)
            index += 1
        evaluated_population.sort(reverse=True)
        return evaluated_population, individuals

    # perform a selection of k individuals from the population
    # and returns that selection
    def selection(self, k=3):
        evaluated_population, individuals = self.evaluate()
        selection_list = []
        for x in range(k):
            selection_list.append(individuals[evaluated_population[x][1]])
        return selection_list

    def set_new_population(self, new_population):
        self.__population.clear()
        for individual in new_population:
            self.__population.append(individual)
        evaluated_population, individuals = self.evaluate()
        self.__population.clear()
        for index in range(self.__population_size):
            new_individual = individuals[evaluated_population[index][1]]
            self.__population.append(new_individual)

    def get_the_fittest_individual(self):
        evaluated_population, individuals = self.evaluate()
        max_fit = 0
        new_individual = None
        for index in range(self.__population_size):
            if evaluated_population[index][0] > max_fit:
                new_individual = individuals[evaluated_population[index][1]]
        return new_individual

    def get_population(self):
        return self.__population

