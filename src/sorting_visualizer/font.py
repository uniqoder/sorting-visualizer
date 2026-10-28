from pathlib import Path

import pygame as pg

PROJECT_ROOT: Path = Path(__file__).resolve().parents[2]
FONT_DIR: Path = PROJECT_ROOT / "assets" / "fonts"

VALONIK_BOLD: Path = FONT_DIR / "valonik-valonik-bold-700.otf"
VALONIK_BOLD_SLANTED: Path = FONT_DIR / "valonik-valonik-bold-slanted-700.otf"
INTER_MEDIUM: Path = FONT_DIR / "Inter-Medium.otf"

if not VALONIK_BOLD.is_file():
    print(VALONIK_BOLD, "is not a file.")
if not VALONIK_BOLD_SLANTED.is_file():
    print(VALONIK_BOLD_SLANTED, "is not a file.")
if not INTER_MEDIUM.is_file():
    print(INTER_MEDIUM, "is not a file.")


class Font:
    def __init__(self) -> None:
        self.title: pg.font.Font = pg.font.Font(VALONIK_BOLD_SLANTED, 24)
        self.heading: pg.font.Font = pg.font.Font(VALONIK_BOLD, 18)
        self.label: pg.font.Font = pg.font.Font(INTER_MEDIUM, 16)
        self.small: pg.font.Font = pg.font.Font(INTER_MEDIUM, 14)
        self.index: pg.font.Font = pg.font.Font(INTER_MEDIUM, 12)
