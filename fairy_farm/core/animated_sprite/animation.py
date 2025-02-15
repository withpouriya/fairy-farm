"""Manage entity animations for Fairy Farm."""

from dataclasses import dataclass
from pathlib import Path

import pygame

from fairy_farm.utils import import_assets_from_folder


@dataclass
class Animation:
    """Represent an animation consisting of multiple frames."""

    frames: list[pygame.Surface]

    def get_frame(self, frame_idx: int) -> pygame.Surface:
        """Retrieve a specific frame from the animation based on the given index."""
        return self.frames[frame_idx % len(self.frames)]


class AnimationFactory:
    """Factory class for creating animations from a specified asset folder."""

    @staticmethod
    def from_path(path: Path) -> Animation:
        """Load an animation from the given path by importing assets."""
        return Animation(import_assets_from_folder(path))
