"""
Recruitin Boolean Search Generator

A comprehensive toolkit for generating boolean search strings, look-alike matching,
and training data export for recruitment AI models.

## Features

- **Boolean Search Generation**: Generate targeted LinkedIn boolean searches per functiegroep
- **Look-alike Matching**: Find similar profiles across functiegroepen
- **AI Training Data**: Export Hugging Face compatible training datasets
- **Taxonomy Management**: Structured functiegroep definitions with skills/titles/competitors
- **Excel Integration**: Import vacancies, export search results with formatting

## Quick Start

```python
from recruitin_boolean import JobDiggerBooleanProcessor

# Initialize processor
processor = JobDiggerBooleanProcessor()

# Generate searches for a vacancy
searches = processor.search_generator.generate_all_searches_for_vacancy(
    vacancy_title="Senior Software Engineer",
    company="TechCorp",
    location="Amsterdam"
)

# Run full pipeline
files = processor.run_full_pipeline(
    input_file="vacatures.xlsx",
    output_dir="exports/"
)
```

## CLI Usage

```bash
# Show all functiegroepen
python -m recruitin_boolean --show-taxonomy

# Generate searches for specific functiegroep
python -m recruitin_boolean --search werkvoorbereider_elektro

# Process vacancy file
python -m recruitin_boolean -i vacatures.xlsx -o exports/
```

## Package Structure

- `models/`: Data models (FunctieGroep, taxonomie)
- `search/`: Boolean search generation and validation
- `ai/`: Look-alike matching and HF training data export
- `pipeline/`: Main processor, exporters, and CLI interface
"""

from .pipeline import JobDiggerBooleanProcessor, ExcelExporter, DataExporter
from .models import FunctieGroep, FUNCTIEGROEPEN
from .search import BooleanSearchGenerator, SearchValidator
from .ai import LookAlikeMatcher, HuggingFaceDataGenerator

__version__ = "1.0.0"
__author__ = "Recruitin B.V."

__all__ = [
    # Main processor
    "JobDiggerBooleanProcessor",
    # Models
    "FunctieGroep",
    "FUNCTIEGROEPEN",
    # Search functionality
    "BooleanSearchGenerator",
    "SearchValidator",
    # AI components
    "LookAlikeMatcher",
    "HuggingFaceDataGenerator",
    # Exporters
    "ExcelExporter",
    "DataExporter",
]
