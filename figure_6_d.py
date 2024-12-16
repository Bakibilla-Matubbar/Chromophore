import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set the style for the plot
sns.set_style("white")

# Load the data from the CSV file
file_path = '/content/drive/MyDrive/zscandata/figure_6_d.csv'  # Update this to your actual file path
df = pd.read_csv(file_path)

# Define the columns for concentrations and power
power_col = 'power'  # Ensure this matches the actual column name for power in your DataFrame
concentration_cols = ['conc_3', 'conc_4', 'conc_5']

# Create a plot
plt.figure(figsize=(10, 6))

# Plot each concentration against power
for conc_col in concentration_cols:
    plt.plot(df[power_col], df[conc_col], marker='o', label=conc_col)

# Add labels and title
plt.xlabel('Power (mW)')
plt.ylabel('T$_{oavp}$')
plt.legend()

# Show the plot
plt.tight_layout()
plt.show()
