"""Defines a Sprite protocol for objects with an image and a rectangle."""

from typing import Protocol

import pygame

from fairy_farm import settings


class Sprite(Protocol):
    """Protocol defining a sprite with an image and a rectangle."""

    @property
    def img(self) -> pygame.Surface:
        """Return the image of the sprite."""
        ...

    rect: pygame.Rect
    z: settings.Layers
