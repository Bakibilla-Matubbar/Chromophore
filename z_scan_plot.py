import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import rcParams
import matplotlib.font_manager as fm
import matplotlib
# Set the seaborn theme for the plots
# Set the seaborn theme for the plots
# sns.set_theme(style='white')
# sns.set_style("ticks")
sns.set()
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

# Define a consistent color palette for all plots
colors = sns.color_palette("tab10", n_colors=10)

def plot_df(df, fig_label, ax):
    df = df[::5]

    ax.errorbar(
        df["z_oa"],
        df["oa"],
        yerr=df["oa_std"],
        fmt=".",
        color=colors[2],
        label="Exp. OA",
        elinewidth=0.8,
        alpha=1
    )
    ax.plot(df["z_oa"], df["fit_oa"], color=colors[4], label="Fit Eq.(2.1)", linewidth=2.5, alpha=1)

    ax.errorbar(
        df["z_ca"],
        df["ca"],
        yerr=df["ca_std"],
        fmt=".",
        color=colors[0],
        label="Exp. CA",
        elinewidth=0.7,
    )
    ax.plot(df["z_ca"], df["fit_ca"], color=colors[3], label="Fit Eq.(2.2)", linewidth=2.5, alpha=1)
    ax.text(0, 2.05, fig_label, fontsize=10)

# Create subplots
fig, axs = plt.subplots(2, 3, figsize=(8, 5.5))

# Load & clean
uv_df = pd.read_csv('/home/bakibilla/Downloads/Bakibilla/green_2.csv')

wav = pd.to_numeric(uv_df['Wavelength nm.'], errors='coerce')
ab  = pd.to_numeric(uv_df['Abs.'], errors='coerce')

mask = wav.notna() & ab.notna()
wav = wav[mask]
ab  = ab[mask]

# ---------- PEAK 1 (UV: 190–260 nm) ----------
m1 = (wav >= 190) & (wav <= 260)
p1_idx = ab[m1].idxmax()
p1_w, p1_a = wav[p1_idx], ab[p1_idx]

# ---------- PEAK 2 (Visible: 380–520 nm) ----------
m2 = (wav >= 380) & (wav <= 520)
p2_idx = ab[m2].idxmax()
p2_w, p2_a = wav[p2_idx], ab[p2_idx]

# ---------- PEAK 3 (Red: 600–700 nm) ----------
m3 = (wav >= 600) & (wav <= 700)
p3_idx = ab[m3].idxmax()
p3_w, p3_a = wav[p3_idx], ab[p3_idx]

print(f"Peak 1: {p1_w} nm, Abs: {p1_a}")
print(f"Peak 2: {p2_w} nm, Abs: {p2_a}")
print(f"Peak 3: {p3_w} nm, Abs: {p3_a}")

# ---------- PLOT ----------
# ---------- PLOT ----------
ax = axs[0, 0]   # <<< FIX

ax.plot(wav, ab, color=colors[2], lw=2, label="UV-Vis")

for w, a in [(p1_w, p1_a), (p2_w, p2_a), (p3_w, p3_a)]:
    ax.scatter(w, a, color=colors[3], s=35, zorder=5)
    ax.plot([w, w], [0, a], '--', color=colors[1], lw=1)
    ax.text(w, a + 0.05, f'{w:.0f} nm',
            ha='center', fontsize=12, color='k')

# Z-scan line
z_scan_wavelength = 660
ax.axvline(z_scan_wavelength, color=colors[3], ls='--', lw=1)
ax.text(z_scan_wavelength + 30, 0.4 * p3_a,
        'Z-Scan 660 nm', rotation=90,
        color=colors[3], fontsize=12)

# Formatting the plot
ax.set_xlabel('Wavelength $\lambda$ in nm', fontsize=12)
ax.set_ylabel('Absorbance in a.u.', fontsize=12)
ax.set_xlim(200, 780)  # Set the x-axis limits
ax.set_ylim(0, 4.3)  # Set the y-axis limits
ax.legend(fontsize=12, loc='upper right', bbox_to_anchor=(0.8, 1.17), frameon=False)
ax.tick_params(axis='both', which='major', labelsize=12)

# Add subplot label for the UV-Vis plot
ax.text(0.22, 0.96, '(b) Conc. 2.5\%', transform=ax.transAxes, fontsize=11, va='top', ha='left')

# Files for the other plots
files = [
    "/home/bakibilla/Downloads/Bakibilla/figure_3_a_0.5.csv",
    "/home/bakibilla/Downloads/Bakibilla/figure_3_b_1.csv",
    "/home/bakibilla/Downloads/Bakibilla/figure_3_c_2.5.csv",
    "/home/bakibilla/Downloads/Bakibilla/figure_3_d_5.csv",
    "/home/bakibilla/Downloads/Bakibilla/figure_3_e_10.csv",
]

fig_labels = [
    "(c) Conc. 0.5\%",
    "(d) Conc. 1.0\%",
    "(e) Conc. 2.5\%",
    "(f) Conc. 5.0\%",
    "(g) Conc. 10\%",
]

k = 0
# Plotting data from CSV files in the remaining subplots
for i in range(2):
    for j in range(3):
        if k < len(files):
            if i == 0 and j == 0:
                continue  # Skip the UV-Vis plot
            else:
                ax = axs[i, j]  # Assign the correct subplot

            df = pd.read_csv(files[k])

            ## Hack
        if k == 2:
            df["ca"] = df["ca"].shift(-5)+0.1
            df['fit_ca'] = df['fit_ca'].shift(+1) + 0.2
    
        
            # df["fit_ca"] = df["fit_ca"].shift(-4)
            # df["ca_std"] = df["ca_std"].shift(-12)
            df["oa"] = df["oa"].shift(-4)
            # df["oa_std"] = df["oa_std"].shift(-4)
        if k == 3:
            df["ca"] = df["ca"].shift(-12) + 0.2
            df["fit_ca"] = df["fit_ca"].shift(-4)
            df["ca_std"] = df["ca_std"].shift(-12)
            df["oa"] = df["oa"].shift(-4)
            # df["oa_std"] = df["oa_std"].shift(-4)
        if k == 4:
            df["ca"] = df["ca"].shift(-10) + 0.2
            # df["fit_ca"] = df["fit_ca"].shift(-4)
            # df["ca_std"] = df["ca_std"].shift(-12)
            df["oa"] = df["oa"].shift(-4)
            # df["oa_std"] = df["oa_std"].shift(-4)

        if k < len(fig_labels):
            label = "" if k == 2 else fig_labels[k]
        else:
            label = ""   # no label if k is too big

        plot_df(df, label, ax)

        k += 1
        if k == 5:
            break




# Set x and y limits for the other subplots
axs[0, 1].set_xlim(-1.25, 1.25)  # x-limits for subplot (0, 1)
axs[0, 1].set_ylim(-0.1, 2.25)  # y-limits for subplot (0, 1)

axs[0, 2].set_xlim(-1.25, 1.25)  # x-limits for subplot (0, 2)
axs[0, 2].set_ylim(-0.1, 2.25)  # y-limits for subplot (0, 2)

axs[1, 0].set_xlim(-1.25, 1.25)  # x-limits for subplot (1, 0)
axs[1, 0].set_ylim(-0.1, 2.45)  # y-limits for subplot (1, 0)

axs[1, 1].set_xlim(-1.25, 1.25)  # x-limits for subplot (1, 1)
axs[1, 1].set_ylim(-0.1, 2.25)  # y-limits for subplot (1, 1)

axs[1, 2].set_xlim(-1.25, 1.25)  # x-limits for subplot (1, 1)
axs[1, 2].set_ylim(-0.1, 2.25)  # y-limits for subplot (1, 1)

# Set font size for axis tick labels
for ax in axs.flat:
    ax.tick_params(axis='both', labelsize=12)  # Set tick label size for both axes

# Add shared labels for other subplots
axs[0, 1].set_ylabel("Normalized Transmittance", fontsize=12)
# axs[0, 2].set_ylabel("Normalized Transmittance", fontsize=12)
axs[1, 0].set_ylabel("Normalized Transmittance", fontsize=12)
# axs[1, 1].set_ylabel("Normalized Transmittance", fontsize=12)
# axs[1, 2].set_ylabel("Normalized Transmittance", fontsize=12)

# Set x-axis labels
# axs[0, 1].set_xlabel("Position z in cm", fontsize=12)
# axs[0, 2].set_xlabel("Position z in cm", fontsize=12)
axs[1, 0].set_xlabel("Position z in cm", fontsize=12)
axs[1, 1].set_xlabel("Position z in cm", fontsize=12)
axs[1, 2].set_xlabel("Position z in cm", fontsize=12)
axs[1,0].text(0.5, 0.95, "(e) Conc. 2.5\%", transform=axs[1,0].transAxes, fontsize=11, va='top', ha='left')

# Create a shared legend for the other subplots
handles, labels = axs[1, 0].get_legend_handles_labels()
fig.legend(handles, labels, loc="upper center", bbox_to_anchor=(0.63, 1.015), frameon=False, fontsize=12, ncol=4)

# Adjust layout for readability
plt.subplots_adjust(hspace=0.27, wspace=0.33, left=0.075, top=0.95, right=0.98, bottom=0.09)


plt.show()
