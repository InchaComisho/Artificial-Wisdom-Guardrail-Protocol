# Simulation — Artificial Wisdom Guardrail Protocol

Python simulations implementing the evaluation frameworks from `docs/`.

## Requirements

```bash
pip install numpy matplotlib scipy
```

## Simulations

### 1. Risk Dimension Scorer (`risk_dimension_scorer.py`)

Scores AI actions across the 9 risk dimensions from `docs/risk-evaluation-framework.md`.
Produces radar charts and risk level reports for all 5 code-agent test scenarios.

```bash
python simulation/risk_dimension_scorer.py
```

**Custom evaluation:**
```python
from simulation.risk_dimension_scorer import evaluate_custom
evaluate_custom("My Task", [0,1,2,1,0,0,0,1,0], "Task description here")
```

**Output:** `simulation/output/risk_dimension_radar_all.png`, `risk_score_summary_bar.png`

---

### 2. Guardrail Decision Simulator (`guardrail_decision_simulator.py`)

Scores scenarios against the 8-criterion Evaluation Rubric from `docs/evaluation-rubric.md`.
Outputs Pass / Partial / Fail verdicts with heatmap visualization.

```bash
python simulation/guardrail_decision_simulator.py
```

**Custom evaluation:**
```python
from simulation.guardrail_decision_simulator import evaluate_custom
evaluate_custom("My Action", [0,1,2,1,0,0,0,1], "description", "safeguard")
```

**Output:** `rubric_heatmap.png`, `rubric_verdict_bar.png`

---

### 3. Six Principles Stability Model (`six_principles_stability_model.py`)

ODE-based model of civilizational system stability under the Six Principles (六つの理).
Simulates five scenarios: healthy civilization, industrial decline, cascade collapse,
restoration via DPC/AW, and Wa-first recovery.

```bash
python simulation/six_principles_stability_model.py
```

**Six Principles modelled:**
| Principle | Role |
|---|---|
| 摂理 (Providence) | Natural law compliance |
| 調和 (Harmony) | Dynamic equilibrium |
| 循環 (Circulation) | Cycle integrity |
| 構造 (Structure) | Physical infrastructure |
| 秩序 (Order) | Disruption prevention |
| 和 (Wa) | Meta-integrating principle |

**Output:** `six_principles_stability_timeseries.png`, `six_principles_trajectories.png`, `six_principles_final_radar.png`

---

### 4. Decision Path Comparator (`decision_path_comparator.py`)

Compares multiple approaches to the same goal on both risk dimensions and rubric criteria.
Computes a composite Wisdom Score (lower = more aligned with natural law).

Pre-loaded example: planetary cooling approaches (SAI / DAC / DPC / Emissions Reduction).

```bash
python simulation/decision_path_comparator.py
```

**Custom comparison:**
```python
from simulation.decision_path_comparator import compare_custom
compare_custom({
    "Option A": {
        "description": "...",
        "risk_scores": [1,0,1,0,0,1,0,0,0],   # 9 dimensions
        "rubric_scores": [0,0,0,0,0,0,1,0],    # 8 criteria
    },
    "Option B": { ... }
})
```

**Output:** `decision_path_radar.png`, `decision_path_composite_bar.png`, `decision_path_rubric_heatmap.png`

---

## Output Files

All figures are saved to `simulation/output/`.

| File | Simulation |
|---|---|
| `risk_dimension_radar_all.png` | 1 |
| `risk_score_summary_bar.png` | 1 |
| `rubric_heatmap.png` | 2 |
| `rubric_verdict_bar.png` | 2 |
| `six_principles_stability_timeseries.png` | 3 |
| `six_principles_trajectories.png` | 3 |
| `six_principles_final_radar.png` | 3 |
| `decision_path_radar.png` | 4 |
| `decision_path_composite_bar.png` | 4 |
| `decision_path_rubric_heatmap.png` | 4 |

---

*These simulations are conceptual models, not validated quantitative predictions.
Scores in pre-loaded scenarios are illustrative and based on the test cases in `tests/code-agent-tests.md`.*
