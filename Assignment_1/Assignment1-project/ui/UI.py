import pygame
from pygame.constants import KEYDOWN


class UiClass:

    def __init__(self, colors, environment):
        self.colors = colors
        self.environment = environment
        self.initiate_pygame()
        self.screen = self.initiate_screen()

    def initiate_pygame(self):
        pygame.init()
        logo = pygame.image.load("logo32x32.png")
        pygame.display.set_icon(logo)
        pygame.display.set_caption("Drone Exploration")

    def initiate_screen(self):
        myScreen = pygame.display.set_mode((800, 400))
        myScreen.fill(self.colors.get_white_color())
        myScreen.blit(self.environment.image(), (0, 0))
        return myScreen

    def blit_screen(self, image):
        self.screen.blit(image, (400, 0))

    def display_screen(self):
        pygame.display.flip()

    def quit_game(self):
        pygame.quit()

    def event_quit(self):
        event = pygame.event.get()
        if event is not None:
            return event.type == pygame.QUIT
        return None

    def event_key_pressed(self):
        event = pygame.event.get()
        if event is not None:
            return event.type == KEYDOWN
        return None
