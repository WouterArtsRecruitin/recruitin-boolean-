#!/usr/bin/env python3
"""
Boolean Search Generator

Core logic for generating boolean search strings for LinkedIn and other recruitment platforms.
This module handles the construction of complex search queries based on job functions,
skills, certifications, and other criteria.
"""

from typing import Dict, List, Optional, Tuple
from ..models import FunctieGroep


class BooleanSearchGenerator:
    """
    Genereert boolean search strings voor LinkedIn en andere platforms.
    
    This class provides methods to build sophisticated boolean search strings
    for various recruitment scenarios including title-based searches,
    skill-based searches, competitor searches, and more.
    """

    def __init__(self, functiegroepen: Dict[str, FunctieGroep]):
        """Initialize with function group database."""
        self.functiegroepen = functiegroepen

    def _quote_phrase(self, phrase: str) -> str:
        """
        Zet een phrase tussen quotes als het spaties bevat.
        
        Args:
            phrase: The phrase to potentially quote
            
        Returns:
            Quoted phrase if it contains spaces, otherwise original phrase
        """
        if " " in phrase:
            return f'"{phrase}"'
        return phrase

    def _build_or_clause(self, items: List[str]) -> str:
        """
        Bouwt een OR clause van items.
        
        Args:
            items: List of search terms
            
        Returns:
            OR clause with properly quoted phrases
        """
        quoted = [self._quote_phrase(item) for item in items if item]
        return " OR ".join(quoted)

    def _build_and_clause(self, clauses: List[str]) -> str:
        """
        Bouwt een AND clause van sub-clauses.
        
        Args:
            clauses: List of search clauses
            
        Returns:
            AND clause with properly wrapped sub-clauses
        """
        wrapped = [f"({clause})" if " OR " in clause else clause for clause in clauses if clause]
        return " AND ".join(wrapped)

    def generate_title_search(self, fg: FunctieGroep) -> str:
        """
        Genereert boolean search op basis van functietitels.
        
        Args:
            fg: Function group to generate search for
            
        Returns:
            Boolean search string for job titles
        """
        all_titles = fg.get_all_titles()
        return self._build_or_clause(all_titles)

    def generate_skill_search(self, fg: FunctieGroep) -> str:
        """
        Genereert boolean search op basis van skills.
        
        Args:
            fg: Function group to generate search for
            
        Returns:
            Boolean search string for skills
        """
        return self._build_or_clause(fg.skills)

    def generate_certification_search(self, fg: FunctieGroep) -> str:
        """
        Genereert boolean search op basis van certificeringen.
        
        Args:
            fg: Function group to generate search for
            
        Returns:
            Boolean search string for certifications
        """
        return self._build_or_clause(fg.certificeringen)

    def generate_competitor_search(self, fg: FunctieGroep) -> str:
        """
        Genereert boolean search voor competitor targeting.
        
        Args:
            fg: Function group to generate search for
            
        Returns:
            Boolean search string for competitor companies
        """
        companies = [f'company:"{c}"' for c in fg.concurrenten]
        return " OR ".join(companies)

    def generate_lookalike_company_search(self, fg: FunctieGroep) -> str:
        """
        Genereert boolean search voor huidige werknemers (look-alikes).
        
        Args:
            fg: Function group to generate search for
            
        Returns:
            Boolean search string for typical employer companies
        """
        companies = [f'company:"{c}"' for c in fg.typische_werkgevers]
        return " OR ".join(companies)

    def generate_combined_search(
        self,
        fg: FunctieGroep,
        include_location: bool = False,
        location: Optional[str] = None,
        search_type: str = "breed"
    ) -> Dict[str, str]:
        """
        Genereert gecombineerde boolean searches per type.
        
        This method generates multiple search variations optimized for different
        recruitment scenarios.
        
        Args:
            fg: Function group to generate searches for
            include_location: Whether to include location in base search
            location: Location to include if specified
            search_type: Type of search to generate (not currently used)
            
        Returns:
            Dict with search type as key and boolean string as value
        """
        searches = {}

        # 1. BREED - Alle titels
        title_search = self.generate_title_search(fg)
        if include_location and location:
            searches["breed"] = f"({title_search}) AND ({location})"
        else:
            searches["breed"] = title_search

        # 2. SPECIFIEK - Titels + Sector keywords
        sector_search = self._build_or_clause(fg.sector_keywords)
        if sector_search:
            searches["specifiek"] = f"({title_search}) AND ({sector_search})"

        # 3. LOOKALIKE - Typische werkgevers
        company_search = self.generate_lookalike_company_search(fg)
        if company_search:
            base_titles = self._build_or_clause(fg.titels)  # Alleen hoofdtitels
            searches["lookalike"] = f"({base_titles}) AND ({company_search})"

        # 4. COMPETITOR - Concurrent targeting
        competitor_search = self.generate_competitor_search(fg)
        if competitor_search:
            searches["competitor"] = f"({title_search}) AND ({competitor_search})"

        # 5. SKILL - Skill-based search
        skill_search = self.generate_skill_search(fg)
        if skill_search:
            searches["skill_based"] = f"({title_search}) AND ({skill_search})"

        # 6. OPEN_TO_WORK
        open_to_work = '(#OpenToWork OR "open to work" OR "actively looking" OR "looking for")'
        searches["open_to_work"] = f"({title_search}) AND {open_to_work}"

        # 7. CERTIFICATION - Certificering search
        cert_search = self.generate_certification_search(fg)
        if cert_search:
            searches["certification"] = f"({title_search}) AND ({cert_search})"

        return searches

    def generate_all_searches_for_vacancy(
        self,
        vacancy_title: str,
        company: str,
        location: str,
        fg_id: Optional[str] = None
    ) -> Dict[str, Dict]:
        """
        Genereert alle boolean searches voor een specifieke vacature.
        
        Args:
            vacancy_title: The job title to search for
            company: Company posting the vacancy
            location: Location of the vacancy
            fg_id: Optional function group ID to use
            
        Returns:
            Dict with complete search configuration
        """
        # Probeer de functiegroep te matchen
        if fg_id and fg_id in self.functiegroepen:
            fg = self.functiegroepen[fg_id]
        else:
            fg = self._match_vacancy_to_functiegroep(vacancy_title)

        if not fg:
            return {"error": f"Geen matching functiegroep gevonden voor: {vacancy_title}"}

        # Genereer alle searches
        searches = self.generate_combined_search(fg)

        # Voeg vacancy-specifieke informatie toe
        result = {
            "vacancy": {
                "title": vacancy_title,
                "company": company,
                "location": location
            },
            "functiegroep": {
                "id": fg.id,
                "naam": fg.naam,
                "categorie": fg.categorie
            },
            "searches": {}
        }

        # Bouw de volledige searches met filters
        nearby_locations = self._get_nearby_locations(location)
        location_clause = self._build_or_clause(nearby_locations)

        for search_type, boolean_string in searches.items():
            result["searches"][search_type] = {
                "boolean": boolean_string,
                "boolean_with_location": f"({boolean_string}) AND ({location_clause})",
                "priority": self._get_priority(search_type),
                "expected_results": self._estimate_results(search_type),
                "linkedin_filters": self._get_linkedin_filters(search_type, fg, company, location)
            }

        return result

    def _match_vacancy_to_functiegroep(self, vacancy_title: str) -> Optional[FunctieGroep]:
        """
        Match een vacaturetitel aan de beste functiegroep.
        
        Uses a scoring system based on title matches and sector keywords
        to find the best matching function group.
        
        Args:
            vacancy_title: The job title to match
            
        Returns:
            Best matching FunctieGroep or None if no good match
        """
        title_lower = vacancy_title.lower()
        best_match = None
        best_score = 0

        for fg_id, fg in self.functiegroepen.items():
            score = 0
            all_titles = fg.get_all_titles()

            for title in all_titles:
                if title.lower() in title_lower:
                    score += len(title)  # Langere matches scoren hoger

            for keyword in fg.sector_keywords:
                if keyword.lower() in title_lower:
                    score += 5

            if score > best_score:
                best_score = score
                best_match = fg

        return best_match

    def _get_nearby_locations(self, location: str) -> List[str]:
        """
        Geeft nabijgelegen locaties voor geografische filtering.
        
        Args:
            location: Base location to find nearby locations for
            
        Returns:
            List of nearby locations including the base location
        """
        # Recruitin-specific region mapping for NL
        region_mapping = {
            "GELDERLAND": ["Arnhem", "Nijmegen", "Apeldoorn", "Ede", "Doetinchem"],
            "OVERIJSSEL": ["Zwolle", "Enschede", "Deventer", "Almelo", "Hengelo"],
            "NOORD-BRABANT": ["Eindhoven", "Tilburg", "Breda", "'s-Hertogenbosch", "Helmond"],
            "LIMBURG": ["Maastricht", "Venlo", "Roermond", "Heerlen", "Sittard"],
            "UTRECHT": ["Utrecht", "Amersfoort", "Nieuwegein", "Veenendaal", "Zeist"]
        }

        # Check input validity
        if location is None or (isinstance(location, float) and str(location) == 'nan'):
            return []

        location = str(location).strip()
        if not location:
            return []

        result = [location]
        for region, cities in region_mapping.items():
            if location.upper() in [c.upper() for c in cities]:
                result.extend(cities)
                break
            if location.upper() == region:
                result.extend(cities)
                break

        return list(set(result))

    def _get_priority(self, search_type: str) -> str:
        """Bepaalt de prioriteit van een search type."""
        priorities = {
            "open_to_work": "HIGH",
            "lookalike": "HIGH",
            "competitor": "MEDIUM",
            "specifiek": "MEDIUM",
            "skill_based": "MEDIUM",
            "breed": "LOW",
            "certification": "LOW"
        }
        return priorities.get(search_type, "MEDIUM")

    def _estimate_results(self, search_type: str) -> str:
        """Schat het verwachte aantal resultaten."""
        estimates = {
            "breed": "500-2000",
            "specifiek": "100-500",
            "lookalike": "10-50",
            "competitor": "200-800",
            "skill_based": "100-400",
            "open_to_work": "50-200",
            "certification": "50-150"
        }
        return estimates.get(search_type, "100-500")

    def _get_linkedin_filters(
        self,
        search_type: str,
        fg: FunctieGroep,
        company: str,
        location: str
    ) -> Dict:
        """Genereert aanbevolen LinkedIn Recruiter filters."""
        base_filters = {
            "location": location,
            "industry": self._get_industries(fg)
        }

        if search_type == "open_to_work":
            base_filters["open_to_work"] = True
        elif search_type == "lookalike":
            base_filters["current_company"] = company
        elif search_type == "competitor":
            base_filters["current_past_company"] = fg.concurrenten

        return base_filters

    def _get_industries(self, fg: FunctieGroep) -> List[str]:
        """Bepaalt relevante LinkedIn industries voor een functiegroep."""
        industry_mapping = {
            "werkvoorbereiding": ["Construction", "Engineering", "Utilities"],
            "techniek": ["Construction", "Manufacturing", "Engineering"],
            "automatisering": ["Manufacturing", "Engineering", "IT"],
            "projectleiding": ["Construction", "Engineering"],
            "engineering": ["Engineering", "Manufacturing", "IT"],
            "productie": ["Manufacturing", "Food & Beverage"],
            "metaal": ["Manufacturing", "Construction"],
            "software": ["Information Technology", "Computer Software", "Internet"]
        }
        return industry_mapping.get(fg.categorie, ["Engineering"])
