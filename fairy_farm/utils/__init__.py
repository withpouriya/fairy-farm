"""Handle importing image assets from a folder for use in a Pygame project."""

from pathlib import Path

import pygame


def import_assets_from_folder(path: Path) -> list[pygame.Surface]:
    """Import all images from a specified folder and return them as a list of pygame.Surface objects."""
    surfaces: list[pygame.Surface] = []

    for file in path.iterdir():
        image: pygame.Surface = pygame.image.load(Path.resolve(file)).convert_alpha()
        surfaces.append(image)

    return surfaces
