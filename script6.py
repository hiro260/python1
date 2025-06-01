import pandas as pd
#import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# Load the Excel file
df = pd.read_csv("plotly1.csv")

# Rename columns if needed (adjust based on actual column names)
df.columns = [col.strip() for col in df.columns]  # Clean column names

print(df.columns)

# Create a melted DataFrame to plot both ICP and IDL on the same axis
df_melted = df.melt(
    id_vars=["Device", "Wafer(4-2)", "num", "Bias", "Frc"],
    value_vars=["ICP(A)", "IDL(A)"],
    var_name="Measurement",
    value_name="Value"
)

print(df_melted.head(5))
#quit()

# Get unique values
measurements = df_melted['Measurement'].unique()
nums = sorted(df_melted['num'].unique())
wafers = df_melted['Wafer(4-2)'].unique()

# Build subplot grid: rows = len(measurements) * len(nums), cols = len(wafers)
nrows = len(measurements) * len(nums)
ncols = len(wafers)

# Create subplot titles
row_titles = [f"{m}, x{n}" for m in measurements for n in nums]
col_titles = [f"{w}" for w in wafers]

# Create subplots
fig = make_subplots(
    rows=nrows,
    cols=ncols,
    shared_xaxes=True,
    shared_yaxes=False,
    subplot_titles=[f"{r} | {c}" for r in row_titles for c in col_titles],
    vertical_spacing=0.03,
    horizontal_spacing=0.03
)

# Plot each combination
for i, m in enumerate(measurements):
    for j, n in enumerate(nums):
        row_idx = i * len(nums) + j + 1
        for k, w in enumerate(wafers):
            col_idx = k + 1

            sub_df = df_melted[
                (df_melted["Measurement"] == m) &
                (df_melted["num"] == n) &
                (df_melted["Wafer(4-2)"] == w)
            ]

            for bias in sub_df["Bias"].unique():
                bias_df = sub_df[sub_df["Bias"] == bias]
                fig.add_trace(
                    go.Scatter(
                        x=bias_df["Frc"],
                        y=bias_df["Value"],
                        mode="lines",
                        name=f"Bias {bias}",
                        legendgroup=f"{bias}",
                        showlegend=(row_idx == 1 and col_idx == 1)
                    ),
                    row=row_idx,
                    col=col_idx
                )

# Final layout settings
fig.update_layout(
    height=300 * nrows,
    width=300 * ncols,
    title_text="ICP and IDL vs Frc (stacked by Measurement and num, faceted by Wafer)",
    legend_title="Bias",
    margin=dict(t=100, b=50, l=50, r=50)
)

# Save to HTML
fig.write_html("stacked_plot.html")
