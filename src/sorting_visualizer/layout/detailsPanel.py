from typing import override

import pygame as pg

from .panel import Panel, Style


class DetailsPanel(Panel):
    def __init__(
        self, win_size: tuple[int, int], style: Style, graph_panel: pg.Rect
    ) -> None:
        super().__init__(win_size, style)

        self.panel_rect: pg.Rect = pg.Rect(
            graph_panel.x,
            graph_panel.bottom + style.gap,
            graph_panel.width,
            round(win_size[1] * 0.35) - style.margin - style.gap,
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
