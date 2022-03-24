import time
import pygame


class ControllerClass:

    def __init__(self, ui, drone, dMap):
        self.ui = ui
        self.drone = drone
        self.dMap = dMap

    def run(self):
        running = True
        path_Greedy = self.drone.searchGreedy(self.dMap)
        path_A_Star = self.drone.searchAStar(self.dMap)
        index = 0
        image_Greedy = self.dMap.image()
        image_A_Star = self.dMap.image()

        drone_Greedy = []
        drone_A_Star = []
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if len(path_Greedy) > index:
                    image_Greedy = self.ui.display_with_path(self.dMap.image(),path_Greedy[0:index])
                    drone_Greedy = path_Greedy[index]
                else:
                    drone_Greedy = path_Greedy[len(path_Greedy) - 1]
                if len(path_A_Star) > index:
                    image_A_Star = self.ui.display_with_path(self.dMap.image(), path_A_Star[0:index])
                    drone_A_Star = path_A_Star[index]
                else:
                    drone_A_Star = path_A_Star[len(path_A_Star) - 1]

                self.ui.blit_screen(image_A_Star,image_Greedy, drone_A_Star, drone_Greedy, self.drone.end_point)
                index += 1
                time.sleep(0.1)

    def run_bonus(self):
        running = True
        path_Bonus = self.drone.simulatedAnnealing(self.dMap)
        if len(path_Bonus) == 0 :
            print("NO")
            return
        index = 0
        image_Bonus = self.dMap.image()
        drone_Bonus = []

        while running:
            for event in pygame.event.get():
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    running = False
                if len(path_Bonus) > index:
                    image_Bonus = self.ui.display_with_path(self.dMap.image(), path_Bonus[0:index])
                    drone_Bonus = path_Bonus[index]
                else:
                    drone_Bonus = path_Bonus[len(path_Bonus) - 1]

                index += 1

                self.ui.blit_screen_bonus(image_Bonus, drone_Bonus, self.drone.end_point)

