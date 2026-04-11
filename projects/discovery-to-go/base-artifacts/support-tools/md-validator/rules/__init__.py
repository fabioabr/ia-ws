from . import (
    acronyms,
    callouts,
    diagrams,
    emojis,
    frontmatter,
    headings,
    naming,
    section_order,
    skill_fields,
    wikilinks,
)

ALL_VALIDATORS = [
    ("frontmatter", frontmatter.validate),
    ("heading", headings.validate),
    ("emoji", emojis.validate),
    ("section-order", section_order.validate),
    ("acronym", acronyms.validate),
    ("wikilink", wikilinks.validate),
    ("callout", callouts.validate),
    ("diagram", diagrams.validate),
    ("naming", naming.validate),
    ("skill-fields", skill_fields.validate),
]
