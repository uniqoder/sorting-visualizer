from hashlib import algorithms_available
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

        uiTransStyle: ui.Style = uiStyle.copy()
        uiTransStyle.bg_color = style.theme.panel
        uiTransStyle.hover_color = uiTransStyle.bg_color
        uiTransStyle.active_color = style.theme.secondary_accent
        uiTransStyle.fg_color = style.theme.secondary_text

        # Run button
        width: int = round(0.6 * self.panel_rect.width)
        height: int = round(0.06 * self.panel_rect.height)
        y: int = round(0.7 * self.panel_rect.height)
        x: int = self.panel_rect.centerx - width // 2

        self.runButton: Button = Button(
            "Run",
            pg.Rect(x, y, width, height),
            lambda: None,
            style=uiStyle,
        )

        # Headings
        self.arrayHeading: pg.Surface = style.font.heading.render(
            "Array:", True, style.theme.primary_text
        )
        self.arrayHeadingRect: pg.Rect = pg.Rect(
            round(0.1 * self.panel_rect.width),
            round(0.15 * self.panel_rect.height),
            *self.arrayHeading.get_size(),
        )

        # Labels
        self.algLabel: pg.Surface = style.font.small.render(
            "Algorithm:", True, style.theme.secondary_text
        )
        self.algLabelRect: pg.Rect = self.algLabel.get_rect()
        self.algLabelRect.left = round(0.15 * self.panel_rect.width)
        self.algLabelRect.top = round(0.18 * self.panel_rect.height)

        # Sorting algorithm dropdown
        self.algorithmDropdown: Dropdown = Dropdown(
            ["Bubble", "Selection", "Insertion", "Merge", "Quick"],
            pg.Rect(
                round(0.50 * self.panel_rect.width),
                round(0.17 * self.panel_rect.height),
                round(0.7 * width),
                round(0.7 * height),
            ),
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

        # Text
        _ = _surface.blit(
            self.title,
            (
                rect.left + self.style.pad,
                rect.top + self.style.pad,
            ),
        )

        _ = _surface.blit(self.arrayHeading, self.arrayHeadingRect)
        _ = _surface.blit(self.algLabel, self.algLabelRect)

        self.runButton.draw(_surface)
        self.algorithmDropdown.draw(_surface)

    @override
    def update(self) -> None:
        self.runButton.update()
        self.algorithmDropdown.update()
