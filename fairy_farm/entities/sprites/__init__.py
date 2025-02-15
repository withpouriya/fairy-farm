"""Defines a Sprite protocol for objects with an image and a rectangle."""

import pygame

from fairy_farm import settings


class Sprite(pygame.sprite.Sprite):
    """Protocol defining a sprite with an image and a rectangle."""

    def __init__(self, group: pygame.sprite.Group) -> None:  # type: ignore  # noqa: PGH003
        """Initialize the world with a sprite group and set its layer."""
        super().__init__(group)  # type: ignore  # noqa: PGH003

    rect: pygame.Rect
    z: settings.Layers
