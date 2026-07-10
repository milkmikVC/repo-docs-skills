# Repo Docs Skills

Two reusable agent skills for making repository documentation discoverable,
actionable, and maintainable across new and existing software projects.

> [!IMPORTANT]
> Install both skills inside each project under `.agents/skills/` and commit
> them with the repository. Project-scoped installation keeps the documentation
> workflow versioned with the codebase and gives every contributor and coding
> agent the same behavior. Personal installation is best reserved for temporary
> evaluation.

## Skills

| Skill | Responsibility | Trigger |
| --- | --- | --- |
| `repo-docs-router` | Finds the smallest relevant project docs set and decides whether durable conversation facts or completed work require documentation updates. | Every conversation conducted in a software repository. |
| `project-docs-governance` | Creates, migrates, audits, or repairs the repository documentation system itself. | New-project setup, legacy-project migration, documentation drift, or governance changes. |

The split is intentional. The router participates in normal work; the
governance skill changes the docs system only when that system is the task.

## How It Works

For every repository conversation, `repo-docs-router` performs a lightweight
preflight:

1. Find the repository root and documentation entry points.
2. Read `docs/contributing/documentation.md` for project-specific structure,
   update rules, and special paths.
3. Use `docs/README.md` as the documentation map when it exists.
4. Load only the product, architecture, API, reference, ADR, roadmap, status,
   or other docs relevant to the current request.
5. Treat document status before trusting a file as current project truth.
6. During discussion and at task completion, update the smallest appropriate
   doc when a durable fact, accepted decision, shipped feature, or changed plan
   requires it.

The router may conclude that no task-specific documentation is needed. An
always-triggered router is a routing check, not a requirement to read or edit
docs on every turn.

Use `project-docs-governance` separately when the repository needs a new docs
structure, a migration from scattered legacy docs, or a drift audit.

## Recommended: Project-Scoped Installation

From the target repository root, copy both skill directories into
`.agents/skills/`:

```bash
mkdir -p .agents/skills
cp -R /path/to/repo-docs-skills/skills/repo-docs-router .agents/skills/
cp -R /path/to/repo-docs-skills/skills/project-docs-governance .agents/skills/
```

Commit the installed skills so their behavior changes through normal repository
review and versioning:

```bash
git add .agents/skills/repo-docs-router .agents/skills/project-docs-governance
git commit -m "Add repository documentation skills"
```

Refresh the coding-agent runtime if it does not discover newly added project
skills immediately.

### Personal Installation

Personal installation is supported for evaluation or individual experiments:

```bash
mkdir -p "${CODEX_HOME:-$HOME/.codex}/skills"
cp -R skills/repo-docs-router "${CODEX_HOME:-$HOME/.codex}/skills/"
cp -R skills/project-docs-governance "${CODEX_HOME:-$HOME/.codex}/skills/"
```

For team repositories, prefer project-scoped installation. A personal copy can
drift from the repository and cannot guarantee that other agents use the same
documentation contract.

## Standard Documentation Contract

The skills recognize this default structure while allowing each project to
declare different paths in its own documentation:

```text
AGENTS.md
docs/README.md
docs/contributing/documentation.md
docs/contributing/cross-cutting-concerns.md
docs/product/vision.md
docs/architecture/
docs/reference/
docs/adr/
docs/planning/roadmap.md
docs/planning/implementation-status.md
```

`AGENTS.md` remains a project rule source when present. It is not responsible
for discovering the skills or acting as the required documentation router.

## New and Existing Projects

For a new project, use `project-docs-governance` to copy only the useful files
from `assets/docs-skeleton/`, replace placeholders with verified project facts,
and establish the initial documentation lifecycle.

For an existing project, use it to inventory current docs, preserve useful
facts, identify duplicates and stale claims, migrate toward clear entry points,
and mark superseded or historical material explicitly.

After the governance work is complete, normal repository conversations return
to `repo-docs-router`.

## Document Status

Significant documents can be marked as `Current`, `Draft`, `Experimental`,
`Superseded`, `Historical`, `Archived`, or `Unknown`. Planning items can be
marked as `Planned`, `In progress`, `Shipped`, `Partial`, `Deferred`, `Dropped`,
or `Superseded`.

These markers prevent an old experiment or abandoned plan from silently
presenting itself as current project truth.

## Repository Layout

```text
skills/
  repo-docs-router/
    SKILL.md
    agents/openai.yaml
    references/
    scripts/
  project-docs-governance/
    SKILL.md
    agents/openai.yaml
    references/
    scripts/
    assets/docs-skeleton/
```

## Validation

Validate both skills with the standard skill validator:

```bash
python3 /path/to/skill-creator/scripts/quick_validate.py skills/repo-docs-router
python3 /path/to/skill-creator/scripts/quick_validate.py skills/project-docs-governance
```

The included inventory scripts are read-only:

```bash
python3 skills/repo-docs-router/scripts/inventory_docs.py /path/to/repository
python3 skills/project-docs-governance/scripts/inventory_docs.py /path/to/repository
python3 skills/project-docs-governance/scripts/next_adr_number.py /path/to/repository
```
