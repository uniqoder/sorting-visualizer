import pygame as pg

from sorting_visualizer.font import Font
from sorting_visualizer.theme import Theme


def construct_layout(
    win_size: tuple[int, int], theme: Theme
) -> dict[str, tuple[tuple[int, int], pg.Surface]]:
    font: Font = Font()
    margin: int = 24
    gap: int = 16
    padd: int = 12

    options_pos, options_panel = construct_options_panel(
        win_size, theme, font, margin, padd
    )
    visual_pos, visual_panel = construct_visual_panel(
        win_size, theme, pg.Rect(*options_pos, *options_panel.get_size()), margin, gap
    )
    details_pos, details_panel = construct_details_panel(
        win_size, theme, pg.Rect(*visual_pos, *visual_panel.get_size()), margin, gap
    )
    stats_pos, stats_panel = construct_stats_panel(
        win_size, theme, pg.Rect(*visual_pos, *visual_panel.get_size()), margin, gap
    )

    return {
        "options": (options_pos, options_panel),
        "visual": (visual_pos, visual_panel),
        "details": (details_pos, details_panel),
        "stats": (stats_pos, stats_panel),
    }


def construct_options_panel(
    win_size: tuple[int, int], theme: Theme, font: Font, margin: int, padd: int
) -> tuple[tuple[int, int], pg.Surface]:
    options_pos: tuple[int, int] = (margin, margin)
    options_panel: pg.Surface = pg.Surface(
        (round(win_size[0] * 0.2) - margin, win_size[1] - 2 * margin)
    )

    title: pg.Surface = font.title.render("Visualizer", True, theme.primary_text)

    _ = options_panel.fill(theme.panel)
    _ = options_panel.blit(title, (options_pos[0] + padd, options_pos[1] + padd))

    return (options_pos, options_panel)


def construct_visual_panel(
    win_size: tuple[int, int],
    theme: Theme,
    options_pane: pg.Rect,
    margin: int,
    gap: int,
) -> tuple[tuple[int, int], pg.Surface]:
    visual_pos: tuple[int, int] = (
        options_pane.x + options_pane.width + gap,
        margin,
    )
    visual_panel: pg.Surface = pg.Surface(
        (
            round(win_size[0] * 0.6) - margin - gap,
            round(win_size[1] * 0.65) - margin,
        )
    )

    _ = visual_panel.fill(theme.panel)

    return (visual_pos, visual_panel)


def construct_details_panel(
    win_size: tuple[int, int], theme: Theme, visual_pane: pg.Rect, margin: int, gap: int
) -> tuple[tuple[int, int], pg.Surface]:
    details_pos: tuple[int, int] = (
        visual_pane.x,
        visual_pane.y + visual_pane.height + gap,
    )
    details_panel: pg.Surface = pg.Surface(
        (
            visual_pane.width,
            round(win_size[1] * 0.35) - margin - gap,
        )
    )

    _ = details_panel.fill(theme.panel)

    return (details_pos, details_panel)


def construct_stats_panel(
    win_size: tuple[int, int], theme: Theme, visual_pane: pg.Rect, margin: int, gap: int
) -> tuple[tuple[int, int], pg.Surface]:
    stats_pos: tuple[int, int] = (
        visual_pane.x + visual_pane.width + gap,
        margin,
    )
    stats_panel: pg.Surface = pg.Surface(
        (
            round(win_size[0] * 0.2) - gap,
            win_size[1] - 2 * margin,
        )
    )

    _ = stats_panel.fill(theme.panel)

    return (stats_pos, stats_panel)
