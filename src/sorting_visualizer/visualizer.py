import pygame as pg

from sorting_visualizer.layout import construct_layout

from . import theme

WIN_SIZE = WIN_WIDTH, WIN_HEIGHT = 1280, 800
FPS = 60


def run() -> None:
    _ = pg.init()
    pg.display.set_caption("Sorting Algorithm Visualizer")

    screen = pg.display.set_mode(WIN_SIZE)
    clock = pg.time.Clock()

    current_theme = theme.Theme()
    panels: dict[str, tuple[tuple[int, int], pg.Surface]] = construct_layout(
        WIN_SIZE, current_theme
    )
    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False

        # Update

        # Draw
        _ = screen.fill(current_theme.main_background)

        for panel in panels.values():
            _ = screen.blit(panel[1], panel[0])

        pg.display.flip()
        _ = clock.tick(FPS)

    pg.quit()
