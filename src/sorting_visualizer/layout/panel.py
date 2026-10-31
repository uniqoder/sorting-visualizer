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
