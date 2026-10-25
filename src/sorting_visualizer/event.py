from enum import Enum
from typing import override


class EventType(Enum):
    COMPARE = 1
    SWAP = 2
    DONE = 3


class Event:
    def __init__(self, e_type: EventType, *args: int) -> None:
        self.type: EventType = e_type
        self.args: list[int] = list(args)

    @override
    def __repr__(self) -> str:
        return f"<Event: {self.type.name} {self.args}>"
