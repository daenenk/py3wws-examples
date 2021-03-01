import string
import py3wws
from py3wws.wrap import streamop, wws_start

# this annotation is needed register the function as operator
@streamop
def to_upper(data):
    return data.upper()

# Start the processor
wws_start()