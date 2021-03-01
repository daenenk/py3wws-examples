from py3wws.wrap.operator.istreamop import istreamop
from typing import TypeVar, Iterator
from py3wws.wrap import streamop

T = TypeVar('T')

@streamop(module="simple")
def identity(elem: T) -> T:
    """Just passed what comes in."""
    return elem


@istreamop(module="simple")
def successive(stream: Iterator[int]) -> Iterator[bool]:
    """Check whether this element is the successor of the previous."""
    last = -1
    for elem in stream:
        if elem == last + 1:
            yield True
        else:
            yield False
        last = elem
