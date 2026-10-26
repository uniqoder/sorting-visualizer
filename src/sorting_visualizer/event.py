from enum import Enum
from typing import override


class EventType(Enum):
    COMPARE = 1  # To compare two values
    SWAP = 2  # Two swap values at two indices
    WRITE = 3  # To write a value at an index
    SET_KEY = 4  # To set the key (for Insertion Sort)
    SET_PIVOT = 5  # To set the pivot (for Quick Sort)
    SET_SWAP = 6  # To set the index of element to be swapped (in Selection Sort)
    DONE = 7  # To mark the end of the algorithm


class Event:
    def __init__(self, e_type: EventType, *args: int) -> None:
        self.type: EventType = e_type
        self.args: list[int] = list(args)

    @override
    def __repr__(self) -> str:
        return f"<Event: {self.type.name} {self.args}>"
