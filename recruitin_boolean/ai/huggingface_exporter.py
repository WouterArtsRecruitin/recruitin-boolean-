#!/usr/bin/env python3
"""
Hugging Face Training Data Generator

Generates training datasets for various machine learning tasks including:
1. Text Classification (function group classification)
2. Sentence Similarity (profile-vacancy matching)
3. Named Entity Recognition (skills/certification extraction)
"""

import json
from datetime import datetime
from pathlib import Path
from typing import Dict, List
from dataclasses import asdict

from ..models import FunctieGroep


class HuggingFaceDataGenerator:
    """
    Genereert training data voor Hugging Face modellen.

    Ondersteunt:
    1. Text Classification (functiegroep classificatie)
    2. Sentence Similarity (profiel-vacature matching)
    3. Named Entity Recognition (skills/certificaten extractie)
    """

    def __init__(self, functiegroepen: Dict[str, FunctieGroep]):
        """
        Initialize with function groups database.
        
        Args:
            functiegroepen: Dictionary of function groups for training data generation
        """
        self.functiegroepen = functiegroepen

    def generate_classification_dataset(self) -> List[Dict]:
        """
        Genereert dataset voor text classification.

        Creates training samples for classifying job titles into function groups.
        Each sample contains a job title/description and its corresponding function group.

        Returns:
            List of dictionaries with format: {"text": "...", "label": "functiegroep_id"}
        """
        dataset = []

        for fg_id, fg in self.functiegroepen.items():
            # Genereer variaties van titels
            for title in fg.titels + fg.synoniemen + fg.english_titles:
                dataset.append({
                    "text": title,
                    "label": fg_id,
                    "category": fg.categorie
                })

            # Genereer combinaties van titel + skills
            for title in fg.titels:
                for skill in fg.skills[:5]:  # Top 5 skills only
                    dataset.append({
                        "text": f"{title} met ervaring in {skill}",
                        "label": fg_id,
                        "category": fg.categorie
                    })

            # Genereer combinaties met sector keywords
            for title in fg.titels:
                for keyword in fg.sector_keywords[:3]:  # Top 3 keywords only
                    dataset.append({
                        "text": f"{title} {keyword}",
                        "label": fg_id,
                        "category": fg.categorie
                    })

        return dataset

    def generate_similarity_dataset(self) -> List[Dict]:
        """
        Genereert dataset voor sentence similarity (profiel-vacature matching).

        Creates training pairs for measuring similarity between job descriptions
        and candidate profiles. Includes positive, negative, and neutral examples.

        Returns:
            List of dictionaries with format: 
            {"sentence1": "vacature", "sentence2": "profiel", "score": 0.0-1.0}
        """
        dataset = []

        for fg_id, fg in self.functiegroepen.items():
            # Positieve matches (hoge score)
            for title in fg.titels:
                for synonym in fg.synoniemen:
                    dataset.append({
                        "sentence1": f"Vacature: {title}",
                        "sentence2": f"Profiel: {synonym}",
                        "score": 0.95,
                        "match_type": "exact"
                    })

            # Skill matches (medium-hoge score)
            for title in fg.titels:
                for skill in fg.skills[:10]:  # Top 10 skills
                    dataset.append({
                        "sentence1": f"Vacature: {title} met {skill}",
                        "sentence2": f"Ervaring: {skill}",
                        "score": 0.8,
                        "match_type": "skill"
                    })

            # Look-alike matches (medium score)
            for la_id in fg.look_alikes:
                if la_id in self.functiegroepen:
                    la_fg = self.functiegroepen[la_id]
                    for title1 in fg.titels[:2]:
                        for title2 in la_fg.titels[:2]:
                            dataset.append({
                                "sentence1": f"Vacature: {title1}",
                                "sentence2": f"Profiel: {title2}",
                                "score": 0.6,
                                "match_type": "lookalike"
                            })

            # Negatieve matches (lage score) - different categories
            other_categories = [f for f in self.functiegroepen.values()
                               if f.categorie != fg.categorie]
            for other_fg in other_categories[:3]:  # Max 3 negative examples per function group
                dataset.append({
                    "sentence1": f"Vacature: {fg.titels[0]}",
                    "sentence2": f"Profiel: {other_fg.titels[0]}",
                    "score": 0.1,
                    "match_type": "negative"
                })

        return dataset

    def generate_ner_dataset(self) -> List[Dict]:
        """
        Genereert dataset voor Named Entity Recognition (skill extractie).

        Creates training data for extracting job titles, skills, and certifications
        from job descriptions using BIO tagging scheme.

        Returns:
            List of dictionaries with format: {"tokens": [...], "ner_tags": [...]}
        """
        dataset = []

        for fg_id, fg in self.functiegroepen.items():
            # Genereer voorbeeldzinnen met getagde entities
            for title in fg.titels:
                for skill in fg.skills[:3]:  # Top 3 skills per title
                    text = f"Gezocht: {title} met kennis van {skill}"
                    tokens = text.split()
                    tags = []

                    for token in tokens:
                        if token in title.split():
                            tags.append("B-TITLE" if not tags or tags[-1] not in ["B-TITLE", "I-TITLE"] else "I-TITLE")
                        elif token in skill.split():
                            tags.append("B-SKILL" if not tags or tags[-1] not in ["B-SKILL", "I-SKILL"] else "I-SKILL")
                        else:
                            tags.append("O")

                    dataset.append({
                        "tokens": tokens,
                        "ner_tags": tags,
                        "functiegroep": fg_id
                    })

            # Certificeringen
            for cert in fg.certificeringen[:5]:  # Top 5 certifications
                text = f"Vereist: certificering {cert}"
                tokens = text.split()
                
                # Create proper BIO tags for certification
                tags = ["O", "O"]  # "Vereist:" "certificering"
                cert_tokens = cert.split()
                if cert_tokens:
                    tags.append("B-CERT")
                    tags.extend(["I-CERT"] * (len(cert_tokens) - 1))

                # Ensure tags match tokens length
                tags = tags[:len(tokens)]
                if len(tags) < len(tokens):
                    tags.extend(["O"] * (len(tokens) - len(tags)))

                dataset.append({
                    "tokens": tokens,
                    "ner_tags": tags,
                    "functiegroep": fg_id
                })

        return dataset

    def generate_training_data_bundle(self) -> Dict:
        """
        Genereert complete training data bundle voor alle modellen.
        
        Returns:
            Dictionary containing all training datasets and metadata
        """
        return {
            "classification": self.generate_classification_dataset(),
            "similarity": self.generate_similarity_dataset(),
            "ner": self.generate_ner_dataset(),
            "metadata": {
                "generated_at": datetime.now().isoformat(),
                "num_functiegroepen": len(self.functiegroepen),
                "functiegroepen": list(self.functiegroepen.keys())
            }
        }

    def export_to_huggingface_format(self, output_dir: Path) -> Dict[str, Path]:
        """
        Exporteert training data in Hugging Face compatible formaten.

        Creates JSONL files that can be directly used with Hugging Face
        transformers library for model training.

        Args:
            output_dir: Directory to save the training files

        Returns:
            Dict with file type as key and path as value
        """
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        files = {}

        # Classification dataset (JSONL)
        classification_data = self.generate_classification_dataset()
        classification_path = output_dir / "classification_train.jsonl"
        with open(classification_path, 'w', encoding='utf-8') as f:
            for item in classification_data:
                f.write(json.dumps(item, ensure_ascii=False) + '\n')
        files["classification"] = classification_path

        # Similarity dataset (JSONL)
        similarity_data = self.generate_similarity_dataset()
        similarity_path = output_dir / "similarity_train.jsonl"
        with open(similarity_path, 'w', encoding='utf-8') as f:
            for item in similarity_data:
                f.write(json.dumps(item, ensure_ascii=False) + '\n')
        files["similarity"] = similarity_path

        # NER dataset (JSONL)
        ner_data = self.generate_ner_dataset()
        ner_path = output_dir / "ner_train.jsonl"
        with open(ner_path, 'w', encoding='utf-8') as f:
            for item in ner_data:
                f.write(json.dumps(item, ensure_ascii=False) + '\n')
        files["ner"] = ner_path

        # Metadata
        metadata = {
            "functiegroepen": {fg_id: asdict(fg) for fg_id, fg in self.functiegroepen.items()},
            "statistics": {
                "total_classification_samples": len(classification_data),
                "total_similarity_samples": len(similarity_data),
                "total_ner_samples": len(ner_data)
            },
            "generated_at": datetime.now().isoformat(),
            "data_version": "1.0",
            "supported_tasks": [
                "text-classification",
                "sentence-similarity", 
                "token-classification"
            ]
        }
        metadata_path = output_dir / "metadata.json"
        with open(metadata_path, 'w', encoding='utf-8') as f:
            json.dump(metadata, f, indent=2, ensure_ascii=False)
        files["metadata"] = metadata_path

        # Generate training config files for each task
        self._generate_training_configs(output_dir, files)

        return files

    def _generate_training_configs(self, output_dir: Path, files: Dict[str, Path]) -> None:
        """
        Generate Hugging Face training configuration files.
        
        Args:
            output_dir: Directory to save config files
            files: Dictionary of generated data files
        """
        # Classification config
        classification_config = {
            "task": "text-classification",
            "model_name_or_path": "distilbert-base-multilingual-cased",
            "train_file": str(files["classification"]),
            "validation_split_percentage": 20,
            "output_dir": "./classification_model",
            "num_train_epochs": 3,
            "per_device_train_batch_size": 16,
            "per_device_eval_batch_size": 16,
            "warmup_steps": 500,
            "weight_decay": 0.01,
            "logging_dir": "./logs",
        }
        
        with open(output_dir / "classification_config.json", 'w') as f:
            json.dump(classification_config, f, indent=2)

        # Similarity config  
        similarity_config = {
            "task": "sentence-similarity",
            "model_name_or_path": "sentence-transformers/paraphrase-multilingual-mpnet-base-v2",
            "train_file": str(files["similarity"]),
            "validation_split_percentage": 20,
            "output_dir": "./similarity_model",
            "num_train_epochs": 4,
            "per_device_train_batch_size": 8,
            "per_device_eval_batch_size": 8,
            "warmup_steps": 100,
            "weight_decay": 0.01,
        }
        
        with open(output_dir / "similarity_config.json", 'w') as f:
            json.dump(similarity_config, f, indent=2)

        # NER config
        ner_config = {
            "task": "token-classification",
            "model_name_or_path": "distilbert-base-multilingual-cased", 
            "train_file": str(files["ner"]),
            "validation_split_percentage": 20,
            "output_dir": "./ner_model",
            "num_train_epochs": 3,
            "per_device_train_batch_size": 16,
            "per_device_eval_batch_size": 16,
            "warmup_steps": 500,
            "weight_decay": 0.01,
            "label_all_tokens": True,
        }
        
        with open(output_dir / "ner_config.json", 'w') as f:
            json.dump(ner_config, f, indent=2)

    def export_for_specific_model(self, model_type: str, output_dir: Path) -> Path:
        """
        Export training data optimized for a specific model type.
        
        Args:
            model_type: Type of model ('classification', 'similarity', 'ner')
            output_dir: Directory to save the data
            
        Returns:
            Path to the generated training file
        """
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)
        
        if model_type == "classification":
            data = self.generate_classification_dataset()
            filename = "classification_optimized.jsonl"
        elif model_type == "similarity":
            data = self.generate_similarity_dataset()
            filename = "similarity_optimized.jsonl"
        elif model_type == "ner":
            data = self.generate_ner_dataset()
            filename = "ner_optimized.jsonl"
        else:
            raise ValueError(f"Unknown model type: {model_type}")
        
        output_path = output_dir / filename
        with open(output_path, 'w', encoding='utf-8') as f:
            for item in data:
                f.write(json.dumps(item, ensure_ascii=False) + '\n')
        
        return output_path

    def get_label_mapping(self) -> Dict:
        """
        Get label mapping for classification tasks.
        
        Returns:
            Dictionary mapping function group IDs to human-readable labels
        """
        return {
            fg_id: {
                "name": fg.naam,
                "category": fg.categorie,
                "id": fg_id
            }
            for fg_id, fg in self.functiegroepen.items()
        }

    def get_training_statistics(self) -> Dict:
        """
        Get statistics about the training data.
        
        Returns:
            Dictionary with training data statistics
        """
        classification_data = self.generate_classification_dataset()
        similarity_data = self.generate_similarity_dataset()
        ner_data = self.generate_ner_dataset()
        
        return {
            "total_samples": {
                "classification": len(classification_data),
                "similarity": len(similarity_data), 
                "ner": len(ner_data)
            },
            "function_groups": len(self.functiegroepen),
            "categories": len(set(fg.categorie for fg in self.functiegroepen.values())),
            "total_skills": sum(len(fg.skills) for fg in self.functiegroepen.values()),
            "total_certifications": sum(len(fg.certificeringen) for fg in self.functiegroepen.values()),
            "label_distribution": {
                fg_id: len([item for item in classification_data if item["label"] == fg_id])
                for fg_id in self.functiegroepen.keys()
            }
        }
