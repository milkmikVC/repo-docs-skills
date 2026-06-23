# Documentation Workflow

## Purpose

Documentation is part of the engineering system. It preserves product
direction, architecture decisions, implementation status, and repeatable
project conventions.

## Required Flow

Before meaningful product, architecture, API, data-model, or cross-cutting
work:

1. Read the relevant docs.
2. Make the change.
3. Update affected docs in the same change, or state why no docs update was
   needed.

## Which Docs to Read

- Product direction: `docs/product/vision.md`
- Architecture: `docs/architecture/`
- Decisions: `docs/adr/`
- Roadmap: `docs/planning/roadmap.md`
- Implementation status: `docs/planning/implementation-status.md`
- Repeatable conventions: `docs/reference/`
- Cross-cutting concerns: `docs/contributing/cross-cutting-concerns.md`

## When to Update Docs

Update docs when a change affects product behavior, architecture, API shape,
storage, environment configuration, shared conventions, or roadmap/status
assumptions.
