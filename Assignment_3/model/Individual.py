import random

from model import Gene
from model import Directions


class IndividualClass:

    # args[0] - population size
    # args[1] - individual_size
    # args[2] - dMap
    # args[3] - start point
    # args[4] - battery level
    # args[5] - mutation probability
    # args[6] - crossover probability
    def __init__(self, args):
        self.__size = args[4]
        self.start_point = args[3]
        self.dMap = args[2]
        self.__individual = self.generate_individual()
        self.crossover_probability = args[6]
        self.mutation_probability = args[5]
        self.__fitness = self.fitness()
        self.args = args

    # Generates the Genes for an Individual
    def generate_individual(self):
        gene_list = []
        previous_gene = self.start_point
        for index in range(self.__size):
            gene_list.append(Gene.GeneClass(Directions.DirectionsClass(),previous_gene))
        return gene_list

    # The maximum Fitness "level" an Individual can have it's the Battery Level. Fitness Criteria:
    # - the point should not be outside the table
    # - the point should not be a wall
    # - the point should not repeat itself in the path
    def fitness(self):
        fitness_count = 0
        for gene in self.__individual:
            if not self.dMap.outside_table(gene.get_gene()):
                if not self.dMap.hit_wall(gene.get_gene()):
                    fitness_count += 1
                    if self.gene_count(gene) == 0:
                        fitness_count += 1
        return fitness_count

    def gene_count(self, gene):
        count = -1
        for other_gene in self.__individual:
            if gene.equals(other_gene.get_gene()): count += 1
        return count

    def mutate(self, mutate_probability=0.04):
        previous_gene = self.start_point
        for gene in self.__individual:
            current_gene = gene.get_gene()
            if random.randint(-1, 10) < mutate_probability:
                current_gene = gene.random_gene(previous_gene)
                gene.set_gene(current_gene)
            previous_gene = current_gene

    def crossover(self, otherParent):
        offspring1 = IndividualClass(self.args)
        offspring2 = IndividualClass(self.args)
        for index in range(self.__size):
            if random.randint(-1, 10) < self.crossover_probability:
                offspring1.__individual[index] = self.__individual[index]
                offspring2.__individual[index] = otherParent.__individual[index]
        return offspring1, offspring2

    def get_path(self):
        path = []
        for gene in self.__individual:
            path.append(gene.get_gene())
        return path

    def __str__(self):
        string = ""
        for gene in self.__individual:
            string += str(gene.get_gene()) + " "
        return string + "--> " + str(self.fitness())
