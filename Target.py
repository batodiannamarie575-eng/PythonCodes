
import os
import pygame
from pygame.locals import *
import random


# Target class
class Target:

    def __init__(self, window, window_width, window_height):
        self.window = window
        self.window_width = window_width
        self.window_height = window_height

        # Load the target image from the same folder as Target.py
        base_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(base_dir, "Target.png")

        self.image = pygame.image.load(image_path).convert_alpha()

        # Get the target image dimensions
        target_rect = self.image.get_rect()
        self.width = target_rect.width
        self.height = target_rect.height

        self.max_width = window_width - self.width
        self.max_height = window_height - self.height

        # Pick a random starting position
        self.x = random.randrange(self.max_width + 1)
        self.y = random.randrange(self.max_height + 1)

    def handle_event(self, event_obj):
        if event_obj.type == MOUSEBUTTONDOWN and event_obj.button == 1:

            target_rect = self.image.get_rect()
            target_rect.left = self.x
            target_rect.top = self.y

            mouse_x, mouse_y = pygame.mouse.get_pos()

            if target_rect.collidepoint(mouse_x, mouse_y):

                print("Target clicked!")

                # Move the target to a new random position
                self.x = random.randrange(self.max_width + 1)
                self.y = random.randrange(self.max_height + 1)

                return True

        return False

    def draw(self):
        self.window.blit(self.image, (self.x, self.y))
