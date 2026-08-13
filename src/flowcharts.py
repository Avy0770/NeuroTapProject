import matplotlib.pyplot as plt

MEDICAL_BLUE = "#1f4ed8"
BORDER_COLOR = "black"

def draw_flowchart(title, boxes, arrows, filename):
    fig, ax = plt.subplots(figsize=(8, 10))
    ax.set_facecolor("white")
    ax.axis("off")

    # Header bar
    ax.add_patch(
        plt.Rectangle(
            (0.05, 0.92), 0.9, 0.07,
            transform=ax.transAxes,
            facecolor=MEDICAL_BLUE,
            edgecolor=BORDER_COLOR,
            linewidth=1.5
        )
    )
    ax.text(
        0.5, 0.955,
        title,
        ha="center", va="center",
        fontsize=20,
        fontweight="bold",
        color="white",
        fontname="Times New Roman"
    )

    # Boxes
    for text, (x, y) in boxes.items():
        ax.text(
            x, y, text,
            ha="center", va="center",
            fontsize=14,
            fontname="Times New Roman",
            bbox=dict(
                boxstyle="round,pad=0.4",
                facecolor="white",
                edgecolor=BORDER_COLOR,
                linewidth=1.3
            )
        )

    # Arrows
    for start, end in arrows:
        x1, y1 = boxes[start]
        x2, y2 = boxes[end]
        ax.annotate(
            "",
            xy=(x2, y2 + 0.05),
            xytext=(x1, y1 - 0.05),
            arrowprops=dict(arrowstyle="->", lw=2)
        )

    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close()


# =========================
# FLOWCHARTS
# =========================

# Experimental Design
draw_flowchart(
    "Experimental Design: Dopamine → Motor Variability",
    {
        "Simulated Dopamine Level\n(40–100%)": (0.5, 0.80),
        "Basal Ganglia\nTiming Model": (0.5, 0.65),
        "Finger-Tapping Output\n(ms)": (0.5, 0.50),
        "Inter-Tap Intervals": (0.5, 0.35),
        "ITI Variability\n(Dependent Variable)": (0.5, 0.20),
    },
    [
        ("Simulated Dopamine Level\n(40–100%)", "Basal Ganglia\nTiming Model"),
        ("Basal Ganglia\nTiming Model", "Finger-Tapping Output\n(ms)"),
        ("Finger-Tapping Output\n(ms)", "Inter-Tap Intervals"),
        ("Inter-Tap Intervals", "ITI Variability\n(Dependent Variable)"),
    ],
    "results/flow_experimental_design.png"
)

# Data Analysis
draw_flowchart(
    "Data Analysis Pipeline",
    {
        "Raw Tap Timestamps\n(ms)": (0.5, 0.78),
        "Compute Inter-Tap\nIntervals (ITI)": (0.5, 0.62),
        "Calculate ITI\nVariability (SD)": (0.5, 0.46),
        "Group by Dopamine\nLevel (40–100%)": (0.5, 0.30),
        "One-Way ANOVA\n(F, p-value)": (0.5, 0.14),
    },
    [
        ("Raw Tap Timestamps\n(ms)", "Compute Inter-Tap\nIntervals (ITI)"),
        ("Compute Inter-Tap\nIntervals (ITI)", "Calculate ITI\nVariability (SD)"),
        ("Calculate ITI\nVariability (SD)", "Group by Dopamine\nLevel (40–100%)"),
        ("Group by Dopamine\nLevel (40–100%)", "One-Way ANOVA\n(F, p-value)"),
    ],
    "results/flow_data_analysis.png"
)

# Parkinson’s Detection Pipeline
draw_flowchart(
    "Potential Parkinson’s Disease Screening Pipeline",
    {
        "Finger-Tapping Task": (0.5, 0.75),
        "Tap Timing Recorded\n(ms)": (0.5, 0.60),
        "Motor Variability\nAnalysis": (0.5, 0.45),
        "Comparison to\nHealthy Baseline": (0.5, 0.30),
        "Early Parkinson’s\nRisk Flag": (0.5, 0.15),
    },
    [
        ("Finger-Tapping Task", "Tap Timing Recorded\n(ms)"),
        ("Tap Timing Recorded\n(ms)", "Motor Variability\nAnalysis"),
        ("Motor Variability\nAnalysis", "Comparison to\nHealthy Baseline"),
        ("Comparison to\nHealthy Baseline", "Early Parkinson’s\nRisk Flag"),
    ],
    "results/flow_pd_detection.png"
)
