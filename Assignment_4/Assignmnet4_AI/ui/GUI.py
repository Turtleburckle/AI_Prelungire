import sys

import pygame
import time


class GUIClass:

    def __init__(self, dimensions, colors, dMap):
        self.__dimensions = dimensions
        self.colors = colors
        self.dMap = dMap

    def init_PyGame(self):
        # init the pygame
        pygame.init()
        logo = pygame.image.load("logo32x32.png")
        pygame.display.set_icon(logo)
        pygame.display.set_caption("drone exploration with AE")

        # create a surface on screen that has the size of 800 x 480
        screen = pygame.display.set_mode(self.__dimensions)
        screen.fill(self.colors.get_white())
        return screen

    def select_drone_position(self):
        screen = self.init_PyGame()
        screen.blit(self.image(self.dMap), (0, 0))
        drona = pygame.image.load("drona.png")
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    result = (round(pos[0] / 20), round(pos[1] / 20))
                    screen.blit(drona, (result[0] * 20, result[1] * 20))
                    pygame.display.flip()
                    time.sleep(1)
                    pygame.quit()
                    return result
                if event.type == pygame.QUIT:
                    pygame.quit()

    def select_sensors_position(self, sensors_number, drone_position):
        result = []
        screen = self.init_PyGame()
        screen.blit(self.image(self.dMap), (0, 0))
        drona = pygame.image.load("drona.png")
        sensor = pygame.image.load("sensor.png")
        screen.blit(drona, (drone_position[1] * 20, drone_position[0] * 20))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    position = (round(pos[0] / 20), round(pos[1] / 20))
                    screen.blit(sensor, (position[0] * 20, position[1] * 20))
                    pygame.display.flip()
                    result.append(position)
                    if len(result) == sensors_number:
                        time.sleep(1)
                        pygame.quit()
                        return result
                if event.type == pygame.QUIT:
                    pygame.quit()

    def close_PyGame(self):
        # closes the pygame
        running = True
        # loop for events
        while running:
            # event handling, gets all event from the event queue
            for event in pygame.event.get():
                # only do something if the event is of type QUIT
                if event.type == pygame.QUIT:
                    # change the value to False, to exit the main loop
                    running = False
        pygame.quit()

    def show_path(self, path, drone, sensors, current_map):
        screen = self.init_PyGame()

        drona = pygame.image.load("drona.png")
        screen.blit(drona, (drone[1] * 20, drone[0] * 20))
        sensor = pygame.image.load("sensor.png")
        for x in sensors:
            screen.blit(sensor, (x[1] * 20, x[0] * 20))

        pygame.display.flip()
        ray = []
        brick = pygame.Surface((20, 20))
        brick.fill(self.colors.get_green())
        charge = pygame.Surface((20, 20))
        charge.fill(self.colors.get_red())
        i = 0
        while i < len(path):
            screen.blit(self.image(current_map), (0, 0))

            for j in range(i+1):
                screen.blit(brick, (path[j][1] * 20, path[j][0] * 20))

            screen.blit(drona, (path[i][1] * 20, path[i][0] * 20))
            for x in sensors:
                if path[i][0] == x[0] and path[i][1] == x[1]:
                    found = False
                    if current_map.surface[path[i][0]-1][path[i][1]] != 1:
                        ray.append([path[i][0]-1, path[i][1]])
                        found = True
                    if current_map.surface[path[i][0]+1][path[i][1]] != 1:
                        ray.append([path[i][0]+1, path[i][1]])
                        found = True
                    if current_map.surface[path[i][0]][path[i][1]-1] != 1:
                        ray.append([path[i][0], path[i][1]-1])
                        found = True
                    if current_map.surface[path[i][0]][path[i][1]+1] != 1:
                        ray.append([path[i][0], path[i][1]+1])
                        found = True
                    if found:
                        i += 1
                screen.blit(sensor, (x[1] * 20, x[0] * 20))
            for spot in ray:
                screen.blit(charge, (spot[1] * 20, spot[0] * 20))
            pygame.display.flip()
            time.sleep(0.1)
            i += 1
        self.close_PyGame()

    def movingDrone(self, currentMap, path, speed=1, markSeen=True):
        # animation of a drone on a path

        screen = self.init_PyGame((currentMap.n * 20, currentMap.m * 20))

        drona = pygame.image.load("drona.png")

        for i in range(len(path)):
            screen.blit(self.image(currentMap), (0, 0))

            if markSeen:
                brick = pygame.Surface((20, 20))
                brick.fill(self.colors.get_green())
                for j in range(i + 1):
                    for var in []:
                        x = path[j][0]
                        y = path[j][1]
                        while ((0 <= x + var[0] < currentMap.n and
                                0 <= y + var[1] < currentMap.m) and
                               currentMap.surface[x + var[0]][y + var[1]] != 1):
                            x = x + var[0]
                            y = y + var[1]
                            screen.blit(brick, (y * 20, x * 20))

            screen.blit(drona, (path[i][1] * 20, path[i][0] * 20))
            pygame.display.flip()
            time.sleep(0.5 * speed)
        self.close_PyGame()

        for i in range(len(path)):
            screen.blit(self.image(currentMap), (0, 0))

            if markSeen:
                brick = pygame.Surface((20, 20))
                brick.fill(self.colors.get_green())
                for j in range(i + 1):
                    for var in []:
                        x = path[j][0]
                        y = path[j][1]
                        while ((0 <= x + var[0] < currentMap.n and
                                0 <= y + var[1] < currentMap.m) and
                               currentMap.surface[x + var[0]][y + var[1]] != 1):
                            x = x + var[0]
                            y = y + var[1]
                            screen.blit(brick, (y * 20, x * 20))

            screen.blit(drona, (path[i][1] * 20, path[i][0] * 20))
            pygame.display.flip()
            time.sleep(0.5 * speed)
        self.close_PyGame()

    def image(self, currentMap):
        # creates the image of a map

        imagine = pygame.Surface((currentMap.n * 20, currentMap.m * 20))
        brick = pygame.Surface((20, 20))
        brick.fill(self.colors.get_blue())
        imagine.fill(self.colors.get_white())
        for i in range(currentMap.n):
            for j in range(currentMap.m):
                if currentMap.surface[i][j] == 1:
                    imagine.blit(brick, (j * 20, i * 20))

        return imagine
