from types import FunctionType

from .event import Event, EventType


def bubble_sort(
    values: list[int], ascending: bool = True, onOperation: FunctionType | None = None
) -> list[int]:
    lst: list[int] = values.copy()
    cmp = (lambda a, b: a > b) if ascending else (lambda a, b: a < b)

    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            if onOperation:
                onOperation(Event(EventType.COMPARE, j, j + 1))
            if cmp(lst[j], lst[j + 1]):
                if onOperation:
                    onOperation(Event(EventType.SWAP, j, j + 1))
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    if onOperation:
        onOperation(Event(EventType.DONE))

    return lst
