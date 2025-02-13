"""Camera system for rendering sprites with an offset based on the player's position."""

from typing import cast

import pygame

from fairy_farm import settings
from fairy_farm.entities.sprites import Sprite
from fairy_farm.entities.sprites.player import Player


class CameraGroup(pygame.sprite.Group):  # type: ignore  # noqa: PGH003
    """A custom sprite group that implements a camera system for rendering with an offset."""

    def __init__(self, *sprites: Sprite) -> None:
        """Initialize the CameraGroup with given sprites."""
        super().__init__(*sprites)  # type: ignore  # noqa: PGH003
        self.display_surface: pygame.Surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()

    def custom_draw(self, player: Player) -> None:
        """Draw all sprites with an offset based on the player's position."""
        self.offset.x = player.rect.centerx - settings.SCREEN_WIDTH / 2
        self.offset.y = player.rect.centery - settings.SCREEN_HEIGHT / 2

        for sprite in sorted(cast(list[Sprite], self.sprites()), key=lambda x: x.z.value):
            offset_rect: pygame.Rect = sprite.rect.copy()
            offset_rect.center -= self.offset
            self.display_surface.blit(sprite.img, offset_rect)
