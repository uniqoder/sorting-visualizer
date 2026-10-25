def bubble_sort(values: list[int], ascending: bool = True) -> list[int]:
    lst: list[int] = values.copy()
    cmp = (lambda a, b: a > b) if ascending else (lambda a, b: a < b)

    for i in range(len(lst)):
        for j in range(len(lst) - i - 1):
            if cmp(lst[j], lst[j + 1]):
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst
