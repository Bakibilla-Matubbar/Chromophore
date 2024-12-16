import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load the data from CSV file
file_path = '/home/bakibilla/Downloads/plot-data.csv'
df = pd.read_csv(file_path)

# Extracting data
ab = df['y']  # Absorption
wav = df['x']  # Wavelength
peak = ab.max()
peak_wavelength = wav[ab.idxmax()]  # Get the wavelength corresponding to the peak

# Print the peak value and corresponding wavelength
print(f'Peak Absorbance: {peak}, Wavelength: {peak_wavelength} nm')

# Set the style for the plot
sns.set(style="white")

# Create the plot
plt.figure(figsize=(10, 6))  # Set figure size
plt.plot(wav, ab, color='g', marker='o', linewidth=3, label=f'Peak: {peak:.2f} at {peak_wavelength:.0f} nm')  # Plot with line color and width

# Set the x-axis limits to start at 350
plt.xlim(left=350)

# Set plot labels and title
plt.xlabel('Wavelength (nm)', fontsize=18)  # X-axis label
plt.ylabel('Absorbance (a.u.)', fontsize=18)  # Y-axis label
plt.legend(fontsize=16)  # Legend

# Adjust tick parameters for better readability
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)

# Use tight layout for better spacing
plt.tight_layout()

# Show the plot
plt.show()
