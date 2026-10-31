from collections.abc import Callable
from typing import override

import pygame as pg
from pygame.event import Event

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

        self.text_surf: pg.Surface = style.font.label.render(text, True, style.fg_color)

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
        _ = pg.draw.rect(
            _surface, self.style.bg_color, rect, border_radius=self.style.border_radius
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
    def handle_event(self, _event: Event) -> None:
        rect: pg.Rect = self.rect

        # Add padding
        rect.width += 2 * self.style.padding
        rect.x -= self.style.padding

        rect.height += 2 * self.style.padding
        rect.y -= self.style.padding

        if (
            _event.type == pg.MOUSEBUTTONDOWN
            and _event.button == 1
            and rect.collidepoint(_event.pos)
        ):
            self.onClick()
