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

        btnStyle: ui.Style = ui.Style(
            style.font.label,
            bg_color=style.theme.primary_accent,
            fg_color=style.theme.primary_text,
            border_color=style.theme.border,
            hover_color=style.theme.secondary_accent,
            active_color=style.theme.panel,
            border_width=2,
            border_radius=12,
        )

        dropdownStyle: ui.Style = btnStyle.copy()
        dropdownStyle.font = style.font.small
        dropdownStyle.bg_color = style.theme.panel
        dropdownStyle.hover_color = dropdownStyle.bg_color
        dropdownStyle.active_color = style.theme.secondary_accent
        dropdownStyle.fg_color = style.theme.secondary_text

        # Run button
        btnWidth: int = round(0.6 * self.panel_rect.width)
        btnHeight: int = round(0.06 * self.panel_rect.height)

        self.runButton: Button = Button(
            "Run",
            pg.Rect(0, round(0.7 * self.panel_rect.height), btnWidth, btnHeight),
            lambda: None,
            style=btnStyle,
        )
        self.runButton.rect.centerx = self.panel_rect.centerx

        # Headings
        self.arrayHeading: pg.Surface = style.font.heading.render(
            "Array:", True, style.theme.primary_text
        )
        self.arrayHeadingRect: pg.Rect = self.arrayHeading.get_rect(
            left=self.panel_rect.left + style.pad,
            top=round(0.15 * self.panel_rect.height),
        )

        # Labels
        self.algLabel: pg.Surface = style.font.small.render(
            "Algorithm:", True, style.theme.secondary_text
        )
        self.algLabelRect: pg.Rect = self.algLabel.get_rect(
            left=self.panel_rect.left + 2 * style.pad,
            top=round(0.24 * self.panel_rect.height),
        )

        self.arrSizeLabel: pg.Surface = style.font.small.render(
            "Size:", True, style.theme.secondary_text
        )
        self.arrSizeRect: pg.Rect = self.arrSizeLabel.get_rect(
            left=self.panel_rect.left + 2 * style.pad,
            top=round(0.18 * self.panel_rect.height),
        )

        # Shuffle button
        self.shuffleButton: Button = Button(
            "Shuffle",
            pg.Rect(
                0,
                round(0.30 * self.panel_rect.height),
                round(0.8 * btnWidth),
                round(0.8 * btnHeight),
            ),
            lambda: None,
            style=dropdownStyle,
        )
        self.shuffleButton.rect.centerx = self.panel_rect.centerx

        # Sorting algorithm dropdown
        srtAlgRect: pg.Rect = pg.Rect(
            0, 0, round(0.7 * btnWidth), round(0.6 * btnHeight)
        )
        srtAlgRect.right = self.panel_rect.right - style.pad
        srtAlgRect.top = round(0.235 * self.panel_rect.height)

        self.algorithmDropdown: Dropdown = Dropdown(
            ["Bubble", "Selection", "Insertion", "Merge", "Quick"],
            srtAlgRect,
            lambda op: None,
            style=dropdownStyle,
        )

        # Array size dropdown
        sizeRect: pg.Rect = srtAlgRect.copy()
        sizeRect.top = round(0.175 * self.panel_rect.height)

        self.sizeDropdown: Dropdown = Dropdown(
            ["10", "20", "30", "40", "50", "60", "70"],
            sizeRect,
            lambda op: None,
            style=dropdownStyle,
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
        _ = _surface.blit(self.arrSizeLabel, self.arrSizeRect)

        self.runButton.draw(_surface)
        self.shuffleButton.draw(_surface)
        self.sizeDropdown.draw(_surface)
        self.algorithmDropdown.draw(_surface)

    @override
    def update(self) -> None:
        self.runButton.update()
        self.shuffleButton.update()
        self.sizeDropdown.update()
        self.algorithmDropdown.update()
