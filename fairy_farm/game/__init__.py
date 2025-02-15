"""Main game module for Fairy Farm."""

import sys

import pygame

from fairy_farm import settings
from fairy_farm.levels import Level


class Game:
    """Represents the main game loop and initialization."""

    def __init__(self) -> None:
        """Initialize the game window, clock, and level."""
        pygame.init()
        self.screen: pygame.Surface = pygame.display.set_mode(
            (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT),
        )
        pygame.display.set_caption("Fairy Farm")
        self.clock = pygame.time.Clock()
        self.level = Level()

    def run(self) -> None:
        """Start the game loop and handle events."""
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            dt: float = self.clock.tick(60) / 1000
            self.level.run(dt)
            pygame.display.flip()
