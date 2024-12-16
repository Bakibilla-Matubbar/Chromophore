import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from CSV file
file_path = '/content/drive/MyDrive/zscandata/figure_4_a.csv'
df = pd.read_csv(file_path)

# Set the figure size
plt.figure(figsize=(12, 8))

# Colors for each concentration
colors = sns.color_palette("tab10", n_colors=5)

# Plot concentrations with error bars
for i in range(1, 6):
    plt.errorbar(df['power'], abs(df[f'conc_{i}']), yerr=df[f'std_{i}'], 
                 fmt='o', color=colors[i-1], label=f'Conc {i}', 
                 capsize=5, elinewidth=2)

# Plot fitted lines
for i in range(1, 6):
    plt.plot(df['power'], df[f'fit_{i}'], color=colors[i-1], linestyle='--', 
             linewidth=2, label=f'Fit {i}')

# Set plot labels and title
plt.xlabel('Power (mW)', fontsize=14)
plt.ylabel('Concentration', fontsize=14)
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
