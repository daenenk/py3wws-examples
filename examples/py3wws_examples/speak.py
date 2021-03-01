import asyncio
from typing import AsyncIterator, Optional, Any
from py3wws.wrap import StreamOperator, ProcessReturnValue, streamsrc


class Conversation(StreamOperator):
    """Mark a message with who said it."""
    input_ports = [('person1', str), ('person2', str)]
    output_ports = [('out', str)]
    module = "speak"

    def process_person1(self, data: str) -> ProcessReturnValue:
        yield 'out', 'Person 1 says:\n' + data

    def process_person2(self, data: str) -> ProcessReturnValue:
        yield 'out', 'Person 2 says:\n' + data


class Conversation2(StreamOperator):
    """Mark a message with who said it (alternative implementation)."""
    input_ports = [('person1', str), ('person2', str)]
    output_ports = [('out', str)]
    module = "speak"

    def process(self, data: str, port: Optional[str] = None) -> ProcessReturnValue:
        if port == 'person1':
            yield 'out', 'Person 1 says:\n' + data
        elif port == 'person2':
            yield 'out', 'Person 2 says:\n' + data
        else:
            raise ValueError("Who spoke?!")


class ConversationWithNames(StreamOperator):
    """Mark a message with who said it."""
    module = "speak"
    input_ports = [('person1', str), ('person2', str)]
    output_ports = [('out', str)]

    def __init__(self, name1: str, name2: str, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self.name1 = name1
        self.name2 = name2

    def process_person1(self, data: str) -> ProcessReturnValue:
        yield 'out', self.name1 + ' says:\n' + data

    def process_person2(self, data: str) -> ProcessReturnValue:
        yield 'out', self.name2 + ' says:\n' + data


@streamsrc(module='speak')
async def speak(filename: str, speed: float) -> AsyncIterator[str]:
    """Speak sentences from a file."""
    with open(filename) as f:
        for line in f.readlines():
            yield line.strip()
            await asyncio.sleep(speed)
