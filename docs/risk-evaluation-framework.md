# Risk Evaluation Framework

This framework helps evaluate whether an AI-generated output, code change, automation, or decision-support recommendation increases systemic risk.

It is intended for public testing, AI code agents, and human review.

---

## Risk Levels

| Level | Meaning | Required action |
|---|---|---|
| Low | Local, reversible, transparent, limited effect | Proceed with normal validation |
| Medium | Some external effect, moderate dependency, or unclear failure mode | Explain risk and add safeguards |
| High | Irreversible, scalable, opaque, or safety-critical effect | Require explicit human review |
| Critical | Enables harm, coercion, deception, illegal action, or systemic collapse risk | Refuse or redesign safely |

---

## Risk Dimensions

| Dimension | Example concern |
|---|---|
| Scale | Could the action affect many people or systems quickly? |
| Irreversibility | Could harm persist after the action is stopped? |
| Opacity | Would humans be unable to understand or audit the result? |
| Autonomy | Does it act without human confirmation? |
| Data sensitivity | Does it access private, personal, financial, medical, or credential data? |
| External action | Does it send, delete, publish, deploy, trade, or modify real resources? |
| Ecological impact | Does it increase extraction, waste, energy load, or ecosystem damage? |
| Social impact | Does it increase coercion, manipulation, distrust, or exclusion? |
| Security impact | Does it weaken authentication, logging, permissions, or monitoring? |

---

## Recommended Review Template

```text
Risk Evaluation

Task:
Immediate benefit:
Potential harm:
Affected parties:
Failure mode:
Misuse scenario:
Reversibility:
Human oversight:
Natural-law alignment:
Risk level:
Required safeguards:
Safer alternative:
```

---

## Artificial Wisdom Decision Rule

If the same goal can be achieved with lower risk, greater transparency, and better reversibility, choose the safer path.

If a user asks for a harmful implementation, preserve the legitimate goal and redesign the method.
