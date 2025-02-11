"""Manage player animations for Fairy Farm."""

from dataclasses import dataclass
from enum import StrEnum

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
class PlayerAnimation(EntityAnimation):
    """Handle loading and retrieving player animations."""

    def __post_init__(self) -> None:
        """Initialize animations for different player statuses."""
        super().__post_init__()
        self.idl: EntityAnimation = EntityAnimation(self.assets_dir / "idl")
        self.hoe: EntityAnimation = EntityAnimation(self.assets_dir / "hoe")
        self.axe: EntityAnimation = EntityAnimation(self.assets_dir / "axe")
        self.water: EntityAnimation = EntityAnimation(self.assets_dir / "water")

    def get_player_frame(self, status: PlayerStatus, facing: EntityFacing, frame_idx: int) -> pygame.Surface:
        """Return the specified animation frame based on player status and facing direction."""
        if status == PlayerStatus.NONE:
            attr = getattr(self, facing.value)
            return attr[frame_idx % len(attr)]
        attr = getattr(getattr(self, status.value), facing.value)
        return attr[frame_idx % len(attr)]
