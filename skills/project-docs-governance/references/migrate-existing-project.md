# Migrate an Existing Project

Use this workflow when docs exist but are scattered, duplicated, or hard for
agents to navigate.

## Steps

1. Inventory current docs with `scripts/inventory_docs.py <repo-root>`.
2. Identify entry points, duplicates, and stale claims.
3. Preserve useful project-specific facts.
4. Move long repeatable rules into `docs/reference/`.
5. Keep `AGENTS.md` short if it exists.
6. Put workflow rules in `docs/contributing/documentation.md`.
7. Put durable decisions in ADRs.
8. Use implementation status for factual code-vs-doc alignment.
9. Remove or rewrite obsolete duplicate passages after confirming their new home.

## Migration Output

For a migration plan, include:

- Current entry points.
- Proposed target entry points.
- Content to preserve.
- Content to merge or delete.
- Docs requiring user confirmation.
- Verification steps.

## Safety

Do not delete old docs until their useful content has a clear new home or the
user confirms it is obsolete.
