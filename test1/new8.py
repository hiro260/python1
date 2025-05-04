import numpy as np
import pandas as pd

df =pd.DataFrame({
    'Wafer': ['W1', 'W1', 'W1', 'W2', 'W2', 'W2'],
    'colA': [1, 2, 3, 4, 5, 6],
    'colB': [11, 12, 13, 14, 15, 16],
    'colC': [21, 22, 23, 24, 25, 26],
})

stacked = pd.melt(df, id_vars=['Wafer'], value_vars=['colA', 'colB', 'colC'],
                  var_name='metrics', value_name='Meas1')

print(stacked)