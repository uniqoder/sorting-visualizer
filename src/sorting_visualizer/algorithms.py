def bubble_sort(values: list[int], ascending: bool = True) -> None:
    cmp = (lambda a, b: a > b) if ascending else (lambda a, b: a < b)

    for i in range(len(values)):
        for j in range(len(values) - i - 1):
            if cmp(values[j], values[j + 1]):
                values[j], values[j + 1] = values[j + 1], values[j]
