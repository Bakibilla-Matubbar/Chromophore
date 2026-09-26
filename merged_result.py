import pandas as pd
import os

# Folder base path
base_path = "/home/bakibilla/Downloads/zscandata"

# Concentrations (folder names and labels)
concs = {
    "green0.5%": "0.5",
    "green1%": "1",
    "green2.5%": "2.5",
    "green5%": "5",
    "green10%": "10"
}

merged_df = None

for folder, label in concs.items():
    file_path = os.path.join(base_path, folder, "results", "all_parameters_results.csv")
    
    df = pd.read_csv(file_path)
    
    # Keep only required columns
    df = df[["power", "I0", "delta_phi_3", "delta_phi_5", "T_ca", "alpha", "T_oa"]]
    
    # Rename columns with concentration label (except power and I0)
    df = df.rename(columns={
        "delta_phi_3": f"delta_phi_3_{label}",
        "delta_phi_5": f"delta_phi_5_{label}",
        "T_ca": f"T_ca_{label}",
        "alpha": f"alpha_{label}",
        "T_oa": f"T_oa_{label}"
    })
    
    if merged_df is None:
        merged_df = df
    else:
        # Merge on power and I0
        merged_df = pd.merge(merged_df, df, on=["power", "I0"], how="outer")

# Save final merged file
merged_df.to_csv("/home/bakibilla/Downloads/zscandata/merged_green_results.csv", index=False)

print("✅ Merged CSV saved at /home/bakibilla/Downloads/zscandata/merged_green_results.csv")
