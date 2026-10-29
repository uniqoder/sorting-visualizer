from typing import cast

import pygame as pg
from pygame.time import Clock

from .font import Font
from .layout import (
    DetailsPanel,
    GraphPanel,
    OptionsPanel,
    Panel,
    StatsPanel,
    Style,
    construct_layout,
)
from .theme import MIDNIGHT_INDIGO, Theme

WIN_SIZE = WIN_WIDTH, WIN_HEIGHT = 1280, 800
FPS = 60

screen: pg.Surface
clock: Clock
style: Style
optionsPanel: OptionsPanel
graphPanel: GraphPanel
detailsPanel: DetailsPanel
statsPanel: StatsPanel
events: list[str] = []


def init() -> None:
    global screen, clock, style, optionsPanel, graphPanel, detailsPanel, statsPanel

    _ = pg.init()
    pg.display.set_caption("Sorting Algorithm Visualizer")

    screen = pg.display.set_mode(WIN_SIZE)
    clock = Clock()

    style = Style(
        theme=Theme(MIDNIGHT_INDIGO),
        font=Font(),
        margin=12,
        gap=6,
        pad=16,
        border_width=2,
        border_radius=8,
    )

    panels: dict[str, Panel] = construct_layout(WIN_SIZE, style)
    optionsPanel = cast(OptionsPanel, panels.get("options"))
    graphPanel = cast(GraphPanel, panels.get("graph"))
    detailsPanel = cast(DetailsPanel, panels.get("details"))
    statsPanel = cast(StatsPanel, panels.get("stats"))


def update() -> None:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            events.append("quit")
            return

    # Update
    graphPanel.update()

    # Draw
    _ = screen.fill(style.theme.main_background)

    optionsPanel.draw(screen)
    graphPanel.draw(screen)
    detailsPanel.draw(screen)
    statsPanel.draw(screen)

    pg.display.flip()
    _ = clock.tick(FPS)
