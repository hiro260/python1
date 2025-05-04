from script2 import *
#from ./script3 import *

import sys
import os
# Add parent directory to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from script3 import *  # Now this works
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(sys.path)
print(__name__)

def function1(w, x, y, z):
    return w + x + y + z

def main():
    a = 10
    b = 3
    c = 8
    d = 5
    #result1 = function1(a, b, c, d)
    #print(result1)

    result2 = function2(a, b, c, d)
    print(result2)

    result3 = function3(a, b, c, d)
    print(result3)

    result4 = function4(a, b, c, d)
    print(result4)
    
    result5 = function5(a, b)
    print(result5)

    result6 = function6(a, b)
    print(result6)


if __name__ == "__main__":
    main()
