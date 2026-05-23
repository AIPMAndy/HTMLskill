from setuptools import setup, find_packages

setup(
    name="htmlskill",
    version="0.1.0",
    description="Python-first HTML generation framework with design system",
    author="Andy",
    author_email="your-email@example.com",
    url="https://github.com/AIPMAndy/python-html-designer",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "jinja2>=3.1.0",
        "click>=8.1.0",
        "playwright>=1.40.0",
        "pillow>=10.0.0",
        "colour-science>=0.4.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.0",
            "pytest-cov>=4.1.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
        ]
    },
    entry_points={
        "console_scripts": [
            "htmlskill=htmlskill.cli.main:cli",
        ],
    },
    python_requires=">=3.10",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
)
