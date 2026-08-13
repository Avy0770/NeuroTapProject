import matplotlib.pyplot as plt
import textwrap
import os

# =========================
# PAGE SETTINGS
# =========================
PAGE_WIDTH = 8.5
PAGE_HEIGHT = 11
FONT = "Times New Roman"

OUTPUT_DIR = "results"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# =========================
# CONTENT
# =========================
TITLE = "Motor Timing Variability as a Digital Biomarker of Dopamine Loss in Parkinson’s Disease"

AUTHOR_INFO = [
    "Avyaan Maniar",
    "Chantilly High School",
    "Chantilly, Virginia, USA"
]

ABSTRACT_TEXT = (
    "Parkinson’s disease is a progressive neurodegenerative disorder characterized by the loss "
    "of dopamine-producing neurons in the basal ganglia, leading to impaired motor timing and "
    "coordination. Early-stage Parkinson’s disease often presents with subtle motor irregularities "
    "that are difficult to detect through clinical observation. Finger-tapping tasks are commonly "
    "used to assess fine motor control, and increased variability in tapping rhythm has been "
    "associated with early Parkinson’s disease. This study investigated whether dopamine depletion "
    "alone is sufficient to produce measurable increases in finger-tapping variability.\n\n"
    "A computational neuromotor simulation was used to generate finger-tapping data under four "
    "simulated dopamine levels (100%, 80%, 60%, and 40%). Multiple trials were conducted for each "
    "dopamine condition, and tap timestamps were recorded in milliseconds. Inter-tap intervals "
    "were calculated, and motor variability was quantified as the standard deviation of these "
    "intervals. Differences in variability across dopamine levels were evaluated using statistical "
    "analysis.\n\n"
    "The results demonstrated a consistent increase in finger-tapping variability as simulated "
    "dopamine levels decreased. Lower dopamine conditions showed significantly greater variability "
    "in motor timing compared to higher dopamine conditions. Statistical analysis revealed a "
    "highly significant effect of dopamine level on inter-tap interval variability.\n\n"
    "These findings supported the hypothesis that dopamine depletion leads to increased motor "
    "timing variability due to disrupted basal ganglia control. This study suggests that "
    "finger-tapping variability may serve as a sensitive, quantitative, and non-invasive digital "
    "biomarker for early Parkinson’s disease detection."
)

# =========================
# CREATE ABSTRACT PAGE
# =========================
def create_plain_abstract(output_filename="ISEF_Abstract_Plain.pdf"):
    fig = plt.figure(figsize=(PAGE_WIDTH, PAGE_HEIGHT))
    fig.patch.set_facecolor("white")

    # ---- TITLE ----
    fig.text(
        0.5, 0.95,
        TITLE,
        ha="center",
        va="top",
        fontsize=16,
        fontweight="bold",
        fontname=FONT
    )

    # ---- AUTHOR INFO ----
    y = 0.91
    for line in AUTHOR_INFO:
        fig.text(
            0.5, y,
            line,
            ha="center",
            va="top",
            fontsize=11,
            fontname=FONT
        )
        y -= 0.025

    # ---- ABSTRACT BODY ----
    wrapped_text = textwrap.fill(ABSTRACT_TEXT, width=95)

    fig.text(
        0.1, 0.82,
        wrapped_text,
        ha="left",
        va="top",
        fontsize=11,
        fontname=FONT
    )

    plt.savefig(
        os.path.join(OUTPUT_DIR, output_filename),
        dpi=300,
        bbox_inches="tight"
    )
    plt.close()

    print(f"✅ Plain abstract saved to {OUTPUT_DIR}/{output_filename}")

# =========================
# RUN
# =========================
if __name__ == "__main__":
    create_plain_abstract()