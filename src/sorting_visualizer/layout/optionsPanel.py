from typing import override

import pygame as pg

from sorting_visualizer.layout.panel import Panel, Style


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

    @override
    def update(self) -> None:
        return super().update()
