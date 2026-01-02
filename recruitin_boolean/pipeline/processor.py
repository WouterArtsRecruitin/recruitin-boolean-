"""
JobDigger Boolean Search Processor

Hoofdprocessor die alles combineert:
- Boolean search generatie per functiegroep
- Look-alike matching
- Hugging Face training data export
- Excel export van searches
"""

from datetime import datetime
from pathlib import Path
from typing import Dict, Optional
import json
import pandas as pd

from ..models.taxonomie import FUNCTIEGROEPEN
from ..search.boolean_builder import BooleanSearchGenerator
from ..ai.lookalike_matcher import LookAlikeMatcher
from ..ai.huggingface_exporter import HuggingFaceDataGenerator


class JobDiggerBooleanProcessor:
    """
    Hoofdprocessor die alles combineert:
    - Boolean search generatie per functiegroep
    - Look-alike matching
    - Hugging Face training data export
    - Excel export van searches
    """

    def __init__(self):
        self.functiegroepen = FUNCTIEGROEPEN
        self.search_generator = BooleanSearchGenerator(self.functiegroepen)
        self.lookalike_matcher = LookAlikeMatcher(self.functiegroepen)
        self.hf_generator = HuggingFaceDataGenerator(self.functiegroepen)

    def process_vacancies_file(self, input_file: Path) -> pd.DataFrame:
        """
        Verwerkt een vacature Excel bestand en genereert boolean searches.

        Args:
            input_file: Path naar Excel bestand met vacatures

        Returns:
            DataFrame met gegenereerde searches
        """
        # Lees input
        df = pd.read_excel(input_file, header=1)

        results = []
        for idx, row in df.iterrows():
            vacancy_title = row.get("Vacature", row.get("Functietitel", ""))
            company = row.get("Bedrijf", row.get("Bedrijfsnaam", ""))
            location = row.get("Locatie", row.get("Standplaats", ""))

            if not vacancy_title:
                continue

            # Genereer searches
            searches = self.search_generator.generate_all_searches_for_vacancy(
                vacancy_title=vacancy_title, company=company, location=location
            )

            if "error" not in searches:
                for search_type, search_data in searches.get("searches", {}).items():
                    results.append(
                        {
                            "Vacature_ID": idx + 1,
                            "Functietitel": vacancy_title,
                            "Bedrijf": company,
                            "Standplaats": location,
                            "Functiegroep": searches["functiegroep"]["naam"],
                            "Search_Type": search_type.upper(),
                            "Priority": search_data["priority"],
                            "Boolean_String": search_data["boolean"],
                            "Boolean_Met_Locatie": search_data["boolean_with_location"],
                            "Verwachte_Resultaten": search_data["expected_results"],
                        }
                    )

        return pd.DataFrame(results)

    def generate_full_taxonomy_export(self) -> pd.DataFrame:
        """
        Exporteert de volledige functiegroep taxonomie met searches.

        Returns:
            DataFrame met alle functiegroepen en hun searches
        """
        results = []

        for fg_id, fg in self.functiegroepen.items():
            searches = self.search_generator.generate_combined_search(fg)

            for search_type, boolean_string in searches.items():
                results.append(
                    {
                        "Functiegroep_ID": fg_id,
                        "Functiegroep_Naam": fg.naam,
                        "Categorie": fg.categorie,
                        "Search_Type": search_type.upper(),
                        "Boolean_String": boolean_string,
                        "Titels": " | ".join(fg.titels),
                        "Skills": " | ".join(fg.skills[:5]),
                        "Look_Alikes": " | ".join(fg.look_alikes),
                        "Concurrenten": " | ".join(fg.concurrenten[:5]),
                    }
                )

        return pd.DataFrame(results)

    def generate_lookalike_matrix(self) -> pd.DataFrame:
        """
        Genereert een look-alike similarity matrix.

        Returns:
            DataFrame met similarity scores tussen functiegroepen
        """
        data = []

        for fg1_id, fg1 in self.functiegroepen.items():
            row = {"Functiegroep": fg1.naam}

            for fg2_id, fg2 in self.functiegroepen.items():
                if fg1_id == fg2_id:
                    row[fg2.naam] = 1.0
                else:
                    similarity = self.lookalike_matcher.calculate_similarity(fg1, fg2)
                    row[fg2.naam] = similarity

            data.append(row)

        return pd.DataFrame(data).set_index("Functiegroep")

    def run_full_pipeline(
        self,
        input_file: Optional[Path] = None,
        output_dir: Path = Path("exports"),
        generate_hf_data: bool = True,
    ) -> Dict[str, Path]:
        """
        Voert de volledige pipeline uit.

        Args:
            input_file: Optioneel Excel bestand met vacatures
            output_dir: Directory voor output bestanden
            generate_hf_data: Of Hugging Face data gegenereerd moet worden

        Returns:
            Dict met paden naar alle gegenereerde bestanden
        """
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        files = {}

        # 1. Taxonomie export
        print("📊 Genereren functiegroep taxonomie...")
        taxonomy_df = self.generate_full_taxonomy_export()
        taxonomy_path = output_dir / f"boolean_taxonomy_{timestamp}.xlsx"
        taxonomy_df.to_excel(taxonomy_path, index=False)
        files["taxonomy"] = taxonomy_path
        print(f"   ✅ {len(taxonomy_df)} searches gegenereerd")

        # 2. Look-alike matrix
        print("🔗 Genereren look-alike matrix...")
        matrix_df = self.generate_lookalike_matrix()
        matrix_path = output_dir / f"lookalike_matrix_{timestamp}.xlsx"
        matrix_df.to_excel(matrix_path)
        files["lookalike_matrix"] = matrix_path
        print(f"   ✅ {len(matrix_df)} x {len(matrix_df)} matrix")

        # 3. Verwerk input bestand indien aanwezig
        if input_file and input_file.exists():
            print(f"📁 Verwerken vacatures uit {input_file.name}...")
            vacancies_df = self.process_vacancies_file(input_file)
            vacancies_path = output_dir / f"boolean_searches_{timestamp}.xlsx"
            vacancies_df.to_excel(vacancies_path, index=False)
            files["vacancies"] = vacancies_path
            print(f"   ✅ {len(vacancies_df)} searches voor vacatures")

        # 4. Hugging Face training data
        if generate_hf_data:
            print("🤗 Genereren Hugging Face training data...")
            hf_dir = output_dir / "huggingface_data"
            hf_files = self.hf_generator.export_to_huggingface_format(hf_dir)
            files["huggingface"] = hf_files

            # Print statistics
            with open(hf_files["metadata"], "r") as f:
                metadata = json.load(f)
            stats = metadata.get("statistics", {})
            print(
                f"   ✅ Classification: {stats.get('total_classification_samples', 0)} samples"
            )
            print(
                f"   ✅ Similarity: {stats.get('total_similarity_samples', 0)} samples"
            )
            print(f"   ✅ NER: {stats.get('total_ner_samples', 0)} samples")

        print("\n✨ Pipeline voltooid!")
        return files
