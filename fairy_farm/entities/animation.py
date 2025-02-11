"""Manage entity animations for Fairy Farm."""

from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path

import pygame

from fairy_farm.utils import import_assets_from_folder


class EntityFacing(StrEnum):
    """Define possible facing directions of an entity."""

    UP = "up"
    RIGHT = "right"
    DOWN = "down"
    LEFT = "left"


@dataclass
class EntityAnimation:
    """Handle loading and retrieving entity animations."""

    assets_dir: Path

    def __post_init__(self) -> None:
        """Load animation frames from the specified asset directory."""
        self.up: list[pygame.Surface] = import_assets_from_folder(self.assets_dir / "up")
        self.right: list[pygame.Surface] = import_assets_from_folder(self.assets_dir / "right")
        self.down: list[pygame.Surface] = import_assets_from_folder(self.assets_dir / "down")
        self.left: list[pygame.Surface] = import_assets_from_folder(self.assets_dir / "left")

    def get_frame(self, facing: EntityFacing, frame_idx: int) -> pygame.Surface:
        """Return the specified animation frame for the given facing direction."""
        frame_idx = frame_idx % len(getattr(self, facing.value))
        return getattr(self, facing.value)[frame_idx]
