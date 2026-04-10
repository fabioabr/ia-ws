"""Skill-fields validation rule.

Additional frontmatter and body checks specific to SKILL.md files,
based on conventions/frontmatter/skill-schema.md.
"""

import os
import re
from typing import List

from models import Issue, Severity

RULE = "skill-fields"

KEBAB_CASE_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

INPUT_REQUIRED_KEYS = {"name", "type", "required", "description"}
OUTPUT_REQUIRED_KEYS = {"name", "type", "description"}


def validate(
    file_path: str, content: str, frontmatter: dict, body: str
) -> List[Issue]:
    """Validate skill-specific fields for SKILL.md files."""
    # Only applies to SKILL.md files
    basename = os.path.basename(file_path)
    if basename != "SKILL.md":
        return []

    issues: List[Issue] = []

    # --- Frontmatter checks ---

    # Mandatory skill fields
    for field in ("name", "inputs", "outputs"):
        if field not in frontmatter:
            issues.append(
                Issue(
                    rule=RULE,
                    severity=Severity.ERROR,
                    message=f"SKILL.md missing mandatory field: {field}",
                )
            )

    # Name format (kebab-case, no uppercase, no spaces)
    name = frontmatter.get("name")
    if name is not None:
        name_str = str(name)
        if name_str != name_str.lower() or " " in name_str:
            issues.append(
                Issue(
                    rule=RULE,
                    severity=Severity.WARNING,
                    message=(
                        f"Skill name '{name_str}' should be kebab-case "
                        "(lowercase, no spaces)."
                    ),
                )
            )

    # Inputs validation
    inputs = frontmatter.get("inputs")
    if inputs is not None:
        if not isinstance(inputs, list):
            issues.append(
                Issue(
                    rule=RULE,
                    severity=Severity.WARNING,
                    message="Field 'inputs' should be a list.",
                )
            )
        else:
            for idx, inp in enumerate(inputs):
                if not isinstance(inp, dict):
                    continue
                missing = INPUT_REQUIRED_KEYS - set(inp.keys())
                if missing:
                    issues.append(
                        Issue(
                            rule=RULE,
                            severity=Severity.WARNING,
                            message=(
                                f"Input #{idx + 1} missing keys: "
                                f"{', '.join(sorted(missing))}. "
                                "Expected: name, type, required, description."
                            ),
                        )
                    )

    # Outputs validation
    outputs = frontmatter.get("outputs")
    if outputs is not None:
        if not isinstance(outputs, list):
            issues.append(
                Issue(
                    rule=RULE,
                    severity=Severity.WARNING,
                    message="Field 'outputs' should be a list.",
                )
            )
        else:
            for idx, out in enumerate(outputs):
                if not isinstance(out, dict):
                    continue
                missing = OUTPUT_REQUIRED_KEYS - set(out.keys())
                if missing:
                    issues.append(
                        Issue(
                            rule=RULE,
                            severity=Severity.WARNING,
                            message=(
                                f"Output #{idx + 1} missing keys: "
                                f"{', '.join(sorted(missing))}. "
                                "Expected: name, type, description."
                            ),
                        )
                    )

    # --- Body section checks ---

    # Check for "## 🔧 claude-code" section
    if "## 🔧 claude-code" not in body:
        issues.append(
            Issue(
                rule=RULE,
                severity=Severity.WARNING,
                message=(
                    "Missing section '## 🔧 claude-code' in SKILL.md body."
                ),
            )
        )

    # Check for at least one example section (## ... Example ...)
    example_pattern = re.compile(r"^## .*Example", re.MULTILINE | re.IGNORECASE)
    if not example_pattern.search(body):
        issues.append(
            Issue(
                rule=RULE,
                severity=Severity.WARNING,
                message=(
                    "No examples section found. "
                    "SKILL.md should have at least one '## ' heading "
                    "containing 'Example'."
                ),
            )
        )

    return issues
