from pathlib import Path

import pygame


def import_assets_from_folder(path: Path) -> list[pygame.Surface]:
    surfaces: list[pygame.Surface] = []

    for file in path.iterdir():
        image: pygame.Surface = pygame.image.load(Path.resolve(file)).convert_alpha()
        surfaces.append(image)

    return surfaces
