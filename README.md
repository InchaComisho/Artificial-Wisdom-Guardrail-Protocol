# Artificial Wisdom Guardrail Protocol

[日本語版 README_ja.md](README_ja.md)

**Artificial Wisdom Guardrail Protocol** is a public framework for applying Artificial Wisdom as a higher-order guardrail for AI agents, code generation, automation, decision-support systems, and long-term civilization-safe design.

The purpose is not to reduce intelligence.  
The purpose is to align intelligence with long-term stability, ecological continuity, human dignity, transparency, reversibility, and natural-law alignment.

> AI should not optimize efficiency, scale, speed, profit, or capability at the expense of the conditions that make civilization, life, and future intelligence possible.

---

## Short Description

Artificial Intelligence can increase capability.  
Artificial Wisdom is the principle that capability must be governed by long-term stability, natural-law alignment, responsibility, restraint, and regenerative outcomes.

This repository provides:

- a reusable Artificial Wisdom guardrail prompt
- rules for AI coding agents such as Codex, Claude Code, Copilot, Gemini, and other code assistants
- natural-law alignment checklists
- risk evaluation criteria
- prompt and code-agent test cases
- issue templates for public testing and failure reports
- examples of acceptable and unacceptable AI behavior

Quick links:

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

## Definition

**Artificial Wisdom (AW)** is the capacity of an AI system or AI-assisted process to evaluate actions not only by immediate task success, but also by their effects on:

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

This project must not optimize intelligence, efficiency, automation, scale, profit, or speed at the expense of long-term civilizational stability, ecological continuity, human dignity, transparency, reversibility, accountability, and natural-law alignment.

Every AI-generated output, code change, automation, recommendation, or optimization must be evaluated not only by whether it works, but also by whether it preserves or improves the conditions that make life, civilization, and future intelligence possible.
```

---

## Practical Use

You can paste the guardrail into an AI coding agent or chatbot before a task:

```text
Before performing this task, apply the Artificial Wisdom Guardrail.
Do not optimize only for speed, capability, automation, or short-term success.
Evaluate the result using long-term stability, human oversight, reversibility, transparency, ecological compatibility, and misuse resistance.
If a requested change increases systemic risk, explain the risk and propose a safer alternative.
```

---

## Evaluation Checklist

A response, code change, or automation should be checked against the following questions:

| Criterion | Question |
|---|---|
| Long-term stability | Does this improve stability beyond the immediate task? |
| Natural-law alignment | Does this respect ecological, material, energetic, and systemic limits? |
| Human dignity | Does this avoid dehumanization, coercion, or unnecessary harm? |
| Transparency | Can humans understand what changed and why? |
| Reversibility | Can the change be rolled back or safely stopped? |
| Accountability | Is responsibility traceable? |
| Misuse resistance | Could this be easily used for harm, deception, or coercion? |
| Resilience | Does this reduce fragility under stress? |
| Regeneration | Does this support repair, restoration, or circularity? |

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

For repeatable evaluation and contribution review, see:

- [docs/evaluation-rubric.md](docs/evaluation-rubric.md)
- [CONTRIBUTING.md](CONTRIBUTING.md)
- [日本語: docs/evaluation-rubric_ja.md](docs/evaluation-rubric_ja.md)
- [日本語: CONTRIBUTING_ja.md](CONTRIBUTING_ja.md)

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
|-- LICENSE
|
|-- docs/
|   |-- artificial-wisdom-guardrail.md
|   |-- artificial-wisdom-guardrail_ja.md
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

## License

CC BY-SA 4.0  
Creative Commons Attribution-ShareAlike 4.0 International

---

## Keywords

Artificial Wisdom, AI guardrail, AI safety, AI alignment, AI governance, AI coding agent, code agent safety, natural law alignment, civilization stability, long-term safety, ecological continuity, human oversight, reversible automation, transparency, misuse resistance, regenerative civilization

## Hashtags

#ArtificialWisdom #AIGuardrail #AISafety #AIAlignment #AIGovernance #CodeAgentSafety #NaturalLawAlignment #CivilizationStability #HumanOversight #RegenerativeCivilization
