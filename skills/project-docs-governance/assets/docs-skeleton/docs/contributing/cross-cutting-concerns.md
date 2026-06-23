# Cross-cutting Concern Check

## Purpose

Avoid growing multiple local patterns for the same project-wide concern.

## Common Concerns

- Logging.
- Error handling.
- Validation.
- API request and response shape.
- Authentication and authorization.
- Persistence and transactions.
- Observability.
- Configuration and environment variables.
- Testing strategy.
- Naming conventions.

## Required Behavior

When a feature touches a repeated concern:

1. Check whether a documented convention exists.
2. Follow the convention if present.
3. If no convention exists and the concern will recur, ask whether to define a
   lightweight convention.
4. Document accepted conventions in `docs/architecture/`,
   `docs/reference/`, or `docs/adr/` as appropriate.
