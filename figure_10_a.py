import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams

# Set visualization style
sns.set_theme(style="white")
rcParams['font.family'] = 'Times New Roman Cyr'
rcParams['font.size'] = 20

# Load the processed data with actual, fit, and std values
data = pd.read_csv('/home/bakibilla/Downloads/figure_10_b.csv')

# Define columns for plotting
mW_columns = ['144mW', '149mW', '153mW', '157mW', '161mW', '164mW', '166mW', '168mW']

# Create a plot
plt.figure(figsize=(10, 7))

# Loop through each mW column to plot both actual data and fit
for column in mW_columns:
    # Extract fit column
    fit_column = f'{column}_fit'
    
    # Plot original data as scatter points
    plt.scatter(data['conc'], data[column], marker='o', label=f'{column}', s=40)
    
    # Plot fit data as a line
    plt.plot(data['conc'], data[fit_column], linestyle='dashed', linewidth=3)

# Customize the plot
plt.xlabel('Concentration (v/v)%', fontsize=20)
plt.ylabel('$|\Delta\phi_5|$', fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)
plt.legend(fontsize=19, loc='upper center', bbox_to_anchor=(0.5, 1.19), ncol=4, frameon=False)
plt.tight_layout()

# Show the plot
plt.show()
