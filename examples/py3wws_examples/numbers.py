from typing import Any, Optional
from py3wws.wrap import streamop
from py3wws.wrap.operator.streamop import ProcessReturnValue, StreamOperator

@streamop(module="numbers")
def plus_n(elem: float, n: float) -> float:
    """Adds <n> to the number."""
    return elem + n


@streamop(module="numbers")
def filter_even(elem: float) -> Optional[float]:
    """Filter out even numbers."""
    if elem % 2 != 0:
        return elem
    else:
        return None


class PlusX(StreamOperator):
    """Add <x> to the number, where <x> can be changed."""
    # We'll let the library discover input_ports automatically based on process_* methods
    output_ports = [('out', float)]
    module = "numbers"

    def __init__(self, x_initial: float, **kwargs: Any):
        # Pass on **kwargs to the parent.
        super().__init__(**kwargs)
        # Initialize internal state.
        self.x = x_initial

    # The default input port should be mentioned first.
    def process_data(self, elem: float) -> ProcessReturnValue:
        """Process the data."""
        yield 'out', elem + self.x

    def process_param(self, x: float) -> None:
        """Update the parameter."""
        self.x = x


@streamop(module="numbers", outputs=[('out0', int), ('out1', int)], multi=True)
def split_mod_2(data: int) -> ProcessReturnValue:
    if data % 2 == 0:
        yield 'out0', data
    else:
        yield 'out1', data
