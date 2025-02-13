import pygame

from fairy_farm.entities.sprites.player import Player
from fairy_farm.entities.sprites.world import World
from fairy_farm.levels.camera_group import CameraGroup
from fairy_farm.ui.overlays import Overlay


class Level:
    def __init__(self) -> None:
        self.display_surface: pygame.Surface = pygame.display.get_surface()
        self.all_sprites: CameraGroup = CameraGroup()

        World(self.all_sprites)

        self.player = Player((640, 360), self.all_sprites)
        self.overlay = Overlay(self.player)

    def run(self, dt: float) -> None:
        self.display_surface.fill("black")
        self.all_sprites.custom_draw(self.player)
        self.all_sprites.update(dt)
        self.overlay.draw()
