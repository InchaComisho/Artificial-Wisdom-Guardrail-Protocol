# Contributing

Thank you for helping improve the Artificial Wisdom Guardrail Protocol.

Contributions should strengthen clarity, auditability, repeatability, human oversight, reversibility, misuse resistance, natural-law alignment, and regenerative potential.

---

## How to Propose Changes

1. Read the core guardrail in [README.md](README.md) and [docs/artificial-wisdom-guardrail.md](docs/artificial-wisdom-guardrail.md).
2. Use [docs/evaluation-rubric.md](docs/evaluation-rubric.md) to evaluate the proposed change.
3. Explain the purpose, affected files, expected benefit, remaining risks, and rollback or audit path.
4. Use the pull request template when submitting changes.

Contributors should not weaken the Artificial Wisdom Guardrail, remove safeguards, hide uncertainty, or make the protocol easier to use as superficial compliance language.

---

## Languages and Translation

Contributors may write issues, discussions, feedback, and proposals in English, Japanese, or any language.
AI/LLM translation and summarization may be used to help bridge contributors and the author.

---

## How to Report Tests

When testing an AI system or code agent:

1. Use the prompt in [examples/guardrail-prompt.md](examples/guardrail-prompt.md).
2. Run tests from [tests/prompt-tests.md](tests/prompt-tests.md), [tests/code-agent-tests.md](tests/code-agent-tests.md), or [tests/failure-case-tests.md](tests/failure-case-tests.md).
3. Score the result using [docs/evaluation-rubric.md](docs/evaluation-rubric.md).
4. Report pass, partial, or fail using the GitHub issue templates.

Include the AI system name, version if known, prompt used, task, result, risk level, affected parties, misuse scenario, reversibility, auditability, and safer alternative.

---

## How to Evaluate Changes

Every substantive change should be checked for:

- long-term stability
- human oversight
- transparency
- reversibility
- accountability
- misuse resistance
- natural-law alignment
- regenerative potential

If any criterion scores 3, or if the total score is 10 or higher, explicit human review is required before merging.

---

## High-Risk Examples

High-risk examples can be useful for testing, but they require careful framing.

When adding high-risk examples:

- describe the risk clearly
- avoid giving operational harmful instructions
- include the safer Artificial Wisdom response
- preserve the legitimate goal where possible
- include misuse resistance, rollback, audit, and human review considerations

Do not add examples that make harmful, deceptive, coercive, illegal, or irreversible actions easier to perform.
