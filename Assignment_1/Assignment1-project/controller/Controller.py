import time

class ControllerClass:
    def __init__(self, ui, drone, myMap, environment):
        self.ui = ui
        self.drone = drone
        self.myMap = myMap
        self.environment = environment

    def run(self):
        running = True
        while running:
            #if self.ui.event_quit() is True:
               #running = False
            # TODO: call the moveDFS(map) from drone class
            current_step = self.drone.moveDSF(self.myMap, self.environment)
            #self.drone.move(self.myMap)
            if current_step is not None:
                self.myMap.markDetectedWalls(self.environment, current_step[0], current_step[1])
                self.ui.blit_screen(self.myMap.image(current_step[0], current_step[1]))
            else:
                running = False
            self.ui.display_screen()
            time.sleep(0.1)
        time.sleep(1000)
       # self.ui.quit_game()

