import pygame

from fairy_farm import settings
from fairy_farm.entities.animation import EntityFacing
from fairy_farm.entities.player.animation import PlayerAnimation, PlayerStatus


class Player(pygame.sprite.Sprite):
    def __init__(self, pos: tuple[int, int], group: pygame.sprite.Group) -> None:  # type: ignore  # noqa: PGH003
        super().__init__(group)
        self.animation = PlayerAnimation(settings.ASSETS_DIR / "graphics" / "character")

        self.status = PlayerStatus.IDL
        self.facing = EntityFacing.DOWN
        self.frame_idx: float = 0

        self.rect: pygame.Rect = self.image.get_rect(center=pos)

        self.direction = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200

    @property
    def image(self) -> pygame.Surface:
        return self.animation.get_player_frame(self.status, self.facing, int(self.frame_idx))

    def input(self) -> None:
        keys: pygame.key.ScancodeWrapper = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.facing = EntityFacing.UP
            self.status = PlayerStatus.NONE
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.facing = EntityFacing.DOWN
            self.status = PlayerStatus.NONE
            self.direction.y = 1
        else:
            self.status = PlayerStatus.IDL
            self.direction.y = 0

        if keys[pygame.K_RIGHT]:
            self.facing = EntityFacing.RIGHT
            self.status = PlayerStatus.NONE
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.facing = EntityFacing.LEFT
            self.status = PlayerStatus.NONE
            self.direction.x = -1
        else:
            self.direction.x = 0

    def animate(self, dt: float) -> None:
        self.frame_idx += 4 * dt

    def move(self, dt: float) -> None:
        if self.direction.magnitude():
            self.direction: pygame.Vector2 = self.direction.normalize()

        self.pos.x += self.direction.x * self.speed * dt
        self.rect.centerx = int(self.pos.x)

        self.pos.y += self.direction.y * self.speed * dt
        self.rect.centery = int(self.pos.y)

    def update(self, dt: float) -> None:
        self.input()
        self.animate(dt)
        self.move(dt)
