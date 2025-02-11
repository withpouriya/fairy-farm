import pygame

from fairy_farm.entities.player import Player


class Level:
    def __init__(self) -> None:
        self.display_surface: pygame.Surface = pygame.display.get_surface()
        self.all_sprites: pygame.sprite.Group = pygame.sprite.Group()

        self.setup()

    def setup(self) -> None:
        self.player = Player((640, 360), self.all_sprites)

    def run(self, dt: float) -> None:
        self.display_surface.fill("black")
        self.all_sprites.draw(self.display_surface)
        self.all_sprites.update(dt)
