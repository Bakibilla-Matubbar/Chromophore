import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mtick
from matplotlib.ticker import ScalarFormatter

# Load the data from CSV file
file_path = 'figure_5_b.csv'
df = pd.read_csv(file_path)

# Set the figure size
plt.figure(figsize=(12, 8))

# Colors for each concentration
colors = sns.color_palette("tab10", n_colors=5)

# Plot concentrations with error bars and calculate fitted values and std deviations
for i in range(3, 6):
    # Plot data with error bars
    plt.errorbar(df['power'], abs(df[f'conc_{i}']), yerr=df[f'std_del_n_{i}'],
                 fmt='o', color=colors[i-1], label=f'Conc {i}',
                 capsize=5, elinewidth=2, linestyle='-.')

    # # Plot fitted line
    plt.plot(df['power'], abs(df[f'fit_{i}']), color=colors[i-1], linestyle='--', linewidth=2, label=f'Fit {i}')

# Set plot labels and title
plt.xlabel('Power (mW)', fontsize=14)
plt.ylabel(r'|$\Delta n$|', fontsize=14)

# Use ScalarFormatter for scientific notation on y-axis
ax = plt.gca()
ax.yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax.ticklabel_format(style='sci', axis='y', scilimits=(0, 0))  # Force scientific notation

# Add grid, legend, and display the plot
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
