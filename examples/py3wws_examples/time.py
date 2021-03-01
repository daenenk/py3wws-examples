import time
import asyncio

from typing import TypeVar
from py3wws.wrap import streamop

T = TypeVar('T')


@streamop(module="time.bad", function_name='delay')
def delay_bad(data: T, delay: float) -> T:
    """Delay a message - don't use this one!"""
    time.sleep(delay)
    return data


@streamop(module="time")
async def delay(data: T, delay: float) -> T:
    """Delay a message - use this one!"""
    await asyncio.sleep(delay)
    return data


"""
Explanation:

'time.sleep' blocks the thread of the operator.
This means no other messages can be processed while it is sleeping.

When message arrive every second and we have a delay of 5 seconds,
this will lead to the following behaviour:

        arrives         processed       sent
0          A                A
1          B
2          C
3          D
4          E
5          F                B             A
6          G
7          H
8          I
9          J
10         K                C             B

This means that messages get an increasing delay and the message
queue grows.

'asyncio.sleep' does not block the thread of the operator.
Other messages can be processed asyncronously during the sleep.

        arrives         processed       sent
0          A                A
1          B                B
2          C                C
3          D                D
4          E                E
5          F                F             A
6          G                G             B
7          H                H             C
8          I                I             D
9          J                J             E
10         K                K             F

This means that each message is delayed by 5 seconds.

"""