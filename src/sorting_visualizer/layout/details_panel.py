from typing import override

import pygame as pg
from pygame.font import Font

from sorting_visualizer.theme import Theme

from .panel import Panel, Style


class DetailsPanel(Panel):
    def __init__(
        self, win_size: tuple[int, int], style: Style, graph_panel: pg.Rect
    ) -> None:
        super().__init__(win_size, style)

        self.panel_rect: pg.Rect = pg.Rect(
            graph_panel.x,
            graph_panel.bottom + style.gap,
            graph_panel.width,
            round(win_size[1] * 0.35) - style.margin - style.gap,
        )

        # Algorithm description
        self.descHeading: pg.Surface = style.font.heading.render(
            "Description", True, style.theme.primary_text
        )
        self.descHeadingRect: pg.Rect = self.descHeading.get_rect(
            left=self.panel_rect.left + style.pad,
            top=self.panel_rect.top + style.pad,
        )

        self.description: str
        self.descTexts: list[pg.Surface] = []
        self.descTextRect: pg.Rect = pg.Rect(
            self.panel_rect.left + 2 * style.pad,
            self.panel_rect.top + round(2.5 * style.pad),
            self.panel_rect.width - 4 * style.pad,
            0,
        )

        # Time complexity
        self.timeHeading: pg.Surface = style.font.heading.render(
            "Time", True, style.theme.primary_text
        )
        self.timeHeadingRect: pg.Rect = self.timeHeading.get_rect(
            left=self.panel_rect.left + style.pad,
            top=self.panel_rect.bottom - 4 * style.pad,
        )

        self.labelBest: pg.Surface = style.font.label.render(
            "Best:", True, style.theme.primary_text
        )
        self.labelBestRect: pg.Rect = self.labelBest.get_rect(
            left=self.panel_rect.left + 2 * style.pad,
            top=self.panel_rect.bottom - 2 * style.pad,
        )
        self.timeBestTxt: str
        self.timeBest: pg.Surface
        self.timeBestPos: list[int] = [0, self.labelBestRect.y]

        self.labelAvg: pg.Surface = style.font.label.render(
            "Average:", True, style.theme.primary_text
        )
        self.labelAvgRect: pg.Rect = self.labelAvg.get_rect(
            left=self.labelBestRect.right + style.gap,
            top=self.panel_rect.bottom - 2 * style.pad,
        )
        self.timeAvgTxt: str
        self.timeAvg: pg.Surface
        self.timeAvgPos: list[int] = [0, self.labelAvgRect.y]

        self.labelWorst: pg.Surface = style.font.label.render(
            "Worst:", True, style.theme.primary_text
        )
        self.labelWorstRect: pg.Rect = self.labelWorst.get_rect(
            left=self.labelAvgRect.right + style.gap,
            top=self.panel_rect.bottom - 2 * style.pad,
        )
        self.timeWorstTxt: str
        self.timeWorst: pg.Surface
        self.timeWorstPos: list[int] = [0, self.labelWorstRect.y]

        # Space complexity
        self.spaceHeading: pg.Surface = style.font.heading.render(
            "Space", True, style.theme.primary_text
        )
        self.spaceHeadingRect: pg.Rect = self.spaceHeading.get_rect(
            left=self.panel_rect.right - style.pad,
            top=self.panel_rect.bottom - 4 * style.pad,
        )
        self.spaceHeadingRect.x -= self.spaceHeadingRect.width

        self.spaceComplexityTxt: str
        self.spaceComplexity: pg.Surface
        self.spacePos: list[int] = [
            0,
            self.panel_rect.bottom - 2 * style.pad,
        ]

    def set_details(self, description: str, time: dict[str, str], space: str):
        self.description = description
        self.timeBestTxt = time.get("best", "")
        self.timeAvgTxt = time.get("avg", "")
        self.timeWorstTxt = time.get("worst", "")
        self.spaceComplexityTxt = space

        self.render_texts()

        # Time complexities
        self.timeBestPos[0] = self.labelBestRect.right + self.style.pad

        self.labelAvgRect.x = (
            self.timeBestPos[0] + self.timeBest.get_width() + self.style.pad
        )
        self.timeAvgPos[0] = self.labelAvgRect.right + self.style.pad

        self.labelWorstRect.x = (
            self.timeAvgPos[0] + self.timeAvg.get_width() + self.style.pad
        )
        self.timeWorstPos[0] = self.labelWorstRect.right + self.style.pad

        # Space complexity
        self.spacePos[0] = (
            self.spaceHeadingRect.centerx - self.spaceComplexity.get_width() // 2
        )

    @override
    def draw(self, _surface: pg.Surface) -> None:
        bw: int = self.style.border_width // 2
        rect: pg.Rect = pg.Rect(
            self.panel_rect.x + bw,
            self.panel_rect.y + bw,
            self.panel_rect.width,
            self.panel_rect.height,
        )
        _ = pg.draw.rect(
            _surface,
            self.style.theme.panel,
            rect,
            border_radius=self.style.border_radius,
        )
        _ = pg.draw.rect(
            _surface,
            self.style.theme.border,
            rect,
            border_radius=self.style.border_radius,
            width=self.style.border_width,
        )

        _ = _surface.blit(self.descHeading, self.descHeadingRect)
        _ = _surface.blit(self.timeHeading, self.timeHeadingRect)
        _ = _surface.blit(self.spaceHeading, self.spaceHeadingRect)

        _ = _surface.blit(self.labelBest, self.labelBestRect)
        _ = _surface.blit(self.labelAvg, self.labelAvgRect)
        _ = _surface.blit(self.labelWorst, self.labelWorstRect)

        _ = _surface.blit(self.timeBest, self.timeBestPos)
        _ = _surface.blit(self.timeAvg, self.timeAvgPos)
        _ = _surface.blit(self.timeWorst, self.timeWorstPos)
        _ = _surface.blit(self.spaceComplexity, self.spacePos)

        y = self.descTextRect.y
        line_size: int = self.style.font.small.get_linesize()
        line_spacing: int = 2
        for line in self.descTexts:
            _ = _surface.blit(line, (self.descTextRect.x, y))
            y += line_size + line_spacing

    @override
    def set_theme(self, theme: Theme) -> None:
        super().set_theme(theme)

        self.descHeading = self.style.font.heading.render(
            "Description", True, self.style.theme.primary_text
        )
        self.timeHeading = self.style.font.heading.render(
            "Time", True, self.style.theme.primary_text
        )
        self.labelBest = self.style.font.label.render(
            "Best:", True, self.style.theme.primary_text
        )
        self.labelAvg = self.style.font.label.render(
            "Average:", True, self.style.theme.primary_text
        )
        self.labelWorst = self.style.font.label.render(
            "Worst:", True, self.style.theme.primary_text
        )
        self.spaceHeading = self.style.font.heading.render(
            "Space", True, self.style.theme.primary_text
        )

        self.render_texts()

    def render_texts(self) -> None:
        self.descTexts.clear()

        for line in wrap_text(
            self.description, self.style.font.small, self.descTextRect.width
        ):
            self.descTexts.append(
                self.style.font.small.render(
                    line, True, self.style.theme.secondary_text
                )
            )

        # Time complexities
        self.timeBest = self.style.font.small.render(
            self.timeBestTxt, True, self.style.theme.secondary_text
        )
        self.timeAvg = self.style.font.small.render(
            self.timeAvgTxt, True, self.style.theme.secondary_text
        )
        self.timeWorst = self.style.font.small.render(
            self.timeWorstTxt, True, self.style.theme.secondary_text
        )

        self.spaceComplexity = self.style.font.small.render(
            self.spaceComplexityTxt, True, self.style.theme.secondary_text
        )


def wrap_text(text: str, font: Font, max_width: int) -> list[str]:
    words: list[str] = text.split()
    lines: list[str] = []
    current_line: str = ""

    for word in words:
        test_line: str = f"{current_line} {word}".strip()

        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            if current_line:
                lines.append(current_line)
            current_line = word

    if current_line:
        lines.append(current_line)

    return lines
