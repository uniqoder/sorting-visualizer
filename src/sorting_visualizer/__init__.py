from collections.abc import Callable
from random import randrange, shuffle

from sorting_visualizer.event import Event, EventType

from . import algorithms as algs
from . import visualizer as viz

Sorter = Callable[
    [list[int], algs.Comparator, Callable[[Event], None] | None],
    list[int],
]
sorting_funcs: dict[str, Sorter] = {
    "bubble": algs.bubble_sort,
    "insertion": algs.insertion_sort,
    "selection": algs.selection_sort,
    "merge": algs.merge_sort,
    "quick": algs.quick_sort,
}

array: list[int] = []
selected_sorter: str = "merge"
sorting: bool = False
sort_events: list[Event] = []


def set_sorting() -> None:
    global sorting
    sorting = True
    set_algorithm(selected_sorter)
    sort_events.clear()

    if selected_sorter in sorting_funcs:
        _ = sorting_funcs[selected_sorter](
            array, algs.ascending, lambda e: sort_events.append(e)
        )


def set_algorithm(alg: str) -> None:
    global selected_sorter
    selected_sorter = alg.lower()
    viz.graphPanel.set_algorithm_name(alg.capitalize() + " Sort")


def set_size(size: int) -> None:
    global array, sorting
    array = [randrange(1, 100) for _ in range(size)]
    viz.graphPanel.set_array(array)
    sorting = False
    viz.graphPanel.reset()


def shuffle_array() -> None:
    viz.graphPanel.reset()
    shuffle(array)
    sort_events.clear()


def main() -> None:
    viz.init()

    viz.optionsPanel.runButton.onClick = lambda: set_sorting()
    viz.optionsPanel.shuffleButton.onClick = lambda: shuffle_array()
    viz.optionsPanel.algorithmDropdown.onClick = lambda alg: set_algorithm(alg)
    viz.optionsPanel.sizeDropdown.onClick = lambda size: set_size(int(size))

    viz.optionsPanel.algorithmDropdown.set_options(list(sorting_funcs.keys()))
    viz.optionsPanel.sizeDropdown.set_options(
        ["10", "20", "30", "40", "50", "60", "70"]
    )

    set_algorithm(viz.optionsPanel.algorithmDropdown.getOption())
    set_size(int(viz.optionsPanel.sizeDropdown.getOption()))
    run_sorter()


def run_sorter() -> None:
    running: int = 1

    while running:
        viz.update()

        for event in viz.events:
            if event == "quit":
                running = 0

        if not sorting:
            continue

        if len(sort_events) > 0:
            ev: Event = sort_events.pop(0)
            if ev.type == EventType.SWAP:
                i, j = ev.args
                array[i], array[j] = (
                    array[j],
                    array[i],
                )
            elif ev.type == EventType.INSERT:
                i, val = ev.args
                array[i] = val
            elif ev.type == EventType.WRITE:
                val, i = ev.args
                array[i] = val

            viz.graphPanel.handle_sort_event(ev)
