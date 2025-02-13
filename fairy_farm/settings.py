"""Configuration settings for the game."""

from pathlib import Path

from pygame.math import Vector2

BASE_DIR: Path = Path(__file__).parent.parent
ASSETS_DIR: Path = BASE_DIR / "assets"


SCREEN_WIDTH, SCREEN_HEIGHT = (1280, 720)
TILE_SIZE = 64

OVERLAY_POSITIONS: dict[str, tuple[int, int]] = {
    "tool": (40, SCREEN_HEIGHT - 15),
    "seed": (70, SCREEN_HEIGHT - 5),
}

PLAYER_TOOL_OFFSET: dict[str, Vector2] = {
    "left": Vector2(-50, 40),
    "right": Vector2(50, 40),
    "up": Vector2(0, -10),
    "down": Vector2(0, 50),
}

LAYERS: list[str] = [
    "water",
    "ground",
    "soil",
    "soil water",
    "rain floor",
    "house bottom",
    "ground plant",
    "main",
    "house top",
    "fruit",
    "rain drops",
]

APPLE_POS: dict[str, list[tuple[int, int]]] = {
    "Small": [(18, 17), (30, 37), (12, 50), (30, 45), (20, 30), (30, 10)],
    "Large": [(30, 24), (60, 65), (50, 50), (16, 40), (45, 50), (42, 70)],
}

GROW_SPEED: dict[str, float] = {"corn": 1, "tomato": 0.7}

SALE_PRICES: dict[str, int] = {"wood": 4, "apple": 2, "corn": 10, "tomato": 20}
PURCHASE_PRICES: dict[str, int] = {"corn": 4, "tomato": 5}
