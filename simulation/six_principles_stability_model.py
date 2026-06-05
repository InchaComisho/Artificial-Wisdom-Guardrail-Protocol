"""
six_principles_stability_model.py
Artificial Wisdom Guardrail Protocol — Simulation 3

Six Principles (六つの理) System Stability Model

Models how adherence to the six natural law principles affects
civilizational system stability over time.

The Six Principles:
  p1: 摂理 (Providence / Natural Law)
  p2: 調和 (Harmony)
  p3: 循環 (Circulation)
  p4: 構造 (Structure)
  p5: 秩序 (Order)
  p6: 和   (Wa — the integrating meta-principle)

Dynamics:
  - Each principle drifts toward a scenario-specific target
  - Principles support each other through a coupling matrix
  - Wa (p6) amplifies all coupling effects: low Wa → principles decouple
  - If any principle falls below a collapse threshold (0.2),
    it accelerates degradation in coupled principles
  - System stability = weighted mean of all six principles

Scenarios:
  1. Healthy Civilization          — All principles near 1.0, stable
  2. Industrial Decline            — Natural law / circulation / structure eroding
  3. Cascade Collapse              — Multiple principles violated simultaneously
  4. Restoration via DPC / AW     — Starts degraded; systematic restoration applied
  5. Wa-First Recovery             — Wa restored first; others follow by coupling
"""

import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import os
from datetime import datetime

OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# ── Principle labels ─────────────────────────────────────────────────────────
PRINCIPLES = ["摂理\n(Providence)", "調和\n(Harmony)", "循環\n(Circulation)",
              "構造\n(Structure)", "秩序\n(Order)", "和\n(Wa)"]
PRINCIPLE_COLORS = ["#2196f3", "#4caf50", "#00bcd4", "#795548", "#ff9800", "#9c27b0"]
COLLAPSE_THRESHOLD = 0.15

# ── Coupling matrix ───────────────────────────────────────────────────────────
# A[i,j]: how much principle j SUPPORTS principle i
# (positive = j being high helps i recover)
COUPLING = np.array([
    #  p1    p2    p3    p4    p5    p6
    [0.00, 0.00, 0.20, 0.00, 0.00, 0.15],  # p1 (摂理)  ← circulation, Wa
    [0.00, 0.00, 0.00, 0.00, 0.15, 0.15],  # p2 (調和)  ← order, Wa
    [0.20, 0.00, 0.00, 0.20, 0.00, 0.10],  # p3 (循環)  ← natural law, structure, Wa
    [0.00, 0.00, 0.20, 0.00, 0.00, 0.10],  # p4 (構造)  ← circulation, Wa
    [0.00, 0.20, 0.00, 0.15, 0.00, 0.15],  # p5 (秩序)  ← harmony, structure, Wa
    [0.05, 0.05, 0.05, 0.05, 0.05, 0.00],  # p6 (和)    ← all principles weakly
])

# ── ODE model ────────────────────────────────────────────────────────────────
def six_principles_ode(t, y, scenario):
    p = np.clip(y, 0.0, 1.0)
    wa = max(p[5], 0.05)   # Wa as global coupling amplifier

    # Support from other principles (coupling × Wa)
    support = (COUPLING @ p) * wa

    # Drift toward scenario targets (externally applied pressure)
    target = scenario["targets"](t)
    drift_rate = scenario["drift_rate"]
    drift = drift_rate * (target - p)

    # Cascade collapse: principle below threshold drags coupled ones down
    cascade = np.zeros(6)
    for i, pi in enumerate(p):
        if pi < COLLAPSE_THRESHOLD:
            collapse_force = (COLLAPSE_THRESHOLD - pi) * 0.4
            # Propagate to coupled principles via COUPLING column i
            cascade -= COUPLING[:, i] * collapse_force

    dp = support + drift + cascade
    # Enforce bounds
    dp = np.where(p >= 1.0, np.minimum(dp, 0.0), dp)
    dp = np.where(p <= 0.0, np.maximum(dp, 0.0), dp)
    return dp

# ── Stability metric ──────────────────────────────────────────────────────────
WEIGHTS = np.array([0.20, 0.15, 0.20, 0.15, 0.15, 0.15])  # Wa slightly lower (meta)

def system_stability(p_array):
    return np.average(p_array, axis=1, weights=WEIGHTS)

# ── Scenarios ────────────────────────────────────────────────────────────────
def make_scenarios():
    t_span = (0, 200)
    t_eval = np.linspace(0, 200, 1000)

    scenarios = {}

    # 1. Healthy Civilization
    scenarios["Healthy\nCivilization"] = {
        "y0": [0.90, 0.85, 0.88, 0.87, 0.85, 0.92],
        "targets": lambda t: np.array([0.90, 0.85, 0.88, 0.87, 0.85, 0.92]),
        "drift_rate": 0.05,
        "color": "#4caf50",
        "linestyle": "-",
    }

    # 2. Industrial Decline
    def industrial_target(t):
        target = np.array([0.90, 0.80, 0.88, 0.85, 0.82, 0.85])
        # p1 (natural law), p3 (circulation), p4 (structure) degrade over time
        target[0] -= 0.003 * min(t, 150)
        target[2] -= 0.004 * min(t, 150)
        target[3] -= 0.003 * min(t, 150)
        return np.clip(target, 0.0, 1.0)

    scenarios["Industrial\nDecline"] = {
        "y0": [0.80, 0.75, 0.78, 0.76, 0.74, 0.78],
        "targets": industrial_target,
        "drift_rate": 0.06,
        "color": "#ff9800",
        "linestyle": "-",
    }

    # 3. Cascade Collapse
    def collapse_target(t):
        base = np.array([0.60, 0.55, 0.58, 0.56, 0.54, 0.60])
        decay = 0.006 * min(t, 180)
        return np.clip(base - decay, 0.0, 1.0)

    scenarios["Cascade\nCollapse"] = {
        "y0": [0.55, 0.50, 0.52, 0.50, 0.48, 0.55],
        "targets": collapse_target,
        "drift_rate": 0.08,
        "color": "#f44336",
        "linestyle": "-",
    }

    # 4. Restoration via DPC / AW
    def restoration_target(t):
        # Starts at degraded; restoration accelerates after t=30
        base = np.array([0.35, 0.40, 0.32, 0.38, 0.36, 0.42])
        if t > 30:
            recovery = 0.005 * min(t - 30, 140)
            base += recovery
        return np.clip(base, 0.0, 1.0)

    scenarios["Restoration\n(DPC / AW)"] = {
        "y0": [0.30, 0.38, 0.28, 0.35, 0.33, 0.40],
        "targets": restoration_target,
        "drift_rate": 0.07,
        "color": "#2196f3",
        "linestyle": "--",
    }

    # 5. Wa-First Recovery
    def wa_first_target(t):
        base = np.array([0.30, 0.32, 0.28, 0.30, 0.29, 0.35])
        if t > 20:
            # Wa recovers first
            base[5] += 0.008 * min(t - 20, 130)
            # Others follow via coupling, with a delay
        if t > 50:
            base[:5] += 0.004 * min(t - 50, 120)
        return np.clip(base, 0.0, 1.0)

    scenarios["Wa-First\nRecovery"] = {
        "y0": [0.28, 0.30, 0.25, 0.28, 0.27, 0.32],
        "targets": wa_first_target,
        "drift_rate": 0.07,
        "color": "#9c27b0",
        "linestyle": "--",
    }

    return scenarios, t_span, t_eval

# ── Run simulation (RK4 integration — numpy only) ────────────────────────────
def run_simulation(scenario_name, scenario, t_span, t_eval):
    dt = t_eval[1] - t_eval[0]
    y = np.array(scenario["y0"], dtype=float)
    ys = [y.copy()]

    for i in range(1, len(t_eval)):
        t = t_eval[i - 1]
        k1 = np.array(six_principles_ode(t,          y,              scenario))
        k2 = np.array(six_principles_ode(t + dt/2,   y + dt/2 * k1, scenario))
        k3 = np.array(six_principles_ode(t + dt/2,   y + dt/2 * k2, scenario))
        k4 = np.array(six_principles_ode(t + dt,     y + dt   * k3, scenario))
        y = np.clip(y + (dt / 6) * (k1 + 2*k2 + 2*k3 + k4), 0.0, 1.0)
        ys.append(y.copy())

    p = np.array(ys)          # shape: (time_steps, 6)
    stability = system_stability(p)
    return t_eval, p, stability

# ── Plot: stability time series ───────────────────────────────────────────────
def plot_stability_timeseries(results):
    fig, ax = plt.subplots(figsize=(11, 5))

    for name, (t, p, stab) in results.items():
        scenario = scenarios_dict[name]
        label = name.replace("\n", " ")
        ax.plot(t, stab, color=scenario["color"],
                linestyle=scenario["linestyle"], linewidth=2.5, label=label)

    ax.axhline(y=COLLAPSE_THRESHOLD, color="#f44336", linestyle=":", linewidth=1.2,
               alpha=0.7, label=f"Collapse threshold ({COLLAPSE_THRESHOLD})")
    ax.fill_between([0, 200], 0, COLLAPSE_THRESHOLD, color="#f44336", alpha=0.05)
    ax.set_ylim(0, 1.05)
    ax.set_xlabel("Time (arbitrary civilizational units)", fontsize=10)
    ax.set_ylabel("System Stability", fontsize=10)
    ax.set_title(
        "Artificial Wisdom — Six Principles (六つの理) System Stability Model\n"
        "Civilizational stability under five scenarios",
        fontsize=11, fontweight="bold"
    )
    ax.legend(loc="center right", fontsize=9)
    ax.grid(alpha=0.3)
    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "six_principles_stability_timeseries.png")
    plt.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"[Saved] {path}")

# ── Plot: individual principle trajectories per scenario ─────────────────────
def plot_principle_trajectories(results):
    n = len(results)
    fig, axes = plt.subplots(1, n, figsize=(3.5 * n, 4), sharey=True)
    fig.suptitle(
        "Artificial Wisdom — Six Principles Trajectories by Scenario",
        fontsize=11, fontweight="bold"
    )

    for ax, (name, (t, p, stab)) in zip(axes, results.items()):
        for i, (label, color) in enumerate(zip(PRINCIPLES, PRINCIPLE_COLORS)):
            ax.plot(t, p[:, i], color=color, linewidth=1.6,
                    label=label.replace("\n", " "))
        ax.axhline(y=COLLAPSE_THRESHOLD, color="#f44336", linestyle=":", linewidth=1, alpha=0.6)
        ax.set_title(name.replace("\n", " "), fontsize=8, fontweight="bold")
        ax.set_ylim(0, 1.05)
        ax.set_xlabel("Time", fontsize=7)
        ax.grid(alpha=0.2)

    axes[0].set_ylabel("Principle Adherence Level", fontsize=9)
    handles, labels = axes[0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="lower center", ncol=6, fontsize=7.5,
               bbox_to_anchor=(0.5, -0.05))
    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "six_principles_trajectories.png")
    plt.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"[Saved] {path}")

# ── Plot: final state radar ───────────────────────────────────────────────────
def plot_final_state_radar(results):
    n = len(results)
    fig, axes = plt.subplots(1, n, figsize=(3.5 * n, 3.5),
                              subplot_kw=dict(projection="polar"))
    fig.suptitle("Artificial Wisdom — Final Principle State (t=200)",
                 fontsize=11, fontweight="bold")

    for ax, (name, (t, p, stab)) in zip(axes, results.items()):
        final = p[-1, :]
        labels = [pr.replace("\n", " ") for pr in PRINCIPLES]
        n_axes = len(labels)
        angles = np.linspace(0, 2 * np.pi, n_axes, endpoint=False).tolist()
        angles += angles[:1]
        values = final.tolist() + [final[0]]

        ax.set_theta_offset(np.pi / 2)
        ax.set_theta_direction(-1)
        ax.set_xticks(angles[:-1])
        ax.set_xticklabels(labels, fontsize=6.5)
        ax.set_ylim(0, 1)
        ax.set_yticks([0.25, 0.5, 0.75, 1.0])
        ax.set_yticklabels(["0.25", "0.5", "0.75", "1.0"], fontsize=5)

        color = scenarios_dict[name]["color"]
        ax.plot(angles, values, color=color, linewidth=2)
        ax.fill(angles, values, color=color, alpha=0.25)
        final_stability = system_stability(p[-1:, :])[0]
        ax.set_title(f"{name.replace(chr(10), ' ')}\nStability: {final_stability:.2f}",
                     fontsize=7.5, fontweight="bold", pad=12)

    plt.tight_layout()
    path = os.path.join(OUTPUT_DIR, "six_principles_final_radar.png")
    plt.savefig(path, dpi=150, bbox_inches="tight")
    plt.close()
    print(f"[Saved] {path}")

# ── Print summary ─────────────────────────────────────────────────────────────
def print_summary(results):
    print(f"\n{'='*62}")
    print(f"  SCENARIO SUMMARY (t=0 → t=200)")
    print(f"{'='*62}")
    print(f"  {'Scenario':<28}  {'Start':>7}  {'End':>7}  {'Trend'}")
    print(f"  {'-'*52}")
    for name, (t, p, stab) in results.items():
        start = stab[0]
        end = stab[-1]
        trend = "[+] recovering" if end > start + 0.05 else \
                "[-] declining" if end < start - 0.05 else \
                "[=] stable"
        collapsed = "⚠ COLLAPSE" if end < COLLAPSE_THRESHOLD else ""
        print(f"  {name.replace(chr(10), ' '):<28}  {start:>7.3f}  {end:>7.3f}  {trend} {collapsed}")
    print()

# ── Global for cross-function access ─────────────────────────────────────────
scenarios_dict = {}

# ── Main ─────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    print("\n" + "="*62)
    print("  ARTIFICIAL WISDOM GUARDRAIL PROTOCOL")
    print("  Simulation 3: Six Principles Stability Model")
    print(f"  {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    print("="*62)
    print()
    PRINCIPLES_ASCII = [
        "Providence (Setsuri)", "Harmony (Chowa)", "Circulation (Junkan)",
        "Structure (Kozo)", "Order (Chitsujo)", "Wa (Integration)",
    ]
    print("  Six Principles (Mutsu-no-Kotowari):")
    for label in PRINCIPLES_ASCII:
        print(f"    - {label}")
    print()
    print("  Running 5 civilizational scenarios...")

    scenarios_dict, t_span, t_eval = make_scenarios()

    results = {}
    for name, scenario in scenarios_dict.items():
        print(f"  - {name.replace(chr(10), ' '):<30}", end="", flush=True)
        t, p, stab = run_simulation(name, scenario, t_span, t_eval)
        results[name] = (t, p, stab)
        print(f"  final stability: {stab[-1]:.3f}")

    print()
    plot_stability_timeseries(results)
    plot_principle_trajectories(results)
    plot_final_state_radar(results)
    print_summary(results)
    print("  Figures saved to: simulation/output/")
