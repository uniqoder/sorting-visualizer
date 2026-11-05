from typing import override

import pygame as pg

from sorting_visualizer.ui.dropdown import Dropdown

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

        # Run button
        width: int = round(0.6 * self.panel_rect.width)
        height: int = round(0.06 * self.panel_rect.height)
        y: int = round(0.7 * self.panel_rect.height)
        x: int = self.panel_rect.centerx - width // 2

        uiStyle: ui.Style = ui.Style(
            style.font,
            bg_color=style.theme.primary_accent,
            fg_color=style.theme.primary_text,
            border_color=style.theme.border,
            hover_color=style.theme.secondary_accent,
            active_color=style.theme.panel,
            border_width=2,
            border_radius=12,
        )

        self.runButton: Button = Button(
            "Run",
            pg.Rect(x, y, width, height),
            lambda: None,
            style=uiStyle,
        )

        # Sorting algorithm dropdown
        y = round(0.3 * self.panel_rect.height)

        uiTransStyle: ui.Style = uiStyle.copy()
        uiTransStyle.bg_color = style.theme.panel
        uiTransStyle.hover_color = uiTransStyle.bg_color
        uiTransStyle.active_color = style.theme.secondary_accent

        self.algorithmDropdown: Dropdown = Dropdown(
            ["Bubble", "Selection", "Insertion", "Merge", "Quick"],
            pg.Rect(x, y, width, height),
            lambda op: None,
            style=uiTransStyle,
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
        self.algorithmDropdown.draw(_surface)

    @override
    def update(self) -> None:
        self.runButton.update()
        self.algorithmDropdown.update()
