# Agent Instructions

You are working on a **Juju charm** that follows the **holistic reconciliation pattern** using `ops` (Charmed Operator Framework).

## Placeholders

Files contain `__DUNDER__` placeholders that must be replaced when initialising a new charm from this template:

| Placeholder | Meaning |
|---|---|
| `__AUTHOR_NAME__` | Copyright holder |
| `__CHARM_NAME__` | Juju charm name (kebab-case) |
| `__CHARM_TITLE__` | Human-readable title |
| `__CHARM_SUMMARY__` | One-line description |
| `__CHARM_DESCRIPTION__` | Full description |
| `__REPO_LINK__` | GitHub repo URL |
| `__ISSUES_LINK__` | GitHub issues URL |
| `__CHARMHUB_URL__` | Charmhub docs URL |

## Project Structure

```
src/
├── charm.py          # Entry point: observe events, delegate to state + workload
├── state.py          # Single source of truth (CharmState, CharmBaseWithState)
├── config.py         # Pydantic model for charm config (CharmConfig)
├── templates/        # Jinja2 templates for workload config files
tests/
├── unit/             # Unit tests (ops.testing)
└── integration/      # Integration tests (jubilant)
terraform/            # Terraform module for Juju deployment
.github/instructions/ # Detailed design and coding style docs
```

## Design Pattern

**Single reconcile method** — all event handlers call `self.reconcile()` which:
1. Builds `CharmState` from config + relations (via `CharmState.from_charm()`)
2. Passes state to workload module to configure the service
3. Sets unit status

**Module boundaries:**
- `charm.py` — event observation only; no business logic
- `state.py` — aggregates config + relation data into a frozen model
- `config.py` — validates charm config with Pydantic (use `ops.CharmBase.load_config()`)
- Relation handlers — dependency-injected into `CharmState.from_charm()`, never instantiated in state.py

Full design details: `.github/instructions/charm-design-pattern.instructions.md`

## Development Commands

```bash
uv sync --all-groups              # Install all dev dependencies
source .venv/bin/activate         # Activate virtualenv
tox                               # Run lint + unit + static + coverage
tox -e fmt                        # Format code
tox -e lint                       # Lint (codespell, ruff, mypy)
tox -e unit                       # Unit tests only
tox -e integration                # Integration tests
charmcraft pack                   # Build the .charm file
```

## Code Style

- 4 spaces, double quotes, Google-style docstrings
- Constants in UPPER_CASE; project-wide constants in `constants.py`
- Log with `logging`, never log confidential data
- Functions: no side effects, dependency injection, single responsibility
- Type annotations required (`mypy` with `disallow_untyped_defs`)

Full style details: `.github/instructions/general-coding-style.instructions.md`
Review checklist: `.github/instructions/code-review.instructions.md`

## Conventions

- State model uses `model_config = ConfigDict(frozen=True)`
- Config model uses `model_config = ConfigDict(arbitrary_types_allowed=True, frozen=True)`
- Configuration files rendered from Jinja2 templates in `src/templates/`
- Relation handlers expose `get_*()` (never raise) and `write_*()` methods
- `reconcile()` must be idempotent
- Missing config/relations → `BlockedStatus`; runtime errors → logged and reflected in status
