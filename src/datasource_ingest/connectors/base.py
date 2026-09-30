from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class BaseConnector(ABC):
    """Base abstraction for source-specific connectors."""

    source_name: str
    source_type: str

    @abstractmethod
    def fetch(self) -> list[dict[str, Any]]:
        """Retrieve records from the upstream source."""

    @abstractmethod
    def normalize(self, records: list[dict[str, Any]]) -> list[dict[str, Any]]:
        """Convert raw source data into a consistent structure."""
