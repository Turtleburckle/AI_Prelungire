import random

import ui.UI
from model import Colors
from model import Directions
from model import DMap

from controller import Controller

from repository import Repository

from ui import UI
from ui import GUI
from matplotlib import pyplot


def main():
    x = random.randint(0, 19)
    y = random.randint(0, 19)

    start_point = [x, y]

    colors = Colors.ColorsClass()

    directions = Directions.DirectionsClass()

    dMap = DMap.DMapClass()

    repository = Repository.RepositoryClass(dMap, start_point)

    controller = Controller.ControllerClass(repository)

    dimension = (400, 400)
    gui = GUI.GUIClass(dimension, colors)

    ui = UI.UIClass(repository, controller, gui, dMap)

    ui.run()


if __name__ == '__main__':
    main()
