from model import Colors
from model import DMap
from model import Drone

from repository import Repository

from controller import Controller

from ui import UI
from ui import GUI



def main():
    colors = Colors.ColorsClass()

    dimensions = (400,400)
    dMap = DMap.DMapClass((20,20))

    drone = Drone.DroneClass()

    args_repo = [dMap, drone]

    repository = Repository.RepositoryClass(args_repo)

    controller = Controller.ControllerClass()

    gui = GUI.GUIClass(dimensions, colors, dMap)
    ui = UI.UIClass(gui, repository, controller)
    ui.run()


if __name__ == '__main__':
    main()
