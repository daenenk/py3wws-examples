from py3wws.wrap import streamop, ProcessReturnValue, StreamOperator


@streamop(module='fizzbuzz')
def fizzbuzz(data: int) -> str:
    """Do the Fizz Buzz"""
    if data % 15 == 0:
        return "fizz buzz"
    elif data % 5 == 0:
        return "buzz"
    elif data % 3 == 0:
        return "fizz"
    else:
        return str(data)


class FizzBuzzMulti(StreamOperator):
    """Do the Fizz Buzz with outputs"""
    module = "fizzbuzz"
    output_ports = [("fizz", int), ("buzz", int), ("regular", int)]

    def process_data(self, data: int) -> ProcessReturnValue:
        if data % 15 == 0:
            yield "fizz", data
            yield "buzz", data
        elif data % 5 == 0:
            yield "buzz", data
        elif data % 3 == 0:
            yield "fizz", data
        else:
            yield "regular", data
