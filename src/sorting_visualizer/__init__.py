from random import randrange

from sorting_visualizer.event import Event, EventType

from . import algorithms as algs
from . import visualizer as viz


def main() -> None:
    viz.init()

    sort_events: list[Event] = []
    array: list[int] = [randrange(1, 100) for _ in range(50)]
    viz.graphPanel.set_array(array)
    viz.update()

    _sorter = algs.merge_sort(array, onOperation=lambda e: sort_events.append(e))

    running: int = 1
    while running:
        viz.update()

        for event in viz.events:
            if event == "quit":
                running = 0

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

            viz.graphPanel.handle_event(ev)
