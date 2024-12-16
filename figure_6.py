import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
input_file_path = "figur_6_a"
df = pd.read_csv(input_file_path)

# Set seaborn style for better aesthetics
sns.set(style="whitegrid")

# Create a new figure with a specified size
plt.figure(figsize=(10, 6))

# Plot Original Data
plt.plot(df['z'], df['oa'],marker='o', label='Original Data (OA)', color='#0000a2')
plt.plot(df['z'], df['2pa_z'], label='2PA Z', linestyle=':', color='green', linewidth=2)
plt.plot(df['z'], df['2pa_lsm'], label='2PA LSM Fit', linestyle='-.', color='red', linewidth=2)
plt.plot(df['z'], df['3pa_z'], label='3PA Z ', linestyle='-', color='#bc272d', linewidth=2)
plt.plot(df['z'], df['3pa_lsm'], label='3PA LSM Fit', linestyle=':', color='green', linewidth=2)

# Set titles and labels
plt.title('Comparison of Original Data and Fitted Values', fontsize=16)
plt.xlabel('Z Position (units)', fontsize=14)
plt.ylabel('Values (units)', fontsize=14)

# Add grid lines
plt.grid(True)

# Add legend
plt.legend(fontsize=12)

# Show the plot
plt.tight_layout()
plt.show()
