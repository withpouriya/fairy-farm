from functools import cache

import pygame

from fairy_farm import settings
from fairy_farm.entities.sprites import Sprite


class World(pygame.sprite.Sprite, Sprite):
    def __init__(self, group: pygame.sprite.Group) -> None:  # type: ignore  # noqa: PGH003
        super().__init__(group)  # type: ignore  # noqa: PGH003
        self.z = settings.Layers.GROUND
        self.rect: pygame.Rect = self.img.get_rect(topleft=(0, 0))

    @property
    @cache
    def img(self) -> pygame.Surface:
        return pygame.image.load(settings.ASSETS_DIR / "graphics" / "world" / "ground.png").convert_alpha()
