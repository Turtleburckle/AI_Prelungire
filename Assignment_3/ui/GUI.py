import pygame
import time


class GUIClass:

    def __init__(self, dimension, colors):
        self.colors = colors
        self.dimension = dimension
        self.__screen = None
        self.v = [[-1, 0], [1, 0], [0, 1], [0, -1]]

    def run(self, dMap):
        self.init_pygame()
        self.blit_screen(dMap)
        self.close_pygame()

    def init_pygame(self):
        pygame.init()
        logo = pygame.image.load("logo32x32.png")
        pygame.display.set_icon(logo)
        pygame.display.set_caption("drone exploration with AE")
        self.__screen = self.set_screen(self.dimension)

    def set_screen(self, dimension):
        screen = pygame.display.set_mode(dimension)
        screen.fill(self.colors.get_white_color())
        return screen

    def blit_screen(self, current_map):
        current_map_image = self.image(current_map)
        self.__screen.blit(current_map_image,(0,0))
        pygame.display.flip()

    def close_pygame(self):
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

    def moving_drone(self, current_map, path, speed=1, mark_seen=True):
        # Animation of a drone on a path
        screen = self.set_screen(self.dimension)
        drona = pygame.image.load("drona.png")

        for i in range(len(path)):
            screen.blit(self.image(current_map), (0, 0))

            if mark_seen:
                brick = pygame.Surface((20, 20))
                brick.fill(self.colors.get_green_color())
                for j in range(i + 1):
                    for var in self.v:
                        x = path[j][0]
                        y = path[j][1]
                        while ((0 <= x + var[0] < current_map.n and
                                0 <= y + var[1] < current_map.m) and
                               current_map.surface[x + var[0]][y + var[1]] != 1):
                            x = x + var[0]
                            y = y + var[1]
                            screen.blit(brick, (y * 20, x * 20))

            screen.blit(drona, (path[i][1] * 20, path[i][0] * 20))
            pygame.display.flip()
            time.sleep(0.5 * speed)
        self.close_pygame()

    def display_with_path(self, image, path):
        mark = pygame.Surface((20, 20))
        mark.fill(self.colors.get_green_color())
        for move in path:
            image.blit(mark, (move[1] * 20, move[0] * 20))
        return image

    def map_with_drone(self, map_image, point):
        drona = pygame.image.load("car.png")
        map_image.blit(drona, (point[1] * 20, point[0] * 20))
        return map_image

    def image(self, current_map):
        # creates the image of a map
        imagine = pygame.Surface((current_map.n * 20, current_map.m * 20))
        brick = pygame.Surface((20, 20))
        brick.fill(self.colors.get_blue_color())
        imagine.fill(self.colors.get_white_color())
        for i in range(current_map.n):
            for j in range(current_map.m):
                if current_map.surface[i][j] == 1:
                    imagine.blit(brick, (j * 20, i * 20))
        return imagine
