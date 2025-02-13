"""Player class for handling movement and animation in the game."""

from enum import Enum

import pygame

from fairy_farm import settings
from fairy_farm.entities.animation import EntityFacing
from fairy_farm.entities.sprites import Sprite
from fairy_farm.entities.sprites.player.animation import PlayerAnimation, PlayerStatus
from fairy_farm.entities.sprites.player.items import Seed, Tool
from fairy_farm.utils.timer import Timer


class HeldItem(Enum):
    """Represent the type of item currently held by the player."""

    TOOL = 1
    SEED = 2


class Player(pygame.sprite.Sprite, Sprite):
    """Represent the player character with movement and animation functionality."""

    def __init__(self, pos: tuple[int, int], group: pygame.sprite.Group) -> None:  # type: ignore  # noqa: PGH003
        """Initialize the player with position, sprite group, and initial animation and status."""
        super().__init__(group)  # type: ignore  # noqa: PGH003

        self.z = settings.Layers.MAIN

        self.animation = PlayerAnimation(settings.ASSETS_DIR / "graphics" / "character")

        self.facing = EntityFacing.DOWN
        self.frame_idx: float = 0

        self.rect: pygame.Rect = self.img.get_rect(center=pos)

        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200

        self.held_item: HeldItem | None = None

        self.selected_tool: Tool = Tool.AXE
        self.tool_use_timer: Timer = Timer(350, self.end_tool_usage)
        self.tool_switch_timer: Timer = Timer(200)

        self.selected_seed: Seed = Seed.CORN
        self.seed_use_timer: Timer = Timer(350, self.end_tool_usage)
        self.seed_switch_timer: Timer = Timer(200)

    @property
    def status(self) -> PlayerStatus | None:
        """Return the player's current status based on selected tool and movement state."""
        if hasattr(self, "held_item") and self.held_item == HeldItem.TOOL and hasattr(self, "selected_tool"):
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

        return None

    @property
    def img(self) -> pygame.Surface:
        """Return the current player frame based on status and facing direction."""
        return self.animation.get_player_frame(self.status, self.facing, int(self.frame_idx))

    @property
    def can_move(self) -> bool:
        """Return True if the player is allowed to move, else False."""
        return not self.tool_use_timer.active and not self.seed_use_timer.active

    def input(self) -> None:
        """Handle input to update player direction and facing."""
        keys: pygame.key.ScancodeWrapper = pygame.key.get_pressed()

        if self.can_move:
            if keys[pygame.K_UP] or keys[pygame.K_w]:
                self.facing = EntityFacing.UP
                self.direction.y = -1
            elif keys[pygame.K_DOWN] or keys[pygame.K_s]:
                self.facing = EntityFacing.DOWN
                self.direction.y = 1
            else:
                self.direction.y = 0

            if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                self.facing = EntityFacing.RIGHT
                self.direction.x = 1
            elif keys[pygame.K_LEFT] or keys[pygame.K_a]:
                self.facing = EntityFacing.LEFT
                self.direction.x = -1
            else:
                self.direction.x = 0

        if keys[pygame.K_SPACE]:
            self.held_item = HeldItem.TOOL
            self.tool_use_timer.activate()
            self.direction = pygame.math.Vector2()

        if keys[pygame.K_q] and not self.tool_switch_timer.active:
            self.tool_switch_timer.activate()
            self.selected_tool = self.selected_tool.next()

        if keys[pygame.K_LCTRL]:
            self.held_item = HeldItem.SEED
            self.seed_use_timer.activate()
            self.direction = pygame.math.Vector2()

        if keys[pygame.K_e] and not self.seed_switch_timer.active:
            self.seed_switch_timer.activate()
            self.selected_seed = self.selected_seed.next()

    def end_tool_usage(self) -> None:
        """Reset the selected tool after usage."""
        self.held_item = None

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
        self.tool_use_timer.update()
        self.tool_switch_timer.update()
        self.seed_use_timer.update()
        self.seed_switch_timer.update()

        self.input()
        self.animate(dt)
        self.move(dt)
