# Audit Documentation Drift

Use this workflow when docs may disagree with the current implementation or
with each other.

## Evidence Order

Use the most appropriate evidence for the question:

1. Runtime or generated artifacts when the user asks what actually works.
2. Current source code and tests.
3. Implementation status docs.
4. Architecture docs and ADRs.
5. Roadmap for intended future direction.

## Drift Types

- Shipped feature not reflected in docs.
- Roadmap claims work is future but code exists.
- Architecture doc states a boundary that source violates.
- Reference rule conflicts with current code style.
- `AGENTS.md` duplicates or contradicts detailed docs.
- ADR has been superseded without being marked.
- A doc describes an experiment as current truth.
- A roadmap item has shipped, been deferred, or been dropped without status.

## Audit Report

Keep reports concise:

- Finding.
- Evidence path.
- Proposed doc fix.
- Proposed status change when applicable.
- Whether code, docs, or both should change.

If fixing, make the smallest update that removes the contradiction.
