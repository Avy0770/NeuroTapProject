import matplotlib.pyplot as plt
import textwrap

# =========================
# STYLING
# =========================
BACKGROUND_COLOR = "white"
HEADER_COLOR = "#1f4ed8"   # medical blue
HEADER_TEXT_COLOR = "white"
BORDER_COLOR = "black"

# =========================
# FUTURE RESEARCH PANEL (BULLET STYLE — FIXED)
# =========================
def make_future_research_panel(filename):
    fig, ax = plt.subplots(figsize=(8.5, 6.5))
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.axis("off")

    left, bottom, width, height = 0.08, 0.08, 0.84, 0.84

    # Main panel
    ax.add_patch(
        plt.Rectangle(
            (left, bottom),
            width,
            height,
            transform=ax.transAxes,
            facecolor="white",
            edgecolor=BORDER_COLOR,
            linewidth=1.5
        )
    )

    # Header
    header_height = 0.14
    ax.add_patch(
        plt.Rectangle(
            (left, bottom + height - header_height),
            width,
            header_height,
            transform=ax.transAxes,
            facecolor=HEADER_COLOR,
            edgecolor=BORDER_COLOR,
            linewidth=1.2
        )
    )

    ax.text(
        left + width / 2,
        bottom + height - header_height / 2,
        "Future Research",
        ha="center",
        va="center",
        fontsize=24,
        fontweight="bold",
        color="white",
        fontname="Times New Roman"
    )

    # Bullet-style future research (ISEF standard)
    future_items = [
        "Validate the computational findings using real finger-tapping data from "
        "individuals with early Parkinson’s disease.",

        "Extend the neuromotor model to incorporate additional features such as fatigue, "
        "tremor, and bilateral asymmetry.",

        "Integrate the analysis into mobile or wearable platforms to enable scalable, "
        "low-cost digital screening tools for Parkinson’s disease."
    ]


    text_left = left + 0.08
    text_top = bottom + height - header_height - 0.07

    wrap_width = 55
    font_size = 16
    line_height = 0.058

    y = text_top
    for item in future_items:
        wrapped = textwrap.wrap(item, wrap_width)
        for i, line in enumerate(wrapped):
            prefix = "– " if i == 0 else "  "
            ax.text(
                text_left,
                y,
                prefix + line,
                ha="left",
                va="top",
                fontsize=font_size,
                fontname="Times New Roman"
        )
            y -= line_height
        y -= line_height * 0.6


    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close()


# =========================
# REFERENCES PANEL (NEWER RESEARCH, TWO COLUMNS)
# =========================
def make_references_panel(filename):
    fig, ax = plt.subplots(figsize=(8.5, 6.5))
    fig.patch.set_facecolor("white")
    ax.set_facecolor("white")
    ax.axis("off")

    left, bottom, width, height = 0.08, 0.08, 0.84, 0.84

    # Main panel
    ax.add_patch(
        plt.Rectangle(
            (left, bottom),
            width,
            height,
            transform=ax.transAxes,
            facecolor="white",
            edgecolor=BORDER_COLOR,
            linewidth=1.5
        )
    )

    # Header
    header_height = 0.14
    ax.add_patch(
        plt.Rectangle(
            (left, bottom + height - header_height),
            width,
            header_height,
            transform=ax.transAxes,
            facecolor=HEADER_COLOR,
            edgecolor=BORDER_COLOR,
            linewidth=1.2
        )
    )

    ax.text(
        left + width / 2,
        bottom + height - header_height / 2,
        "References",
        ha="center",
        va="center",
        fontsize=24,
        fontweight="bold",
        color="white",
        fontname="Times New Roman"
    )

    # Recent (last ~5 years), APA-style, compact
    references = [
        "Arora, S., Venkataraman, V., Zhan, A., et al. (2021). Detecting and monitoring "
        "Parkinson’s disease symptoms using smartphones. Parkinsonism & Related Disorders, "
        "33, 17–23.",

        "Del Din, S., Galna, B., Godfrey, A., et al. (2021). Analysis of free-living gait "
        "in Parkinson’s disease. Movement Disorders, 36(6), 1419–1427.",

        "Espay, A. J., Hausdorff, J. M., Sánchez-Ferro, Á., et al. (2020). A roadmap for "
        "digital outcomes in Parkinson’s disease. Journal of Parkinson’s Disease, "
        "10(S1), S85–S97.",

        "Warmerdam, E., Hausdorff, J. M., Atrsaei, A., et al. (2020). Long-term unsupervised "
        "mobility assessment in movement disorders. The Lancet Neurology, 19(5), 462–470.",

        "Lipsmeier, F., Taylor, K. I., Kilchenmann, T., et al. (2019). Smartphone-based "
        "digital biomarkers of Parkinson’s disease. Movement Disorders, 34(4), 507–516."
    ]

    col1 = references[:3]
    col2 = references[3:]

    wrap_width = 46
    font_size = 9
    line_height = 0.040

    col1_x = left + 0.05
    col2_x = left + width / 2 + 0.02
    start_y = bottom + height - header_height - 0.07

    # Column 1
    y = start_y
    for ref in col1:
        for line in textwrap.wrap(ref, wrap_width):
            ax.text(col1_x, y, line,
                    ha="left", va="top",
                    fontsize=font_size,
                    fontname="Times New Roman")
            y -= line_height
        y -= line_height * 0.55

    # Column 2
    y = start_y
    for ref in col2:
        for line in textwrap.wrap(ref, wrap_width):
            ax.text(col2_x, y, line,
                    ha="left", va="top",
                    fontsize=font_size,
                    fontname="Times New Roman")
            y -= line_height
        y -= line_height * 0.55

    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close()


# =========================
# GENERATE PANELS
# =========================
make_future_research_panel("results/panel_future_work.png")
make_references_panel("results/panel_references.png")
