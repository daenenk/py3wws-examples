import time
from typing import Iterator

from py3wws.wrap import streamsrc

@streamsrc(module="time")
def clock(seconds: float) -> Iterator[float]:
    """Tick-tock"""
    n = 0
    while True:
        time.sleep(seconds)
        n = n + 1
        yield n
