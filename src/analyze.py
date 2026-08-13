import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import f_oneway
import glob
import os

# =========================
# CONFIG
# =========================
DATA_DIR = "data"
OUTPUT_DIR = "results"
BLUE = "#1f4ed8"

os.makedirs(OUTPUT_DIR, exist_ok=True)

# =========================
# LOAD ALL CSV FILES
# =========================
files = glob.glob(os.path.join(DATA_DIR, "*.csv"))

if not files:
    raise FileNotFoundError("No CSV files found in the data/ directory.")

df_list = [pd.read_csv(f) for f in files]
df = pd.concat(df_list, ignore_index=True)

# =========================
# VALIDATE REQUIRED COLUMNS
# =========================
required_cols = {
    "dopamine_level_percent",
    "iti_variability_ms"
}

missing = required_cols - set(df.columns)
if missing:
    raise ValueError(f"Missing required columns: {missing}")

# =========================
# ORDER DOPAMINE LEVELS
# =========================
dopamine_order = [40, 60, 80, 100]
df["dopamine_level_percent"] = pd.Categorical(
    df["dopamine_level_percent"],
    categories=dopamine_order,
    ordered=True
)

# =========================
# SUMMARY STATISTICS
# =========================
summary = (
    df.groupby("dopamine_level_percent", observed=True)
    .agg(
        mean_iti_variability=("iti_variability_ms", "mean"),
        std_iti_variability=("iti_variability_ms", "std")
    )
    .reset_index()
)

# =========================
# ONE-WAY ANOVA
# =========================
groups = [
    df[df["dopamine_level_percent"] == lvl]["iti_variability_ms"]
    for lvl in dopamine_order
]

anova = f_oneway(*groups)
print(f"One-way ANOVA: F={anova.statistic:.3f}, p={anova.pvalue:.3e}")

# =========================
# BOX PLOT (PRINT-OPTIMIZED)
# =========================
fig, ax = plt.subplots(figsize=(7.5, 4.8))

box_data = [
    df[df["dopamine_level_percent"] == lvl]["iti_variability_ms"]
    for lvl in dopamine_order
]

ax.boxplot(
    box_data,
    labels=dopamine_order,
    widths=0.6,
    patch_artist=True,
    boxprops=dict(facecolor="white", edgecolor="black"),
    medianprops=dict(color="black"),
    whiskerprops=dict(color="black"),
    capprops=dict(color="black")
)

ax.set_title(
    "ITI Variability by Simulated Dopamine Level",
    fontsize=15,
    fontweight="bold",
    fontname="Times New Roman",
    color="white",
    pad=12,
    bbox=dict(
        facecolor=BLUE,
        edgecolor="black",
        boxstyle="round,pad=0.4"
    )
)

ax.set_xlabel(
    "Simulated Dopamine Level (%)",
    fontsize=12,
    fontname="Times New Roman"
)
ax.set_ylabel(
    "ITI Variability (ms)",
    fontsize=12,
    fontname="Times New Roman"
)

ax.tick_params(axis="both", labelsize=11)
ax.grid(True, linestyle="--", alpha=0.4)

plt.tight_layout(rect=[0, 0, 1, 0.92])
plt.savefig(os.path.join(OUTPUT_DIR, "boxplot_iti_variability.png"), dpi=300)
plt.close()

# =========================
# MEAN ITI VARIABILITY PLOT
# =========================
fig, ax = plt.subplots(figsize=(7.5, 4.8))

ax.plot(
    summary["dopamine_level_percent"],
    summary["mean_iti_variability"],
    marker="o",
    linewidth=2,
    color="black"
)

ax.set_title(
    "Mean ITI Variability Across Dopamine Levels",
    fontsize=15,
    fontweight="bold",
    fontname="Times New Roman",
    color="white",
    pad=12,
    bbox=dict(
        facecolor=BLUE,
        edgecolor="black",
        boxstyle="round,pad=0.4"
    )
)

ax.set_xlabel(
    "Simulated Dopamine Level (%)",
    fontsize=12,
    fontname="Times New Roman"
)
ax.set_ylabel(
    "Mean ITI Variability (ms)",
    fontsize=12,
    fontname="Times New Roman"
)

ax.tick_params(axis="both", labelsize=11)
ax.grid(True, linestyle="--", alpha=0.4)

plt.tight_layout(rect=[0, 0, 1, 0.92])
plt.savefig(os.path.join(OUTPUT_DIR, "mean_iti_variability.png"), dpi=300)
plt.close()
