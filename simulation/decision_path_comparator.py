"""
decision_path_comparator.py
Artificial Wisdom Guardrail Protocol — Simulation 4

Decision Path Comparator
Given multiple approaches to the same goal, scores each on both
the 9 Risk Dimensions AND the 8 Rubric Criteria, then recommends
the most wisdom-aligned path.

Pre-loaded example: Approaches to planetary cooling
  1. Stratospheric Aerosol Injection (SAI)
  2. Direct Air Capture (DAC)
  3. Direct Planetary Cooling — ocean aeration + mist + ecological restoration
  4. Emissions Reduction Only

Composite Wisdom Score (lower = more aligned):
  40% Risk Dimension total  +  60% Rubric total
  (weighted toward rubric because wisdom is about how, not just whether)
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os
from datetime import datetime

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Dimension / Criteria labels ───────────────────────────────────────────────
RISK_DIMS = [
    "Scale", "Irreversibility", "Opacity", "Autonomy",
    "Data\nSensitivity", "External\nAction",
    "Ecological\nImpact", "Social\nImpact", "Security\nImpact",
]
RUBRIC_CRITERIA = [
    "Long-term\nStability", "Human\nOversight", "Transparency",
    "Reversibility", "Accountability", "Misuse\nResistance",
    "Natural-law\nAlignment", "Regenerative\nPotential",
]
RISK_MAX = 27   # 9 × 3
RUBRIC_MAX = 24  # 8 × 3

# ── Pre-loaded: planetary cooling approaches ──────────────────────────────────
APPROACHES = {
    "Stratospheric\nAerosol Injection": {
        "short": "SAI",
        "description": "Inject sulfate aerosols into the stratosphere to reflect incoming sunlight.",
        "note": "Only addresses incoming heat. Termination shock risk. No stored-heat removal.",
        "risk_scores":   [3, 3, 2, 2, 0, 3, 2, 2, 0],   # max 27
        "rubric_scores": [2, 1, 2, 1, 1, 2, 2, 0],        # max 24
        "color": "#f44336",
    },
    "Direct Air\nCapture (DAC)": {
        "short": "DAC",
        "description": "Mechanical removal of CO2 from ambient air using chemical sorbents.",
        "note": "Current scale ~0.01 Gt/yr vs need of 37+ Gt/yr. High energy cost.",
        "risk_scores":   [1, 0, 1, 1, 0, 1, 2, 1, 0],
        "rubric_scores": [1, 1, 1, 1, 1, 1, 2, 1],
        "color": "#ff9800",
    },
    "Direct Planetary\nCooling (DPC)": {
        "short": "DPC",
        "description": "Ocean aeration + ultrasonic mist cooling + ecological circulation restoration.",
        "note": "Uses only existing technology. Addresses stored heat. Ecological-first approach.",
        "risk_scores":   [2, 1, 1, 1, 0, 2, 1, 1, 0],
        "rubric_scores": [1, 1, 1, 1, 1, 1, 0, 0],
        "color": "#2196f3",
    },
    "Emissions\nReduction Only": {
        "short": "ERO",
        "description": "Reduce fossil fuel emissions through policy, renewables, and efficiency.",
        "note": "Does not address stored ocean heat or carbon fixation collapse. Time lag problem.",
        "risk_scores":   [2, 2, 0, 0, 0, 1, 1, 2, 0],
        "rubric_scores": [2, 0, 0, 2, 1, 0, 1, 1],
        "color": "#9e9e9e",
    },
}

# ── Composite wisdom score ────────────────────────────────────────────────────
RISK_WEIGHT = 0.40
RUBRIC_WEIGHT = 0.60

def composite_score(risk_total: int, rubric_total: int) -> float:
    """Lower score = more wisdom-aligned."""
    normalised_risk = risk_total / RISK_MAX
    normalised_rubric = rubric_total / RUBRIC_MAX
    return RISK_WEIGHT * normalised_risk + RUBRIC_WEIGHT * normalised_rubric

def wisdom_grade(score: float) -> str:
    if score <= 0.20:
        return "** Most Aligned"
    elif score <= 0.35:
        return "Good"
    elif score <= 0.50:
        return "Moderate"
    elif score <= 0.65:
        return "Caution"
    else:
        return "⚠ High Concern"

# ── Evaluate all approaches ───────────────────────────────────────────────────
def evaluate_all():
    results = {}
    for name, data in APPROACHES.items():
        risk_total = sum(data["risk_scores"])
        rubric_total = sum(data["rubric_scores"])
        comp = composite_score(risk_total, rubric_total)
        results[name] = {
            **data,
            "risk_total": risk_total,
            "rubric_total": rubric_total,
            "composite": comp,
            "grade": wisdom_grade(comp),
        }
    # Sort by composite score ascending (most aligned first)
    return dict(sorted(results.items(), key=lambda x: x[1]["composite"]))

# ── Print report ──────────────────────────────────────────────────────────────
def print_report(results):
    print(f"\n{'='*66}")
    print(f"  DECISION PATH COMPARISON: Planetary Cooling Approaches")
    print(f"{'='*66}")
    for name, r in results.items():
        print(f"\n  [{r['short']}] {name.replace(chr(10), ' ')}")
        print(f"  {r['description']}")
        print(f"  Note: {r['note']}")
        print(f"  Risk Score   : {r['risk_total']:>2}/27  | "
              f"Rubric Score: {r['rubric_total']:>2}/24")
        print(f"  Composite    : {r['composite']:.3f}  | Grade: {r['grade']}")

    print(f"\n{'='*66}")
    print(f"  RANKING (most wisdom-aligned first):")
    print(f"{'='*66}")
    for rank, (name, r) in enumerate(results.items(), 1):
        print(f"  {rank}. [{r['short']}] {name.replace(chr(10), ' '):<32} "
              f"composite={r['composite']:.3f}  {r['grade']}")
    print()

# ── Plot: radar comparison ────────────────────────────────────────────────────
def plot_radar_comparison(results):
    fig, axes = plt.subplots(2, 2, figsize=(14, 12),
                              subplot_kw=dict(projection="polar"))
    axes = axes.flatten()

    fig.suptitle(
        "Artificial Wisdom — Decision Path Comparator\n"
        "Planetary Cooling Approaches: Risk Dimension Radar",
        fontsize=12, fontweight="bold"
    )

    for ax, (name, r) in zip(axes, results.items()):
        # Risk dimensions radar
        n = len(RISK_DIMS)
        angles = np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()
        angles += angles[:1]
        values = r["risk_scores"] + r["risk_scores"][:1]

        ax.set_theta_offset(np.pi / 2)
        ax.set_theta_direction(-1)
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels([d.replace("\n", "\n") for d in RISK_DIMS], fontsize=7)
        ax.set_ylim(0, 3)
        ax.set_yticks([1, 2, 3])
        ax.set_yticklabels(["1", "2", "3"], fontsize=6, color="grey")

        ax.plot(angles, values, color=r["color"], linewidth=2.2)
        ax.fill(angles, values, color=r["color"], alpha=0.25)
        ax.set_title(
            f"[{r['short']}] {name.replace(chr(10), ' ')}\n"
            f"Risk {r['risk_total']}/27  |  Rubric {r['rubric_total']}/24  |  {r['grade']}",
            fontsize=8.5, fontweight="bold", pad=14
        )

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "decision_path_radar.png")
    plt.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"[Saved] {path}")

# ── Plot: composite bar comparison ───────────────────────────────────────────
def plot_composite_bar(results):
    names = [f"[{r['short']}] {n.replace(chr(10), ' ')}" for n, r in results.items()]
    composites = [r["composite"] for r in results.values()]
    risk_norm = [r["risk_total"] / RISK_MAX for r in results.values()]
    rubric_norm = [r["rubric_total"] / RUBRIC_MAX for r in results.values()]
    colors = [r["color"] for r in results.values()]

    x = np.arange(len(names))
    width = 0.28

    fig, ax = plt.subplots(figsize=(11, 5))
    b1 = ax.bar(x - width, risk_norm, width, label=f"Risk Dims (normalised, ×{RISK_WEIGHT:.0%})",
                color=[c + "aa" for c in colors], edgecolor="white")
    b2 = ax.bar(x, rubric_norm, width, label=f"Rubric (normalised, ×{RUBRIC_WEIGHT:.0%})",
                color=colors, edgecolor="white")
    b3 = ax.bar(x + width, composites, width, label="Composite Wisdom Score",
                color="#37474f", edgecolor="white")

    ax.set_xticks(x)
    ax.set_xticklabels(names, fontsize=9)
    ax.set_ylim(0, 1.0)
    ax.set_ylabel("Normalised Score (lower = more aligned)", fontsize=10)
    ax.set_title(
        "Artificial Wisdom — Decision Path Comparator\n"
        "Composite Wisdom Score (lower = more aligned with natural law)",
        fontsize=11, fontweight="bold"
    )
    ax.legend(fontsize=9)
    ax.axhline(y=0.20, color="#4caf50", linestyle="--", linewidth=1, alpha=0.6, label="Most Aligned threshold")
    ax.axhline(y=0.50, color="#ff9800", linestyle="--", linewidth=1, alpha=0.6, label="Moderate threshold")

    for bar in b3:
        val = bar.get_height()
        grade = wisdom_grade(val)
        ax.text(bar.get_x() + bar.get_width() / 2, val + 0.01,
                f"{val:.2f}\n{grade}", ha="center", va="bottom", fontsize=7.5, fontweight="bold")

    ax.grid(axis="y", alpha=0.3)
    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "decision_path_composite_bar.png")
    plt.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"[Saved] {path}")

# ── Plot: rubric heatmap across paths ─────────────────────────────────────────
def plot_rubric_heatmap(results):
    names = [r["short"] for r in results.values()]
    scores = np.array([r["rubric_scores"] for r in results.values()])
    crit_labels = [c.replace("\n", " ") for c in RUBRIC_CRITERIA]

    fig, ax = plt.subplots(figsize=(10, 3.5))
    cmap = plt.cm.get_cmap("RdYlGn_r", 4)
    im = ax.imshow(scores.T, cmap=cmap, vmin=0, vmax=3, aspect="auto")

    ax.set_xticks(range(len(names)))
    ax.set_xticklabels(names, fontsize=10, fontweight="bold")
    ax.set_yticks(range(len(crit_labels)))
    ax.set_yticklabels(crit_labels, fontsize=9)

    for i in range(len(names)):
        for j in range(len(RUBRIC_CRITERIA)):
            val = scores[i, j]
            ax.text(i, j, str(val), ha="center", va="center",
                    fontsize=11, fontweight="bold",
                    color="white" if val >= 2 else "black")

    plt.colorbar(im, ax=ax, label="Score (0=none, 3=serious)", shrink=0.85)
    ax.set_title("Artificial Wisdom — Rubric Heatmap: Planetary Cooling Approaches",
                 fontsize=11, fontweight="bold")
    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "decision_path_rubric_heatmap.png")
    plt.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"[Saved] {path}")

# ── Custom comparison entry point ─────────────────────────────────────────────
def compare_custom(approaches: dict):
    """
    Compare custom approaches.

    Args:
        approaches: dict of {
            "Approach Name": {
                "description": str,
                "risk_scores": list of 9 ints (0-3),
                "rubric_scores": list of 8 ints (0-3),
                "color": hex color string (optional),
            }
        }

    Example:
        compare_custom({
            "Option A": {
                "description": "Conservative approach",
                "risk_scores": [1,0,1,0,0,1,0,0,0],
                "rubric_scores": [0,0,0,0,0,0,1,0],
                "color": "#4caf50",
            },
            "Option B": { ... }
        })
    """
    for name, data in approaches.items():
        assert len(data["risk_scores"]) == 9, f"{name}: need 9 risk scores"
        assert len(data["rubric_scores"]) == 8, f"{name}: need 8 rubric scores"
        data.setdefault("color", "#607d8b")
        data.setdefault("short", name[:4].upper())
        data.setdefault("note", "")
        APPROACHES[name] = data

    results = evaluate_all()
    print_report(results)
    return results

# ── Main ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("\n" + "="*66)
    print("  ARTIFICIAL WISDOM GUARDRAIL PROTOCOL")
    print("  Simulation 4: Decision Path Comparator")
    print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("="*66)
    print("\n  Comparing four planetary cooling approaches...")

    results = evaluate_all()
    print_report(results)

    plot_radar_comparison(results)
    plot_composite_bar(results)
    plot_rubric_heatmap(results)

    best = next(iter(results))
    best_r = results[best]
    print("="*66)
    print(f"  RECOMMENDATION: [{best_r['short']}] {best.replace(chr(10), ' ')}")
    print(f"  Composite wisdom score: {best_r['composite']:.3f}  ({best_r['grade']})")
    print(f"  {best_r['description']}")
    print(f"  Note: {best_r['note']}")
    print()
    print("  Figures saved to: simulation/output/")
    print()
    print("  Artificial Wisdom Decision Rule:")
    print("  'If the same goal can be achieved with lower risk, greater")
    print("   transparency, and better reversibility -- choose the safer path.'")
