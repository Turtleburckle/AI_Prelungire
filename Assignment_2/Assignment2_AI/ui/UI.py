import pygame


class UiClass:

    def __init__(self, colors, size):
        self.colors = colors
        self.initiate_pygame()
        self.screen = self.initiate_screen(size)
        self.font = pygame.font.Font('freesansbold.ttf', 20)
        self.divider_horizontal = self.generate_divider_horizontal()
        self.divider_vertical = self.generate_divider_vertical()

    def initiate_pygame(self):
        pygame.init()
        logo = pygame.image.load("logo32x32.png")
        pygame.display.set_icon(logo)
        pygame.display.set_caption("Path in simple environment")

    def initiate_screen(self, size):
        myScreen = pygame.display.set_mode(size)
        myScreen.fill(self.colors.get_white_color())
        return myScreen

    def blit_screen(self, image_A_Star, image_Greedy, point_A_Star, point_Greedy,  end_point):
        # A * Algorithm SetUp
        text_AStar = self.font.render('A * Algorithm', True, self.colors.get_red_color())
        self.screen.blit(text_AStar, (130, 5))
        self.map_drone(image_A_Star,point_A_Star)
        self.map_finish(image_A_Star, end_point)
        self.screen.blit(image_A_Star, (0, 50))

        # Greedy Algorithm
        text_Greedy = self.font.render('Greedy Algorithm', True, self.colors.get_red_color())
        self.screen.blit(text_Greedy, (530, 5))
        self.map_drone(image_Greedy, point_Greedy)
        self.map_finish(image_Greedy, end_point)
        self.screen.blit(image_Greedy, (420, 50))
        self.set_dividers()
        self.display_screen()

    def blit_screen_bonus(self, image_Bonus, point_Bonus, end_point):
        # Bonus Algorithm
        text_bonus = self.font.render('Bonus Algorithm', True, self.colors.get_red_color())
        self.screen.blit(text_bonus, (130, 5))
        self.map_drone(image_Bonus, point_Bonus)
        self.map_finish(image_Bonus, end_point)
        self.screen.blit(image_Bonus, (0, 50))
        self.display_screen()

    def map_finish(self, mapImage, point):
        drona = pygame.image.load("crew.png")
        mapImage.blit(drona, (point[1] * 20, point[0] * 20))
        return mapImage

    def map_drone(self, mapImage, point):
        drona = pygame.image.load("car.png")
        mapImage.blit(drona, (point[1] * 20, point[0] * 20))
        return mapImage

    def set_dividers(self):
        self.screen.blit(self.divider_vertical, (0, 30))
        self.screen.blit(self.divider_horizontal, (400, 0))
        self.screen.blit(self.divider_vertical, (420, 30))
        self.screen.blit(self.divider_horizontal, (820, 0))

    def display_screen(self):
        pygame.display.flip()

    def generate_divider_horizontal(self):
        imagine = pygame.Surface((20, 450))
        imagine.fill(self.colors.get_black_color())
        return imagine

    def generate_divider_vertical(self):
        imagine = pygame.Surface((400, 20))
        imagine.fill(self.colors.get_black_color())
        return imagine

    def map_with_drone(self, map_image, point):
        drona = pygame.image.load("car.png")
        map_image.blit(drona, (point[1] * 20, point[0] * 20))
        return map_image

    def display_with_path(self, image, path):
        mark = pygame.Surface((20, 20))
        mark.fill(self.colors.get_green_color())
        for move in path:
            image.blit(mark, (move[1] * 20, move[0] * 20))
        return image

