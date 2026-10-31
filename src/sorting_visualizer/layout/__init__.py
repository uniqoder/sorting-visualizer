from .detailsPanel import DetailsPanel
from .graphPanel import GraphPanel
from .optionsPanel import OptionsPanel
from .panel import Panel, Style
from .statsPanel import StatsPanel


def construct_layout(win_size: tuple[int, int], style: Style) -> dict[str, Panel]:
    options_panel = OptionsPanel(win_size, style)
    graph_panel = GraphPanel(win_size, style, options_panel.panel_rect)
    details_panel = DetailsPanel(win_size, style, graph_panel.panel_rect)
    stats_panel = StatsPanel(win_size, style, graph_panel.panel_rect)

    return {
        "options": options_panel,
        "graph": graph_panel,
        "details": details_panel,
        "stats": stats_panel,
    }
