from collections.abc import Callable

import pytest

from sorting_visualizer import algorithms as algs
from sorting_visualizer.event import Event, EventType

Algorithm = Callable[..., list[int]]

ALGORITHMS: list[Algorithm] = [
    algs.bubble_sort,
    algs.selection_sort,
    algs.insertion_sort,
    algs.merge_sort,
    algs.quick_sort,
]

ExpectedEvent = tuple[EventType, list[int]]
ExpectedEvents = list[ExpectedEvent]
EventCases = list[tuple[Algorithm, ExpectedEvents]]


def collect_events(
    algorithm: Algorithm,
    values: list[int],
    compare: algs.Comparator = algs.ascending,
) -> tuple[list[int], list[Event]]:
    events: list[Event] = []
    result: list[int] = algorithm(values, compare=compare, onOperation=events.append)
    return result, events


def replay_events(values: list[int], events: list[Event]) -> list[int]:
    array: list[int] = values.copy()
    key_index: int | None = None
    key_value: int | None = None
    last_write_index: int | None = None

    for event in events:
        if event.type == EventType.SWAP:
            i, j = event.args
            array[i], array[j] = array[j], array[i]
        elif event.type == EventType.INSERT:
            index, value = event.args
            array[index] = value
        elif event.type == EventType.SET_KEY:
            key_index = event.args[0]
            key_value = array[key_index]
            last_write_index = None
        elif event.type == EventType.WRITE and len(event.args) == 2:
            value, index = event.args
            array[index] = value
            last_write_index = index
        elif event.type == EventType.WRITE:
            assert key_index is not None
            assert key_value is not None
            index = key_index if last_write_index is None else last_write_index - 1
            array[index] = key_value

    return array


def assert_valid_event_indices(events: list[Event], size: int) -> None:
    for event in events:
        if event.type == EventType.COMPARE:
            assert event.args
            assert all(0 <= index < size for index in event.args)
        elif event.type == EventType.SWAP:
            assert len(event.args) == 2
            assert all(0 <= index < size for index in event.args)
        elif event.type in (
            EventType.SET_KEY,
            EventType.SET_PIVOT,
            EventType.SET_SWAP,
            EventType.SPLIT,
            EventType.MERGE,
        ):
            assert len(event.args) == 1
            assert 0 <= event.args[0] < size
        elif event.type == EventType.INSERT:
            assert len(event.args) == 2
            index, _ = event.args
            assert 0 <= index < size
        elif event.type == EventType.WRITE:
            assert len(event.args) in (0, 2)
            if len(event.args) == 2:
                _, index = event.args
                assert 0 <= index < size
        elif event.type == EventType.DONE:
            assert event.args == []


def assert_merge_events_are_balanced(events: list[Event]) -> None:
    splits: list[int] = []
    for event in events:
        if event.type == EventType.SPLIT:
            splits.append(event.args[0])
        elif event.type == EventType.MERGE:
            assert event.args[0] in splits
            splits.remove(event.args[0])

    assert splits == []


EXPECTED_EVENT_CASES: EventCases = [
    (
        algs.bubble_sort,
        [
            (EventType.COMPARE, [0, 1]),
            (EventType.SWAP, [0, 1]),
            (EventType.COMPARE, [1, 2]),
            (EventType.SWAP, [1, 2]),
            (EventType.COMPARE, [0, 1]),
            (EventType.DONE, []),
        ],
    ),
    (
        algs.selection_sort,
        [
            (EventType.COMPARE, [0, 1]),
            (EventType.SET_SWAP, [1]),
            (EventType.COMPARE, [1, 2]),
            (EventType.SWAP, [0, 1]),
            (EventType.COMPARE, [1, 2]),
            (EventType.SET_SWAP, [2]),
            (EventType.SWAP, [1, 2]),
            (EventType.DONE, []),
        ],
    ),
    (
        algs.insertion_sort,
        [
            (EventType.SET_KEY, [1]),
            (EventType.COMPARE, [0]),
            (EventType.WRITE, [3, 1]),
            (EventType.WRITE, []),
            (EventType.SET_KEY, [2]),
            (EventType.COMPARE, [1]),
            (EventType.WRITE, [3, 2]),
            (EventType.COMPARE, [0]),
            (EventType.WRITE, []),
            (EventType.DONE, []),
        ],
    ),
    (
        algs.merge_sort,
        [
            (EventType.SPLIT, [1]),
            (EventType.SPLIT, [2]),
            (EventType.MERGE, [2]),
            (EventType.COMPARE, [1, 2]),
            (EventType.INSERT, [1, 1]),
            (EventType.INSERT, [2, 2]),
            (EventType.MERGE, [1]),
            (EventType.COMPARE, [0, 1]),
            (EventType.INSERT, [0, 1]),
            (EventType.COMPARE, [0, 2]),
            (EventType.INSERT, [1, 2]),
            (EventType.INSERT, [2, 3]),
            (EventType.DONE, []),
        ],
    ),
    (
        algs.quick_sort,
        [
            (EventType.SET_PIVOT, [2]),
            (EventType.COMPARE, [2, 0]),
            (EventType.COMPARE, [2, 1]),
            (EventType.SWAP, [0, 1]),
            (EventType.SWAP, [1, 2]),
            (EventType.SET_PIVOT, [1]),
            (EventType.DONE, []),
        ],
    ),
]


@pytest.mark.parametrize(
    ("algorithm", "expected"),
    EXPECTED_EVENT_CASES,
    ids=["bubble", "selection", "insertion", "merge", "quick"],
)
def test_algorithm_emits_expected_events(
    algorithm: Algorithm,
    expected: ExpectedEvents,
) -> None:
    _, events = collect_events(algorithm, [3, 1, 2])

    assert [(event.type, event.args) for event in events] == expected


@pytest.mark.parametrize(
    "algorithm",
    ALGORITHMS,
    ids=["bubble", "selection", "insertion", "merge", "quick"],
)
@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([], []),
        ([42], [42]),
        ([1, 2, 3], [1, 2, 3]),
        ([7, 6, 5], [5, 6, 7]),
        ([-3, 1, -5, 0], [-5, -3, 0, 1]),
        ([3, 1, 3, 2, 1], [1, 1, 2, 3, 3]),
    ],
)
def test_events_replay_to_the_sorted_array(
    algorithm: Algorithm,
    values: list[int],
    expected: list[int],
) -> None:
    result, events = collect_events(algorithm, values)

    assert result == expected
    assert events[-1].type == EventType.DONE
    assert sum(event.type == EventType.DONE for event in events) == 1
    assert replay_events(values, events) == expected
    assert_valid_event_indices(events, len(values))

    if algorithm is algs.merge_sort:
        assert_merge_events_are_balanced(events)


@pytest.mark.parametrize(
    "algorithm",
    ALGORITHMS,
    ids=["bubble", "selection", "insertion", "merge", "quick"],
)
@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([], []),
        ([42], [42]),
        ([1, 2, 3], [3, 2, 1]),
        ([6, 6, 2, 5, 2, 4, 5], [6, 6, 5, 5, 4, 2, 2]),
    ],
)
def test_descending_events_replay_to_the_sorted_array(
    algorithm: Algorithm,
    values: list[int],
    expected: list[int],
) -> None:
    result, events = collect_events(algorithm, values, compare=algs.descending)

    assert result == expected
    assert events[-1].type == EventType.DONE
    assert sum(event.type == EventType.DONE for event in events) == 1
    assert replay_events(values, events) == expected
    assert_valid_event_indices(events, len(values))

    if algorithm is algs.merge_sort:
        assert_merge_events_are_balanced(events)
