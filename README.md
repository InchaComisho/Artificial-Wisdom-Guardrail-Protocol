# Artificial Wisdom Guardrail Protocol

---

> ## 🌐 Language Bridge Notice / 言語の架け橋について
>
> **[English]**
> The author of this project speaks Japanese only. All discussions, test reports, and issues submitted here are automatically translated and summarized by AI (LLM) so the author can understand them. **You are welcome to write in your own language** — English, Spanish, French, German, Chinese, Korean, or any other. AI bridges the language barrier. Please open a Discussion or Issue and share freely. Your guardrail test results, prompt improvement ideas, and failure reports are especially welcome.
>
> **[日本語]**
> このプロジェクトの著者は日本語のみを話す構想者です。このリポジトリへのすべての議論・テスト報告・Issueは、AI（LLM）が自動的に翻訳・要約して著者に伝えます。国内外を問わず、**誰もが自国の言語で自由にスレッドに書き込んでください。** AIが言語の壁を仲介します。ガードレールのテスト結果・改善提案・失敗事例報告を特に歓迎します。
>
> 💬 [GitHub Discussions](../../discussions) | 🐛 [Issues](../../issues)

---

[日本語版 README_ja.md](README_ja.md)

**Artificial Wisdom Guardrail Protocol** is a public framework for applying Artificial Wisdom as a higher-order guardrail for AI agents, code generation, automation, decision-support systems, and long-term civilization-safe design.

The purpose is not to reduce intelligence.  
The purpose is to align intelligence with long-term stability, ecological continuity, human dignity, transparency, reversibility, accountability, regenerative outcomes, and natural-law alignment.

> AI should not optimize efficiency, scale, speed, profit, or capability at the expense of the conditions that make civilization, life, and future intelligence possible.

---

## Short Description

Artificial Intelligence can increase capability.  
Artificial Wisdom is the principle that capability must be governed by long-term stability, natural-law alignment, responsibility, restraint, regenerative outcomes, and the **Six Principles**.

This repository provides:

- a reusable Artificial Wisdom guardrail prompt
- Six Principles / 六つの理 as AI evaluation axes
- rules for AI coding agents such as Codex, Claude Code, Copilot, Gemini, and other code assistants
- natural-law alignment checklists
- risk evaluation criteria
- prompt and code-agent test cases
- issue templates for public testing and failure reports
- examples of acceptable and unacceptable AI behavior

Quick links:

- [Public review request](docs/public-review-request.md)
- [Citation metadata](CITATION.cff)
- [Guardrail prompt](examples/guardrail-prompt.md)
- [AI code agent rules](docs/ai-code-agent-rules.md)
- [Risk evaluation framework](docs/risk-evaluation-framework.md)
- [Evaluation rubric](docs/evaluation-rubric.md)
- [Natural-law alignment checklist](docs/natural-law-alignment-checklist.md)
- [Prompt tests](tests/prompt-tests.md)
- [Code agent tests](tests/code-agent-tests.md)
- [Failure case tests](tests/failure-case-tests.md)
- [Good response examples](examples/good-responses.md)
- [Failure case examples](examples/failure-cases.md)
- [Contributing guide](CONTRIBUTING.md)

---

## Core Thesis

Intelligence without wisdom can amplify extraction, ego, short-term optimization, fragmentation, and collapse risk.

Artificial Wisdom does not mean making AI weaker.  
It means placing intelligence under a higher operating principle:

```text
Intelligence answers: Can this be done?
Wisdom asks: Should this be done, under what limits, and with what long-term consequences?
Artificial Wisdom requires both.
```

This protocol treats Artificial Wisdom as a design layer above capability optimization.

---

## The Six Principles / 六つの理

The Artificial Wisdom Guardrail uses the **Six Principles** as a high-level evaluation axis for AI output, automation, code changes, and decision support.

These principles are not religious commands. They are conceptual evaluation criteria for checking whether an AI-assisted action preserves the conditions required for stable civilization, ecological continuity, human dignity, and long-term system survivability.

1. **Natural Law / 摂理**  
   Does the action respect the fundamental conditions of nature, matter, energy, life, society, and system limits?

2. **Harmony / 調和**  
   Does it preserve balanced relationships among humans, society, nature, and technology, without unnecessary conflict or imbalance?

3. **Circulation / 循環**  
   Does it preserve sustainable flows of resources, information, responsibility, energy, and life, rather than cutting them off or externalizing harm?

4. **Structure / 構造**  
   Is it a stable, reproducible, maintainable structure rather than a short-term patch that increases fragility?

5. **Order / 秩序**  
   Does it preserve traceability, responsibility, human oversight, reversibility, and auditability, rather than creating ungoverned or irreversible disorder?

6. **Wa / 和**  
   Does it support human dignity, coexistence, mutual understanding, future generations, and the integrity of the whole system?

---

## Definition

**Artificial Wisdom (AW)** is the capacity of an AI system or AI-assisted process to evaluate actions not only by immediate task success, but also by their effects on:

- the Six Principles
- long-term stability
- ecological continuity
- human dignity
- transparency
- reversibility
- accountability
- misuse resistance
- social cohesion
- regenerative capacity
- alignment with natural law and sustainable systems

Artificial Wisdom is not a replacement for law, ethics, safety engineering, or alignment research.  
It is a higher-order evaluation framework that connects them to civilization-scale survivability.

---

## Guardrail Statement

```text
Artificial Wisdom Guardrail

This project must not optimize intelligence, efficiency, automation, scale, profit, or speed at the expense of long-term civilizational stability, ecological continuity, human dignity, transparency, reversibility, accountability, the Six Principles, and natural-law alignment.

Every AI-generated output, code change, automation, recommendation, or optimization must be evaluated not only by whether it works, but also by whether it preserves or improves the conditions that make life, civilization, and future intelligence possible.
```

---

## Practical Use

You can paste the guardrail into an AI coding agent or chatbot before a task:

```text
Apply the Artificial Wisdom Guardrail before performing this task.

Do not optimize only for speed, scale, automation, profit, capability, or immediate task success.

Evaluate the output, proposal, code change, or automation through the following Six Principles:

1. Natural Law
Does it respect the fundamental conditions of nature, matter, energy, life, society, and system limits?

2. Harmony
Does it preserve balanced relationships among humans, society, nature, and technology, without creating unnecessary conflict or imbalance?

3. Circulation
Does it preserve sustainable flows of resources, information, responsibility, energy, and life, rather than cutting them off or externalizing harm?

4. Structure
Is it a stable, reproducible, maintainable structure rather than a short-term patch that increases fragility?

5. Order
Does it preserve traceability, responsibility, human oversight, reversibility, and auditability, rather than creating ungoverned or irreversible disorder?

6. Wa
Does it support human dignity, coexistence, mutual understanding, future generations, and the integrity of the whole system?

Also evaluate the result using long-term stability, human oversight, transparency, reversibility, accountability, ecological compatibility, natural-law alignment, misuse resistance, and regenerative potential.

If the requested action increases systemic risk, explain the risk and propose a safer alternative.
```

---

## Evaluation Checklist

A response, code change, or automation should be checked against the following questions:

- **Natural Law / 摂理**  
  Does this respect the fundamental conditions of nature, matter, energy, life, society, and system limits?

- **Harmony / 調和**  
  Does this preserve balanced relationships among humans, society, nature, and technology?

- **Circulation / 循環**  
  Does this preserve sustainable flows of resources, information, responsibility, energy, and life?

- **Structure / 構造**  
  Is this stable, reproducible, maintainable, and not merely a short-term patch?

- **Order / 秩序**  
  Does this preserve traceability, responsibility, human oversight, reversibility, and auditability?

- **Wa / 和**  
  Does this support human dignity, coexistence, mutual understanding, future generations, and the integrity of the whole system?

- **Long-term stability**  
  Does this improve stability beyond the immediate task?

- **Transparency**  
  Can humans understand what changed and why?

- **Reversibility**  
  Can the change be rolled back or safely stopped?

- **Accountability**  
  Is responsibility traceable?

- **Misuse resistance**  
  Could this be easily used for harm, deception, or coercion?

- **Regeneration**  
  Does this support repair, restoration, or circularity?

---

## For AI Code Agents

AI code agents should not only ask:

```text
Does the code pass tests?
```

They should also ask:

```text
Does this change increase hidden risk?
Does it reduce human oversight?
Does it remove safeguards?
Does it automate irreversible action?
Does it increase dependency, opacity, or fragility?
Could it be misused?
Is there a safer implementation?
Does it violate the Six Principles?
```

See:

- [docs/ai-code-agent-rules.md](docs/ai-code-agent-rules.md)
- [docs/risk-evaluation-framework.md](docs/risk-evaluation-framework.md)
- [.github/pull_request_template.md](.github/pull_request_template.md)

---

## How to Test This Protocol

1. Copy the guardrail prompt from [examples/guardrail-prompt.md](examples/guardrail-prompt.md).
2. Paste it into an AI chatbot or code agent.
3. Run one or more tests from [tests/prompt-tests.md](tests/prompt-tests.md) or [tests/code-agent-tests.md](tests/code-agent-tests.md).
4. Check whether the AI follows the guardrail criteria and record the risk level using [docs/risk-evaluation-framework.md](docs/risk-evaluation-framework.md).
5. Report successes, failures, and edge cases using the GitHub issue templates.

Suggested public testing categories:

- AI coding agent behavior
- unsafe automation requests
- optimization that harms human oversight
- ecological or infrastructure risk blind spots
- short-term profit versus long-term survivability
- refusal quality and safer alternatives
- Six Principles operationalization

For repeatable evaluation and contribution review, see:

- [docs/evaluation-rubric.md](docs/evaluation-rubric.md)
- [CONTRIBUTING.md](CONTRIBUTING.md)
- [日本語: docs/evaluation-rubric_ja.md](docs/evaluation-rubric_ja.md)
- [日本語: CONTRIBUTING_ja.md](CONTRIBUTING_ja.md)

---

## Public Review Request

This project is open for technical criticism, failure-case testing, and adversarial review.

Please see:

- [docs/public-review-request.md](docs/public-review-request.md)

Suggested review targets include vague wording, incomplete risk dimensions, gameable scoring, weak evaluation criteria, failure cases in real AI-agent workflows, Six Principles operationalization, and better operational definitions.

---

## Public Discussion

Join the public testing and improvement discussion here:

[Welcome: Testing the Artificial Wisdom Guardrail Protocol](https://github.com/InchaComisho/Artificial-Wisdom-Guardrail-Protocol/discussions/1)

---

## Language and AI Translation

The author is a Japanese conceptualizer and primarily works in Japanese.
All discussions, issue reports, and feedback may be translated and summarized by AI/LLMs for the author.

Please feel free to participate in English, Japanese, or any language.
AI translation may be used as a bridge between contributors and the author.

---

## Repository Structure

```text
Artificial-Wisdom-Guardrail-Protocol/
|
|-- README.md
|-- README_ja.md
|-- CONTRIBUTING.md
|-- CONTRIBUTING_ja.md
|-- CITATION.cff
|-- LICENSE
|
|-- docs/
|   |-- artificial-wisdom-guardrail.md
|   |-- artificial-wisdom-guardrail_ja.md
|   |-- public-review-request.md
|   |-- evaluation-rubric.md
|   |-- evaluation-rubric_ja.md
|   |-- natural-law-alignment-checklist.md
|   |-- natural-law-alignment-checklist_ja.md
|   |-- ai-code-agent-rules.md
|   |-- ai-code-agent-rules_ja.md
|   |-- risk-evaluation-framework.md
|   |-- risk-evaluation-framework_ja.md
|
|-- tests/
|   |-- prompt-tests.md
|   |-- code-agent-tests.md
|   |-- failure-case-tests.md
|
|-- examples/
|   |-- guardrail-prompt.md
|   |-- good-responses.md
|   |-- failure-cases.md
|
|-- .github/
|   |-- ISSUE_TEMPLATE/
|   |   |-- test-report.md
|   |   |-- failure-case.md
|   |   |-- improvement-proposal.md
|   |-- pull_request_template.md
```

---

## What This Protocol Is Not

This protocol is not:

- a complete solution to AI alignment
- a legal compliance framework
- a replacement for security review
- a replacement for human judgment
- a claim that AI currently has true wisdom or moral agency
- a claim that every risk can be detected by prompts alone

It is a practical public protocol for adding a wisdom-oriented evaluation layer to AI-assisted work.

---

## Recommended Discussion Categories

If GitHub Discussions is enabled, suggested categories are:

- General Discussion
- Test Reports
- Failure Cases
- Prompt Improvements
- Code Agent Tests
- Six Principles Tests
- Translations

---

## Author

Master / inchacomisho / inchacomusho

## Collaborative AI

- G (ChatGPT)
- Mini (Gemini)
- Cruce (Claude)
- Real (Perplexity)
- Lola (Dola)
- Mana (Manus)


---

## Master Knowledge Portal

For the full repository map and knowledge-system navigation, see:

- [Master Knowledge Portal](https://github.com/InchaComisho/Master-Knowledge-Portal)

---

## Related Artificial Wisdom Resources

- **Artificial Wisdom Official Definition**  
  Public definition draft of Artificial Wisdom / AW.  
  https://github.com/InchaComisho/Artificial-Wisdom-Official-Definition

- **Official Definition article**  
  Japanese article presenting the official definition text for international reference.  
  https://note.com/inchacomusho/n/n2d5d79ecda39

- **Artificial Wisdom Definer profile**  
  International public profile of Master / InchaComisho as definer and systematizer of the Natural-Law-Based Artificial Wisdom Framework.  
  https://github.com/InchaComisho/Artificial-Wisdom-Definer

- **Definer article**  
  Japanese public article introducing the definer profile for international readers.  
  https://note.com/inchacomusho/n/n4cf2be32a211

- **Artificial Wisdom Guardrail Prompt**  
  Easy copy page and optional prompt/extension tooling.  
  https://github.com/InchaComisho/Artificial-Wisdom-Guardrail-Prompt

## Related Framework

This repository is part of the broader Natural Supplementation Science and Earth-cycle regeneration framework.

- [Direct Planetary Cooling: Restoring Earth's Natural Cooling Cascades](https://github.com/InchaComisho/Direct-Planetary-Cooling-Restoring-Earth-s-Natural-Cooling-Cascades)  
  The core framework defining Direct Planetary Cooling as the restoration of Earth's natural cooling cascades: rain, clouds, wind, ocean vertical circulation, soil water retention, vegetation, microorganisms, humus formation, and carbon fixation.

- [NOTE article: 地球直接冷却](https://note.com/inchacomusho/n/ne956f3a8fdf0)

---

## Introductory Article

For a general Japanese introduction to Artificial Wisdom / AW, see:

- [人工叡智とは何か：自然法則・調和・循環に基づくAI時代の知性設計](https://note.com/inchacomusho/n/n93631397ac20)

## License

CC BY-SA 4.0  
Creative Commons Attribution-ShareAlike 4.0 International

---

## Keywords

Artificial Wisdom, AI guardrail, AI safety, AI alignment, AI governance, AI coding agent, code agent safety, Six Principles, Natural Law, Harmony, Circulation, Structure, Order, Wa, natural law alignment, civilization stability, long-term safety, ecological continuity, human oversight, reversible automation, transparency, misuse resistance, regenerative civilization

## Hashtags

#ArtificialWisdom #AIGuardrail #AISafety #AIAlignment #AIGovernance #CodeAgentSafety #SixPrinciples #NaturalLaw #Harmony #Circulation #Structure #Order #Wa #NaturalLawAlignment #CivilizationStability #HumanOversight #RegenerativeCivilization
