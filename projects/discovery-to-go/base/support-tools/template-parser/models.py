"""Data models for the template parser.

Represents the AST produced by parsing a report-template `template.md`.
The AST is a faithful structural representation of the template — no
placeholder resolution happens here.
"""

from dataclasses import dataclass, field, asdict
from enum import Enum
from typing import Any, Dict, List, Optional


class CardType(Enum):
    REG = "reg"          # REG-GROUP-NN, optionally with :variant
    CUSTOM = "custom"    # CUSTOM-N
    SUB = "sub"          # SUB-NAME:variant


@dataclass
class Card:
    type: CardType
    id: str                          # "REG-FIN-01", "CUSTOM-1", "SUB-SCENARIO"
    variant: Optional[str] = None    # "total", "{scenario}", "recomendado"

    def to_dict(self) -> Dict[str, Any]:
        return {"type": self.type.value, "id": self.id, "variant": self.variant}


@dataclass
class Row:
    cards: List[Card] = field(default_factory=list)
    line: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        return {"cards": [c.to_dict() for c in self.cards], "line": self.line}


@dataclass
class Section:
    name: str
    rows: List[Row] = field(default_factory=list)
    line: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "rows": [r.to_dict() for r in self.rows],
            "line": self.line,
        }


@dataclass
class Tab:
    name: str
    sections: List[Section] = field(default_factory=list)
    line: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "sections": [s.to_dict() for s in self.sections],
            "line": self.line,
        }


@dataclass
class CustomRegion:
    id: str           # "CUSTOM-1"
    title: str
    prompt: str
    line: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)


@dataclass
class SubTemplate:
    id: str                     # "SUB-SCENARIO"
    title_template: str         # "Cenario ({scenario})"
    sections: List[Section] = field(default_factory=list)
    line: Optional[int] = None

    def to_dict(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "title_template": self.title_template,
            "sections": [s.to_dict() for s in self.sections],
            "line": self.line,
        }


@dataclass
class Template:
    frontmatter: Dict[str, Any] = field(default_factory=dict)
    custom_regions: List[CustomRegion] = field(default_factory=list)
    sub_templates: List[SubTemplate] = field(default_factory=list)
    tabs: List[Tab] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "frontmatter": self.frontmatter,
            "custom_regions": [c.to_dict() for c in self.custom_regions],
            "sub_templates": [s.to_dict() for s in self.sub_templates],
            "tabs": [t.to_dict() for t in self.tabs],
        }


class ParseError(Exception):
    """Raised when the template has invalid syntax."""

    def __init__(self, message: str, line: Optional[int] = None):
        self.line = line
        if line is not None:
            super().__init__(f"line {line}: {message}")
        else:
            super().__init__(message)
