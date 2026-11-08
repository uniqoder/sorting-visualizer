from typing import override

import pygame as pg

from .panel import Panel, Style


class StatsPanel(Panel):
    def __init__(
        self, win_size: tuple[int, int], style: Style, graph_panel: pg.Rect
    ) -> None:
        super().__init__(win_size, style)

        self.panel_rect: pg.Rect = pg.Rect(
            graph_panel.right + style.gap,
            style.margin,
            round(win_size[0] * 0.2) - style.gap,
            win_size[1] - 2 * style.margin,
        )

        self.title: pg.Surface = style.font.heading.render(
            "Statistics", True, style.theme.primary_text
        )
        self.titleRect: pg.Rect = self.title.get_rect(
            left=self.panel_rect.left + style.pad, top=self.panel_rect.top + style.pad
        )

        # Labels
        self.labelCmp: pg.Surface = style.font.small.render(
            "Comparisons", True, style.theme.secondary_text
        )
        self.labelCmpRect: pg.Rect = self.labelCmp.get_rect(
            left=self.titleRect.left,
            top=self.titleRect.bottom + 2 * style.pad,
        )

        self.labelSwp: pg.Surface = style.font.small.render(
            "Swaps", True, style.theme.secondary_text
        )
        self.labelSwpRect: pg.Rect = self.labelSwp.get_rect(
            left=self.titleRect.left,
            top=self.labelCmpRect.bottom + style.gap,
        )

        self.labelWrt: pg.Surface = style.font.small.render(
            "Writes", True, style.theme.secondary_text
        )
        self.labelWrtRect: pg.Rect = self.labelWrt.get_rect(
            left=self.titleRect.left,
            top=self.labelSwpRect.bottom + style.gap,
        )

        # Values
        self.valCmp: pg.Surface = style.font.small.render(
            "0", True, style.theme.secondary_text
        )
        self.valCmpRect: pg.Rect = self.valCmp.get_rect(
            left=self.panel_rect.right - self.valCmp.get_width() - style.pad,
            top=self.labelCmpRect.top,
        )

        self.valSwp: pg.Surface = style.font.small.render(
            "0", True, style.theme.secondary_text
        )
        self.valSwpRect: pg.Rect = self.valSwp.get_rect(
            left=self.panel_rect.right - self.valSwp.get_width() - style.pad,
            top=self.labelSwpRect.top,
        )

        self.valWrt: pg.Surface = style.font.small.render(
            "0", True, style.theme.secondary_text
        )
        self.valWrtRect: pg.Rect = self.valWrt.get_rect(
            left=self.panel_rect.right - self.valWrt.get_width() - style.pad,
            top=self.labelWrtRect.top,
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

        _ = _surface.blit(self.title, self.titleRect)

        _ = _surface.blit(self.labelCmp, self.labelCmpRect)
        _ = _surface.blit(self.labelSwp, self.labelSwpRect)
        _ = _surface.blit(self.labelWrt, self.labelWrtRect)

        _ = _surface.blit(self.valCmp, self.valCmpRect)
        _ = _surface.blit(self.valSwp, self.valSwpRect)
        _ = _surface.blit(self.valWrt, self.valWrtRect)

    def update_stat(self, name: str, val: str) -> None:
        if name == "compare":
            self.valCmp = self.style.font.small.render(
                val, True, self.style.theme.secondary_text
            )
            self.valCmpRect = self.valCmp.get_rect(
                left=self.panel_rect.right - self.valCmp.get_width() - self.style.pad,
                top=self.labelCmpRect.top,
            )
        elif name == "swap":
            self.valSwp = self.style.font.small.render(
                val, True, self.style.theme.secondary_text
            )
            self.valSwpRect = self.valSwp.get_rect(
                left=self.panel_rect.right - self.valSwp.get_width() - self.style.pad,
                top=self.labelSwpRect.top,
            )
        elif name == "write":
            self.valWrt: pg.Surface = self.style.font.small.render(
                val, True, self.style.theme.secondary_text
            )
            self.valWrtRect: pg.Rect = self.valWrt.get_rect(
                left=self.panel_rect.right - self.valWrt.get_width() - self.style.pad,
                top=self.labelWrtRect.top,
            )
