from typing import override

import pygame as pg

from sorting_visualizer.font import Font
from sorting_visualizer.theme import Theme


class Style:
    def __init__(
        self,
        theme: Theme,
        font: Font,
        margin: int,
        gap: int,
        pad: int,
        border_width: int,
        border_radius: int,
    ) -> None:
        self.theme: Theme = theme
        self.font: Font = font
        self.margin: int = margin
        self.gap: int = gap
        self.pad: int = pad
        self.border_width: int = border_width
        self.border_radius: int = border_radius


class Panel:
    def __init__(self, win_size: tuple[int, int], style: Style) -> None:
        self.win_size: tuple[int, int] = win_size
        self.style: Style = style

    def draw(self, _surface: pg.Surface) -> None:
        raise NotImplementedError

    def update(self) -> None:
        raise NotImplementedError


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


class GraphPanel(Panel):
    def __init__(
        self, win_size: tuple[int, int], style: Style, options_panel: pg.Rect
    ) -> None:
        super().__init__(win_size, style)

        self.panel_rect: pg.Rect = pg.Rect(
            options_panel.right + style.gap,
            style.margin,
            round(win_size[0] * 0.6) - style.margin - style.gap,
            round(win_size[1] * 0.65) - style.margin,
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

    @override
    def update(self) -> None:
        return super().update()


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

    @override
    def update(self) -> None:
        return super().update()


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

    @override
    def update(self) -> None:
        return super().update()


def construct_layout(win_size: tuple[int, int], style: Style) -> dict[str, Panel]:
    options_panel: Panel = OptionsPanel(win_size, style)
    graph_panel: Panel = GraphPanel(win_size, style, options_panel.panel_rect)
    details_panel: Panel = DetailsPanel(win_size, style, graph_panel.panel_rect)
    stats_panel: Panel = StatsPanel(win_size, style, graph_panel.panel_rect)

    return {
        "options": options_panel,
        "graph": graph_panel,
        "details": details_panel,
        "stats": stats_panel,
    }
