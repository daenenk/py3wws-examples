# Need to import all files that have operators in them.
from . import sources
from . import numbers
from . import time
from . import simple
from . import speak
from . import fizzbuzz

# This line doesn't do anything, except get rid of some Python warnings.
MODULES = [sources, numbers, time, simple, speak, fizzbuzz]
