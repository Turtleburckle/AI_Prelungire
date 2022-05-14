class UIClass:

    def __init__(self, gui, repository, controller):
        self.gui = gui
        self.repository = repository
        self.controller = controller

    def run(self):
        while True:
            self.main_menu_print()
            command = input(">>> ")
            if command == "1":
                self.set_drone_position()
            elif command == "2":
                self.set_energy_drone()
            elif command == "3":
                self.set_sensors_position()
            elif command == "4":
                self.set_map()
            elif command == "5":
                self.run_controller()
            else:
                exit()

    def set_drone_position(self):
        while True:
            result = self.gui.select_drone_position()
            print(result)
            if self.repository.hit_wall(result):
                print("The drone can't be placed there!")
            else:
                print("Do you want to set the drone there?")
                response = input(">>> ")
                if response == "y":
                    self.repository.set_drone_position(result)
                    return

    def set_energy_drone(self):
        while True:
            print("Please enter the energy of the drone: ")
            print("default : 20")
            energy_drone = input(">>> ")
            if energy_drone == "" or energy_drone == '':
                energy_drone = 20
            else:
                energy_drone = int(energy_drone)
            if energy_drone <= 0:
                print("The energy must be greater than 0!")
            else:
                self.repository.set_drone_energy(energy_drone)
                return

    def set_sensors_position(self):
        while True:
            print("Please enter the number of sensors you want to have: ")
            print("default: 3")
            sensor_number = input(">>> ")
            if sensor_number == "" or sensor_number == '':
                sensor_number = 3
            else:
                sensor_number = int(sensor_number)
            if sensor_number <= 0:
                print("The number of sensors must be greater than 0!")
            else:
                result = self.gui.select_sensors_position(sensor_number, self.repository.get_drone_position())
                self.repository.set_sensors(result)
                print(result)
                return

    def set_map(self):
        print("Please enter the files name: ")
        file_name = input(">>> ")
        self.repository.load_map(file_name)

    def run_controller(self):
        self.repository.set_colony()
        path = self.controller.run(self.repository.get_colony())
        self.gui.show_path(path, self.repository.get_drone_position(), self.repository.get_sensors(), self.repository.get_map())

    def main_menu_print(self):
        print("__ANT COLONY OPTIMIZATION MENU__")
        print("1. Set Drone Position")
        print("2. Set Energy for Drone")
        print("3. Set Sensors positions")
        print("4. Set Map")
        print("5. Run ACO")
        print("0. EXIT")
