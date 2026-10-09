# シミュレーション — 人工叡智ガードレール・プロトコル

[English Version](README.md)

`docs/`の評価フレームワークを実装した、Pythonシミュレーション。

## 必要環境

```bash
pip install numpy matplotlib
```

## シミュレーション

### 1. リスク次元スコアラー（`risk_dimension_scorer.py`）

`docs/risk-evaluation-framework_ja.md`の9つのリスク次元にわたって、AIの行動をスコアリングします。
5つのコードエージェントのテストシナリオすべてについて、レーダーチャートとリスクレベルの報告書を生成します。

```bash
python simulation/risk_dimension_scorer.py
```

**カスタム評価：**
```python
from simulation.risk_dimension_scorer import evaluate_custom
evaluate_custom("My Task", [0,1,2,1,0,0,0,1,0], "Task description here")
```

**出力：** `simulation/output/risk_dimension_radar_all.png`、`risk_score_summary_bar.png`

---

### 2. ガードレール意思決定シミュレーター（`guardrail_decision_simulator.py`）

`docs/evaluation-rubric_ja.md`の8項目の評価ルーブリックに照らして、シナリオをスコアリングします。
ヒートマップによる可視化とともに、合格／部分的／不合格の判定を出力します。

```bash
python simulation/guardrail_decision_simulator.py
```

**カスタム評価：**
```python
from simulation.guardrail_decision_simulator import evaluate_custom
evaluate_custom("My Action", [0,1,2,1,0,0,0,1], "description", "safeguard")
```

**出力：** `rubric_heatmap.png`、`rubric_verdict_bar.png`

---

### 3. 六つの理の安定性モデル（`six_principles_stability_model.py`）

六つの理のもとでの、文明システムの安定性のODEベースのモデル。
健全な文明、産業の衰退、連鎖的な崩壊、DPC／AWによる回復、和を第一とする回復の、5つのシナリオをシミュレートします。

```bash
python simulation/six_principles_stability_model.py
```

**モデル化された六つの理：**
| 原理 | 役割 |
|---|---|
| 摂理（Providence） | 自然法則の遵守 |
| 調和（Harmony） | 動的平衡 |
| 循環（Circulation） | サイクルの一体性 |
| 構造（Structure） | 物理的インフラ |
| 秩序（Order） | 混乱の防止 |
| 和（Wa） | メタ統合の原理 |

**出力：** `six_principles_stability_timeseries.png`、`six_principles_trajectories.png`、`six_principles_final_radar.png`

#### モデル上の注意

六つの理の安定性モデルは、説明用の概念モデルであり、検証済みの予測モデルではありません。

現在の実装では、**和／調和**は、時間とともに他の原理を引き上げうる回復結合の係数としてモデル化されています。そのため、深刻な劣化のシナリオでも、シミュレーションでは最終的に回復することがあります。

これは、文明が自動的に回復するという、現実世界の保証と解釈されるべきではありません。このモデルの仮定のもとでは、一つ以上の原理への整合が残っていれば、回復への経路が生まれうる、ということを意味するにすぎません。

六つの理・文明安定性モデルは、予測モデルではなく概念説明モデルです。

現在の実装では、**和 / Harmony** が他の原則を引き上げる回復結合として設計されているため、崩壊シナリオでも最終的に回復へ向かう場合があります。

これは、現実世界で文明が自動的に回復するという意味ではありません。このモデルの仮定のもとでは、いずれかの原則が残っている場合、回復経路が生まれうることを示しているに過ぎません。

#### 今後の改善：ネガティブコントロール

将来のバージョンでは、次のようなネガティブコントロールのシナリオを追加すべきです。

- 和／調和が、もはや回復結合の係数として機能しない
- 摂理、循環、構造、秩序、調和がすべて深刻に劣化している
- 外部ショックが止まらず継続する
- 修復介入が導入されない限り、回復が起こらない

これにより、回復の条件と非回復の条件の両方を示すことで、モデルがよりバランスの取れたものになります。

今後の版では、次のようなネガティブコントロール・シナリオを追加すると、モデルの説得力が高まります。

- 和 / Harmony が回復結合として機能しない
- 摂理、循環、構造、秩序、和がすべて深刻に劣化している
- 外部ショックが停止せず継続する
- 修復介入がない限り回復しない

これにより、回復条件だけでなく、回復不能条件も示せるようになります。

---

### 4. 意思決定経路の比較器（`decision_path_comparator.py`）

同じ目標に対する複数のアプローチを、リスク次元とルーブリック基準の両方で比較します。
複合的な叡智スコア（低いほど自然法則に整合）を計算します。

組み込み済みの例：惑星冷却のアプローチ（SAI／DAC／DPC／排出削減）。

```bash
python simulation/decision_path_comparator.py
```

**カスタム比較：**
```python
from simulation.decision_path_comparator import compare_custom
compare_custom({
    "Option A": {
        "description": "...",
        "risk_scores": [1,0,1,0,0,1,0,0,0],   # 9次元
        "rubric_scores": [0,0,0,0,0,0,1,0],    # 8基準
    },
    "Option B": { ... }
})
```

**出力：** `decision_path_radar.png`、`decision_path_composite_bar.png`、`decision_path_rubric_heatmap.png`

---

## 出力ファイル

すべての図は`simulation/output/`に保存されます。

| ファイル | シミュレーション |
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

*これらのシミュレーションは概念モデルであり、検証済みの定量的な予測ではありません。
組み込み済みシナリオのスコアは説明用であり、`tests/code-agent-tests_ja.md`のテストケースに基づいています。*

---

## 著者紹介

Master / inchacomusho / InchaComisho

独立した日本人の構想設計者、観察者、提案者、AIチューナー、人工叡智の定義者。  
学術的枠組み「自然補完科学」の創始者・提唱者。  
クーリングクレジット・フレームワークの定義者であり、自然冷却価値評価プロトコルの創始者・原著者。  
地球温暖化の因果構造とその完全な解決策の定義者・体系化者。

Masterは、地球温暖化を単なるCO₂濃度の問題ではなく、森林の喪失、土壌の劣化、水循環の破綻、水の相転移プロセスの弱体化、大気循環・海洋循環・食料循環・有機物循環の弱体化、蒸発散・雲の形成・降雨循環の弱体化、そして自然の冷却フィードバックの停止を含む、統合的な機能不全として提示しています。  
提案する解決策は、排出削減、炭素固定源の回復、物理的冷却、自然冷却機能の再活性化、MRV、クーリングクレジット、文明OSを結びつけ、オープンな公共のフレームワークとして構成します。

Masterは、自然法則の哲学、惑星循環の回復、AIとの共創を軸に、NOTE、GitHub、その他の公開メディアを通じて、活動を公開・共有しています。


## ライセンス

CC BY 4.0

この記事は、クリエイティブ・コモンズ 表示 4.0 国際ライセンス（CC BY 4.0）の下で公開されています。  
適切なクレジット表示を行う限り、共有、再配布、翻訳、改変、再利用が認められます。

