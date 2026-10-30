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

    def merge(
        left: list[int], right: list[int], start_left: int = 0, start_right: int = 0
    ) -> list[int]:
        out: list[int] = []
        left_i: int = 0
        right_i: int = 0

        while left_i < len(left) and right_i < len(right):
            onOperation(
                Event(EventType.COMPARE, start_left + left_i, start_right + right_i)
            )
            if compare(left[left_i], right[right_i]):
                onOperation(
                    Event(EventType.INSERT, start_left + len(out), right[right_i])
                )
                out.append(right[right_i])
                right_i += 1
            else:
                onOperation(
                    Event(EventType.INSERT, start_left + len(out), left[left_i])
                )
                out.append(left[left_i])
                left_i += 1

        while left_i < len(left):
            onOperation(Event(EventType.INSERT, start_left + len(out), left[left_i]))
            out.append(left[left_i])
            left_i += 1

        while right_i < len(right):
            onOperation(Event(EventType.INSERT, start_left + len(out), right[right_i]))
            out.append(right[right_i])
            right_i += 1

        return out

    def sort_recursive(arr: list[int], start: int = 0) -> list[int]:
        if len(arr) <= 1:
            return arr

        middle: int = len(arr) // 2
        onOperation(Event(EventType.SPLIT, start + middle))

        left: list[int] = sort_recursive(arr[:middle], start=start)
        right: list[int] = sort_recursive(arr[middle:], start=start + middle)

        onOperation(Event(EventType.MERGE, start + middle))
        lst: list[int] = merge(
            left, right, start_left=start, start_right=start + middle
        )

        return lst

    lst: list[int] = sort_recursive(values)
    onOperation(Event(EventType.DONE))
    return lst


def quick_sort(
    values: list[int],
    compare: Comparator = ascending,
    onOperation: Callable[[Event], None] | None = None,
) -> list[int]:
    lst: list[int] = values.copy()

    if not onOperation:
        onOperation = lambda e: None

    def partition(arr: list[int], low: int, high: int) -> int:
        onOperation(Event(EventType.SET_PIVOT, high))
        pivot: int = arr[high]
        i: int = low - 1

        for j in range(low, high):
            onOperation(Event(EventType.COMPARE, high, j))
            if compare(pivot, arr[j]):
                i += 1
                onOperation(Event(EventType.SWAP, i, j))
                arr[i], arr[j] = arr[j], arr[i]

        onOperation(Event(EventType.SWAP, i + 1, high))
        arr[i + 1], arr[high] = arr[high], arr[i + 1]

        return i + 1

    def sort_recursive(arr: list[int], low: int, high: int) -> None:
        if low >= high:
            return

        pivot_idx: int = partition(arr, low, high)
        onOperation(Event(EventType.SET_PIVOT, pivot_idx))

        sort_recursive(arr, low, pivot_idx - 1)
        sort_recursive(arr, pivot_idx + 1, high)

    sort_recursive(lst, 0, len(lst) - 1)

    onOperation(Event(EventType.DONE))
    return lst
