from pathlib import Path

import pygame

from fairy_farm import settings


class Sprite(pygame.sprite.Sprite):
    """Represent the game world and its rendering."""

    def __init__(
        self,
        group: pygame.sprite.Group,  # type: ignore  # noqa: PGH003
        z: int,
        img_path: Path,
        pos: tuple[int, int],
    ) -> None:
        """Initialize the world with a sprite group and set its layer."""
        super().__init__(group)  # type: ignore  # noqa: PGH003
        self.z: int = z
        self.img: pygame.Surface = pygame.image.load(img_path).convert_alpha()
        self.rect: pygame.Rect = self.img.get_rect()
        self.rect.center = pos
