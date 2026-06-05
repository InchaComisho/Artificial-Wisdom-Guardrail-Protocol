# Simulation — Artificial Wisdom Guardrail Protocol

Python simulations implementing the evaluation frameworks from `docs/`.

## Requirements

```bash
pip install numpy matplotlib
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

#### Model Limitation / モデル上の注意

The Six Principles stability model is an illustrative conceptual model, not a validated prediction model.

In the current implementation, **Wa / Harmony** is modeled as a restorative coupling factor that can lift other principles over time. Therefore, even severe degradation scenarios may eventually recover in the simulation.

This should not be interpreted as a real-world guarantee that civilization will recover automatically. It means only that, under this model's assumptions, remaining alignment with one or more principles can create a pathway toward recovery.

六つの理・文明安定性モデルは、予測モデルではなく概念説明モデルです。

現在の実装では、**和 / Harmony** が他の原則を引き上げる回復結合として設計されているため、崩壊シナリオでも最終的に回復へ向かう場合があります。

これは、現実世界で文明が自動的に回復するという意味ではありません。このモデルの仮定のもとでは、いずれかの原則が残っている場合、回復経路が生まれうることを示しているに過ぎません。

#### Future Improvement: Negative-Control Scenarios / 今後の改善：ネガティブコントロール

A future version should add negative-control scenarios where:

- Wa / Harmony no longer functions as a restorative coupling factor
- Providence, Circulation, Structure, Order, and Harmony are all severely degraded
- external shocks continue instead of stopping
- recovery does not occur unless a restoration intervention is introduced

This would make the model more balanced by showing both recovery conditions and non-recovery conditions.

今後の版では、次のようなネガティブコントロール・シナリオを追加すると、モデルの説得力が高まります。

- 和 / Harmony が回復結合として機能しない
- 摂理、循環、構造、秩序、和がすべて深刻に劣化している
- 外部ショックが停止せず継続する
- 修復介入がない限り回復しない

これにより、回復条件だけでなく、回復不能条件も示せるようになります。

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
