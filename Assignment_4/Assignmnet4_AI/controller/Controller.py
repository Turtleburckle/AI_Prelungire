from repository import *


class ControllerClass:
    def __init__(self):
        # args - list of parameters needed in order to create the controller
        pass

    def run(self, colony):
        colony.send_colony()
        return colony.get_best_path()