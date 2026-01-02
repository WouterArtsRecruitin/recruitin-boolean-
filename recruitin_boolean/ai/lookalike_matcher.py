#!/usr/bin/env python3
"""
Look-alike Profile Matching

AI-powered matching system for finding similar job profiles and generating
cross-matching boolean searches based on skill overlap and similarity scoring.
"""

from typing import Dict, List, Optional
from ..models import FunctieGroep
from ..search import BooleanSearchGenerator


class LookAlikeMatcher:
    """
    Matcht profielen met vacatures en look-alike profielen.
    
    This class provides AI-powered functionality to:
    1. Find related function groups based on similarity scoring
    2. Generate cross-matching boolean searches
    3. Calculate similarity scores between job functions
    """

    def __init__(self, functiegroepen: Dict[str, FunctieGroep]):
        """
        Initialize with function groups database.
        
        Args:
            functiegroepen: Dictionary of function groups
        """
        self.functiegroepen = functiegroepen
        self.search_generator = BooleanSearchGenerator(functiegroepen)

    def get_lookalike_groups(self, fg_id: str) -> List[FunctieGroep]:
        """
        Haalt look-alike functiegroepen op.
        
        Args:
            fg_id: Function group ID to find look-alikes for
            
        Returns:
            List of similar function groups
        """
        if fg_id not in self.functiegroepen:
            return []

        fg = self.functiegroepen[fg_id]
        look_alikes = []

        for la_id in fg.look_alikes:
            if la_id in self.functiegroepen:
                look_alikes.append(self.functiegroepen[la_id])

        return look_alikes

    def generate_lookalike_searches(self, fg_id: str) -> Dict[str, Dict]:
        """
        Genereert boolean searches voor look-alike matching.

        Dit combineert:
        1. De primaire functiegroep searches
        2. Look-alike functiegroep searches  
        3. Cross-matching searches (combinaties)
        
        Args:
            fg_id: Primary function group ID
            
        Returns:
            Dictionary with primary searches, lookalike searches, and cross-matches
        """
        if fg_id not in self.functiegroepen:
            return {"error": f"Functiegroep niet gevonden: {fg_id}"}

        fg = self.functiegroepen[fg_id]
        look_alikes = self.get_lookalike_groups(fg_id)

        result = {
            "primary_group": {
                "id": fg.id,
                "naam": fg.naam,
                "searches": self.search_generator.generate_combined_search(fg)
            },
            "lookalike_groups": [],
            "cross_match_searches": []
        }

        # Look-alike group searches
        for la_fg in look_alikes:
            la_searches = self.search_generator.generate_combined_search(la_fg)
            result["lookalike_groups"].append({
                "id": la_fg.id,
                "naam": la_fg.naam,
                "similarity_score": self.calculate_similarity(fg, la_fg),
                "searches": la_searches
            })

        # Cross-match searches (combineer skills van beide groepen)
        for la_fg in look_alikes:
            cross_search = self._generate_cross_match_search(fg, la_fg)
            result["cross_match_searches"].append({
                "primary": fg.id,
                "lookalike": la_fg.id,
                "boolean": cross_search,
                "description": f"Profielen met overlap tussen {fg.naam} en {la_fg.naam}"
            })

        return result

    def calculate_similarity(self, fg1: FunctieGroep, fg2: FunctieGroep) -> float:
        """
        Berekent similarity score tussen twee functiegroepen.
        
        Uses multiple factors to calculate similarity:
        - Skill overlap (weighted 40%)
        - Certification overlap (weighted 20%)
        - Sector keyword overlap (weighted 20%) 
        - Category match bonus (weighted 20%)
        
        Args:
            fg1: First function group
            fg2: Second function group
            
        Returns:
            Similarity score between 0.0 and 1.0
        """
        score = 0.0
        max_score = 5.0

        # Skill overlap (most important factor)
        skills1 = set(s.lower() for s in fg1.skills)
        skills2 = set(s.lower() for s in fg2.skills)
        if skills1 and skills2:
            skill_overlap = len(skills1 & skills2) / len(skills1 | skills2)
            score += skill_overlap * 2  # Weight: 40%

        # Certification overlap
        certs1 = set(c.lower() for c in fg1.certificeringen)
        certs2 = set(c.lower() for c in fg2.certificeringen)
        if certs1 and certs2:
            cert_overlap = len(certs1 & certs2) / len(certs1 | certs2)
            score += cert_overlap  # Weight: 20%

        # Sector overlap
        sectors1 = set(s.lower() for s in fg1.sector_keywords)
        sectors2 = set(s.lower() for s in fg2.sector_keywords)
        if sectors1 and sectors2:
            sector_overlap = len(sectors1 & sectors2) / len(sectors1 | sectors2)
            score += sector_overlap  # Weight: 20%

        # Same category bonus
        if fg1.categorie == fg2.categorie:
            score += 1  # Weight: 20%

        return round(score / max_score, 2)

    def find_similar_profiles(self, fg_id: str, similarity_threshold: float = 0.3) -> List[Dict]:
        """
        Find function groups similar to the given one based on calculated similarity.
        
        Args:
            fg_id: Base function group ID
            similarity_threshold: Minimum similarity score (0.0 to 1.0)
            
        Returns:
            List of similar function groups with similarity scores
        """
        if fg_id not in self.functiegroepen:
            return []
        
        base_fg = self.functiegroepen[fg_id]
        similar_profiles = []
        
        for other_id, other_fg in self.functiegroepen.items():
            if other_id == fg_id:
                continue
                
            similarity = self.calculate_similarity(base_fg, other_fg)
            if similarity >= similarity_threshold:
                similar_profiles.append({
                    "id": other_fg.id,
                    "naam": other_fg.naam,
                    "categorie": other_fg.categorie,
                    "similarity_score": similarity
                })
        
        # Sort by similarity score descending
        return sorted(similar_profiles, key=lambda x: x["similarity_score"], reverse=True)

    def generate_hybrid_search(self, primary_fg_id: str, secondary_fg_ids: List[str]) -> str:
        """
        Generate a hybrid boolean search combining multiple function groups.
        
        Args:
            primary_fg_id: Main function group ID
            secondary_fg_ids: List of secondary function group IDs to combine
            
        Returns:
            Hybrid boolean search string
        """
        if primary_fg_id not in self.functiegroepen:
            return ""
        
        primary_fg = self.functiegroepen[primary_fg_id]
        
        # Start with primary function group titles
        all_titles = primary_fg.titels.copy()
        combined_skills = set(primary_fg.skills)
        
        # Add titles and skills from secondary function groups
        for sec_id in secondary_fg_ids:
            if sec_id in self.functiegroepen:
                sec_fg = self.functiegroepen[sec_id]
                all_titles.extend(sec_fg.titels[:2])  # Top 2 titles only
                combined_skills.update(sec_fg.skills[:10])  # Top 10 skills only
        
        # Build the hybrid search
        title_clause = self.search_generator._build_or_clause(list(set(all_titles)))
        skill_clause = self.search_generator._build_or_clause(list(combined_skills)[:15])
        
        return f"({title_clause}) AND ({skill_clause})"

    def _generate_cross_match_search(self, fg1: FunctieGroep, fg2: FunctieGroep) -> str:
        """
        Genereert cross-match boolean search.
        
        Creates a boolean search that targets profiles with overlap between
        two function groups by combining their titles and common skills.
        
        Args:
            fg1: First function group
            fg2: Second function group
            
        Returns:
            Cross-match boolean search string
        """
        # Combineer titels van beide groepen (top 3 each)
        titles1 = fg1.titels[:3]
        titles2 = fg2.titels[:3]
        all_titles = list(set(titles1 + titles2))

        # Gemeenschappelijke skills
        skills1 = set(fg1.skills)
        skills2 = set(fg2.skills)
        common_skills = list(skills1 & skills2)

        title_clause = self.search_generator._build_or_clause(all_titles)

        if common_skills:
            # Use top 5 common skills to avoid overly complex queries
            skill_clause = self.search_generator._build_or_clause(common_skills[:5])
            return f"({title_clause}) AND ({skill_clause})"

        return title_clause

    def analyze_market_overlap(self, fg1_id: str, fg2_id: str) -> Dict:
        """
        Analyze market overlap between two function groups.
        
        Args:
            fg1_id: First function group ID
            fg2_id: Second function group ID
            
        Returns:
            Analysis of market overlap including competition and opportunities
        """
        if fg1_id not in self.functiegroepen or fg2_id not in self.functiegroepen:
            return {"error": "One or both function groups not found"}
        
        fg1 = self.functiegroepen[fg1_id]
        fg2 = self.functiegroepen[fg2_id]
        
        # Calculate overlaps
        skill_overlap = set(fg1.skills) & set(fg2.skills)
        cert_overlap = set(fg1.certificeringen) & set(fg2.certificeringen)
        employer_overlap = set(fg1.typische_werkgevers) & set(fg2.typische_werkgevers)
        competitor_overlap = set(fg1.concurrenten) & set(fg2.concurrenten)
        
        return {
            "function_groups": {
                "fg1": {"id": fg1.id, "naam": fg1.naam, "categorie": fg1.categorie},
                "fg2": {"id": fg2.id, "naam": fg2.naam, "categorie": fg2.categorie}
            },
            "similarity_score": self.calculate_similarity(fg1, fg2),
            "overlaps": {
                "skills": list(skill_overlap),
                "certifications": list(cert_overlap),
                "typical_employers": list(employer_overlap),
                "competitors": list(competitor_overlap)
            },
            "overlap_counts": {
                "skills": len(skill_overlap),
                "certifications": len(cert_overlap), 
                "employers": len(employer_overlap),
                "competitors": len(competitor_overlap)
            },
            "market_insights": {
                "talent_competition": "HIGH" if len(employer_overlap) > 3 else "MEDIUM" if len(employer_overlap) > 1 else "LOW",
                "skill_transferability": "HIGH" if len(skill_overlap) > 10 else "MEDIUM" if len(skill_overlap) > 5 else "LOW",
                "cross_training_potential": "HIGH" if len(cert_overlap) > 3 else "MEDIUM" if len(cert_overlap) > 1 else "LOW"
            }
        }
