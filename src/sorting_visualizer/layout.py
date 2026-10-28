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


def construct_layout(
    win_size: tuple[int, int], theme: Theme
) -> dict[str, tuple[tuple[int, int], pg.Surface]]:
    style: Style = Style(
        theme=theme,
        font=Font(),
        margin=12,
        gap=6,
        pad=4,
        border_width=2,
        border_radius=8,
    )

    options_pos, options_panel = construct_options_panel(win_size, style)
    visual_pos, visual_panel = construct_visual_panel(
        win_size,
        style,
        pg.Rect(*options_pos, *options_panel.get_size()),
    )
    details_pos, details_panel = construct_details_panel(
        win_size,
        style,
        pg.Rect(*visual_pos, *visual_panel.get_size()),
    )
    stats_pos, stats_panel = construct_stats_panel(
        win_size,
        style,
        pg.Rect(*visual_pos, *visual_panel.get_size()),
    )

    return {
        "options": (options_pos, options_panel),
        "visual": (visual_pos, visual_panel),
        "details": (details_pos, details_panel),
        "stats": (stats_pos, stats_panel),
    }


def construct_options_panel(
    win_size: tuple[int, int], style: Style
) -> tuple[tuple[int, int], pg.Surface]:
    bw: int = style.border_width // 2
    pos: tuple[int, int] = (style.margin, style.margin)
    panel: pg.Surface = pg.Surface(
        (round(win_size[0] * 0.2) - style.margin, win_size[1] - 2 * style.margin),
        pg.SRCALPHA,
    )

    title: pg.Surface = style.font.title.render(
        "Visualizer", True, style.theme.primary_text
    )

    surf_rect: pg.Rect = pg.Rect(
        bw, bw, panel.get_width() - bw, panel.get_height() - bw
    )
    _ = pg.draw.rect(
        panel, style.theme.panel, surf_rect, border_radius=style.border_radius
    )
    _ = pg.draw.rect(
        panel,
        style.theme.border,
        surf_rect,
        border_radius=style.border_radius,
        width=style.border_width,
    )

    _ = panel.blit(title, (pos[0] + style.pad, pos[1] + style.pad))

    return (pos, panel)


def construct_visual_panel(
    win_size: tuple[int, int],
    style: Style,
    options_pane: pg.Rect,
) -> tuple[tuple[int, int], pg.Surface]:
    bw: int = style.border_width // 2
    pos: tuple[int, int] = (
        options_pane.x + options_pane.width + style.gap,
        style.margin,
    )
    panel: pg.Surface = pg.Surface(
        (
            round(win_size[0] * 0.6) - style.margin - style.gap,
            round(win_size[1] * 0.65) - style.margin,
        ),
        pg.SRCALPHA,
    )

    surf_rect: pg.Rect = pg.Rect(
        bw, bw, panel.get_width() - bw, panel.get_height() - bw
    )
    _ = pg.draw.rect(
        panel, style.theme.panel, surf_rect, border_radius=style.border_radius
    )
    _ = pg.draw.rect(
        panel,
        style.theme.border,
        surf_rect,
        border_radius=style.border_radius,
        width=style.border_width,
    )

    return (pos, panel)


def construct_details_panel(
    win_size: tuple[int, int],
    style: Style,
    visual_pane: pg.Rect,
) -> tuple[tuple[int, int], pg.Surface]:
    bw: int = style.border_width // 2
    pos: tuple[int, int] = (
        visual_pane.x,
        visual_pane.y + visual_pane.height + style.gap,
    )
    panel: pg.Surface = pg.Surface(
        (
            visual_pane.width,
            round(win_size[1] * 0.35) - style.margin - style.gap,
        ),
        pg.SRCALPHA,
    )

    surf_rect: pg.Rect = pg.Rect(
        bw, bw, panel.get_width() - bw, panel.get_height() - bw
    )
    _ = pg.draw.rect(
        panel, style.theme.panel, surf_rect, border_radius=style.border_radius
    )
    _ = pg.draw.rect(
        panel,
        style.theme.border,
        surf_rect,
        border_radius=style.border_radius,
        width=style.border_width,
    )

    return (pos, panel)


def construct_stats_panel(
    win_size: tuple[int, int],
    style: Style,
    visual_pane: pg.Rect,
) -> tuple[tuple[int, int], pg.Surface]:
    bw: int = style.border_width // 2
    pos: tuple[int, int] = (
        visual_pane.x + visual_pane.width + style.gap,
        style.margin,
    )
    panel: pg.Surface = pg.Surface(
        (
            round(win_size[0] * 0.2) - style.gap,
            win_size[1] - 2 * style.margin,
        ),
        pg.SRCALPHA,
    )

    surf_rect: pg.Rect = pg.Rect(
        bw, bw, panel.get_width() - bw, panel.get_height() - bw
    )
    _ = pg.draw.rect(
        panel, style.theme.panel, surf_rect, border_radius=style.border_radius
    )
    _ = pg.draw.rect(
        panel,
        style.theme.border,
        surf_rect,
        border_radius=style.border_radius,
        width=style.border_width,
    )

    return (pos, panel)
