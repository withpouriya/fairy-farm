"""Camera system for rendering sprites with an offset based on the player's position."""

from typing import cast

import pygame

from fairy_farm import settings
from fairy_farm.entities.sprites import Sprite
from fairy_farm.entities.sprites.player import Player


class CameraGroup(pygame.sprite.Group):  # type: ignore  # noqa: PGH003
    """A custom sprite group that implements a smooth camera system for rendering with an offset."""

    def __init__(self, *sprites: Sprite) -> None:
        """Initialize the CameraGroup with given sprites."""
        super().__init__(*sprites)  # type: ignore  # noqa: PGH003
        self.display_surface: pygame.Surface = pygame.display.get_surface()
        self.offset = pygame.math.Vector2()
        self.target_offset = pygame.math.Vector2()
        self.smooth_factor = 0.05

    def custom_draw(self, player: Player) -> None:
        """Draw all sprites with a smooth offset based on the player's position."""
        self.target_offset.x = player.rect.centerx - settings.SCREEN_WIDTH / 2
        self.target_offset.y = player.rect.centery - settings.SCREEN_HEIGHT / 2

        self.offset.x += (self.target_offset.x - self.offset.x) * self.smooth_factor
        self.offset.y += (self.target_offset.y - self.offset.y) * self.smooth_factor

        for sprite in sorted(cast(list[Sprite], self.sprites()), key=lambda x: (x.z.value, x.rect.centery)):
            offset_rect: pygame.Rect = sprite.rect.copy()
            offset_rect.center -= self.offset  # type: ignore  # noqa: PGH003
            self.display_surface.blit(sprite.img, offset_rect)
