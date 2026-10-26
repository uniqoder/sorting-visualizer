import pytest

from sorting_visualizer import algorithms as algs


@pytest.mark.parametrize(("values", "expected"), [([], [])])
def test_empty_lists(values: list[int], expected: list[int]) -> None:
    result: list[int] = algs.bubble_sort(values)
    assert result == expected

    result = algs.selection_sort(values)
    assert result == expected

    result = algs.insertion_sort(values)
    assert result == expected

    result = algs.merge_sort(values)
    assert result == expected

    result = algs.quick_sort(values)
    assert result == expected


@pytest.mark.parametrize(("values", "expected"), [([42], [42]), ([0], [0])])
def test_single_element(values: list[int], expected: list[int]) -> None:
    result: list[int] = algs.bubble_sort(values)
    assert result == expected

    result = algs.selection_sort(values)
    assert result == expected

    result = algs.insertion_sort(values)
    assert result == expected

    result = algs.merge_sort(values)
    assert result == expected

    result = algs.quick_sort(values)
    assert result == expected


@pytest.mark.parametrize(
    ("values", "expected"),
    [([1, 2, 3], [1, 2, 3]), ([5, 6], [5, 6]), ([99, 100, 101], [99, 100, 101])],
)
def test_alread_sorted(values: list[int], expected: list[int]) -> None:
    result: list[int] = algs.bubble_sort(values)
    assert result == expected

    result = algs.selection_sort(values)
    assert result == expected

    result = algs.insertion_sort(values)
    assert result == expected

    result = algs.merge_sort(values)
    assert result == expected

    result = algs.quick_sort(values)
    assert result == expected


@pytest.mark.parametrize(
    ("values", "expected"),
    [([7, 6, 5], [5, 6, 7]), ([3, 1, 0], [0, 1, 3]), ([43, 13], [13, 43])],
)
def test_reverse_sorted(values: list[int], expected: list[int]) -> None:
    result: list[int] = algs.bubble_sort(values)
    assert result == expected

    result = algs.selection_sort(values)
    assert result == expected

    result = algs.insertion_sort(values)
    assert result == expected

    result = algs.merge_sort(values)
    assert result == expected

    result = algs.quick_sort(values)
    assert result == expected


@pytest.mark.parametrize(
    ("values", "expected"),
    [([-3, 1, -5, 0], [-5, -3, 0, 1]), ([-2, -1, -5, 99], [-5, -2, -1, 99])],
)
def test_negative_values(values: list[int], expected: list[int]) -> None:
    result: list[int] = algs.bubble_sort(values)
    assert result == expected

    result = algs.selection_sort(values)
    assert result == expected

    result = algs.insertion_sort(values)
    assert result == expected

    result = algs.merge_sort(values)
    assert result == expected

    result = algs.quick_sort(values)
    assert result == expected


@pytest.mark.parametrize(
    ("values", "expected"),
    [([3, 1, 3, 2, 1], [1, 1, 2, 3, 3]), ([1, 1, 1, 1], [1, 1, 1, 1])],
)
def test_duplicate_elements(values: list[int], expected: list[int]) -> None:
    result: list[int] = algs.bubble_sort(values)
    assert result == expected

    result = algs.selection_sort(values)
    assert result == expected

    result = algs.insertion_sort(values)
    assert result == expected

    result = algs.merge_sort(values)
    assert result == expected

    result = algs.quick_sort(values)
    assert result == expected


@pytest.mark.parametrize(
    ("values", "expected"),
    [([3, 1, 3, 2, 1], [1, 1, 2, 3, 3]), ([1, 1, 1, 1], [1, 1, 1, 1])],
)
def test_non_mutative(values: list[int], expected: list[int]) -> None:
    org: list[int] = values.copy()

    result: list[int] = algs.bubble_sort(values)
    assert result == expected
    assert values == org

    result = algs.selection_sort(values)
    assert result == expected
    assert values == org

    result = algs.insertion_sort(values)
    assert result == expected
    assert values == org

    result = algs.merge_sort(values)
    assert result == expected
    assert values == org

    result = algs.quick_sort(values)
    assert result == expected
    assert values == org


@pytest.mark.parametrize(
    ("values", "expected"),
    [
        ([-7, -100, -9, 100, 9], [100, 9, -7, -9, -100]),
        ([1, 2, 3], [3, 2, 1]),
        ([], []),
        ([23], [23]),
        ([6, 6, 2, 5, 2, 4, 5], [6, 6, 5, 5, 4, 2, 2]),
    ],
)
def test_descending_sort(values: list[int], expected: list[int]) -> None:
    result: list[int] = algs.bubble_sort(values, compare=algs.descending)
    assert result == expected

    result = algs.selection_sort(values, compare=algs.descending)
    assert result == expected

    result = algs.insertion_sort(values, compare=algs.descending)
    assert result == expected

    result = algs.merge_sort(values, compare=algs.descending)
    assert result == expected

    result = algs.quick_sort(values, compare=algs.descending)
    assert result == expected
