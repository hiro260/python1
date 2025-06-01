import pandas as pd
import plotly.express as px

# Load the Excel file
df = pd.read_excel("plotly1.xlsx")

# Rename columns if needed (adjust based on actual column names)
df.columns = [col.strip() for col in df.columns]  # Clean column names

# Create a melted DataFrame to plot both ICP and IDL on the same axis
df_melted = df.melt(
    id_vars=["Device", "wafer(4-2)", "num", "Bias", "Frc"],
    value_vars=["ICP", "IDL"],
    var_name="Measurement",
    value_name="Value"
)

# Create the facet plot
fig = px.scatter(
    df_melted,
    x="Frc",
    y="Value",
    color="Bias",
    facet_col="wafer(4-2)",
    facet_row="num",
    symbol="Measurement",
    animation_frame="Device",  # One plot per Device, use dropdown to change
    title="ICP and IDL vs Frc, grouped by Bias, Wafer, and Num"
)

# Update layout for better spacing
fig.update_layout(
    height=800,
    width=1200,
    margin=dict(t=50, l=50, r=50, b=50),
    legend_title_text='Bias'
)

# Show plot
fig.show()