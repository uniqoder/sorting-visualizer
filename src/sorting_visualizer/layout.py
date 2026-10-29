from math import floor
from typing import override

import pygame as pg

from sorting_visualizer.event import Event, EventType
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
        self.array: list[int] = []

        self.comparing: tuple[int, int] = (-1, -1)
        self.swapping: tuple[int, int] = (-1, -1)
        self.pivot_idx: int = -1
        self.done: bool = False
        self.sorted_count: int = 0

        self.panel_rect: pg.Rect = pg.Rect(
            options_panel.right + style.gap,
            style.margin,
            round(win_size[0] * 0.6) - style.margin - style.gap,
            round(win_size[1] * 0.65) - style.margin,
        )

        self.bar_height: int = round(self.panel_rect.height * 0.7)
        self.bar_width: int = 10

        self.algorithm_name: pg.Surface = style.font.heading.render(
            "Select an Algorithm", True, style.theme.primary_text
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
            self.algorithm_name,
            (rect.left + 2 * self.style.pad, rect.top + 2 * self.style.pad),
        )

        # Print the bars
        if len(self.array) == 0:
            return

        max_val: int = max(self.array)
        start_x: int = self.panel_rect.left + 2 * self.style.pad
        for i, val in enumerate(self.array):
            color: str = self.style.theme.bar_default
            if not self.done:
                if i in self.comparing:
                    color = self.style.theme.bar_compare
                elif i in self.swapping:
                    color = self.style.theme.bar_swap
                if i == self.pivot_idx:
                    color = self.style.theme.bar_pivot
            if i < self.sorted_count:
                color = self.style.theme.bar_sorted

            val_height: int = floor(val / max_val * self.bar_height)
            bar: pg.Rect = pg.Rect(
                start_x + (self.bar_width + self.style.gap // 2) * i,
                self.panel_rect.bottom - val_height,
                self.bar_width,
                val_height,
            )
            _ = pg.draw.rect(
                _surface,
                color,
                bar,
                border_top_left_radius=self.style.border_radius // 4,
                border_top_right_radius=self.style.border_radius // 4,
            )

    @override
    def update(self) -> None:
        if self.done:
            self.sorted_count += 1

    def set_algorithm_name(self, name: str) -> None:
        self.algorithm_name = self.style.font.heading.render(
            name, True, self.style.theme.primary_text
        )

    def set_array(self, array: list[int]) -> None:
        self.array = array

        if len(array) == 0:
            return

        self.bar_width = (self.panel_rect.width - 2 * self.style.pad) // len(
            array
        ) - self.style.gap // 2

    def handle_event(self, event: Event) -> None:
        if event.type == EventType.COMPARE:
            self.comparing = (event.args[0], event.args[1])
        elif event.type == EventType.SWAP:
            self.swapping = (event.args[0], event.args[1])
        elif event.type == EventType.SET_PIVOT:
            self.pivot_idx = event.args[0]
        elif event.type == EventType.DONE:
            self.done = True


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
    options_panel = OptionsPanel(win_size, style)
    graph_panel = GraphPanel(win_size, style, options_panel.panel_rect)
    details_panel = DetailsPanel(win_size, style, graph_panel.panel_rect)
    stats_panel = StatsPanel(win_size, style, graph_panel.panel_rect)

    return {
        "options": options_panel,
        "graph": graph_panel,
        "details": details_panel,
        "stats": stats_panel,
    }
