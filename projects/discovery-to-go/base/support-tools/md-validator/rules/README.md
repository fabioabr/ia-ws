# Validation Rules

Individual rule implementations for the markdown validator. Each module exports a `validate` function that checks one aspect of markdown convention compliance.

## Rules

| Module | Rule ID | What it checks |
|--------|---------|----------------|
| `frontmatter.py` | frontmatter | YAML frontmatter presence and required fields |
| `headings.py` | heading | Heading hierarchy and formatting |
| `emojis.py` | emoji | Emoji usage conventions |
| `section_order.py` | section-order | Required section ordering |
| `acronyms.py` | acronym | Acronym definitions and formatting |
| `wikilinks.py` | wikilink | Wikilink syntax and targets |
| `callouts.py` | callout | Callout block formatting |
| `diagrams.py` | diagram | Diagram block conventions |
| `naming.py` | naming | File and reference naming conventions |
| `skill_fields.py` | skill-fields | SKILL.md-specific frontmatter fields |
