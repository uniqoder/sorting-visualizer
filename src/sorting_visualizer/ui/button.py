from collections.abc import Callable
from typing import override

import pygame as pg

from . import UI, Alignment, Style


class Button(UI):
    def __init__(
        self,
        text: str,
        rect: pg.Rect,
        onClick: Callable[[], None],
        style: Style,
    ) -> None:
        super().__init__(rect, style)

        self.text: str = text
        self.onClick: Callable[[], None] = onClick

        self.text_surf: pg.Surface
        self.render_texts()

        # Settings
        self.hovered: bool = False
        self.pressed: bool = False
        self.enabled: bool = True

    @override
    def render_texts(self) -> None:
        self.text_surf = self.style.font.render(self.text, True, self.style.fg_color)

    @override
    def draw(self, _surface: pg.Surface) -> None:
        rect: pg.Rect = self.rect

        # Add padding
        rect.width += 2 * self.style.padding
        rect.x -= self.style.padding

        rect.height += 2 * self.style.padding
        rect.y -= self.style.padding

        # Align the text
        text_rect: pg.Rect = self.text_surf.get_rect()
        if self.style.alignment == Alignment.Left:
            text_rect.midleft = self.rect.midleft
        elif self.style.alignment == Alignment.Right:
            text_rect.midright = self.rect.midright
        elif self.style.alignment == Alignment.Center:
            text_rect.center = self.rect.center

        # Draw background and border
        bg_color: str = self.style.bg_color
        if self.hovered:
            bg_color = self.style.hover_color
        if self.pressed:
            bg_color = self.style.active_color
        if not self.enabled:
            bg_color = self.style.disabled_color

        _ = pg.draw.rect(
            _surface, bg_color, rect, border_radius=self.style.border_radius
        )
        _ = pg.draw.rect(
            _surface,
            self.style.border_color,
            rect,
            width=self.style.border_width,
            border_radius=self.style.border_radius,
        )

        # Draw text
        _ = _surface.blit(self.text_surf, text_rect)

    @override
    def update(self) -> None:
        rect: pg.Rect = self.rect

        # Add padding
        rect.width += 2 * self.style.padding
        rect.x -= self.style.padding

        rect.height += 2 * self.style.padding
        rect.y -= self.style.padding

        pressed: tuple[bool, bool, bool] = pg.mouse.get_pressed(3)
        pos: tuple[int, int] = pg.mouse.get_pos()

        # Click
        if pressed[0]:
            if rect.collidepoint(pos):
                self.pressed = True
                self.onClick()
        else:
            self.pressed = False

        # Hover
        self.hovered = rect.collidepoint(pos)
