from dataclasses import dataclass
from enum import Enum
from typing import List, Optional


class Severity(Enum):
    ERROR = "error"
    WARNING = "warning"
    INFO = "info"


@dataclass
class Issue:
    rule: str
    severity: Severity
    message: str
    line: Optional[int] = None


@dataclass
class ValidationResult:
    file_path: str
    issues: List[Issue]

    @property
    def passed(self) -> bool:
        return not any(i.severity == Severity.ERROR for i in self.issues)
