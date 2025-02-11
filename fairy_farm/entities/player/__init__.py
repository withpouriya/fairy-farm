"""Player class for handling movement and animation in the game."""

from enum import Enum

import pygame

from fairy_farm import settings
from fairy_farm.entities.animation import EntityFacing
from fairy_farm.entities.player.animation import PlayerAnimation, PlayerStatus
from fairy_farm.utils.timer import Timer


class Tool(Enum):
    """Represent the different tools available to the player."""

    AXE = 2
    HOE = 3
    WATER = 4


class Player(pygame.sprite.Sprite):
    """Represent the player character with movement and animation functionality."""

    def __init__(self, pos: tuple[int, int], group: pygame.sprite.Group) -> None:  # type: ignore  # noqa: PGH003
        """Initialize the player with position, sprite group, and initial animation and status."""
        super().__init__(group)  # type: ignore  # noqa: PGH003
        self.animation = PlayerAnimation(settings.ASSETS_DIR / "graphics" / "character")

        self.facing = EntityFacing.DOWN
        self.frame_idx: float = 0

        self.rect: pygame.Rect = self.image.get_rect(center=pos)

        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200

        self.selected_tool: Tool | None = None

        self.axe_tool_use_timer: Timer = Timer(350, self.end_tool_usage)

    @property
    def status(self) -> PlayerStatus:
        """Return the player's current status based on selected tool and movement state."""
        if hasattr(self, "selected_tool") and self.selected_tool:
            match self.selected_tool:
                case Tool.AXE:
                    return PlayerStatus.AXE
                case Tool.HOE:
                    return PlayerStatus.HOE
                case Tool.WATER:
                    return PlayerStatus.WATER
                case _:
                    pass

        if hasattr(self, "direction") and self.direction.magnitude() == 0:
            return PlayerStatus.IDL

        return PlayerStatus.NONE

    @property
    def image(self) -> pygame.Surface:
        """Return the current player frame based on status and facing direction."""
        return self.animation.get_player_frame(self.status, self.facing, int(self.frame_idx))

    @property
    def can_move(self) -> bool:
        """Return True if the player is allowed to move, else False."""
        return not self.axe_tool_use_timer.active

    def input(self) -> None:
        """Handle input to update player direction and facing."""
        keys: pygame.key.ScancodeWrapper = pygame.key.get_pressed()

        if self.can_move:
            if keys[pygame.K_UP]:
                self.facing = EntityFacing.UP
                self.direction.y = -1
            elif keys[pygame.K_DOWN]:
                self.facing = EntityFacing.DOWN
                self.direction.y = 1
            else:
                self.direction.y = 0

            if keys[pygame.K_RIGHT]:
                self.facing = EntityFacing.RIGHT
                self.direction.x = 1
            elif keys[pygame.K_LEFT]:
                self.facing = EntityFacing.LEFT
                self.direction.x = -1
            else:
                self.direction.x = 0

        if keys[pygame.K_SPACE]:
            self.selected_tool = Tool.AXE
            self.axe_tool_use_timer.activate()
            self.direction = pygame.math.Vector2()

    def end_tool_usage(self) -> None:
        """Reset the selected tool after usage."""
        self.selected_tool = None

    def animate(self, dt: float) -> None:
        """Update the player's animation frame index based on delta time."""
        self.frame_idx += 4 * dt

    def move(self, dt: float) -> None:
        """Move the player based on direction and speed."""
        if self.direction.magnitude():
            self.direction: pygame.Vector2 = self.direction.normalize()

        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = int(self.pos.x)

        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = int(self.pos.y)

    def update(self, dt: float) -> None:
        """Update player state: process input, animate, move, and update tool timer."""
        self.input()
        self.animate(dt)
        self.move(dt)
        self.axe_tool_use_timer.update()
