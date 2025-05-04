from .. import script3
from . import script2


def function1(w, x, y, z):
    return w + x + y + z

def main():
    a = 10
    b = 3
    c = 8
    d = 5
    result1 = function1(a, b, c, d)
    print(result1)

    result2 = script2.function2(a, b, c, d)
    print(result2)

    result3 = script2.function3(a, b, c, d)
    print(result3)

    result4 = script3.function4(a, b, c, d)
    print(result4)
    
    result5 = script3.function5(a, b)
    print(result5)

    result6 = script3.function6(a, b)
    print(result6)


if __name__ == "__main__":
    main()
