import matplotlib.pyplot as plt
import textwrap

# =========================
# TINY CAPTION PANEL
# =========================
def make_caption_panel(
    caption_text,
    output_path,
    font_size=10,      # VERY SMALL
    wrap_width=90
):
    fig, ax = plt.subplots(figsize=(8, 2))  # SHORT + WIDE
    ax.axis("off")
    fig.patch.set_facecolor("white")

    wrapped = textwrap.fill(caption_text, wrap_width)

    ax.text(
        0.5,
        0.5,
        wrapped,
        ha="center",
        va="center",
        fontsize=font_size,
        fontname="Times New Roman"
    )

    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    plt.close()


# =========================
# CAPTIONS
# =========================

make_caption_panel(
    "Figure 1. Dopaminergic modulation of basal ganglia motor pathways involved in movement timing. "
    "Graybiel, A. M. (2019). Basal ganglia motor circuits and dopamine modulation [Diagram]. "
    "Wikimedia Commons.",
    "results/figure1_caption.png"
)

make_caption_panel(
    "Figure 2. Finger-tapping task used to assess fine motor timing and rhythm in neurological evaluation. "
    "Stanford Medicine. (2024). Parkinson’s remote monitoring tools. https://med.stanford.edu",
    "results/figure2_caption.png"
)

make_caption_panel(
    "Figure 3. Increased motor timing variability associated with neurological dysfunction and dopamine loss. "
    "Del Din, S., et al. (2020). Frontiers in Neurology, 11, 477. https://doi.org/10.3389/fneur.2020.00477",
    "results/figure3_caption.png"
)

make_caption_panel(
    "Figure 4. Digital motor assessment pipeline linking task performance, feature extraction, and clinical insight. "
    "Scientific Reports. (2024). Digital biomarkers for neurological disease. "
    "https://doi.org/10.1038/s41598-024-63946-4",
    "results/figure4_caption.png"
)