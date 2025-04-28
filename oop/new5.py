import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Wafer': ['W1', 'W1', 'W1', 'W2', 'W2', 'W2'],
    'Site': ['N1N1', 'N1N2', 'N1N3', 'N1N1', 'N1N2', 'N1N3'],
    'Frc': [0.0, 1.0, 2.0, 0.0, 1.0, 2.0],
    'Meas1': [6, 7, 9, 10, 11, 12],
    'Meas2': [1, 2, 3, 2, 2, 2],
    'Meas3': [7, 8, 9, 10, 9, 8],   

    })

print(df)
print(df.shape)
df.to_csv("EP1ME.csv")
