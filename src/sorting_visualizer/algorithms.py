from collections.abc import Callable

from .event import Event, EventType

Comparator = Callable[[int, int], bool]
ascending: Comparator = lambda a, b: a > b
descending: Comparator = lambda a, b: a < b


def bubble_sort(
    values: list[int],
    compare: Comparator = ascending,
    onOperation: Callable[[Event], None] | None = None,
) -> list[int]:
    lst: list[int] = values.copy()

    if not onOperation:
        onOperation = lambda e: None

    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            onOperation(Event(EventType.COMPARE, j, j + 1))
            if compare(lst[j], lst[j + 1]):
                onOperation(Event(EventType.SWAP, j, j + 1))
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    onOperation(Event(EventType.DONE))
    return lst


def selection_sort(
    values: list[int],
    compare: Comparator = ascending,
    onOperation: Callable[[Event], None] | None = None,
) -> list[int]:
    lst: list[int] = values.copy()

    if not onOperation:
        onOperation = lambda e: None

    for i in range(len(lst)):
        swp_i: int = i
        for j in range(i + 1, len(lst)):
            onOperation(Event(EventType.COMPARE, swp_i, j))
            if compare(lst[swp_i], lst[j]):
                onOperation(Event(EventType.SET_SWAP, j))
                swp_i = j

        onOperation(Event(EventType.SWAP, i, swp_i))
        lst[i], lst[swp_i] = lst[swp_i], lst[i]

    onOperation(Event(EventType.DONE))
    return lst
