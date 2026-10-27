import pygame as pg


def construct_layout(win_size: tuple[int, int]) -> dict[str, pg.Rect]:
    margin: int = 24
    gap: int = 16

    # Left menu panel
    options_panel: pg.Rect = pg.Rect(
        margin, margin, round(win_size[0] * 0.2) - margin, win_size[1] - 2 * margin
    )

    # Middle visualization
    visual_panel: pg.Rect = pg.Rect(
        options_panel.x + options_panel.width + gap,
        margin,
        round(win_size[0] * 0.6) - gap,
        round(win_size[1] * 0.8) - margin,
    )
    details_panel: pg.Rect = pg.Rect(
        visual_panel.x,
        visual_panel.y + visual_panel.height + gap,
        visual_panel.width,
        round(win_size[1] * 0.2) - margin - gap,
    )

    # Right stats
    stats_panel: pg.Rect = pg.Rect(
        visual_panel.x + visual_panel.width + gap,
        margin,
        round(win_size[0] * 0.2) - gap,
        win_size[1] - 2 * margin,
    )

    return {
        "options": options_panel,
        "visual": visual_panel,
        "details": details_panel,
        "stats": stats_panel,
    }
