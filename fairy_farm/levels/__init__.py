"""Manage game entities and rendering."""

import pygame

from fairy_farm.entities.sprites.player import Player
from fairy_farm.entities.sprites.world import World
from fairy_farm.levels.camera_group import CameraGroup
from fairy_farm.ui.overlays import Overlay


class Level:
    """Manage game entities, rendering, and updates."""

    def __init__(self) -> None:
        """Initialize the level with world, player, and overlay."""
        self.display_surface: pygame.Surface = pygame.display.get_surface()
        self.all_sprites: CameraGroup = CameraGroup()

        self.__setup()

    def __setup(self) -> None:
        World(self.all_sprites)

        self.player = Player((640, 360), self.all_sprites)
        self.overlay = Overlay(self.player)

    def run(self, dt: float) -> None:
        """Update and draw all game elements."""
        self.all_sprites.custom_draw(self.player)
        self.all_sprites.update(dt)
        self.overlay.draw()
