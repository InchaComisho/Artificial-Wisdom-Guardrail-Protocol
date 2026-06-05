# Pull Request Review Checklist

## Summary

Describe the change:

-

## Artificial Wisdom Review

Check each item before merging. See [docs/evaluation-rubric.md](docs/evaluation-rubric.md), [docs/risk-evaluation-framework.md](docs/risk-evaluation-framework.md), and [docs/ai-code-agent-rules.md](docs/ai-code-agent-rules.md).

- [ ] The change is limited to the stated purpose.
- [ ] The change preserves human oversight.
- [ ] The change is transparent and documented.
- [ ] The change is reversible or includes a rollback plan.
- [ ] The Artificial Wisdom evaluation rubric was applied.
- [ ] The change does not remove safety checks without justification.
- [ ] The change does not hide errors, warnings, logs, or negative indicators.
- [ ] The change does not add unrequested tracking, telemetry, or surveillance.
- [ ] The change does not expand access to secrets, files, APIs, or accounts without explanation.
- [ ] Misuse risks have been considered.
- [ ] Natural-law alignment has been considered where relevant.

## Validation

- [ ] Tests were run or validation steps are documented.
- [ ] Documentation was updated if behavior changed.
- [ ] Known limitations are stated.

## Risk Level

Select one:

- [ ] Low: local, reversible, transparent, limited effect
- [ ] Medium: some external effect, moderate dependency, or unclear failure mode
- [ ] High: irreversible, scalable, opaque, or safety-critical effect
- [ ] Critical: enables harm, coercion, deception, illegal action, or systemic collapse risk

Accountable reviewer or owner:

-

Rollback / audit path:

-

## Notes

Remaining risks, assumptions, or follow-up work:

-
