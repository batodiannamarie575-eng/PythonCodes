import pygame
from Target import Target

class TargetManager():

    def __init__(self, window, window_width, window_height, n_target):
        self.targets = []

        for target_number in range(n_target):
            target = Target(window, window_width, window_height)
            self.targets.append(target)

    def handle_event(self, event_obj):
        clicked = False

        for target in self.targets:
            if target.handle_event(event_obj):
                clicked = True

        return clicked

    def draw_all(self):
        for target in self.targets:
            target.draw()