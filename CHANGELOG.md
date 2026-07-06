# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- GitHub Actions CI/CD pipeline with multi-OS and multi-Python version testing
- Automated release workflow for PyPI publishing
- Issue templates (bug report, feature request)
- Pull request template
- Pre-commit hooks configuration (ruff, mypy, trailing whitespace, etc.)
- Complete example scripts with HTML output generation
- Code quality tools configuration (ruff, mypy, coverage, pytest)
- Enhanced pyproject.toml with full metadata and dependencies

### Changed
- Improved pyproject.toml with comprehensive configuration
- Extended Python version support to 3.8-3.12
- Enhanced documentation structure

### Fixed
- N/A

## [0.1.0] - 2026-01-XX

### Added
- Initial release
- Core API with `@page` and `@component` decorators
- Basic components: heading, text, button, image, spacer, divider
- Layout components: container, grid, section
- Composite components: hero, features, cta, navbar, footer, card
- Web prototype renderer with Jinja2 templates
- Design system with 8px grid and WCAG AA compliance
- Thread-safe render context management
- Comprehensive test suite (30+ tests)
- CLI tool foundation
- Example scripts

[Unreleased]: https://github.com/AIPMAndy/HTMLskill/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/AIPMAndy/HTMLskill/releases/tag/v0.1.0
