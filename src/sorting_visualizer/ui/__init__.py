from enum import Enum
from gc import disable

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
        fg_color: str = "#000000",
        bg_color: str = "#999999",
        padding: int = 0,
        margin: int = 0,
        alignment: Alignment = Alignment.Center,
        border_width: int = 0,
        border_color: str = "#303030",
        border_radius: int = 0,
        hover_color: str = "#A1A1A1",
        active_color: str = "#FFFFFF",
        disabled_color: str = "#454545",
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
        self.hover_color: str = hover_color
        self.active_color: str = active_color
        self.disabled_color: str = disabled_color


class UI:
    def __init__(self, rect: Rect, style: Style) -> None:
        self.rect: Rect = rect
        self.style: Style = style

    def draw(self, _surface: Surface) -> None:
        raise NotImplementedError

    def handle_event(self, _event: Event) -> None:
        raise NotImplementedError
