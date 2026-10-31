from enum import Enum

from pygame import Rect
from pygame.event import Event
from pygame.surface import Surface

from sorting_visualizer.font import Font


class Alignment(Enum):
    Left = 0
    Right = 1
    Center = 2


class Style:
    def __init__(
        self,
        font: Font,
        fg_color: str = "#FFFFFF",
        bg_color: str = "#FFFFFF",
        padding: int = 0,
        margin: int = 0,
        alignment: Alignment = Alignment.Center,
        border_width: int = 0,
        border_color: str = "#303030",
        border_radius: int = 0,
    ):
        self.font: Font = font
        self.fg_color: str = fg_color
        self.bg_color: str = bg_color
        self.padding: int = padding
        self.margin: int = margin
        self.alignment: Alignment = alignment
        self.border_width: int = border_width
        self.border_color: str = border_color
        self.border_radius: int = border_radius


class UI:
    def __init__(self, rect: Rect, style: Style) -> None:
        self.rect: Rect = rect
        self.style: Style = style

    def draw(self, _surface: Surface) -> None:
        raise NotImplementedError

    def handle_event(self, _event: Event) -> None:
        raise NotImplementedError
