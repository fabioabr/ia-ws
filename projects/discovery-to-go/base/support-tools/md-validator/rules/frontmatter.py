"""Frontmatter validation rule.

Validates mandatory fields, formats, and tag conventions
based on conventions/frontmatter/document-schema.md.
"""

import re
from typing import List

from models import Issue, Severity

RULE = "frontmatter"

MANDATORY_FIELDS = [
    "title",
    "description",
    "project-name",
    "version",
    "status",
    "author",
    "category",
    "area",
    "tags",
    "created",
]

VALID_STATUSES = {"rascunho", "ativo", "arquivado", "obsoleto"}

VERSION_PATTERN = re.compile(r"^\d{2}\.\d{2}\.\d{3}$")
CREATED_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}$")
KEBAB_CASE_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
ACCENTED_CHARS_PATTERN = re.compile(r"[àáâãéêíóôõúüç]", re.IGNORECASE)


def validate(
    file_path: str, content: str, frontmatter: dict, body: str
) -> List[Issue]:
    """Validate frontmatter against the document schema."""
    issues: List[Issue] = []

    # No frontmatter at all
    if not frontmatter:
        issues.append(
            Issue(
                rule=RULE,
                severity=Severity.ERROR,
                message="No frontmatter block found.",
            )
        )
        return issues

    # Missing mandatory fields
    for field in MANDATORY_FIELDS:
        if field not in frontmatter:
            issues.append(
                Issue(
                    rule=RULE,
                    severity=Severity.ERROR,
                    message=f"Missing mandatory field: {field}",
                )
            )

    # Version format: XX.YY.ZZZ
    version = frontmatter.get("version")
    if version is not None and not VERSION_PATTERN.match(str(version)):
        issues.append(
            Issue(
                rule=RULE,
                severity=Severity.ERROR,
                message=(
                    f"Invalid version format: '{version}'. "
                    "Expected XX.YY.ZZZ (e.g. 01.00.000)."
                ),
            )
        )

    # Status enum
    status = frontmatter.get("status")
    if status is not None and str(status) not in VALID_STATUSES:
        issues.append(
            Issue(
                rule=RULE,
                severity=Severity.ERROR,
                message=(
                    f"Invalid status: '{status}'. "
                    f"Must be one of: {', '.join(sorted(VALID_STATUSES))}."
                ),
            )
        )

    # Created timestamp format
    created = frontmatter.get("created")
    if created is not None and not CREATED_PATTERN.match(str(created)):
        issues.append(
            Issue(
                rule=RULE,
                severity=Severity.WARNING,
                message=(
                    f"Invalid created format: '{created}'. "
                    "Expected YYYY-MM-DD HH:mm."
                ),
            )
        )

    # Tags validation
    tags = frontmatter.get("tags")
    if tags is not None:
        if not isinstance(tags, list):
            issues.append(
                Issue(
                    rule=RULE,
                    severity=Severity.WARNING,
                    message="Field 'tags' should be a list.",
                )
            )
        else:
            # Count check
            if len(tags) < 2 or len(tags) > 5:
                issues.append(
                    Issue(
                        rule=RULE,
                        severity=Severity.WARNING,
                        message=f"Expected 2-5 tags, found {len(tags)}.",
                    )
                )

            # Individual tag checks
            for tag in tags:
                tag_str = str(tag)
                tag_issues: List[str] = []

                if tag_str != tag_str.lower():
                    tag_issues.append("contains uppercase")

                if ACCENTED_CHARS_PATTERN.search(tag_str):
                    tag_issues.append("contains accented characters")

                if " " in tag_str:
                    tag_issues.append("contains spaces")

                if not KEBAB_CASE_PATTERN.match(tag_str):
                    tag_issues.append("not kebab-case")

                if tag_issues:
                    issues.append(
                        Issue(
                            rule=RULE,
                            severity=Severity.WARNING,
                            message=(
                                f"Tag '{tag_str}': "
                                f"{'; '.join(tag_issues)}. "
                                "Tags must be lowercase kebab-case "
                                "without accents."
                            ),
                        )
                    )

    # Description length
    description = frontmatter.get("description")
    if description is not None and len(str(description)) < 10:
        issues.append(
            Issue(
                rule=RULE,
                severity=Severity.INFO,
                message=(
                    f"Description is very short ({len(str(description))} chars). "
                    "Consider a more descriptive summary."
                ),
            )
        )

    return issues
