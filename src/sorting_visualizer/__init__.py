from random import randrange

from sorting_visualizer.event import Event, EventType

from . import algorithms as algs
from . import visualizer as viz

array: list[int] = []
sorting_func: str = "merge"
sorting: bool = False
sort_events: list[Event] = []


def set_sorting() -> None:
    global sorting
    sorting = True
    set_algorithm(sorting_func)


def set_algorithm(alg: str) -> None:
    global sorting_func
    sorting_func = alg.lower()
    viz.graphPanel.set_algorithm_name(alg.capitalize() + " Sort")

    sort_events.clear()
    if sorting_func == "bubble":
        _ = algs.bubble_sort(array, onOperation=lambda e: sort_events.append(e))
    elif sorting_func == "insertion":
        _ = algs.insertion_sort(array, onOperation=lambda e: sort_events.append(e))
    elif sorting_func == "selection":
        _ = algs.selection_sort(array, onOperation=lambda e: sort_events.append(e))
    elif sorting_func == "merge":
        _ = algs.merge_sort(array, onOperation=lambda e: sort_events.append(e))
    else:
        _ = algs.quick_sort(array, onOperation=lambda e: sort_events.append(e))


def set_size(size: int) -> None:
    global array, sorting
    array = [randrange(1, 100) for _ in range(size)]
    viz.graphPanel.set_array(array)
    viz.graphPanel.done = False
    sorting = False
    viz.graphPanel.sorted_count = 0


def main() -> None:
    viz.init()

    viz.optionsPanel.runButton.onClick = lambda: set_sorting()
    viz.optionsPanel.algorithmDropdown.onClick = lambda alg: set_algorithm(alg)
    viz.optionsPanel.sizeDropdown.onClick = lambda size: set_size(int(size))

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
