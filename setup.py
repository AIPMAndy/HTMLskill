"""Setup script for htmlskill package."""
from setuptools import setup, find_packages
from pathlib import Path

# Read the README for long description
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding="utf-8")

setup(
    name="htmlskill",
    version="0.1.0",
    description="Python-first HTML generation framework with built-in design system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Andy",
    author_email="andy@htmlskill.dev",
    url="https://github.com/AIPMAndy/HTMLskill",
    project_urls={
        "Documentation": "https://github.com/AIPMAndy/HTMLskill#readme",
        "Source": "https://github.com/AIPMAndy/HTMLskill",
        "Issues": "https://github.com/AIPMAndy/HTMLskill/issues",
        "Examples": "https://aipmandty.github.io/HTMLskill/",
    },
    packages=find_packages(exclude=["tests", "tests.*"]),
    package_data={
        "htmlskill": ["templates/*.html"],
    },
    include_package_data=True,
    install_requires=[
        "jinja2>=3.1.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "ruff>=0.1.0",
            "mypy>=1.0.0",
            "black>=23.0.0",
            "pre-commit>=3.0.0",
        ],
        "cli": [
            "click>=8.1.0",
        ],
        "image": [
            "pillow>=10.0.0",
        ],
        "full": [
            "click>=8.1.0",
            "pillow>=10.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "htmlskill=htmlskill.cli.main:cli",
        ],
    },
    python_requires=">=3.8",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Text Processing :: Markup :: HTML",
        "Topic :: Software Development :: Code Generators",
    ],
    keywords="html generator python design-system web templating",
    license="MIT",
)
