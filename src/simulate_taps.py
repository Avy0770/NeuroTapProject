
import numpy as np
import csv
from pathlib import Path

OUT_DIR = Path("data")
OUT_DIR.mkdir(exist_ok=True)

def simulate_trial(hand: str, dopamine_level: int, duration_s: int = 30, base_hz: float = 5.0):
    rng = np.random.default_rng()

    mean_iti_ms = 1000.0 / base_hz
    # Lower dopamine => higher timing noise
    noise_sd_ms = np.interp(dopamine_level, [40, 100], [60, 15])

    taps = []
    t = 0.0
    while t < duration_s * 1000:
        iti = rng.normal(mean_iti_ms, noise_sd_ms)
        iti = max(50, iti)
        t += iti
        if t <= duration_s * 1000:
            taps.append(t)
    return taps

def save_csv(trial_id: str, hand: str, dopamine_level: int, taps_ms: list[float]):
    out = OUT_DIR / f"{trial_id}.csv"
    with out.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["trial_id", "hand", "dopamine_level_percent", "tap_index", "tap_time_ms"])
        for i, t in enumerate(taps_ms, start=1):
            w.writerow([trial_id, hand, dopamine_level, i, round(float(t), 3)])
    print(f"Saved: {out}")

if __name__ == "__main__":
    for dopamine in [100, 80, 60, 40]:
        for hand in ["R", "L"]:
            for trial_num in [1, 2, 3]:
                trial_id = f"SIM_{hand}_{dopamine}_{trial_num}"
                taps = simulate_trial(hand, dopamine)
                save_csv(trial_id, hand, dopamine, taps)
