#!/usr/bin/env python3
"""
Search Input Validation

Provides validation utilities for boolean search generation inputs.
Basic validation without external dependencies.
"""

from typing import List, Optional, Dict, Any
from dataclasses import dataclass
import re


class VacancyInput(BaseModel):
    """
    Validates vacancy input for boolean search generation.
    """

    title: str = Field(..., min_length=1, max_length=200, description="Job title")
    company: str = Field(..., min_length=1, max_length=100, description="Company name")
    location: str = Field(..., min_length=1, max_length=100, description="Job location")
    fg_id: Optional[str] = Field(None, description="Optional function group ID")

    @validator("title")
    def validate_title(cls, v):
        """Validate job title format."""
        if not v.strip():
            raise ValueError("Title cannot be empty")
        # Remove excessive whitespace
        return re.sub(r"\s+", " ", v.strip())

    @validator("company")
    def validate_company(cls, v):
        """Validate company name."""
        if not v.strip():
            raise ValueError("Company cannot be empty")
        return v.strip()

    @validator("location")
    def validate_location(cls, v):
        """Validate location."""
        if not v.strip():
            raise ValueError("Location cannot be empty")
        return v.strip()


class SearchConfig(BaseModel):
    """
    Configuration for search generation.
    """

    include_location: bool = Field(True, description="Include location in search")
    search_types: List[str] = Field(
        default=[
            "breed",
            "specifiek",
            "lookalike",
            "competitor",
            "skill_based",
            "open_to_work",
            "certification",
        ],
        description="Types of searches to generate",
    )
    max_results_estimate: int = Field(
        2000, ge=10, le=10000, description="Maximum expected results"
    )

    @validator("search_types")
    def validate_search_types(cls, v):
        """Validate search type values."""
        valid_types = {
            "breed",
            "specifiek",
            "lookalike",
            "competitor",
            "skill_based",
            "open_to_work",
            "certification",
        }
        for search_type in v:
            if search_type not in valid_types:
                raise ValueError(f"Invalid search type: {search_type}")
        return v


class BooleanQuery(BaseModel):
    """
    Represents a boolean search query with metadata.
    """

    query: str = Field(..., min_length=1, description="Boolean search string")
    search_type: str = Field(..., description="Type of search")
    priority: str = Field(..., description="Search priority level")
    expected_results: str = Field(..., description="Expected result range")

    @validator("query")
    def validate_query(cls, v):
        """Basic validation of boolean query."""
        if not v.strip():
            raise ValueError("Query cannot be empty")

        # Check for balanced parentheses
        if v.count("(") != v.count(")"):
            raise ValueError("Unbalanced parentheses in query")

        return v.strip()

    @validator("priority")
    def validate_priority(cls, v):
        """Validate priority level."""
        valid_priorities = {"HIGH", "MEDIUM", "LOW"}
        if v not in valid_priorities:
            raise ValueError(f"Priority must be one of: {valid_priorities}")
        return v


class SearchValidator:
    """
    Main validation class for boolean search inputs.
    """

    @staticmethod
    def validate_vacancy_input(data: Dict[str, Any]) -> VacancyInput:
        """
        Validate vacancy input data.

        Args:
            data: Raw input data dictionary

        Returns:
            Validated VacancyInput instance

        Raises:
            ValidationError: If validation fails
        """
        return VacancyInput(**data)

    @staticmethod
    def validate_search_config(data: Dict[str, Any]) -> SearchConfig:
        """
        Validate search configuration.

        Args:
            data: Raw configuration data

        Returns:
            Validated SearchConfig instance
        """
        return SearchConfig(**data)

    @staticmethod
    def validate_boolean_query(
        query: str, search_type: str, priority: str, expected_results: str
    ) -> BooleanQuery:
        """
        Validate a boolean search query.

        Args:
            query: Boolean search string
            search_type: Type of search
            priority: Priority level
            expected_results: Expected result range

        Returns:
            Validated BooleanQuery instance
        """
        return BooleanQuery(
            query=query,
            search_type=search_type,
            priority=priority,
            expected_results=expected_results,
        )

    @staticmethod
    def sanitize_search_term(term: str) -> str:
        """
        Sanitize a search term for boolean queries.

        Args:
            term: Raw search term

        Returns:
            Sanitized search term
        """
        if not term:
            return ""

        # Remove excessive whitespace
        term = re.sub(r"\s+", " ", term.strip())

        # Escape special characters that could break boolean logic
        # But preserve intentional quotes
        if not (term.startswith('"') and term.endswith('"')):
            term = term.replace('"', '\\"')

        return term

    @staticmethod
    def validate_function_group_id(fg_id: str, available_ids: List[str]) -> bool:
        """
        Validate that a function group ID exists.

        Args:
            fg_id: Function group ID to validate
            available_ids: List of available function group IDs

        Returns:
            True if valid, False otherwise
        """
        return fg_id in available_ids

    @staticmethod
    def estimate_query_complexity(query: str) -> Dict[str, Any]:
        """
        Estimate the complexity of a boolean query.

        Args:
            query: Boolean search string

        Returns:
            Dictionary with complexity metrics
        """
        if not query:
            return {"complexity": "invalid", "score": 0}

        # Count operators and terms
        and_count = query.upper().count(" AND ")
        or_count = query.upper().count(" OR ")
        not_count = query.upper().count(" NOT ")
        paren_count = query.count("(")

        # Estimate term count (rough)
        terms = len(
            [t for t in re.split(r"\s+(?:AND|OR|NOT)\s+", query.upper()) if t.strip()]
        )

        # Calculate complexity score
        complexity_score = (
            terms * 1 + and_count * 2 + or_count * 1 + not_count * 3 + paren_count * 1
        )

        # Categorize complexity
        if complexity_score <= 10:
            complexity_level = "simple"
        elif complexity_score <= 25:
            complexity_level = "medium"
        else:
            complexity_level = "complex"

        return {
            "complexity": complexity_level,
            "score": complexity_score,
            "terms": terms,
            "operators": {"and": and_count, "or": or_count, "not": not_count},
            "parentheses": paren_count,
        }
