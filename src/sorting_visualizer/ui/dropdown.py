from collections.abc import Callable
from typing import override

import pygame as pg

from . import UI, Alignment, Style


class Dropdown(UI):
    def __init__(
        self,
        options: list[str],
        row_rect: pg.Rect,
        onClick: Callable[[str], None],
        style: Style,
        selected: int = 0,
    ) -> None:
        super().__init__(row_rect, style)

        self.options: list[str] = options
        self.selected: int = selected
        self.onClick: Callable[[str], None] = onClick

        self.text_surfs: list[pg.Surface] = [
            style.font.label.render(txt, True, style.fg_color) for txt in options
        ]

        # Settings
        self.hovered: bool = False
        self.pressed: bool = False
        self.enabled: bool = True
        self.open: bool = False

        self.mouseDown: bool = True
        self.optPressed: int = -1

    @override
    def draw(self, _surface: pg.Surface) -> None:
        rect: pg.Rect = self.rect

        # Add padding
        rect.width += 2 * self.style.padding
        rect.x -= self.style.padding

        rect.height += 2 * self.style.padding
        rect.y -= self.style.padding

        # Align the text
        text_rects: list[pg.Rect] = [surf.get_rect() for surf in self.text_surfs]
        if self.style.alignment == Alignment.Left:
            for trect in text_rects:
                trect.midleft = self.rect.midleft
        elif self.style.alignment == Alignment.Right:
            for trect in text_rects:
                trect.midright = self.rect.midright
        elif self.style.alignment == Alignment.Center:
            for trect in text_rects:
                trect.center = self.rect.center

        # Get BG color
        bg_color: str = self.style.bg_color
        if self.hovered:
            bg_color = self.style.hover_color
        if self.pressed:
            bg_color = self.style.active_color
        if not self.enabled:
            bg_color = self.style.disabled_color

        # Draw first row
        bot_rad: int = 0
        if not self.open:
            bot_rad = self.style.border_radius

        _ = pg.draw.rect(
            _surface,
            bg_color,
            rect,
            border_top_left_radius=self.style.border_radius,
            border_top_right_radius=self.style.border_radius,
            border_bottom_left_radius=bot_rad,
            border_bottom_right_radius=bot_rad,
        )
        _ = pg.draw.rect(
            _surface,
            self.style.border_color,
            rect,
            width=self.style.border_width,
            border_top_left_radius=self.style.border_radius,
            border_top_right_radius=self.style.border_radius,
            border_bottom_left_radius=bot_rad,
            border_bottom_right_radius=bot_rad,
        )
        _ = _surface.blit(self.text_surfs[self.selected], text_rects[self.selected])

        # Draw the other options
        if not self.open:
            return

        op: int = 0
        for i in range(len(text_rects)):
            if i == self.selected:
                continue

            op += 1
            opRect: pg.Rect = rect.copy()
            opRect.y += op * rect.height

            txtRect: pg.Rect = text_rects[i].copy()
            txtRect.y += op * rect.height

            rad: int = 0
            if i == len(text_rects) - 1:
                rad = self.style.border_radius

            _ = pg.draw.rect(
                _surface,
                self.style.bg_color
                if i != self.optPressed
                else self.style.active_color,
                opRect,
                border_bottom_left_radius=rad,
                border_bottom_right_radius=rad,
            )
            _ = pg.draw.rect(
                _surface,
                self.style.border_color,
                opRect,
                width=self.style.border_width,
                border_bottom_left_radius=rad,
                border_bottom_right_radius=rad,
            )
            _ = _surface.blit(self.text_surfs[i], txtRect)

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

        menuRect: pg.Rect = rect.copy()
        menuRect.y += menuRect.height
        menuRect.height *= len(self.options) - 1
        idx: int = limit(
            (pos[1] - menuRect.top) // rect.height, 0, len(self.options) - 1
        )
        if idx >= self.selected:
            idx += 1  # Selected option skipping offset

        # Click
        if pressed[0]:
            self.pressed = rect.collidepoint(pos)
            if self.open and menuRect.collidepoint(pos):
                self.optPressed = idx
            else:
                self.optPressed = -1
        elif not pressed[0]:
            self.pressed = False
            self.optPressed = -1

            if self.mouseDown:
                self.mouseDown = False

                if rect.collidepoint(pos):
                    self.open = not self.open
                elif self.open and menuRect.collidepoint(pos):
                    self.open = False

                    self.selected = idx
                    self.onClick(self.options[idx])

        # Hover
        self.hovered = rect.collidepoint(pos)
        self.mouseDown = pressed[0]

    def getOption(self) -> str:
        self.selected = limit(self.selected, 0, len(self.options) - 1)
        return self.options[self.selected]


def limit(val: int, low: int, high: int):
    return max(low, min(val, high))
