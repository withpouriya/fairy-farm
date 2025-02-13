"""Module defining player items including seeds and tools."""

from enum import StrEnum
from functools import cache
from typing import Self

import pygame

from fairy_farm import settings


class PlayerItem(StrEnum):
    """Base class for player items with cycling and image loading functionality."""

    def next(self) -> Self:
        """Cycle through items in a loop."""
        members = list(self.__class__)  # استفاده از __class__ برای پشتیبانی از کلاس‌های فرزند
        return members[(members.index(self) + 1) % len(members)]

    @property
    @cache
    def item_surf(self) -> pygame.Surface:
        """Load and cache the item's surface image."""
        item_img_path = settings.ASSETS_DIR / "graphics" / "overlay" / f"{self.value}.png"
        return pygame.image.load(item_img_path).convert_alpha()


class Seed(PlayerItem):
    """Represent different types of seeds available in the game."""

    CORN = "corn"
    TOMATO = "tomato"


class Tool(PlayerItem):
    """Represent the different tools available to the player."""

    AXE = "axe"
    HOE = "hoe"
    WATER = "water"
