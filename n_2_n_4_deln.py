# import pandas as pd
# import numpy as np
# import os


# df = pd.read_csv("/home/bakibilla/Downloads/merged_green_results.csv")
# phi_3 = [col for col in df.columns if "delta_phi_3" in col]
# phi_5 = [col for col in df.columns if "delta_phi_5" in col]

# # Calculate n2 and n4 for each concentration
# for col_phi3, col_phi5 in zip(phi_3, phi_5):
#     conc_label = col_phi3.split('_')[-1] # Extract concentration label from column name
#     df[f"n2_{conc_label}"] = df[col_phi3] * 660e-7 / (2 * np.pi * df["I0"])
#     df[f"n4_{conc_label}"] = df[col_phi5] * 660e-7 / (2 * np.pi * df["I0"]**2)
#     df[f'del_n_{conc_label}'] = df[f"n2_{conc_label}"]*df["I0"] + df[f"n4_{conc_label}"] * df["I0"]**2

# df.to_csv("/home/bakibilla/Downloads/green_toa_ca_del_phi_n2_n4.csv", index=False)
# print("✅ Saved CSV with n2 and n4 to /home/bakibilla/Downloads/green_toa_ca_del_phi_n2_n4.csv")
# # Parameters

import pandas as pd
import numpy as np
import os
import matplotlib.pyplot as plt

df = pd.read_csv("/home/bakibilla/Downloads/green_toa_ca_del_phi_n2_n4.csv")
del_n_cols = [col for col in df.columns if "del_n" in col]
df[del_n_cols] = df[del_n_cols]*1e5  # scale delta n for better plotting

# Plotting
plt.figure(figsize=(10, 6))
for col in del_n_cols:
    plt.plot(df["I0"], df[col], label=col.replace("del_n_", "Conc. ") + "%")
plt.xlabel("I0 (GW/cm²)")
plt.ylabel("Δn (x10⁻⁵)")
plt.title("Nonlinear Refractive Index Change vs I0")
plt.legend()
plt.grid()
plt.show()
