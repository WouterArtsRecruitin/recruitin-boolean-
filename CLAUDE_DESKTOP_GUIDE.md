# Recruitin Boolean - Claude Desktop Handleiding

## Wat is dit?

`recruitin-boolean` is een Python package voor het genereren van Boolean zoekopdrachten voor recruitment. Je kunt het gebruiken om snel professionele zoekstrings te maken voor LinkedIn, Indeed, en andere platforms.

## Installatie

Open een terminal in Claude Desktop en run:

```bash
pip install recruitin-boolean
```

## Basisgebruik

### 1. Boolean Query Genereren

```python
from recruitin_boolean import BooleanBuilder

builder = BooleanBuilder()

# Simpele zoekopdracht
query = builder.build(
    title="Software Developer",
    skills=["Python", "JavaScript", "React"],
    location="Amsterdam"
)
print(query)
```

### 2. Vanuit de Command Line

```bash
# Help bekijken
recruitin-boolean --help

# Of de korte versie
rboolean --help
```

### 3. Vacature Verwerken

```python
from recruitin_boolean import JobDiggerBooleanProcessor

processor = JobDiggerBooleanProcessor()

# Genereer searches voor een vacature
searches = processor.search_generator.generate_all_searches_for_vacancy(
    vacancy_title="Data Engineer",
    company="TechBedrijf",
    location="Utrecht"
)

# Print de resultaten
print(f"Functiegroep: {searches['functiegroep']['naam']}")
for search_type, data in searches['searches'].items():
    print(f"\n{search_type}:")
    print(data['boolean'])
```

## Voorbeelden

### LinkedIn Boolean Search

```python
from recruitin_boolean import BooleanBuilder

builder = BooleanBuilder()

# Voor een Python Developer in Amsterdam
query = builder.build(
    title="Python Developer",
    skills=["Python", "Django", "FastAPI", "PostgreSQL"],
    location="Amsterdam",
    exclude=["Junior", "Intern"]
)

# Resultaat (voorbeeld):
# ("Python Developer" OR "Python Engineer") AND (Python AND Django) AND Amsterdam NOT (Junior OR Intern)
```

### Batch Verwerking van Vacatures

```python
from recruitin_boolean import JobDiggerBooleanProcessor

processor = JobDiggerBooleanProcessor()

# Verwerk een Excel bestand met vacatures
results = processor.run_full_pipeline(
    input_file="vacatures.xlsx",
    output_dir="output/"
)

print(f"Verwerkt: {len(results)} vacatures")
```

## Tips voor Claude Desktop

1. **Vraag om Boolean queries**:
   "Genereer een LinkedIn Boolean search voor een Senior React Developer in Rotterdam"

2. **Batch verwerking**:
   "Verwerk dit Excel bestand met vacatures en maak Boolean searches"

3. **Specifieke platforms**:
   "Maak een Indeed-specifieke zoekstring voor Data Analyst"

## Veelgestelde Vragen

**Q: Werkt het met Nederlandse functietitels?**
A: Ja, de package ondersteunt zowel Nederlandse als Engelse titels.

**Q: Kan ik eigen skills toevoegen?**
A: Ja, je kunt custom skills meegeven aan de `build()` functie.

**Q: Waar vind ik meer documentatie?**
A: https://github.com/WouterArtsRecruitin/recruitin-boolean-

## Support

- GitHub Issues: https://github.com/WouterArtsRecruitin/recruitin-boolean-/issues
- PyPI: https://pypi.org/project/recruitin-boolean/
