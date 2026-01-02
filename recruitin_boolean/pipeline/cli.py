"""
Command Line Interface for Recruitin Boolean Search Generator

Provides CLI access to all functionality including:
- Boolean search generation
- Taxonomy exports
- Look-alike analysis
- Hugging Face training data generation
"""

import argparse
from pathlib import Path
from typing import Optional

from .processor import JobDiggerBooleanProcessor


def show_taxonomy(processor: JobDiggerBooleanProcessor) -> None:
    """Display the complete functiegroep taxonomy"""
    print("\n📚 FUNCTIEGROEP TAXONOMIE\n")
    for fg_id, fg in processor.functiegroepen.items():
        print(f"{'='*60}")
        print(f"ID: {fg_id}")
        print(f"Naam: {fg.naam}")
        print(f"Categorie: {fg.categorie}")
        print(f"Titels: {', '.join(fg.titels)}")
        print(f"Skills: {', '.join(fg.skills[:5])}")
        print(f"Look-alikes: {', '.join(fg.look_alikes)}")


def show_search_for_functiegroep(
    processor: JobDiggerBooleanProcessor, fg_id: str
) -> None:
    """Show boolean searches for a specific functiegroep"""
    if fg_id in processor.functiegroepen:
        fg = processor.functiegroepen[fg_id]
        searches = processor.search_generator.generate_combined_search(fg)
        print(f"\n🔍 Boolean Searches voor: {fg.naam}\n")
        for search_type, boolean_string in searches.items():
            print(f"\n[{search_type.upper()}]")
            print(f"Boolean: {boolean_string}")
    else:
        print(f"❌ Functiegroep niet gevonden: {fg_id}")
        print(f"   Beschikbare groepen: {', '.join(processor.functiegroepen.keys())}")


def run_pipeline(
    processor: JobDiggerBooleanProcessor,
    input_file: Optional[Path],
    output_dir: Path,
    generate_hf_data: bool,
) -> None:
    """Run the full boolean search generation pipeline"""
    files = processor.run_full_pipeline(
        input_file=input_file, output_dir=output_dir, generate_hf_data=generate_hf_data
    )

    print("\n📂 Gegenereerde bestanden:")
    for name, path in files.items():
        if isinstance(path, dict):
            for sub_name, sub_path in path.items():
                print(f"   - {sub_name}: {sub_path}")
        else:
            print(f"   - {name}: {path}")


def create_parser() -> argparse.ArgumentParser:
    """Create and configure the argument parser"""
    parser = argparse.ArgumentParser(
        description="Recruitin Boolean Search Generator & Hugging Face Training Data Export",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --show-taxonomy                 # Show all functiegroepen
  %(prog)s --search werkvoorbereider_elektro  # Show searches for specific functiegroep
  %(prog)s -i vacatures.xlsx              # Process vacancy file
  %(prog)s -i vacatures.xlsx --no-hf      # Process without HF data generation
  %(prog)s -o /path/to/output              # Custom output directory
        """,
    )

    # Input/Output options
    parser.add_argument(
        "--input", "-i", type=Path, help="Input Excel bestand met vacatures"
    )
    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        default=Path("exports"),
        help="Output directory (default: exports/)",
    )

    # Processing options
    parser.add_argument(
        "--no-hf", action="store_true", help="Skip Hugging Face training data generatie"
    )

    # Information options
    parser.add_argument(
        "--show-taxonomy", action="store_true", help="Toon de functiegroep taxonomie"
    )
    parser.add_argument(
        "--search",
        type=str,
        metavar="FUNCTIEGROEP_ID",
        help="Genereer searches voor een specifieke functiegroep ID",
    )

    # Additional options
    parser.add_argument("--verbose", "-v", action="store_true", help="Verbose output")
    parser.add_argument(
        "--version",
        action="version",
        version="Recruitin Boolean Search Generator v1.0.0",
    )

    return parser


def main() -> None:
    """Main entry point voor CLI gebruik"""
    parser = create_parser()
    args = parser.parse_args()

    # Initialize processor
    processor = JobDiggerBooleanProcessor()

    # Handle information commands first
    if args.show_taxonomy:
        show_taxonomy(processor)
        return

    if args.search:
        show_search_for_functiegroep(processor, args.search)
        return

    # Validate input file if provided
    if args.input and not args.input.exists():
        print(f"❌ Input bestand niet gevonden: {args.input}")
        return

    # Run pipeline
    try:
        run_pipeline(
            processor=processor,
            input_file=args.input,
            output_dir=args.output,
            generate_hf_data=not args.no_hf,
        )
    except Exception as e:
        print(f"❌ Fout tijdens pipeline uitvoering: {e}")
        if args.verbose:
            import traceback

            traceback.print_exc()
        return


if __name__ == "__main__":
    main()
