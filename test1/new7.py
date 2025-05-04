import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_combined = pd.read_csv('med.csv')
print(df_combined)

wafer_4_2_unique = df_combined['Wafer(4-2)'].unique()
number_parallel_unique = df_combined['Num_Parallel'].unique()
bias_unique = df_combined['bias'].unique()

print(wafer_4_2_unique)
print(number_parallel_unique)
print(bias_unique)

fig, axes = plt.subplots(len(number_parallel_unique), 2, figsize=(20, 20))

for j, bias in enumerate(bias_unique):
    for i, number_parallel in enumerate(number_parallel_unique):
        df_subset = df_combined[
            (df_combined['Num_Parallel'] == number_parallel) &
            (df_combined['bias'] == bias)
            ]
        for wafer in wafer_4_2_unique:
            df_wafer = df_subset[df_subset['Wafer(4-2)'] == wafer]
            axes[i, j].plot(df_wafer['Frc'], df_wafer['log10(normalized|Meas1|)(A/cell)'], label=f'Wafer {wafer}')
            axes[i, j].set_title('x' + str(number_parallel) + '-' +str(bias))
            axes[i, j].set_xlabel('Frc')
            axes[i, j].set_ylabel('log10(normalized|Meas1|)')
            axes[i, j].legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=8)

plt.tight_layout(pad=3)
plt.subplots_adjust(hspace=0.4, right=0.85)
plt.show()