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
colors = sns.color_palette("tab10", n_colors=8)


### double exponential fit
def func_f(x, a, b, c):
    return a * (np.exp(-b * x) - np.exp(-c * x) * c)


def func(x, a, b, c):
    return a + b * np.exp(1 - c * x)


fig, axs = plt.subplots(1, 2, figsize=(7.5, 3))


def df_all(df):
    df_all = df[["conc", y_axes[0]]]
    for i in range(1, len(y_axes)):
        df_temp = df[["conc", y_axes[i]]]
        df_temp.columns = ["conc", y_axes[0]]
        df_all = pd.concat([df_all, df_temp], ignore_index=True)

    return df_all

    # print(df_all)


def plot_fig(filename, y_axes, colors, ax):
    df = pd.read_csv(filename)
    df = df.abs()

    df.plot(
        x="conc",
        y=y_axes,
        style=".",
        color=colors,
        ax=ax,
        markersize=10
    )

    x = np.linspace(0, 12, 100)

    if len(df.conc) > 3:
        df_n = df_all(df)
        popt, pcov = curve_fit(func_f, df_n.conc, df_n[y_axes[0]])
        ax.plot(x, func_f(x, *popt), "-", color=colors[0], label="fit", linewidth=2.5)
    else:
        df_n = df_all(df)
        popt, pcov = curve_fit(func, df_n.conc, df_n[y_axes[0]])
        ax.plot(x, func(x, *popt), "-", color=colors[0], label="fit", linewidth=2.5)

    # print(popt)

    # for i in range(len(y_axes)):
    #     y = df[y_axes[i]].to_numpy()
    #     y_smooth = gaussian_filter1d(y, sigma=1, order=0)
    #
    #     ax.plot(df.conc, y_smooth, "--", color=colors[i], label="")


y_axes = ['144mW', '149mW', '153mW', '157mW', '161mW', '164mW', '166mW', '168mW']
y_axes_labels = ["144", "149", "153", "157", "161", "164", "166", "168"]

plot_fig("/home/bakibilla/Downloads/Bakibilla/figure_10_a.csv", y_axes, colors, axs[0])

# colors = colors[2::]
# y_axes = y_axes[2::]
# x = np.linspace(0, 12, 100)
# y = func(x, 13.3, 0.10, 22, 0.8)
# axs[1].plot(x, y, "-", color="k", label="fit")
#
# y = func(x, 13.3, 0.02, 22, 1.8)
# axs[1].plot(x, y, "-", color="r", label="fit")
axs[1].set_ylim(12, 23)
axs[0].set_ylim(0, 14)

plot_fig("/home/bakibilla/Downloads/Bakibilla/figure_10_b.csv", y_axes, colors, axs[1])
# df = pd.read_csv("./figure_4_b.csv")
# df = df.abs()
#
# df.plot(
#     x="power",
#     y=["fit_3", "fit_4", "fit_5"],
#     style=".",
#     color=colors,
#     ax=axs[1],
# )
#

axs[0].set_ylabel(r"$|\Delta \phi_3|$")
axs[1].set_ylabel(r"$|\Delta \phi_5|$")

axs[0].set_xlabel(r"Concentrations (v/v)")
axs[1].set_xlabel(r"Concentrations (v/v)")

leg = axs[0].legend(
    title=r"Incident Power in mW",
    labels=y_axes_labels,
    # labels=["0.5% (v/v)", "1.0% (v/v)", "2.5% (v/v)", "5.0% (v/v)", "10% (v/v)"],
    loc="upper center",
    bbox_to_anchor=(1, 1.3),
    ncol=8,
    frameon=False, fontsize=11
)


axs[1].set_xticks(np.arange(0, 12.5, 2.5))
axs[0].set_xticks(np.arange(0, 12.5, 2.5))

axs[1].legend([], frameon=False)

axs[0].text(4.5, 11.4, "(a) Third-Order")
axs[1].text(4.5, 21, "(b) Fifth-Order")
# Ensure raw strings are used for LaTeX math expressions
# Define custom arrow properties
arrowprops = dict(arrowstyle='-|>', color='darkred', lw=1.5)

# First subplot annotations
axs[0].annotate(r"$n_2$", xy=(0.8, 3.5), xytext=(2.7, 1.7),  
                arrowprops=arrowprops, fontsize=12)
# axs[0].annotate(r"$n_2 \, \& \alpha_3$", xy=(2.5, 10), xytext=(3, 5.3),  
#                 arrowprops=arrowprops, fontsize=12)
axs[0].annotate(r"Cascade Switching", xy=(2.5, 10), xytext=(1, 5.3),  
                arrowprops=arrowprops, fontsize=12)
axs[0].annotate(r"$n_2 , \, n_4 \, \& \alpha_3$", xy=(6.5, 9.5), xytext=(7, 5.3),  
                arrowprops=arrowprops, fontsize=12)

# Second subplot annotation
axs[1].annotate(r"Saturated $n_4 \,\& \alpha_3$", xy=(7.3, 16), xytext=(4.85, 19),  
                arrowprops=arrowprops, fontsize=12)



fig.subplots_adjust(
    left=0.09, right=0.99, bottom=0.15, top=0.82, hspace=0.8, wspace=0.22
)
plt.show()