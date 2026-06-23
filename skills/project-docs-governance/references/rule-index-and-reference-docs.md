# Rule Index and Reference Docs

Use this reference when designing where project rules should live.

## Recommended Split

- `AGENTS.md`: short project rules that should be visible immediately to coding agents.
- `docs/README.md`: docs map.
- `docs/reference/*.md`: detailed repeatable conventions.
- `docs/contributing/documentation.md`: when and how docs should be updated.

## Rule IDs

Use stable rule IDs for detailed reference rules when agents need precise
targeted loading.

Examples:

- `api.file-naming`
- `web.text-overflow-tooltip`
- `docs.adr-required`
- `env.typed-loader`

## When to Add a Reference Doc

Add a reference doc when a rule:

- will be copied across features,
- is too detailed for `AGENTS.md`,
- affects future reviews or automated agents,
- needs examples, tables, or exceptions.

## When to Keep a Rule Local

Keep a rule local to the task or PR when it is one-off, experimental, or not
likely to recur.
