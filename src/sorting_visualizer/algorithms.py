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

    for i in range(len(lst) - 1):
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


def insertion_sort(
    values: list[int],
    compare: Comparator = ascending,
    onOperation: Callable[[Event], None] | None = None,
) -> list[int]:
    lst: list[int] = values.copy()

    if not onOperation:
        onOperation = lambda e: None

    for i in range(1, len(lst)):
        onOperation(Event(EventType.SET_KEY, i))
        key: int = lst[i]
        j: int = i - 1

        while j >= 0:
            onOperation(Event(EventType.COMPARE, j))
            if compare(lst[j], key):
                onOperation(Event(EventType.WRITE, lst[j], j + 1))
                lst[j + 1] = lst[j]
                j -= 1
            else:
                break

        onOperation(Event(EventType.WRITE))
        lst[j + 1] = key

    onOperation(Event(EventType.DONE))
    return lst


def merge_sort(
    values: list[int],
    compare: Comparator = ascending,
    onOperation: Callable[[Event], None] | None = None,
) -> list[int]:
    if not onOperation:
        onOperation = lambda e: None

    def merge(a: list[int], b: list[int]) -> list[int]:
        out: list[int] = []
        a, b = (a, b) if len(a) < len(b) else (b, a)

        for i in range(len(a)):
            if compare(a[i], b[i]):
                out.append(b[i])
            else:
                out.append(a[i])

        out.append(b[-1])
        return out

    middle: int = len(values) // 2
    lst = merge(
        merge_sort(values[:middle], compare, onOperation),
        merge_sort(values[middle:], compare, onOperation),
    )

    onOperation(Event(EventType.DONE))
    return lst
