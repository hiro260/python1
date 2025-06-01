# type annotation
def add_nums1(num1: int, num2: int) -> int:
    return num1 + num2

print(add_nums1("1", "2"))


import pandas as pd
import numpy as np

series1 = pd.Series([1, 2.4, np.nan, None, "a"])
print(series1)
print("=======")
series1.dropna(inplace=True)
print("++++++++++")
print(series1)

