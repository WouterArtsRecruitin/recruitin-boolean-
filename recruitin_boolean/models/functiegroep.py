#!/usr/bin/env python3
"""
FunctieGroep Data Model

Defines the core data structure for job function groups used in boolean search generation.
"""

from dataclasses import dataclass, field, asdict
from typing import List, Dict, Optional, Set


@dataclass
class FunctieGroep:
    """
    Definieert een functiegroep met alle gerelateerde data voor boolean searches.
    
    Deze dataclass bevat alle informatie die nodig is om effectieve boolean search
    strings te genereren voor verschillende recruitment platforms zoals LinkedIn.
    
    Attributes:
        id: Unieke identifier voor de functiegroep
        naam: Menselijk leesbare naam
        categorie: Hoofdcategorie (engineering, productie, techniek, etc.)
        titels: Kerntitels voor boolean search
        synoniemen: Synoniemen en variaties van functietitels
        english_titles: Engelstalige equivalenten
        skills: Gerelateerde vaardigheden en tools
        certificeringen: Relevante certificaten en opleidingen
        look_alikes: Gerelateerde functiegroepen (ID's)
        typische_werkgevers: Bedrijven waar deze functies vaak voorkomen
        concurrenten: Concurrerende bedrijven (voor competitor search)
        seniority_levels: Verschillende senioriteitsniveaus
        sector_keywords: Sector-specifieke zoekwoorden
    """

    id: str
    naam: str
    categorie: str  # engineering, productie, techniek, etc.

    # Kerntitels voor boolean search
    titels: List[str] = field(default_factory=list)

    # Synoniemen en variaties
    synoniemen: List[str] = field(default_factory=list)

    # Engels equivalent
    english_titles: List[str] = field(default_factory=list)

    # Gerelateerde skills/tools
    skills: List[str] = field(default_factory=list)

    # Certificeringen/opleidingen
    certificeringen: List[str] = field(default_factory=list)

    # Look-alike functiegroepen (ID's)
    look_alikes: List[str] = field(default_factory=list)

    # Typische werkgevers/bedrijven in deze sector
    typische_werkgevers: List[str] = field(default_factory=list)

    # Concurrenten (voor competitor search)
    concurrenten: List[str] = field(default_factory=list)

    # Senioriteitsniveaus
    seniority_levels: List[str] = field(default_factory=lambda: [
        "junior", "medior", "senior", "lead", "hoofd", "manager"
    ])

    # Sector keywords
    sector_keywords: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict:
        """Convert to dictionary for serialization."""
        return asdict(self)
    
    def get_all_titles(self) -> List[str]:
        """Get all titles including synonyms and English titles."""
        return self.titels + self.synoniemen + self.english_titles
    
    def get_unique_skills(self) -> Set[str]:
        """Get unique skills as a set."""
        return set(self.skills)
    
    def has_skill(self, skill: str) -> bool:
        """Check if this function group includes a specific skill."""
        return skill.lower() in [s.lower() for s in self.skills]
    
    def matches_title(self, title: str) -> bool:
        """Check if a given title matches any of this group's titles."""
        title_lower = title.lower()
        all_titles = self.get_all_titles()
        return any(t.lower() in title_lower for t in all_titles)
