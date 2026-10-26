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


merge_sort_depth: int = 0  # Counter to manage merge sort depth


def merge_sort(
    values: list[int],
    compare: Comparator = ascending,
    onOperation: Callable[[Event], None] | None = None,
) -> list[int]:
    global merge_sort_depth
    merge_sort_depth += 1

    if not onOperation:
        onOperation = lambda e: None

    if len(values) <= 1:
        return values

    def merge(a: list[int], b: list[int]) -> list[int]:
        out: list[int] = []
        a_i: int = 0
        b_i: int = 0

        while a_i < len(a) and b_i < len(b):
            onOperation(Event(EventType.COMPARE, a_i, b_i))
            if compare(a[a_i], b[b_i]):
                onOperation(Event(EventType.INSERT, b_i, a_i))
                out.append(b[b_i])
                b_i += 1
            else:
                onOperation(Event(EventType.INSERT, a_i, b_i))
                out.append(a[a_i])
                a_i += 1

        for i in range(a_i, len(a)):
            onOperation(Event(EventType.INSERT, i, i))
            out.append(a[i])
        for i in range(b_i, len(b)):
            onOperation(Event(EventType.INSERT, i, i))
            out.append(b[i])

        return out

    middle: int = len(values) // 2
    onOperation(Event(EventType.SPLIT, middle))

    left: list[int] = merge_sort(values[:middle], compare, onOperation)
    right: list[int] = merge_sort(values[middle:], compare, onOperation)

    onOperation(Event(EventType.MERGE))
    lst: list[int] = merge(left, right)

    merge_sort_depth -= 1

    if merge_sort_depth == 0:
        onOperation(Event(EventType.DONE))
    return lst
