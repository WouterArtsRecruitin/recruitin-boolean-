# Recruitin Boolean Search Generator

Een complete toolkit voor het genereren van boolean search strings, look-alike matching, en training data export voor recruitment AI modellen.

## 📋 Features

- **Boolean Search Generatie**: Genereer gerichte LinkedIn boolean searches per functiegroep
- **Look-alike Matching**: Vind vergelijkbare profielen tussen functiegroepen  
- **AI Training Data**: Export Hugging Face compatibele training datasets
- **Taxonomie Management**: Gestructureerde functiegroep definities met skills/titels/concurrenten
- **Excel Integratie**: Import vacatures, export search resultaten met formatting

## 🚀 Quick Start

### Installatie

```bash
pip install recruitin-boolean
```

Of voor development:
```bash
git clone https://github.com/WouterArtsRecruitin/recruitin-boolean-.git
cd recruitin-boolean-
pip install -e .
```

### Python API Usage

```python
from recruitin_boolean import JobDiggerBooleanProcessor

# Initialize processor
processor = JobDiggerBooleanProcessor()

# Generate searches voor een vacature
searches = processor.search_generator.generate_all_searches_for_vacancy(
    vacancy_title="Senior Software Engineer",
    company="TechCorp", 
    location="Amsterdam"
)

print(f"Functiegroep: {searches['functiegroep']['naam']}")
for search_type, search_data in searches['searches'].items():
    print(f"{search_type}: {search_data['boolean']}")

# Run volledige pipeline
files = processor.run_full_pipeline(
    input_file="vacatures.xlsx",
    output_dir="exports/"
)
```

### CLI Usage

```bash
# Toon alle functiegroepen
python -m recruitin_boolean --show-taxonomy

# Genereer searches voor specifieke functiegroep
python -m recruitin_boolean --search werkvoorbereider_elektro

# Verwerk vacancy bestand
python -m recruitin_boolean -i vacatures.xlsx -o exports/

# Skip Hugging Face data generatie
python -m recruitin_boolean -i vacatures.xlsx --no-hf

# Verbose output
python -m recruitin_boolean -i vacatures.xlsx -v
```

## 📦 Package Structuur

```
recruitin_boolean/
├── models/                    # Data modellen
│   ├── functiegroep.py       # FunctieGroep dataclass  
│   └── taxonomie.py          # FUNCTIEGROEPEN database
├── search/                   # Boolean search generatie
│   ├── boolean_builder.py    # BooleanSearchGenerator
│   └── validators.py         # Pydantic validatie (nieuw)
├── ai/                       # AI componenten
│   ├── lookalike_matcher.py  # LookAlikeMatcher
│   └── huggingface_exporter.py # HuggingFaceDataGenerator
├── pipeline/                 # Hoofdorkestratie
│   ├── processor.py          # JobDiggerBooleanProcessor
│   ├── exporters.py          # Excel/data export (nieuw)
│   └── cli.py               # Command-line interface (nieuw)
└── tests/                   # Test suite
    └── test_recruitin_boolean.py
```

## 🔧 Core Components

### 1. FunctieGroep Model

```python
from recruitin_boolean.models import FunctieGroep, FUNCTIEGROEPEN

# Access functiegroep
fg = FUNCTIEGROEPEN['werkvoorbereider_elektro']
print(f"Naam: {fg.naam}")
print(f"Skills: {fg.skills}")
print(f"Concurrenten: {fg.concurrenten}")

# Get all terms
all_terms = fg.get_all_terms()
```

### 2. Boolean Search Generator

```python
from recruitin_boolean.search import BooleanSearchGenerator

generator = BooleanSearchGenerator(FUNCTIEGROEPEN)

# Find matching functiegroep
match = generator.find_best_functiegroep_match("Software Engineer")

# Generate searches voor functiegroep
fg = FUNCTIEGROEPEN['software_engineer']
searches = generator.generate_combined_search(fg)
print(searches['comprehensive'])  # Full boolean string
```

### 3. Look-alike Matcher

```python
from recruitin_boolean.ai import LookAlikeMatcher

matcher = LookAlikeMatcher(FUNCTIEGROEPEN)

# Find similar profiles
similar = matcher.find_similar_profiles('software_engineer', min_similarity=0.3)

# Generate hybrid search
hybrid = matcher.generate_hybrid_search(['software_engineer', 'werkvoorbereider_elektro'])
```

### 4. Hugging Face Exporter

```python
from recruitin_boolean.ai import HuggingFaceDataGenerator

hf_generator = HuggingFaceDataGenerator(FUNCTIEGROEPEN)

# Export training data
files = hf_generator.export_to_huggingface_format("hf_output/")
print(f"Classification data: {files['classification']}")
print(f"Similarity data: {files['similarity']}")
print(f"NER data: {files['ner']}")
```

## 📊 Input/Output Formats

### Vacancy Input Excel Format

```
| Vacature              | Bedrijf   | Locatie   |
|----------------------|-----------|-----------|
| Senior Software Engineer | TechCorp  | Amsterdam |
| Werkvoorbereider Elektro | ElectroCo | Utrecht   |
```

### Output Boolean Searches

```
| Functiegroep | Search_Type | Boolean_String | Priority |
|--------------|-------------|---------------|----------|
| Software Engineer | COMPREHENSIVE | (software engineer OR developer) AND (python OR java) | 1 |
| Software Engineer | FOCUSED | software engineer AND python | 2 |
```

## 🧪 Testing

```bash
# Run all tests
python -m pytest tests/

# Run specific test
python -m pytest tests/test_recruitin_boolean.py::TestBooleanSearchGenerator

# Run with coverage
pip install pytest-cov
python -m pytest tests/ --cov=recruitin_boolean --cov-report=html
```

## 🔍 Available Functiegroepen

Momenteel ondersteunde functiegroepen:

- `werkvoorbereider_elektro` - Werkvoorbereider Elektrotechniek
- `werkvoorbereider_installatie` - Werkvoorbereider Installatietechniek  
- `calculator_bouw` - Calculator Bouw
- `software_engineer` - Software Engineer/Developer
- `operator` - Operator/Machinist

Elke functiegroep bevat:
- **Titels**: Functietitels en variaties
- **Skills**: Technische vaardigheden
- **Look-alikes**: Vergelijkbare rollen
- **Concurrenten**: Bedrijven in de sector
- **Locaties**: Relevante locaties

## ⚙️ Configuration

### Search Parameters

```python
# Customize search generation
generator = BooleanSearchGenerator(FUNCTIEGROEPEN)

# Override LinkedIn location mapping
custom_locations = {
    "Amsterdam": "Netherlands > North Holland > Amsterdam",
    "Custom City": "Netherlands > Province > City"
}
generator.linkedin_locations.update(custom_locations)

# Generate with custom location
searches = generator.generate_all_searches_for_vacancy(
    vacancy_title="Software Engineer",
    location="Custom City"
)
```

### Export Settings

```python
# Customize output directory structure
files = processor.run_full_pipeline(
    input_file="vacatures.xlsx",
    output_dir="custom_exports/",
    generate_hf_data=False  # Skip HF data generation
)
```

## 🤝 Contributing

1. Maak een feature branch
2. Voeg tests toe voor nieuwe functionaliteit
3. Run tests: `python -m pytest`
4. Update documentatie
5. Submit pull request

## 📈 Performance

- **Boolean Generation**: ~1ms per functiegroep
- **Vacancy Processing**: ~10ms per vacature
- **Look-alike Matrix**: ~100ms voor 5x5 matrix
- **HF Export**: ~500ms voor alle datasets

## 🛠️ Dependencies

- `pandas`: Excel processing
- `openpyxl`: Excel export formatting
- `pydantic`: Data validation
- `scikit-learn`: Similarity calculations
- `pytest`: Testing framework

## 📄 License

Eigendom van Recruitin B.V. - Alle rechten voorbehouden.

## 📞 Support

Voor vragen en ondersteuning:
- Email: wouter@recruitin.nl
- GitHub Issues: <repo-issues-url>

---

**Recruitin B.V.** - Technisch recruitment geautomatiseerd 🤖
