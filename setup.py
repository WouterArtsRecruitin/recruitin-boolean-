"""
Setup script for recruitin_boolean package
"""
from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="recruitin-boolean",
    version="1.0.0",
    author="Recruitin B.V.",
    author_email="warts@recruitin.nl",
    description="Production-ready Boolean search automation for technical recruitment with AI-powered lookalike matching",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/WouterArts/recruitin-boolean",
    project_urls={
        "Bug Reports": "https://github.com/WouterArts/recruitin-boolean/issues",
        "Source": "https://github.com/WouterArts/recruitin-boolean",
        "Documentation": "https://github.com/WouterArts/recruitin-boolean#readme",
        "Recruitin": "https://recruitin.nl",
    },
    packages=find_packages(),
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Office/Business :: Human Resources",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Linguistic",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Natural Language :: Dutch",
        "Natural Language :: English",
    ],
    keywords="recruitment boolean search ai technical hiring automation",
    python_requires=">=3.9",
    install_requires=requirements,
    extras_require={
        "dev": [
            "pytest>=6.0",
            "pytest-cov>=2.10.0",
            "black>=21.0.0",
            "flake8>=3.8.0",
            "mypy>=0.910",
            "bandit>=1.7.0",
            "safety>=1.10.0",
        ],
        "excel": [
            "openpyxl>=3.0.0",
        ],
        "ai": [
            "huggingface-hub>=0.16.0",
            "datasets>=2.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "recruitin-boolean=recruitin_boolean.__main__:main",
            "rboolean=recruitin_boolean.__main__:main",
        ],
    },
    include_package_data=True,
    zip_safe=False,
    package_data={
        "recruitin_boolean": ["*.json", "*.yml", "*.yaml"],
    },
)
