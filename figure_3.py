import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
input_file_path = "figure_3_d.csv"
df = pd.read_csv(input_file_path)

# Set seaborn style for better aesthetics
sns.set(style="whitegrid")

# Create a new figure with a specified size
plt.figure(figsize=(10, 6))

# Plot with error bars for Open Aperture
plt.errorbar(
    df['z_oa'], 
    df['fit_oa'], 
    yerr=df['oa_std'], 
    fmt='s', 
    color='#0000a2', 
    ecolor='#0000a2', 
    elinewidth=3, 
    label='Open Aperture', 
    markersize=8
)

# Plot with error bars for Close Aperture
plt.errorbar(
    df['z_ca'], 
    df['fit_ca'], 
    yerr=df['ca_std'], 
    fmt='o', 
    color='#bc272d', 
    ecolor='#bc272d', 
    elinewidth=1, 
    label='Close Aperture', 
    markersize=8
)

# Set titles and labels
plt.ylabel('Normalized Transmittance', fontsize=16)
plt.xlabel('Position in cm', fontsize=14)

# Add legend
plt.legend(fontsize=12)
# Show the plot
plt.tight_layout()
plt.show()
