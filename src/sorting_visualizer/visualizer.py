import pygame as pg

from sorting_visualizer.font import Font
from sorting_visualizer.layout import Panel, Style, construct_layout

from . import theme

WIN_SIZE = WIN_WIDTH, WIN_HEIGHT = 1280, 800
FPS = 60


def run() -> None:
    _ = pg.init()
    pg.display.set_caption("Sorting Algorithm Visualizer")

    screen: pg.Surface = pg.display.set_mode(WIN_SIZE)
    clock = pg.time.Clock()

    style: Style = Style(
        theme=theme.Theme(),
        font=Font(),
        margin=12,
        gap=6,
        pad=8,
        border_width=2,
        border_radius=8,
    )
    panels: dict[str, Panel] = construct_layout(WIN_SIZE, style)

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # Update

        # Draw
        _ = screen.fill(style.theme.main_background)

        for panel in panels.values():
            panel.draw(screen)

        pg.display.flip()
        _ = clock.tick(FPS)

    pg.quit()
