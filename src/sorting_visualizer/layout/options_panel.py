from typing import override

import pygame as pg

from ..theme import Theme

from .. import ui
from ..ui.button import Button
from ..ui.dropdown import Dropdown
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

        defaultStyle: ui.Style = ui.Style(style.font.label)

        # Run button
        btnWidth: int = round(0.6 * self.panel_rect.width)
        btnHeight: int = round(0.06 * self.panel_rect.height)

        self.runButton: Button = Button(
            "Run",
            pg.Rect(0, round(0.7 * self.panel_rect.height), btnWidth, btnHeight),
            lambda: None,
            style=defaultStyle,
        )
        self.runButton.rect.centerx = self.panel_rect.centerx

        # Array settings
        self.arrayHeading: pg.Surface = style.font.heading.render(
            "Array:", True, style.theme.primary_text
        )
        self.arrayHeadingRect: pg.Rect = self.arrayHeading.get_rect(
            left=self.panel_rect.left + style.pad,
            top=round(0.15 * self.panel_rect.height),
        )

        self.arrSizeLabel: pg.Surface = style.font.small.render(
            "Size:", True, style.theme.secondary_text
        )
        self.arrSizeRect: pg.Rect = self.arrSizeLabel.get_rect(
            left=self.arrayHeadingRect.left + style.pad,
            top=self.arrayHeadingRect.bottom + 2 * style.gap,
        )

        dropdownWidth: int = round(0.7 * btnWidth)
        dropdownHeight: int = round(0.6 * btnHeight)
        self.sizeDropdown: Dropdown = Dropdown(
            [],
            pg.Rect(
                self.panel_rect.right - dropdownWidth - style.pad,
                self.arrSizeRect.top,
                dropdownWidth,
                dropdownHeight,
            ),
            lambda op: None,
            style=defaultStyle,
        )

        sflWidth: int = round(0.8 * btnWidth)
        sflHeight: int = round(0.8 * btnHeight)
        self.shuffleButton: Button = Button(
            "Shuffle",
            pg.Rect(
                self.panel_rect.centerx - sflWidth // 2,
                self.arrSizeRect.bottom + 4 * style.gap,
                sflWidth,
                sflHeight,
            ),
            lambda: None,
            style=defaultStyle,
        )

        # Sorting settings
        self.sortHeading: pg.Surface = style.font.heading.render(
            "Sorting:", True, style.theme.primary_text
        )
        self.sortHeadingRect: pg.Rect = self.sortHeading.get_rect(
            left=self.arrayHeadingRect.left,
            top=self.shuffleButton.rect.bottom + 2 * style.pad,
        )

        self.algLabel: pg.Surface = style.font.small.render(
            "Algorithm:", True, style.theme.secondary_text
        )
        self.algLabelRect: pg.Rect = self.algLabel.get_rect(
            left=self.arrSizeRect.left,
            top=self.sortHeadingRect.bottom + 2 * style.pad,
        )

        self.algorithmDropdown: Dropdown = Dropdown(
            [],
            pg.Rect(
                self.sizeDropdown.rect.left,
                self.algLabelRect.top,
                dropdownWidth,
                dropdownHeight,
            ),
            lambda op: None,
            style=defaultStyle,
        )

        self.orderLabel: pg.Surface = style.font.small.render(
            "Order:", True, style.theme.secondary_text
        )
        self.orderLabelRect: pg.Rect = self.orderLabel.get_rect(
            left=self.algLabelRect.left, top=self.algLabelRect.bottom + 3 * style.gap
        )

        self.orderDropdown: Dropdown = Dropdown(
            [],
            pg.Rect(
                self.sizeDropdown.rect.left,
                self.orderLabelRect.top,
                dropdownWidth,
                dropdownHeight,
            ),
            lambda op: None,
            style=defaultStyle,
        )

        # Theme setting
        self.themeLabel: pg.Surface = style.font.small.render(
            "Theme:", True, style.theme.primary_text
        )
        self.themeLabelRect: pg.Rect = self.themeLabel.get_rect(
            left=self.arrayHeadingRect.left,
            top=self.panel_rect.bottom - self.themeLabel.get_height() - 2 * style.pad,
        )

        self.themeDropdown: Dropdown = Dropdown(
            [],
            pg.Rect(
                self.themeLabelRect.right + 2 * style.gap,
                self.themeLabelRect.top,
                self.panel_rect.width - self.themeLabelRect.width - 3 * style.pad,
                dropdownHeight,
            ),
            lambda op: None,
            style=defaultStyle,
        )

        self.set_theme(style.theme)

    def render_texts(self) -> None:
        self.title = self.style.font.title.render(
            "Visualizer", True, self.style.theme.primary_text
        )

        self.arrayHeading = self.style.font.heading.render(
            "Array:", True, self.style.theme.primary_text
        )
        self.arrSizeLabel = self.style.font.small.render(
            "Size:", True, self.style.theme.secondary_text
        )

        self.sortHeading = self.style.font.heading.render(
            "Sorting:", True, self.style.theme.primary_text
        )
        self.algLabel = self.style.font.small.render(
            "Algorithm:", True, self.style.theme.secondary_text
        )
        self.orderLabel = self.style.font.small.render(
            "Order:", True, self.style.theme.secondary_text
        )

        self.themeLabel = self.style.font.small.render(
            "Theme:", True, self.style.theme.primary_text
        )

        self.runButton.render_texts()
        self.shuffleButton.render_texts()

        self.sizeDropdown.render_texts()
        self.algorithmDropdown.render_texts()
        self.orderDropdown.render_texts()
        self.themeDropdown.render_texts()

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
        _ = _surface.blit(self.sortHeading, self.sortHeadingRect)
        _ = _surface.blit(self.algLabel, self.algLabelRect)
        _ = _surface.blit(self.arrSizeLabel, self.arrSizeRect)
        _ = _surface.blit(self.orderLabel, self.orderLabelRect)
        _ = _surface.blit(self.themeLabel, self.themeLabelRect)

        self.themeDropdown.draw(_surface)
        self.runButton.draw(_surface)
        self.orderDropdown.draw(_surface)
        self.algorithmDropdown.draw(_surface)
        self.shuffleButton.draw(_surface)
        self.sizeDropdown.draw(_surface)

    @override
    def update(self) -> None:
        self.runButton.update()
        self.shuffleButton.update()
        self.sizeDropdown.update()
        self.algorithmDropdown.update()
        self.orderDropdown.update()
        self.themeDropdown.update()

    @override
    def set_theme(self, theme: Theme) -> None:
        super().set_theme(theme)

        btnStyle: ui.Style = ui.Style(
            self.style.font.label,
            bg_color=self.style.theme.primary_accent,
            fg_color=self.style.theme.primary_text,
            border_color=self.style.theme.border,
            hover_color=self.style.theme.secondary_accent,
            active_color=self.style.theme.panel,
            border_width=2,
            border_radius=12,
        )

        self.runButton.style = btnStyle

        dropdownStyle: ui.Style = btnStyle.copy()
        dropdownStyle.bg_color = self.style.theme.panel
        dropdownStyle.hover_color = dropdownStyle.bg_color
        dropdownStyle.active_color = self.style.theme.secondary_accent
        dropdownStyle.fg_color = self.style.theme.secondary_text

        self.shuffleButton.style = dropdownStyle
        self.sizeDropdown.style = dropdownStyle
        self.algorithmDropdown.style = dropdownStyle
        self.orderDropdown.style = dropdownStyle
        self.themeDropdown.style = dropdownStyle

        self.render_texts()
