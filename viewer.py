# viewer.py
# (c) 2020 Karthik Karanth, MIT License
# https://karthikkaranth.me/blog/drawing-pixels-with-python/
# with modifications by me
import pygame


class Viewer:
    def __init__(self, update_func, display_size):
        self.update_func = update_func
        pygame.init()
        self.display = pygame.display.set_mode(display_size)

    def set_title(self, title):
        pygame.display.set_caption(title)

    def start(self):
        running = True
        while running:
            events = []
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                events.append(event)

            Z, overlay = self.update_func(events)
            surf = pygame.surfarray.make_surface(Z)
            overlay(surf)
            self.display.blit(surf, (0, 0))

            pygame.display.update()

        pygame.quit()