import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams
import matplotlib.font_manager as fm
import os
import matplotlib

# from scipy.ndimage.filters import gaussian_filter1d
from scipy.optimize import curve_fit
# Set the seaborn theme for the plots
sns.set_theme(style='white')
sns.set_style("ticks")

# Set the font path manually
font_path = '/usr/share/fonts/truetype/msttcorefonts/Times_New_Roman.ttf'
times_new_roman_font = fm.FontProperties(fname=font_path)

# Set font globally
rcParams['font.family'] = times_new_roman_font.get_name()
# Enable LaTeX rendering and ensure the mathptmx package is used
matplotlib.rcParams["text.usetex"] = True
# Corrected preamble to use newtxtext and newtxmath for Times font with math support
# matplotlib.rcParams["text.latex.preamble"] = r'\usepackage{newtxtext,newtxmath}'  # Use Times New Roman with full math support
matplotlib.rcParams["text.latex.preamble"] = r'\usepackage{mathptmx}'  # Use Times New Roman for text and math
# Concentration levels
conc_levels = ['0.5', '1', '2.5', '5.0', '10']

# Create a figure for 2x2 subplots
fig, axs = plt.subplots(nrows=2, ncols=3, figsize=(7.5, 5))  # Adjusted size for 2x2 grid
axs = axs.flatten()

# Define a consistent color palette for all plots
colors = sns.color_palette("tab10", n_colors=5)

# Plot (a): T$_{V}$ in Open Aperture
file_path = '/home/bakibilla/Downloads/Bakibilla/figure_6_d.csv'
df = pd.read_csv(file_path)

ax = axs[0]
for i in range(1, 6):
    col_name = f'conc_{i}'
    if col_name in df.columns:  # Check if the column exists
        ax.scatter(df['power'], abs(df[col_name]), s=25, color=colors[i - 1])

for i in range(1, 6):
    col_name = f'fit_{i}'
    if col_name in df.columns:  # Check if the column exists
        ax.plot(df['power'], df[col_name], color=colors[i - 1], linestyle='-', linewidth=2,
                label=f'Conc-{conc_levels[i - 1]}%')
ax.set_xlabel('Incident Power in mW', fontsize=12)
ax.set_ylabel('T$_{V}$ in OA', fontsize=12)
ax.tick_params(axis='both', which='major', labelsize=12)
ax.text(0.05, 0.97, '(a)', transform=ax.transAxes, fontsize=12, va='top', ha='left')

# Plot (b): T$_{PV}$ in Close Aperture
file_path = '/home/bakibilla/Downloads/Bakibilla/figure_6_e.csv'
df = pd.read_csv(file_path)

ax = axs[1]
for i in range(1, 6):
    col_name = f'conc_{i}'
    if col_name in df.columns:  # Check if the column exists
        ax.scatter(df['power'], abs(df[col_name]), s=25, color=colors[i - 1])

for i in range(1, 6):
    col_name = f'fit_{i}'
    if col_name in df.columns:  # Check if the column exists
        ax.plot(df['power'], df[col_name], color=colors[i - 1], linestyle='-', linewidth=2,
                label=f'{conc_levels[i - 1]}\%')
ax.set_xlabel('Incident Power in mW', fontsize=12)
ax.set_ylabel('T$_{PV}$ in CA', fontsize=12)
ax.tick_params(axis='both', which='major', labelsize=12)
ax.text(0.85, 0.97, '(b)', transform=ax.transAxes, fontsize=12, va='top', ha='left')

# Plot (c): |Δϕ₃| vs Power
file_path = '/home/bakibilla/Downloads/Bakibilla/figure_4_a.csv'
df = pd.read_csv(file_path)

ax = axs[3]
for i in range(1, 6):
    col_name = f'conc_{i}'
    if col_name in df.columns:  # Check if the column exists
        ax.errorbar(df['power'], abs(df[col_name]), yerr=abs(df[f'std_{i}']),
                    fmt='o', markersize=5, color=colors[i - 1], capsize=2, elinewidth=1)

for i in range(1, 6):
    col_name = f'fit_{i}'
    if col_name in df.columns:  # Check if the column exists
        ax.plot(df['power'], df[col_name], color=colors[i - 1], linestyle='-', linewidth=2,
                label=f'{conc_levels[i - 1]}%')
ax.set_xlabel('Incident Power in mW', fontsize=12)
ax.set_ylabel('$|\Delta\phi_{3}|$', fontsize=12)
ax.tick_params(axis='both', which='major', labelsize=12)
ax.text(0.85, 0.97, '(c)', transform=ax.transAxes, fontsize=12, va='top', ha='left')

# Plot (d): |Δϕ₅| vs Power
file_path = '/home/bakibilla/Downloads/Bakibilla/figure_4_b.csv'
df = pd.read_csv(file_path)

ax = axs[4]
for i in range(1, 6):
    col_name = f'conc_{i}'
    if col_name in df.columns:  # Check if the column exists
        ax.errorbar(df['power'], abs(df[col_name]), yerr=df[f'std_{i}'],
                    fmt='o', markersize=5, color=colors[i - 1], capsize=2, elinewidth=1)

for i in range(1, 6):
    col_name = f'fit_{i}'
    if col_name in df.columns:  # Check if the column exists
        ax.plot(df['power'], df[col_name], color=colors[i - 1], linestyle='-', linewidth=2,
                label=f'{conc_levels[i - 1]}%')
ax.set_xlabel('Incident Power in mW', fontsize=12)
ax.set_ylabel('$|\Delta\phi_{5}|$', fontsize=12)
ax.tick_params(axis='both', which='major', labelsize=12)
ax.text(0.8, 0.97, '(d)', transform=ax.transAxes, fontsize=12, va='top', ha='left')

# Plot (e): |Δn| vs Power
file_path = '/home/bakibilla/Downloads/Bakibilla/figure_5_b.csv'
df = pd.read_csv(file_path)

ax = axs[5]  # Ensure correct subplot index

for i in range(1, 6):  # Concentrations 3, 4, and 5
    col_name = f'conc_{i}'
    if col_name in df.columns:  # Check if the column exists
        # Plot data with error bars, scaled by 10^5
        ax.errorbar(df['power'], abs(df[col_name]) * 10**5, yerr=abs(df[f'std_{i}']) * 10**5,
                    fmt='o', markersize=5, color=colors[i - 1], capsize=2, elinewidth=1,
                    label=f'Conc {i}')

    fit_col_name = f'fit_{i}'
    if fit_col_name in df.columns:  # Check if the fit column exists
        # Plot fitted line, scaled by 10^5
        ax.plot(df['power'], abs(df[fit_col_name]) * 10**5, color=colors[i - 1],
                linestyle='-', linewidth=2, label=f'Fit {i}')

# Correctly label the y-axis with scaling factor
ax.set_ylabel(r'$\Delta n $ ($\times 10^{-5}$)', fontsize=12)
ax.set_xlabel('Incident Power in mW', fontsize=12)
ax.tick_params(axis='both', which='major', labelsize=12)

# Add subplot label
ax.text(0.8, 0.97, '(e)', transform=ax.transAxes, fontsize=12, va='top', ha='left')





# # Add common legend for all plots
# handles, labels = axs[1].get_legend_handles_labels()
# fig.legend(handles, labels, loc='upper center', frameon=False, bbox_to_anchor=(0.5, 0.97), ncol=5, fontsize=12)
# fig.suptitle('Concentrations (v/v)', fontsize=12, x=0.5, y=0.98)  # Centered at the top
# # Add common x-label and title
# # Adjust layout for readability
# plt.subplots_adjust(hspace=0.38,wspace=0.41, left=0.095, top=0.90, right= 0.98, bottom= 0.11)
# Add legend in subplot axs[2]
# Add legend in subplot axs[2] with a title
handles, labels = axs[1].get_legend_handles_labels()  # Extract handles and labels from axs[1]
axs[2].legend(handles, labels, title="Concentrations (v/v)", title_fontsize=12, loc='upper center',
              frameon=False, fontsize=12, bbox_to_anchor=(0.5, 1), ncol=1)
axs[2].tick_params(
    axis='both',         # Apply to both x and y axes
    which='both',        # Apply to major and minor ticks
    bottom=False,        # Disable ticks on the bottom
    top=False,           # Disable ticks on the top
    left=False,          # Disable ticks on the left
    right=False,         # Disable ticks on the right
    labelbottom=False,   # Disable labels on the bottom
    labelleft=False      # Disable labels on the left
)

# Adjust layout for readability
plt.subplots_adjust(hspace=0.3, wspace=0.35, left=0.095, top=0.98, right=0.98, bottom=0.11)

# Show the plot
plt.show()


# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt
# import seaborn as sns
# from matplotlib import rcParams
# import matplotlib.font_manager as fm

# sns.set_theme(style='white')
# sns.set_style("ticks")
# # Set the font path manually
# font_path = '/usr/share/fonts/truetype/msttcorefonts/Times_New_Roman.ttf'
# times_new_roman_font = fm.FontProperties(fname=font_path)

# # Set font globally
# rcParams['font.family'] = times_new_roman_font.get_name()
# # Concentration levels
# conc_levels = ['0.5', '1', '2.5', '5', '10']

# # Create a figure for 2x2 subplots
# fig, axs = plt.subplots(nrows=1, ncols=4, figsize=(9, 3))  # Adjusted size for 2x2 grid
# axs = axs.flatten()

# # Define a consistent color palette for all plots
# colors = sns.color_palette("tab10", n_colors=5)

# # Plot (a): T$_{V}$ in Open Aperture
# file_path = '/home/bakibilla/Downloads/green_T_oa_m_fitted.csv'
# df = pd.read_csv(file_path)

# ax = axs[0]
# for i in range(1, 6):
#     col_name = f'conc_{i}'
#     if col_name in df.columns:  # Check if the column exists
#         ax.scatter(df['power'], abs(df[col_name]), s=25, color=colors[i - 1])

# for i in range(1, 6):
#     col_name = f'fit_{i}'
#     if col_name in df.columns:  # Check if the column exists
#         ax.plot(df['power'], df[col_name], color=colors[i - 1], linestyle='-', linewidth=2,
#                 label=f'Conc-{conc_levels[i - 1]}%')
# ax.set_ylim(-0.02,1.05)
# ax.set_ylabel('T$_{V}$ in Open Aperture', fontsize=14)
# ax.tick_params(axis='both', which='major', labelsize=14)
# ax.text(0.05, 0.97, '(a)', transform=ax.transAxes, fontsize=14, va='top', ha='left')

# # Plot (b): T$_{PV}$ in Close Aperture
# file_path = '/home/bakibilla/Downloads/green_T_ca_m_fitted.csv'
# df = pd.read_csv(file_path)

# ax = axs[1]
# for i in range(1, 6):
#     col_name = f'conc_{i}'
#     if col_name in df.columns:  # Check if the column exists
#         ax.scatter(df['power'], abs(df[col_name]), s=25, color=colors[i - 1])

# for i in range(1, 6):
#     col_name = f'fit_{i}'
#     if col_name in df.columns:  # Check if the column exists
#         ax.plot(df['power'], df[col_name], color=colors[i - 1], linestyle='-', linewidth=2,
#                 label=f'{conc_levels[i - 1]}%')

# ax.set_ylabel('T$_{P-V}$ in Closed Aperture', fontsize=14)
# ax.tick_params(axis='both', which='major', labelsize=14)
# ax.text(0.9, 0.97, '(b)', transform=ax.transAxes, fontsize=14, va='top', ha='left')

# # Plot (c): |Δϕ₃| vs Power
# file_path = '/home/bakibilla/Downloads/green_phi_3_m_fitted.csv'
# df = pd.read_csv(file_path)

# ax = axs[2]
# for i in range(1, 6):
#     col_name = f'conc_{i}'
#     if col_name in df.columns:  # Check if the column exists
#         ax.errorbar(df['power'], abs(df[col_name]), yerr=abs(df[f'std_{i}']),
#                     fmt='o', markersize=5, color=colors[i - 1], capsize=2, elinewidth=1)

# for i in range(1, 6):
#     col_name = f'fit_{i}'
#     if col_name in df.columns:  # Check if the column exists
#         ax.plot(df['power'], abs(df[col_name]), color=colors[i - 1], linestyle='-', linewidth=2,
#                 label=f'{conc_levels[i - 1]}%')

# ax.set_ylabel(r'$|\Delta\phi_{3}|$', fontsize=14)
# ax.tick_params(axis='both', which='major', labelsize=14)
# ax.text(0.9, 0.97, '(c)', transform=ax.transAxes, fontsize=14, va='top', ha='left')

# # Plot (d): |Δϕ₅| vs Power
# file_path = '/home/bakibilla/Downloads/green_phi_5_m_fitted.csv'
# df = pd.read_csv(file_path)

# ax = axs[3]
# for i in range(1, 6):
#     col_name = f'conc_{i}'
#     if col_name in df.columns:  # Check if the column exists
#         ax.errorbar(df['power'], abs(df[col_name]), yerr=abs(df[f'std_{i}']),
#                     fmt='o', markersize=5, color=colors[i - 1], capsize=2, elinewidth=1)

# for i in range(1, 6):
#     col_name = f'fit_{i}'
#     if col_name in df.columns:  # Check if the column exists
#         ax.plot(df['power'], abs(df[col_name]), color=colors[i - 1], linestyle='-', linewidth=2,
#                 label=f'{conc_levels[i - 1]}%')

# ax.set_ylabel(r'$|\Delta\phi_{5}|$', fontsize=14)
# ax.tick_params(axis='both', which='major', labelsize=14)
# ax.text(0.9, 0.97, '(d)', transform=ax.transAxes, fontsize=14, va='top', ha='left')
# # Disable x-axis ticks and labels for the first two plots
# axs[0].tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)
# axs[1].tick_params(axis='x', which='both', bottom=False, top=False, labelbottom=False)


# # Add common legend for all plots
# handles, labels = axs[1].get_legend_handles_labels()
# fig.legend(handles, labels, loc='upper center', frameon=False, bbox_to_anchor=(0.5, 0.97), ncol=5, fontsize=12)
# fig.suptitle('Concentrations (v/v)', fontsize=14, x=0.5, y=0.98)  # Centered at the top
# # Add common x-label and title
# fig.supxlabel('Incident Laser Power in mW', fontsize=14)
# # Adjust layout for readability
# plt.subplots_adjust(hspace=0.1,wspace=0.45, left=0.09, top=0.85, right= 0.98, bottom= 0.18)

# # Show the plot
# plt.show()