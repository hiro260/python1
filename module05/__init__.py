print("in __init__.py")

from ._module05 import hello as hello05
print("check")
from .module06 import hello as hello06

#quit()
__all__ = ['hello05', 'hello06']

# Do initialize something below
hello05(__file__)
hello06(__file__)