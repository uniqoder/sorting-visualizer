from collections.abc import Callable
from types import FunctionType

from .event import Event, EventType

Comparator = Callable[[int, int], bool]
ascending: Comparator = lambda a, b: a > b
descending: Comparator = lambda a, b: a < b


def bubble_sort(
    values: list[int],
    compare: Comparator = ascending,
    onOperation: FunctionType | None = None,
) -> list[int]:
    lst: list[int] = values.copy()

    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            if onOperation:
                onOperation(Event(EventType.COMPARE, j, j + 1))
            if compare(lst[j], lst[j + 1]):
                if onOperation:
                    onOperation(Event(EventType.SWAP, j, j + 1))
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    if onOperation:
        onOperation(Event(EventType.DONE))

    return lst
