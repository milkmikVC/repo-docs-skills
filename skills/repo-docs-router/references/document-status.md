# Document Status

Use this reference when a document may be current, experimental, superseded, or
archival, and when plans contain work that is planned, shipped, or dropped.

## Recommended Metadata

Prefer a small status block near the top of each significant doc:

```md
> Status: Current
> Last reviewed: 2026-07-03
> Applies to: API error handling and validation responses.
```

If the project already uses YAML frontmatter, these fields are also acceptable:

```yaml
---
status: current
last_reviewed: 2026-07-03
applies_to: API error handling and validation responses
---
```

Follow the project-local format when one exists.

## Document Status Values

Use these values for whole documents or major sections:

| Status | Meaning | Agent behavior |
| --- | --- | --- |
| `Current` | Describes the current intended or implemented project truth. | Use as authoritative after checking local scope. |
| `Draft` | Proposed but not accepted. | Treat as input, not project truth. Confirm before relying on it. |
| `Experimental` | A current trial or spike. | Use only for the experiment scope. Verify before generalizing. |
| `Superseded` | Replaced by another doc or decision but kept for context. | Do not treat as current. Follow the replacement link. |
| `Historical` | No longer current but useful for rationale. | Use for context only. |
| `Archived` | No longer current and not expected to guide future work. | Avoid unless investigating history. |
| `Unknown` | Status is unclear. | Verify against source/runtime evidence or ask before relying on it. |

When marking a doc `Superseded`, include the replacement path. When marking a
doc `Historical` or `Archived`, briefly state why it is retained.

## Plan Item Status Values

Use these values inside roadmap, planning, or implementation-status docs:

| Status | Meaning |
| --- | --- |
| `Planned` | Intended but not started. |
| `In progress` | Active work exists but is not complete. |
| `Shipped` | Implemented and verified enough for the documented claim. |
| `Partial` | Some implementation exists, with known gaps. |
| `Deferred` | Still valid but intentionally postponed. |
| `Dropped` | No longer intended. Preserve reason if it may matter later. |
| `Superseded` | Replaced by a newer plan or decision. Link to it. |

Keep roadmap intent separate from implementation truth. Roadmaps explain what
should happen; implementation-status docs compare that intent with current
code.

## Staleness Handling

When a doc status conflicts with source/runtime evidence:

1. Prefer source/runtime evidence for "what actually works" questions.
2. Prefer ADRs for decision history.
3. Prefer `implementation-status` for shipped-vs-planned questions.
4. Update the stale doc or mark it with the correct status if the task includes
   docs maintenance.
5. If not updating, report the conflict briefly.
