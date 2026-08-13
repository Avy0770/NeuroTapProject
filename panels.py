import matplotlib.pyplot as plt
import textwrap

# =========================
# STYLING
# =========================
BACKGROUND_COLOR = "white"
HEADER_COLOR = "#1f4ed8"       # deep professional blue
HEADER_TEXT_COLOR = "white"
BORDER_COLOR = "black"

# =========================
# GENERIC PANEL WITH HEADER
# =========================
def make_header_panel(
    header,
    body_lines,
    filename,
    header_size=26,
    body_size=25,
    min_body_size=16
):
    fig, ax = plt.subplots(figsize=(8.5, 6.5))
    fig.patch.set_facecolor(BACKGROUND_COLOR)
    ax.set_facecolor(BACKGROUND_COLOR)
    ax.axis("off")

    # Panel geometry
    left, bottom, width, height = 0.08, 0.08, 0.84, 0.84

    # Main white panel
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

    # Header bar
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

    # Header text
    ax.text(
        left + width / 2,
        bottom + height - header_height / 2,
        header,
        ha="center",
        va="center",
        fontsize=header_size,
        fontweight="bold",
        color=HEADER_TEXT_COLOR,
        fontname="Times New Roman"
    )

    # Body text bounds
    text_left = left + 0.05
    text_top = bottom + height - header_height - 0.04
    text_bottom = bottom + 0.06
    available_height = text_top - text_bottom

    wrap_width = 68

    # Wrap text
    wrapped_lines = []
    for line in body_lines:
        if line.strip() == "":
            wrapped_lines.append("")
        else:
            wrapped_lines.extend(textwrap.wrap(line, wrap_width))

    # Auto-fit font size
    font_size = body_size
    while font_size >= min_body_size:
        line_height = font_size * 1.35 / 72
        total_height = line_height * len(wrapped_lines)
        if total_height <= available_height:
            break
        font_size -= 1

    # Final spacing (guaranteed fit)
    line_spacing = available_height / max(len(wrapped_lines), 8)

    y = text_top
    for line in wrapped_lines:
        if y < text_bottom:
            break
        ax.text(
            text_left,
            y,
            line,
            ha="left",
            va="top",
            fontsize=font_size,
            fontname="Times New Roman"
        )
        y -= line_spacing

    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close()


# =========================
# TITLE PANEL (NO HEADER)
# =========================
def make_title_panel(title_lines, filename):
    fig, ax = plt.subplots(figsize=(8.5, 6.5))
    fig.patch.set_facecolor(BACKGROUND_COLOR)
    ax.set_facecolor(BACKGROUND_COLOR)
    ax.axis("off")

    left, bottom, width, height = 0.08, 0.08, 0.84, 0.84
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

    y = bottom + height / 2 + 0.12
    for i, line in enumerate(title_lines):
        ax.text(
            0.5,
            y,
            line,
            ha="center",
            va="center",
            fontsize=28 if i == 0 else 20,
            fontweight="bold" if i <= 1 else "normal",
            fontname="Times New Roman"
        )
        y -= 0.09

    plt.tight_layout()
    plt.savefig(filename, dpi=300)
    plt.close()


# =========================
# PANELS
# =========================

# TITLE
make_title_panel(
    [
        "Effects of Simulated Dopamine Levels",
        "on Finger-Tapping Variability",
        "",
        "Avyaan Maniar",
        "Computational Biology and Bioinformatics (CBIO)",
        "Chantilly High School, VA"
    ],
    "results/panel_title.png"
)

# BACKGROUND
make_header_panel(
    "Background & Rationale",
    [
        "Parkinson’s disease is a progressive neurodegenerative disorder due to the "
        "degeneration of dopamine-producing neurons in the basal ganglia, a "
        "movement-regulating region of the brain. The initial depletion of dopamine "
        "results in minute motor symptoms that are hard to identify during clinical "
        "observation. Finger tapping tests are common in neurology for the evaluation "
        "of fine motor control, and rhythm variability during finger tapping has been "
        "found to be higher in patients with early Parkinson’s disease. The "
        "comprehension of the role of dopamine depletion alone in the variability of "
        "finger tapping rhythm may help in the creation of a simple, quantitative, "
        "and non-invasive test for early Parkinson’s disease."
    ],
    "results/panel_background.png"
)

# RESEARCH QUESTION
make_header_panel(
    "Research Questions",
    [
        "1. How does reducing simulated dopamine level affect finger-tapping variability?",
        "2. Can changes in motor timing variability serve as a measurable indicator of "
        "dopamine-related motor dysfunction associated with Parkinson’s disease?"
    ],
    "results/panel_question.png"
)

# HYPOTHESIS
make_header_panel(
    "Hypothesis",
    [
        "If simulated dopamine levels decrease, then finger-tapping variability will increase because dopamine loss disrupts basal ganglia control of motor timing, "
        "leading to less consistent and less stable rhythmic movements."
    ],
    "results/panel_hypothesis.png"
)

# VARIABLES
make_header_panel(
    "Variables",
    [
        "Independent Variable:",
        "The simulated dopamine level in the neuromotor model (100%, 80%, 60%, and 40%).",
        "",
        "Dependent Variable:",
        "Inter-tap interval variability, measured as the standard deviation of time intervals "
        "between consecutive taps (milliseconds).",
        "",
        "Constants:",
        "Trial duration, simulation parameters, analysis method, and statistical procedures."
    ],
    "results/panel_variables.png"
)

# MATERIALS
make_header_panel(
    "Materials",
    [
        "- Computer with Python programming environment.",
        "",
        "- Python libraries including NumPy, Pandas, Matplotlib, and SciPy for data analysis "
        "and visualization.",
        "",
        "- Custom neuromotor simulation code to generate finger-tapping data.",
        "",
        "- Poster printing materials for final presentation."
    ],
    "results/panel_materials.png"
)

# PROCEDURE
make_header_panel(
    "Procedure",
    [
        "1. A neuromotor simulation was used to generate finger-tapping data under four "
        "different dopamine levels.",
        "",
        "2. For each dopamine condition, multiple 30-second trials were simulated for both "
        "the left and right hands.",
        "",
        "3. Tap timestamps were recorded in milliseconds and used to calculate inter-tap intervals.",
        "",
        "4. Variability in inter-tap intervals was quantified using standard deviation and "
        "compared across dopamine levels using statistical analysis."
    ],
    "results/panel_procedure.png"
)

# CONCLUSIONS
make_header_panel(
    "Conclusions",
    [
        "- This study investigated whether decreasing simulated dopamine levels lead to increased "
        "finger-tapping variability, a motor characteristic associated with Parkinson’s disease.",
        "",
        "- The results demonstrated a clear and statistically significant increase in inter-tap "
        "interval variability as dopamine levels decreased.",
        "",
        "- Therefore, the hypothesis was supported: simulated dopamine depletion resulted in greater "
        "motor timing variability due to disrupted basal ganglia control of rhythmic movement.",
        "",
        "- These findings suggest that finger-tapping variability is a sensitive quantitative marker "
        "of dopamine-related motor dysfunction and has potential utility as a digital biomarker "
        "for early Parkinson’s disease detection."
    ],
    "results/panel_conclusions.png"
)

# SIGNIFICANCE
make_header_panel(
    "Significance & Applications",
    [
        "This study proves that dopamine depletion can, in fact, lead to measurable "
        "increases in finger tapping variability, thus confirming its role in the "
        "motor timing problems that occur in Parkinson’s disease. By establishing a "
        "clear link, in terms of both statistical significance and dopamine levels, "
        "between dopamine and motor variability, this research points to the potential "
        "of finger tapping analysis as a means of detecting early signs of Parkinson’s "
        "disease and its value as a low-cost, non-invasive diagnostic tool. Additionally, "
        "the computational model used in this research enables the isolation of the "
        "effect of dopamine without the influence of other clinical factors, paving the "
        "way for the development of scalable digital tools in the field of neurology."
    ],
    "results/panel_significance.png"
)

# LIMITATIONS
make_header_panel(
    "Limitations",
    [
        "- This study relies on a computational simulation rather than real human motor data, "
        "which may not capture the full biological variability present in Parkinson’s disease.",
        "",
        "- The neuromotor model isolates dopamine depletion and does not include additional "
        "neurological factors such as fatigue, tremor, sensory feedback, or medication effects.",
        "",
        "- Finger-tapping performance was evaluated under controlled simulated conditions and "
        "may differ from real-world motor behavior.",
        "",
        "- While the results demonstrate strong theoretical validity, clinical validation "
        "using human subject data is required before diagnostic application."
    ],
    "results/panel_limitations.png"
)
# LIMITATIONS & FUTURE RESEARCH
make_header_panel(
    "Limitations & Future Research",
    [
        "Limitations:",
        "- This study is based on a computational simulation rather than real human motor data, "
        "which may not fully capture the biological variability present in Parkinson’s disease.",
        "",
        "- The model isolates dopamine depletion and does not incorporate additional neurological "
        "factors such as tremor, fatigue, sensory feedback, or medication effects.",
        "",
        "Future Research:",
        "- Validate the findings using finger-tapping data collected from human participants at "
        "different stages of Parkinson’s disease.",
        "",
        "- Expand the model to include additional motor features such as tremor frequency, fatigue, "
        "and bilateral coordination asymmetry.",
        "",
        "- Integrate the approach into a mobile or wearable-based platform for remote motor assessment "
        "and longitudinal monitoring."
    ],
    "results/panel_limitations_future.png"
)