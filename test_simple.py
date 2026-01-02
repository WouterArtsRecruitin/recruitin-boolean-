"""
Simplified test for Boolean Search Generator
"""

import pytest
import sys
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))

# Manually load the necessary modules
exec(open(project_root / "recruitin_boolean" / "models" / "functiegroep.py").read())
exec(open(project_root / "recruitin_boolean" / "models" / "taxonomie.py").read())
exec(open(project_root / "recruitin_boolean" / "search" / "boolean_builder.py").read())


class TestBooleanSearchGenerator:
    def test_generate_7_search_variants(self):
        """Test that all 7 search variants are generated for complete FunctieGroep"""

        # Create a functiegroep with all data types populated
        functiegroep_data = {
            "naam": "test_functiegroep",
            "functietitels": ["Software Engineer", "Developer"],
            "vaardigheden": ["Python", "JavaScript", "SQL", "API"],
            "certificaten": ["AWS", "Azure", "Kubernetes"],
            "concurrent_bedrijven": ["Google", "Microsoft", "Apple"],
            "locaties": ["Amsterdam", "Utrecht"],
            "synoniem_titels": ["Programmer", "Coder"],
            "synoniem_vaardigheden": ["Programming", "Coding"],
            "verwante_functies": ["Backend Developer", "Full Stack"],
        }

        functiegroep = FunctieGroep(**functiegroep_data)
        generator = BooleanSearchGenerator()

        searches = generator.generate_search_variants(functiegroep)

        # Should have all 7 variants
        assert len(searches) == 7
        expected_variants = [
            "breed",
            "specifiek",
            "lookalike",
            "competitor",
            "skill_based",
            "open_to_work",
            "certification",
        ]
        assert set(searches.keys()) == set(expected_variants)

        # Each search should be non-empty string
        for variant, search in searches.items():
            assert isinstance(search, str)
            assert len(search) > 0
            print(f"✅ {variant}: {len(search)} characters")

    def test_search_variant_content_quality(self):
        """Test that each search variant contains expected Boolean operators and structure"""

        functiegroep_data = {
            "naam": "werkvoorbereider_elektro",
            "functietitels": ["Werkvoorbereider Elektro", "Electrical Planner"],
            "vaardigheden": ["AutoCAD", "EPLAN", "Elektrotechniek", "PLC"],
            "certificaten": ["VCA", "NEN3140"],
            "concurrent_bedrijven": ["Siemens", "Schneider Electric"],
            "locaties": ["Rotterdam", "Den Haag"],
        }

        functiegroep = FunctieGroep(**functiegroep_data)
        generator = BooleanSearchGenerator()
        searches = generator.generate_search_variants(functiegroep)

        # Test Boolean structure quality
        for variant, search in searches.items():
            # Should contain Boolean operators
            boolean_operators = ["OR", "AND", "(", ")"]
            has_boolean = any(op in search for op in boolean_operators)
            assert has_boolean, f"{variant} search should contain Boolean operators"

            # Should be reasonable length
            assert (
                10 <= len(search) <= 1000
            ), f"{variant} search should be 10-1000 characters"

            print(f"✅ {variant}: Boolean operators present, {len(search)} chars")

    def test_search_variant_length_limits(self):
        """Test search variants respect platform length limits"""

        # Create complex functiegroep with many fields
        functiegroep_data = {
            "naam": "complex_functiegroep",
            "functietitels": [
                "Senior Software Engineer",
                "Lead Developer",
                "Technical Architect",
                "Full Stack Engineer",
            ],
            "vaardigheden": [
                "Python",
                "JavaScript",
                "TypeScript",
                "React",
                "Node.js",
                "PostgreSQL",
                "MongoDB",
                "AWS",
            ],
            "certificaten": [
                "AWS Solutions Architect",
                "Google Cloud Professional",
                "Kubernetes Administrator",
                "Scrum Master",
            ],
            "concurrent_bedrijven": ["Google", "Microsoft", "Apple", "Amazon", "Meta"],
            "locaties": ["Amsterdam", "Rotterdam", "Utrecht", "Eindhoven"],
        }

        functiegroep = FunctieGroep(**functiegroep_data)
        generator = BooleanSearchGenerator()
        searches = generator.generate_search_variants(functiegroep)

        # Test length constraints
        for variant, search in searches.items():
            # LinkedIn search limit
            assert (
                len(search) <= 1000
            ), f"{variant} search exceeds LinkedIn 1000 char limit: {len(search)}"

            # Meaningful minimum
            assert (
                len(search) >= 10
            ), f"{variant} search too short to be meaningful: {len(search)}"

            print(f"✅ {variant}: {len(search)} chars (within limits)")


if __name__ == "__main__":
    test_instance = TestBooleanSearchGenerator()

    print("🧪 Running Boolean Search Generator Tests...")
    print()

    try:
        print("Test 1: Generate 7 Search Variants")
        test_instance.test_generate_7_search_variants()
        print("✅ PASSED\n")

        print("Test 2: Search Variant Content Quality")
        test_instance.test_search_variant_content_quality()
        print("✅ PASSED\n")

        print("Test 3: Search Variant Length Limits")
        test_instance.test_search_variant_length_limits()
        print("✅ PASSED\n")

        print("🎉 ALL TESTS PASSED!")

    except Exception as e:
        print(f"❌ TEST FAILED: {e}")
        raise e
