from model import Population

import statistics


class ControllerClass:

    def __init__(self, repository):
        self.__repository = repository

    def iteration(self, population):
        new_population = []
        # Step 1: the selection of the parents.
        parents = population.selection()
        # Step 2: the creation of the offspring population (crossover of the parents)
        offspring_population = []
        for index_1 in range(len(parents)):
            for index_2 in range(index_1 + 1, len(parents)):
                offspring_1, offspring_2 = parents[index_1].crossover(parents[index_2])
                offspring_population.append(offspring_1)
                offspring_population.append(offspring_2)
        # Step 3: mutate the offspring generation
        for offspring in offspring_population:
            offspring.mutate()
            new_population.append(offspring)
        # Step 4: selection of the survivors
        for parent in parents:
            new_population.append(parent)
        population.set_new_population(new_population)
        best_individual = population.get_the_fittest_individual()
        return best_individual

    def run(self, number_of_iterations, population):
        fittest_individuals = []
        for x in range(number_of_iterations):
            # Step 1: perform iteration
            fittest_individual = self.iteration(population)
            # Step 2: save the information needed for the statistics
            self.__repository.add_to_statistics(population.get_population())
            fittest_individuals.append(fittest_individual)
        return self.__repository.get_average_fitness(), fittest_individuals

    def solver(self):
        # Step 1: Create a new Population with the specific info from the args.
        population = self.__repository.create_population()
        # Step 2: Calls the run function (runs the algorithm)
        average, fittest_individuals = self.run(self.__repository.get_iterations(), population)
        # Step 3: Returns the Statistics & Results from the Repository
        return statistics.stdev(average), self.__repository.get_fittest_individual(fittest_individuals)
