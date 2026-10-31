from random import randrange

from sorting_visualizer.event import Event, EventType

from . import algorithms as algs
from . import visualizer as viz

array: list[int] = []
sorting_func: str = "merge"
sorting: bool = False


def set_sorting() -> None:
    global sorting
    sorting = True


def main() -> None:
    global array

    viz.init()

    array = [randrange(1, 100) for _ in range(50)]
    viz.graphPanel.set_array(array)
    viz.graphPanel.set_algorithm_name(sorting_func.capitalize() + " Sort")
    viz.update()

    viz.optionsPanel.runButton.onClick = lambda: set_sorting()

    run_sorter()


def run_sorter() -> None:
    sort_events: list[Event] = []

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

            viz.graphPanel.handle_sort_event(ev)
