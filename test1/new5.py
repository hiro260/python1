import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

print(os.getcwd())

# df = pd.DataFrame({
#     'Lot': ['999999.003' for i in range(6)],
#     'Wafer': ['W1', 'W1', 'W1', 'W2', 'W2', 'W2'],
#     'Site': ['N1N1', 'N1N2', 'N1N3', 'N1N1', 'N1N2', 'N1N3'],
#     'Frc': [0.0, 1.0, 2.0, 0.0, 1.0, 2.0],
#     'Meas1': [6, 7, 9, 10, 11, 12],
#     'Meas2': [1, 2, 3, 2, 2, 2],
#     'Meas3': [7, 8, 9, 10, 9, 8],   

#     })



#load file to df
load_file = "EP1ME"
df = pd.read_csv(load_file + '.csv')
print(df)
print(df.shape)
#df.to_csv("EP1ME.csv", index=False)
#plt.figure()
#plot
#ax = df.plot(x="Frc", y="Meas1", kind="line", label='Meas1')
#df.plot(x="Frc", y="Meas2", ax=ax, kind="line", label='Meas2')
#df.plot(x="Frc", y="Meas3", ax=ax, kind="line", label='Meas3')
#df.plot(x="Frc", y=["Meas1","Meas2","Meas3"],  kind="line", style=["-r", "--g", ":b"], figsize=(10, 6))
#plt.savefig('Meas.png')
#plt.show()

#plot site split
#plt.figure()
wafer_unique = df['Wafer'].unique()
site_unique = df['Site'].unique()
print(wafer_unique)
print(site_unique)
print(type(wafer_unique))
print(type(site_unique))
fig, ax = plt.subplots()
#plt.figure()
for wafer in wafer_unique:
    for site in site_unique:
        plot_data = df[(df['Wafer'] == wafer) & (df['Site'] == site)]
        #plt.plot(plot_data['Frc'], plot_data['Meas1', 'Meas2', 'Meas3'], label=wafer, linestyle='-', color='r')
        plot_data.plot(x='Frc', y=['Meas1', 'Meas2', 'Meas3'], kind="line", ax=ax, figsize=(10, 6), style=["-r", "--g", ":b"])
#ax.legend()
ax.legend(loc='upper left', bbox_to_anchor=(1, 1), title='Legend')
plt.savefig('MeasB.png')
plt.show()

quit()
plt.figure()
site1_data = df[(df['Wafer'] == 'W1') & (df['Site'] == 'N1N1')]
site2_data = df[df['Site'] == 'N1N2']
site3_data = df[df['Site'] == 'N1N3']
plt.plot(site1_data['Frc'], site1_data['Meas1'], label="site1 Meas1", linestyle='-', color='r')

plt.show()



quit()
list_group = ['Wafer', 'Frc']
list_meas = ['Meas1', 'Meas2', 'Meas3']
df_med = df.groupby(list_group).median(list_meas)
print(df_med)

df_med.to_csv(load_file + '_med.csv', index=True)
