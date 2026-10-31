from typing import override

import pygame as pg

from .. import ui
from ..ui.button import Button
from .panel import Panel, Style


class OptionsPanel(Panel):
    def __init__(self, win_size: tuple[int, int], style: Style) -> None:
        super().__init__(win_size, style)

        self.panel_rect: pg.Rect = pg.Rect(
            style.margin,
            style.margin,
            round(win_size[0] * 0.2) - style.margin,
            win_size[1] - 2 * style.margin,
        )

        self.title: pg.Surface = style.font.title.render(
            "Visualizer", True, style.theme.primary_text
        )

        width: int = round(0.6 * self.panel_rect.width)
        height: int = round(0.06 * self.panel_rect.height)
        y: int = round(0.7 * self.panel_rect.height)
        x: int = self.panel_rect.centerx - width // 2

        self.runButton: Button = Button(
            "Run",
            pg.Rect(
                x,
                y,
                width,
                height,
            ),
            lambda: None,
            style=ui.Style(
                style.font,
                bg_color=style.theme.primary_accent,
                fg_color=style.theme.primary_text,
                border_color=style.theme.border,
                border_width=2,
                border_radius=12,
            ),
        )

    @override
    def draw(self, _surface: pg.Surface) -> None:
        bw: int = self.style.border_width // 2
        rect: pg.Rect = pg.Rect(
            self.panel_rect.x + bw,
            self.panel_rect.y + bw,
            self.panel_rect.width,
            self.panel_rect.height,
        )
        _ = pg.draw.rect(
            _surface,
            self.style.theme.panel,
            rect,
            border_radius=self.style.border_radius,
        )
        _ = pg.draw.rect(
            _surface,
            self.style.theme.border,
            rect,
            border_radius=self.style.border_radius,
            width=self.style.border_width,
        )

        _ = _surface.blit(
            self.title,
            (
                rect.left + self.style.pad,
                rect.top + self.style.pad,
            ),
        )

        self.runButton.draw(_surface)

    @override
    def handle_event(self, _event: pg.event.Event) -> None:
        self.runButton.handle_event(_event)
