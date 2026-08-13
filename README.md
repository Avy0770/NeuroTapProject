# Motor Timing Variability as a Digital Biomarker of Dopamine Loss in Parkinson’s Disease

## Overview

This project uses a computational neuromotor simulation to investigate how simulated dopamine depletion affects finger-tapping motor timing variability. The model compares four simulated dopamine levels—100%, 80%, 60%, and 40%—and measures changes in inter-tap interval (ITI) variability.

The main goal is to determine whether reduced dopamine alone can produce measurable increases in motor timing variability associated with Parkinson’s disease. The project also explores the potential use of finger-tapping variability as a simple, quantitative digital biomarker for dopamine-related motor dysfunction.

## Research Question

How does reducing simulated dopamine level affect finger-tapping variability, and can motor timing variability serve as a measurable indicator of dopamine-related motor dysfunction associated with Parkinson’s disease?

## Hypothesis

If simulated dopamine levels decrease from 100% to 80%, 60%, and 40%, then inter-tap interval variability will increase because dopamine depletion disrupts basal ganglia regulation of motor timing, producing less consistent rhythmic movement.

## Experimental Design

### Independent Variable

Simulated dopamine level:

- 100% — control
- 80%
- 60%
- 40%

### Dependent Variable

Inter-tap interval variability, calculated as the standard deviation of ITIs in milliseconds.

### Trials

- 4 dopamine levels
- 2 modeled tapping channels representing left and right hands
- 3 trials per channel per dopamine level
- 24 total trials
- 30 seconds per trial

## Project Workflow

1. Initialize the neuromotor simulation at a selected dopamine level.
2. Generate a 30-second finger-tapping sequence.
3. Record simulated tap timestamps in milliseconds.
4. Calculate inter-tap intervals.
5. Calculate ITI variability using standard deviation.
6. Group results by dopamine level.
7. Compare dopamine conditions statistically using one-way ANOVA.
8. Visualize the results using boxplots and summary graphs.

## Data Analysis

The project uses Python for simulation, processing, statistics, and visualization.

Main analysis steps include:

- Calculating inter-tap intervals from tap timestamps
- Measuring ITI variability for each trial
- Grouping variability values by dopamine level
- Calculating descriptive statistics
- Performing one-way ANOVA
- Creating boxplots and summary graphs

The final analysis found a statistically significant effect of simulated dopamine level on motor timing variability.

**ANOVA result:** F = 622.53, p < 0.001

## Main Finding

Finger-tapping variability increased as simulated dopamine levels decreased. The lowest dopamine conditions produced the greatest motor timing variability.

The results supported the hypothesis that simulated dopamine depletion increases motor timing variability.

## Project Structure

```text
NeuroTapProject/
├── assets/
│   ├── basal_ganglia_dopamine.png
│   ├── finger_tapping_task.png
│   ├── variability_concept.png
│   └── digital_health_pipeline.png
│
├── data/
│   └── simulation CSV files
│
├── results/
│   ├── graphs
│   ├── poster panels
│   ├── flowcharts
│   └── figure captions
│
├── src/
│   ├── simulate.py
│   ├── analyze.py
│   ├── panels.py
│   ├── flowcharts.py
│   └── supplemental_panels.py
│
└── README.md
```

File names may vary slightly depending on the final version of the project.

## Main Scripts

### `simulate.py`

Generates simulated finger-tapping data under different dopamine conditions and saves the results for later analysis.

### `analyze.py`

Loads the simulated data, calculates motor timing variability, performs statistical analysis, and generates graphs.

### `panels.py`

Creates the main science-fair poster panels using the project’s white background and medical-blue header design.

### `flowcharts.py`

Generates visual flowcharts for:

- Experimental design
- Data analysis
- Potential Parkinson’s disease screening applications

### `supplemental_panels.py`

Creates additional poster sections such as:

- Future research
- References
- Limitations and future research

## Technologies Used

- Python
- NumPy
- Pandas
- SciPy
- Matplotlib
- Pillow
- CSV data files

## Installation

Create and activate a Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the main dependencies:

```bash
pip install numpy pandas scipy matplotlib pillow
```

## Running the Project

Run commands from the root of the project directory.

### 1. Generate simulated data

```bash
python3 src/simulate.py
```

### 2. Analyze the data

```bash
python3 src/analyze.py
```

### 3. Generate poster panels

```bash
python3 src/panels.py
```

### 4. Generate flowcharts

```bash
python3 src/flowcharts.py
```

### 5. Generate supplemental panels

```bash
python3 src/supplemental_panels.py
```

## Poster Figures

The project includes several supporting visuals:

- Basal ganglia and dopamine pathway diagram
- Finger-tapping task image
- Motor timing variability figure
- Digital biomarker pipeline
- Experimental design flowchart
- Data analysis pipeline
- Potential Parkinson’s disease screening pipeline
- ITI variability graphs

## Limitations

- The project uses computational simulation rather than human-subject data.
- The model isolates dopamine depletion and does not represent every biological factor involved in Parkinson’s disease.
- Real motor behavior may also be affected by tremor, fatigue, medication, sensory feedback, disease stage, and other neurological factors.
- The model should not be interpreted as a diagnostic system.

## Future Research

Future work could:

- Validate the model using real finger-tapping data
- Compare healthy and Parkinson’s disease cohorts
- Add tremor, fatigue, and bilateral asymmetry to the model
- Explore smartphone or wearable implementation
- Investigate machine-learning methods for classifying motor variability patterns

## Applications

Finger-tapping tasks are simple, fast, and non-invasive. If validated with clinical data, quantitative motor timing analysis could contribute to low-cost digital tools for monitoring Parkinson’s-related motor changes. The computational approach also provides a controlled way to study how dopamine-related changes influence motor timing.

## Selected References

Amo-Salas, J., Olivares-Gil, A., García-Bustillo, Á., García-García, D., Arnaiz-González, Á., & Cubo, E. (2024). Computer vision for Parkinson’s disease evaluation: A survey on finger tapping. *Healthcare, 12*(4), 439. https://doi.org/10.3390/healthcare12040439

Marsili, L., Abanto, J., Mahajan, A., Duque, K. R., Chinchihualpa Paredes, N. O., Deraz, H. A., Espay, A. J., & Bologna, M. (2024). Dysrhythmia as a prominent feature of Parkinson’s disease: An app-based tapping test. *Journal of the Neurological Sciences, 463*, 123144. https://doi.org/10.1016/j.jns.2024.123144

Qi, W., Shen, S., Dong, C., Zhao, M., Zang, S., Zhu, X., Li, J., Wang, B., Shi, Y., Dong, Y., Shen, H., Kang, J., Lu, X., Jiang, G., Du, J., Shu, E., Zhou, Q., Wang, J., & Cao, S. (2025). Digital biomarkers for Parkinson’s disease: A bibliometric analysis and a scoping review of deep learning for freezing of gait. *Journal of Medical Internet Research, 27*, e71560. https://doi.org/10.2196/71560

Senft, V., Stewart, T. C., Bekolay, T., Eliasmith, C., & Kröger, B. J. (2018). Inhibiting basal ganglia regions reduces syllable sequencing errors in Parkinson’s disease: A computer simulation study. *Frontiers in Computational Neuroscience, 12*, 41. https://doi.org/10.3389/fncom.2018.00041

Sun, Y.-M., Wang, Z.-Y., Liang, Y.-Y., Hao, C.-W., & Shi, C.-H. (2024). Digital biomarkers for precision diagnosis and monitoring in Parkinson’s disease. *npj Digital Medicine, 7*, 218. https://doi.org/10.1038/s41746-024-01217-2

## Disclaimer

This project is a computational research study and is not intended to diagnose Parkinson’s disease or replace evaluation by a healthcare professional.

## Author

**Avyaan Maniar**  
Chantilly High School, Virginia  
Biomedical & Health Sciences
