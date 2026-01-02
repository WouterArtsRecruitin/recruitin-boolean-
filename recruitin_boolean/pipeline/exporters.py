"""
Export utilities for Boolean Search data

Handles Excel export, data formatting, and file management
"""

from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any
import pandas as pd
import json

from ..models.functiegroep import FunctieGroep


class ExcelExporter:
    """Handles Excel export functionality"""

    def __init__(self):
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    def export_taxonomy_to_excel(
        self, taxonomy_data: List[Dict[str, Any]], output_path: Path
    ) -> Path:
        """
        Export taxonomy data to Excel format.

        Args:
            taxonomy_data: List of taxonomy dictionaries
            output_path: Path where to save the Excel file

        Returns:
            Path to the created Excel file
        """
        df = pd.DataFrame(taxonomy_data)

        # Create Excel writer with multiple sheets
        with pd.ExcelWriter(output_path, engine="xlsxwriter") as writer:
            # Main data sheet
            df.to_excel(writer, sheet_name="Boolean_Searches", index=False)

            # Summary sheet
            summary = self._create_taxonomy_summary(df)
            summary.to_excel(writer, sheet_name="Summary", index=False)

            # Format sheets
            self._format_taxonomy_sheets(writer, df)

        return output_path

    def export_vacancies_to_excel(
        self, vacancies_data: List[Dict[str, Any]], output_path: Path
    ) -> Path:
        """
        Export vacancy search results to Excel.

        Args:
            vacancies_data: List of vacancy search dictionaries
            output_path: Path where to save the Excel file

        Returns:
            Path to the created Excel file
        """
        df = pd.DataFrame(vacancies_data)

        with pd.ExcelWriter(output_path, engine="xlsxwriter") as writer:
            # Main data
            df.to_excel(writer, sheet_name="Vacancy_Searches", index=False)

            # Pivot tables
            if not df.empty:
                pivot_fg = df.pivot_table(
                    index="Functiegroep",
                    columns="Search_Type",
                    values="Vacature_ID",
                    aggfunc="count",
                    fill_value=0,
                )
                pivot_fg.to_excel(writer, sheet_name="By_Functiegroep")

                # Priority distribution
                priority_dist = df["Priority"].value_counts().to_frame("Count")
                priority_dist.to_excel(writer, sheet_name="Priority_Distribution")

            self._format_vacancy_sheets(writer, df)

        return output_path

    def export_matrix_to_excel(
        self, matrix_df: pd.DataFrame, output_path: Path
    ) -> Path:
        """
        Export similarity matrix to Excel with formatting.

        Args:
            matrix_df: Similarity matrix DataFrame
            output_path: Path where to save the Excel file

        Returns:
            Path to the created Excel file
        """
        with pd.ExcelWriter(output_path, engine="xlsxwriter") as writer:
            matrix_df.to_excel(writer, sheet_name="Similarity_Matrix")

            # Add heatmap formatting
            workbook = writer.book
            worksheet = writer.sheets["Similarity_Matrix"]

            # Create color format for similarity scores
            color_format = workbook.add_format(
                {"bg_color": "#E6F3FF", "border": 1, "num_format": "0.00"}
            )

            # Apply formatting to data range
            max_row = len(matrix_df) + 1
            max_col = len(matrix_df.columns) + 1
            worksheet.conditional_format(
                1,
                1,
                max_row,
                max_col,
                {
                    "type": "3_color_scale",
                    "min_color": "#FF9999",
                    "mid_color": "#FFFF99",
                    "max_color": "#99FF99",
                },
            )

        return output_path

    def _create_taxonomy_summary(self, df: pd.DataFrame) -> pd.DataFrame:
        """Create summary statistics for taxonomy export"""
        summary_data = []

        if not df.empty:
            # Count by functiegroep
            fg_counts = df["Functiegroep_Naam"].value_counts()
            for fg, count in fg_counts.items():
                summary_data.append({"Metric": f"Searches for {fg}", "Value": count})

            # Count by search type
            type_counts = df["Search_Type"].value_counts()
            for search_type, count in type_counts.items():
                summary_data.append(
                    {"Metric": f"{search_type} searches", "Value": count}
                )

            # Total stats
            summary_data.extend(
                [
                    {"Metric": "Total Searches", "Value": len(df)},
                    {
                        "Metric": "Total Functiegroepen",
                        "Value": df["Functiegroep_Naam"].nunique(),
                    },
                    {"Metric": "Search Types", "Value": df["Search_Type"].nunique()},
                    {"Metric": "Export Timestamp", "Value": self.timestamp},
                ]
            )

        return pd.DataFrame(summary_data)

    def _format_taxonomy_sheets(self, writer, df: pd.DataFrame):
        """Apply formatting to taxonomy Excel sheets"""
        workbook = writer.book

        # Header format
        header_format = workbook.add_format(
            {
                "bold": True,
                "text_wrap": True,
                "valign": "top",
                "fg_color": "#366092",
                "font_color": "white",
                "border": 1,
            }
        )

        # Data format
        data_format = workbook.add_format(
            {"text_wrap": True, "valign": "top", "border": 1}
        )

        if "Boolean_Searches" in writer.sheets:
            worksheet = writer.sheets["Boolean_Searches"]

            # Set column widths
            worksheet.set_column("A:A", 15)  # Functiegroep_ID
            worksheet.set_column("B:B", 25)  # Functiegroep_Naam
            worksheet.set_column("C:C", 15)  # Categorie
            worksheet.set_column("D:D", 15)  # Search_Type
            worksheet.set_column("E:E", 60)  # Boolean_String
            worksheet.set_column("F:G", 30)  # Titels, Skills
            worksheet.set_column("H:I", 25)  # Look_Alikes, Concurrenten

            # Format headers
            for col_num, value in enumerate(df.columns.values):
                worksheet.write(0, col_num, value, header_format)

    def _format_vacancy_sheets(self, writer, df: pd.DataFrame):
        """Apply formatting to vacancy Excel sheets"""
        workbook = writer.book

        # Header format
        header_format = workbook.add_format(
            {
                "bold": True,
                "text_wrap": True,
                "valign": "top",
                "fg_color": "#D7E4BD",
                "border": 1,
            }
        )

        if "Vacancy_Searches" in writer.sheets:
            worksheet = writer.sheets["Vacancy_Searches"]

            # Set column widths
            worksheet.set_column("A:A", 12)  # Vacature_ID
            worksheet.set_column("B:B", 30)  # Functietitel
            worksheet.set_column("C:C", 25)  # Bedrijf
            worksheet.set_column("D:D", 20)  # Standplaats
            worksheet.set_column("E:E", 25)  # Functiegroep
            worksheet.set_column("F:F", 15)  # Search_Type
            worksheet.set_column("G:G", 10)  # Priority
            worksheet.set_column("H:H", 60)  # Boolean_String
            worksheet.set_column("I:I", 60)  # Boolean_Met_Locatie
            worksheet.set_column("J:J", 15)  # Verwachte_Resultaten

            # Format headers
            for col_num, value in enumerate(df.columns.values):
                worksheet.write(0, col_num, value, header_format)


class DataExporter:
    """Handles various data export formats"""

    def __init__(self):
        self.timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    def export_to_json(self, data: Any, output_path: Path) -> Path:
        """Export data to JSON format"""
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False, default=str)
        return output_path

    def export_to_csv(self, df: pd.DataFrame, output_path: Path) -> Path:
        """Export DataFrame to CSV format"""
        df.to_csv(output_path, index=False, encoding="utf-8")
        return output_path

    def export_functiegroep_details(
        self, functiegroepen: Dict[str, FunctieGroep], output_dir: Path
    ) -> Dict[str, Path]:
        """Export detailed functiegroep information in multiple formats"""
        output_dir.mkdir(parents=True, exist_ok=True)
        files = {}

        # Create detailed data structure
        detailed_data = {}
        for fg_id, fg in functiegroepen.items():
            detailed_data[fg_id] = {
                "id": fg_id,
                "naam": fg.naam,
                "categorie": fg.categorie,
                "titels": fg.titels,
                "skills": fg.skills,
                "look_alikes": fg.look_alikes,
                "concurrenten": fg.concurrenten,
                "locaties": fg.locaties,
                "meta": {
                    "total_titels": len(fg.titels),
                    "total_skills": len(fg.skills),
                    "total_look_alikes": len(fg.look_alikes),
                    "total_concurrenten": len(fg.concurrenten),
                    "total_locaties": len(fg.locaties),
                },
            }

        # Export as JSON
        json_path = output_dir / f"functiegroepen_detailed_{self.timestamp}.json"
        files["json"] = self.export_to_json(detailed_data, json_path)

        # Export as flat CSV
        flat_data = []
        for fg_id, fg in functiegroepen.items():
            flat_data.append(
                {
                    "Functiegroep_ID": fg_id,
                    "Naam": fg.naam,
                    "Categorie": fg.categorie,
                    "Titels_Count": len(fg.titels),
                    "Skills_Count": len(fg.skills),
                    "Look_Alikes_Count": len(fg.look_alikes),
                    "Concurrenten_Count": len(fg.concurrenten),
                    "Locaties_Count": len(fg.locaties),
                    "Sample_Titels": " | ".join(fg.titels[:3]),
                    "Sample_Skills": " | ".join(fg.skills[:3]),
                    "Sample_Look_Alikes": " | ".join(fg.look_alikes[:3]),
                }
            )

        csv_path = output_dir / f"functiegroepen_overview_{self.timestamp}.csv"
        files["csv"] = self.export_to_csv(pd.DataFrame(flat_data), csv_path)

        return files
