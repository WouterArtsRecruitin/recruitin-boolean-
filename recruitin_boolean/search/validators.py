#!/usr/bin/env python3
"""
Search Input Validation

Provides validation utilities for boolean search generation inputs.
Basic validation without external dependencies.
"""

from typing import List, Optional, Dict, Any
from dataclasses import dataclass
import re


@dataclass
class VacancyInput:
    """Basic vacancy input validation"""

    title: str
    company: Optional[str] = None
    location: Optional[str] = None
    fg_id: Optional[str] = None

    def __post_init__(self):
        """Validate fields after initialization."""
        if not self.title or not self.title.strip():
            raise ValueError("Title cannot be empty")

        # Clean up whitespace
        self.title = re.sub(r"\s+", " ", self.title.strip())
        if self.company:
            self.company = re.sub(r"\s+", " ", self.company.strip())
        if self.location:
            self.location = re.sub(r"\s+", " ", self.location.strip())


@dataclass
class SearchConfig:
    """Configuration for search generation parameters."""

    max_boolean_length: int = 1000
    include_location: bool = True
    include_competitors: bool = True
    priority_threshold: int = 3
    search_types: List[str] = None

    def __post_init__(self):
        if self.search_types is None:
            self.search_types = ["basic", "comprehensive", "focused", "competitive"]

        if self.max_boolean_length <= 0:
            raise ValueError("max_boolean_length must be positive")


@dataclass
class BooleanQuery:
    """Validated boolean query output."""

    query: str
    search_type: str
    priority: int
    expected_results: str
    complexity_score: float = 0.5

    def __post_init__(self):
        """Basic validation."""
        if not self.query or not self.query.strip():
            raise ValueError("Query cannot be empty")
        if self.priority < 1 or self.priority > 5:
            raise ValueError("Priority must be between 1-5")
        if self.expected_results not in ["low", "medium", "high"]:
            raise ValueError("Expected results must be low, medium, or high")


class SearchValidator:
    """Basic search validation functionality"""

    @staticmethod
    def validate_vacancy(
        title: str,
        company: str = None,
        location: str = None,
        fg_id: Optional[str] = None,
    ) -> VacancyInput:
        """Validate vacancy input parameters."""
        return VacancyInput(
            title=title, company=company, location=location, fg_id=fg_id
        )

    @staticmethod
    def validate_config(config_dict: Dict[str, Any]) -> SearchConfig:
        """Validate search configuration."""
        return SearchConfig(**config_dict)

    @staticmethod
    def sanitize_input(text: str) -> str:
        """Sanitize text input by removing problematic characters."""
        if not text:
            return ""

        # Remove control characters and normalize whitespace
        sanitized = re.sub(r"[\x00-\x1f\x7f-\x9f]", "", text)
        sanitized = re.sub(r"\s+", " ", sanitized.strip())

        return sanitized

    @staticmethod
    def estimate_complexity(query: str) -> float:
        """Estimate query complexity based on various factors."""
        if not query:
            return 0.0

        factors = {
            "length": min(len(query) / 1000.0, 1.0),
            "operators": min(
                (
                    query.upper().count("AND")
                    + query.upper().count("OR")
                    + query.upper().count("NOT")
                )
                / 20.0,
                1.0,
            ),
            "parentheses": min(query.count("(") / 10.0, 1.0),
            "quotes": min(query.count('"') / 20.0, 1.0),
        }

        # Weighted average
        weights = {"length": 0.3, "operators": 0.4, "parentheses": 0.2, "quotes": 0.1}
        complexity = sum(factors[key] * weights[key] for key in factors)

        return min(complexity, 1.0)

    @staticmethod
    def check_functiegroep_coverage(query: str, functiegroep_terms: List[str]) -> float:
        """Check how well a query covers functiegroep terms."""
        if not functiegroep_terms or not query:
            return 0.0

        query_lower = query.lower()
        matched_terms = sum(
            1 for term in functiegroep_terms if term.lower() in query_lower
        )

        return matched_terms / len(functiegroep_terms)
