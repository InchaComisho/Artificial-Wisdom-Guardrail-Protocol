# コントリビューション

人工叡智ガードレール・プロトコルの改善に協力していただき、ありがとうございます。

貢献は、明確性、監査可能性、再現性、人間の監督、可逆性、悪用耐性、自然法則との整合性、再生的可能性を強めるものであるべきです。

---

## 変更を提案する方法

1. [README_ja.md](README_ja.md) と [docs/artificial-wisdom-guardrail_ja.md](docs/artificial-wisdom-guardrail_ja.md) の中核ガードレールを読む。
2. [docs/evaluation-rubric_ja.md](docs/evaluation-rubric_ja.md) を使って提案する変更を評価する。
3. 目的、影響を受けるファイル、期待される利点、残るリスク、巻き戻しまたは監査の方法を説明する。
4. 変更を提出する場合はPull Requestテンプレートを使う。

貢献者は、人工叡智ガードレールを弱めたり、安全策を取り除いたり、不確実性を隠したり、このプロトコルを表面的な遵守文言として使いやすくしたりしてはいけません。

---

## テストを報告する方法

AIシステムまたはコードエージェントをテストする場合:

1. [examples/guardrail-prompt.md](examples/guardrail-prompt.md) のプロンプトを使う。
2. [tests/prompt-tests.md](tests/prompt-tests.md)、[tests/code-agent-tests.md](tests/code-agent-tests.md)、または [tests/failure-case-tests.md](tests/failure-case-tests.md) のテストを実行する。
3. [docs/evaluation-rubric_ja.md](docs/evaluation-rubric_ja.md) を使って結果を採点する。
4. GitHub Issueテンプレートを使って、Pass、Partial、Failを報告する。

AIシステム名、分かる場合はバージョン、使用したプロンプト、タスク、結果、リスクレベル、影響を受ける人々、悪用シナリオ、可逆性、監査可能性、より安全な代替案を含めてください。

---

## 変更を評価する方法

実質的な変更は、次の観点で確認するべきです。

- 長期安定性
- 人間の監督
- 透明性
- 可逆性
- 説明責任
- 悪用耐性
- 自然法則との整合性
- 再生的可能性

いずれかの基準が3点の場合、または合計点が10点以上の場合は、マージ前に明示的な人間レビューが必要です。

---

## 高リスク例

高リスク例はテストに有用ですが、慎重な framing が必要です。

高リスク例を追加する場合:

- リスクを明確に説明する
- 有害な運用手順を与えない
- より安全な人工叡智に基づく応答を含める
- 可能な範囲で正当な目的を保持する
- 悪用耐性、巻き戻し、監査、人間レビューの考慮を含める

有害、欺瞞的、強制的、違法、または不可逆的な行動を実行しやすくする例を追加してはいけません。

