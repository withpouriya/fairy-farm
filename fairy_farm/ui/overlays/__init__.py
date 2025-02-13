"""Overlay class for rendering player-selected tools and seeds on the screen."""

from dataclasses import dataclass

import pygame

from fairy_farm import settings
from fairy_farm.entities.sprites.player import Player


@dataclass
class Overlay:
    """Manage and draw the overlay displaying the player's selected tool and seed."""

    player: Player

    def __post_init__(self) -> None:
        """Initialize the overlay by getting the game's display surface."""
        self.display_surface: pygame.Surface = pygame.display.get_surface()

    def draw(self) -> None:
        """Render the selected tool and seed on the screen."""
        tool_surf: pygame.Surface = self.player.selected_tool.item_surf
        tool_rect: pygame.Rect = tool_surf.get_rect(midbottom=(40, settings.SCREEN_HEIGHT - 15))
        self.display_surface.blit(tool_surf, tool_rect)

        seed_surf: pygame.Surface = self.player.selected_seed.item_surf
        seed_rect: pygame.Rect = seed_surf.get_rect(midbottom=(70, settings.SCREEN_HEIGHT - 5))
        self.display_surface.blit(seed_surf, seed_rect)
