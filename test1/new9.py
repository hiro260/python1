import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# df = pd.DataFrame({
#     'category': ['A', 'A', 'B', 'B', 'C', 'C'] * 2,
#     'group': ['G1']*6 + ['G2']*6,
#     'value': [10, 12, 14, 15, 9, 8, 11, 13, 16, 14, 10, 9]
# })

np.random.seed(42)

# Categories and groups
categories = ['A', 'B', 'C', 'D']
groups = ['G1', 'G2']

# Generate data
data = []
for cat in categories:
    for grp in groups:
        # 30 samples per (category, group)
        values = np.random.normal(loc=10 + categories.index(cat)*2 + groups.index(grp), scale=2, size=30)
        for v in values:
            data.append({'category': cat, 'group': grp, 'value': v})

# Create DataFrame
df = pd.DataFrame(data)

# Create vertical subplots (2 rows, 1 column)
fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(8, 10))

# Plot 1:

sns.boxplot(x='category', y='value', data=df[df['group'] == 'G1'], ax=axes[0], color='lightgray')
sns.swarmplot(x='category', y='value', data=df[df['group'] == 'G1'], ax=axes[0], color='black', size=5)
axes[0].set_title('Group G1')
#sns.boxplot
#sns.violinplot
#sns.swarmplot

# Plot 2: violinplot
sns.boxplot(x='category', y='value', data=df[df['group'] == 'G2'], ax=axes[1], color='lightgray')
sns.swarmplot(x='category', y='value', data=df[df['group'] == 'G2'], ax=axes[1], color='black', size=5)
#sns.swarmplot(x='category', y='value', data=df[df['group'] == 'G2'], ax=axes[1])
axes[1].set_title('Group G2')

plt.tight_layout()
plt.show()