# ADRs, Roadmaps, and Implementation Status

Use this reference when deciding which planning or decision document to create
or update.

## ADRs

Use ADRs for durable decisions where the project chooses one direction over
another.

Recommended structure:

```md
# ADR NNNN: Title

## Status

Proposed | Accepted | Superseded

## Context

What problem or decision forced this ADR?

## Decision

What are we choosing?

## Consequences

What becomes easier, harder, enabled, or constrained?
```

If an ADR is replaced, mark it `Superseded` and link to the new ADR.

## Roadmap

Use roadmap docs for sequencing and direction. Do not duplicate all
architecture details.

Good roadmap entries state:

- what comes next,
- why it matters,
- what is intentionally deferred.

## Implementation Status

Use implementation status docs to compare documented expectations with the
current codebase.

Good status entries include:

- documented expectation,
- current implementation,
- match state,
- follow-up.

Update status at meaningful checkpoints, not for every small commit.
