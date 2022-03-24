import random

from model import Colors
from model import Directions

from model import Drone
from model import DMap

from controller import Controller
from ui import UI


def main(runs):
    colors = Colors.ColorClass()

    if runs:
        x = 17
        y = 6

        xf = 0
        yf = 0
    else:
        x = 19
        y = 19

        xf = 6
        yf = 9


    drone = Drone.DroneClass(x, y, colors)

    drone.initialize_points([x, y], [xf, yf])

    n = 20
    m = 20
    dMap = DMap.MapClass(n, m, colors)
    #dMap.randomMap()
    #dMap.saveMap()
    dMap.loadMap("test.map")

    if runs:
        size = (820, 450)
    else:
        size = (400, 450)

    ui = UI.UiClass(colors, size)

    controller = Controller.ControllerClass(ui, drone, dMap)
    if runs:
        controller.run()
    else:
        controller.run_bonus()


if __name__ == '__main__':
    run_type = True
    main(run_type)
