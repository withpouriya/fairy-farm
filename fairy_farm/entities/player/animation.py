"""Manage player animations for Fairy Farm."""

from dataclasses import dataclass
from enum import StrEnum
from pathlib import Path

import pygame

from fairy_farm.entities.animation import EntityAnimation, EntityFacing


class PlayerStatus(StrEnum):
    """Define possible statuses for the player."""

    NONE = ""
    IDL = "idl"
    HOE = "hoe"
    AXE = "axe"
    WATER = "water"


@dataclass
class PlayerAnimation:
    """Handle loading and retrieving player animations."""

    assets_dir: Path

    def __post_init__(self) -> None:
        """Initialize animations for different player statuses."""
        self.idl: EntityAnimation = EntityAnimation(self.assets_dir / "idl")
        self.hoe: EntityAnimation = EntityAnimation(self.assets_dir / "hoe")
        self.axe: EntityAnimation = EntityAnimation(self.assets_dir / "axe")
        self.water: EntityAnimation = EntityAnimation(self.assets_dir / "water")

    def get_frame(self, status: PlayerStatus, facing: EntityFacing, frame_idx: int) -> pygame.Surface:
        """Return the specified animation frame based on player status and facing direction."""
        if status == PlayerStatus.NONE:
            return getattr(self, facing.value)[frame_idx]
        return getattr(getattr(self, status.value), facing.value)[frame_idx]
