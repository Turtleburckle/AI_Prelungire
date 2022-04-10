from matplotlib import pyplot
class UIClass:

    def __init__(self, repository, controller, gui, dMap):
        self.__repository = repository
        self.__controller = controller
        self.__gui = gui
        self.dMap = dMap
        self.__statistics_available = False
        self.statistics = 0
        self.individual = None

    def run(self):
        while True:
            self.map_print()
            self.ea_print()
            command = input(">>> ")
            if command == "1":
                self.run_map_options()
            elif command == "2":
                self.run_ea_options()
            else:
                quit()

    def set_status_statistics(self, status):
        self.__statistics_available = status

    def run_map_options(self):
        while True:
            self.map_print()
            command = input(">>> ")
            if command == "a":
                self.create_random_map()
            elif command == "b":
                self.load_map()
            elif command == "c":
                self.save_map()
            elif command == "d":
                self.visualise_map()
            elif command == "0":
                return
            else:
                quit()

    def create_random_map(self):
        self.dMap.random_map()

    def load_map(self):
        print("Please enter the name of the map you want to load")
        file_name = input(">>> ")
        self.dMap.load_map(file_name)

    def save_map(self):
        print("Please enter the name of the map you want to load")
        file_name = input(">>> ")
        self.dMap.save_map(file_name)

    def visualise_map(self):
        self.__gui.run(self.dMap)

    def map_print(self):
        print("1. MAP OPTIONS:")
        print("a. create a random map")
        print("b. load a map")
        print("c. save a map")
        print("d. visualise map")
        print("0. EXIT")

    def run_ea_options(self):
        while True:
            self.ea_print()
            command = input(">>> ")
            if command == "a":
                self.parameters_setup()
            elif command == "b":
                self.run_solver()
            elif command == "c":
                self.visualise_statistics()
            elif command == "d":
                self.view_drone_on_path()
            elif command == "0":
                return
            else:
                quit()

    def parameters_setup(self):
        while True:
            self.parameters_print()
            command = input(">>> ")
            if command == "a":
                print(self.__repository.get_battery_level_string())
                battery_level = int(input(">>> "))
                self.__repository.set_battery_level(battery_level)
            elif command == "b":
                print(self.__repository.get_iterations_string())
                iterations = int(input(">>> "))
                self.__repository.set_iterations(iterations)
            elif command == "c":
                print(self.__repository.get_population_size_string())
                population_size = int(input(">>> "))
                self.__repository.set_population_size(population_size)
            elif command == "d":
                print(self.__repository.get_individual_size_string())
                individual_size = int(input(">>> "))
                self.__repository.set_individual_size(individual_size)
            elif command == "e":
                print(self.__repository.get_mutation_probability_string())
                mutate_probability = float(input(">>> "))
                self.__repository.set_mutation_probability(mutate_probability)
            elif command == "f":
                print(self.__repository.get_crossover_probability_string())
                crossover_probability = float(input(">>> "))
                self.__repository.set_crossover_probability(crossover_probability)
            elif command == "0":
                return
            else:
                quit()

    def parameters_print(self):
        print("PARAMETERS SET-UP: ")
        print("a. Battery Level (by default: 10)")
        print("b. Iterations (by default: 10)")
        print("c. Population Size (by default: 6)")
        print("d. Individual Size (by default: 10)")
        print("e. Mutate Probability (by default: 0.04)")
        print("f. Crossover Probability (by default: 0.8)")
        print("0. EXIT")

    def run_solver(self):
        result, fittest_individual = self.__controller.solver()
        self.__statistics_available = True
        self.statistics = result
        self.individual = fittest_individual

    def visualise_statistics(self):
        if self.__statistics_available:
            print("The average fitness through all iterations:")
            string = ""
            average = self.__repository.get_average_fitness()
            x = []
            for index in range(len(average)):
                string += "Iteration " + str(index) + " : " + str(average[index]) + "\n"
                x.append(index+1)
            print(string)
            print("The standard deviation is : " + str(self.statistics) + "\n")
            pyplot.plot(x, average)
            pyplot.xlabel('Iteration')
            pyplot.ylabel('Average fitness')
            pyplot.title('EA fitness')
            pyplot.show()
        else: print("There is no run yet!")

    def view_drone_on_path(self):
        if self.__statistics_available:
            self.__gui.moving_drone(self.dMap, self.individual.get_path())
        else: print("No")

    def ea_print(self):
        print("2. EA OPTIONS:")
        print("a. parameters set-up")
        print("b. run the solver")
        print("c. visualise the statistics")
        print("d. view the drone moving on path")
        print("0. EXIT")
