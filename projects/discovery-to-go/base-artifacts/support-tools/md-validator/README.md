# md-validator

Python CLI tool that validates `.md` files against workspace conventions.

## Usage

```
python main.py <path> [--rule RULE] [--severity SEVERITY] [--format {text,json}] [--skip RULES]
```

## Examples

```
python main.py ./my-document.md
python main.py ./docs/ --severity error
python main.py ./docs/ --rule frontmatter --format json
python main.py ./docs/ --skip emoji,naming
```

## Structure

- `main.py` -- CLI entry point and argument parsing
- `models.py` -- Data models (Issue, Severity)
- `utils.py` -- Shared utilities
- `rules/` -- Individual validation rule implementations
- `requirements.txt` -- Dependencies (pyyaml)
