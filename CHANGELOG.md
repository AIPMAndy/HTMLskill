# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- GitHub Actions CI/CD pipeline with pytest and linting
- Security policy (SECURITY.md)
- This changelog file
- GitHub Topics for better discoverability

## [0.1.0] - 2024

### Added
- Initial release with core API
- Python-first decorator-based API (`@hs.page()`, `@hs.component()`)
- Basic components: heading, text, button, image, spacer, divider
- Layout components: container, grid, section
- Composite components: hero, features, cta
- Design system with 8px grid, WCAG AA compliance, CJK font optimization
- Web template renderer for semantic HTML5 output
- Thread-safe context management
- Component registry and validation
- CLI tool for rendering pages
- Comprehensive test suite
- Documentation and examples

### Design Principles
- Python-first: No templates, no JSX, just Python code
- Zero build tools: Instant HTML output
- Professional design: Built-in design system
- Accessibility: WCAG AA compliant by default
- Type safety: Full IDE autocomplete support

[Unreleased]: https://github.com/AIPMAndy/HTMLskill/compare/v0.1.0...HEAD
[0.1.0]: https://github.com/AIPMAndy/HTMLskill/releases/tag/v0.1.0
