# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |

## Reporting a Vulnerability

We take security vulnerabilities seriously. If you discover a security issue in HTMLskill, please report it responsibly.

### How to Report

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them via:

1. **Email**: Send details to the maintainers (contact information available in package metadata)
2. **GitHub Security Advisories**: Use the [private vulnerability reporting feature](https://github.com/AIPMAndy/HTMLskill/security/advisories/new)

### What to Include

Please include the following information in your report:

- **Description**: A clear description of the vulnerability
- **Impact**: What an attacker could potentially do
- **Reproduction**: Step-by-step instructions to reproduce the issue
- **Affected versions**: Which versions of HTMLskill are affected
- **Suggested fix**: If you have ideas on how to fix it (optional)

### Response Timeline

- **Acknowledgment**: We will acknowledge receipt within 48 hours
- **Initial assessment**: We will provide an initial assessment within 7 days
- **Fix timeline**: We will work on a fix and keep you updated on progress
- **Disclosure**: Once a fix is available, we will coordinate disclosure timing with you

### Security Best Practices

When using HTMLskill:

1. **Input sanitization**: Always sanitize user input before passing it to HTMLskill components
2. **Output context**: Be aware that HTMLskill generates HTML that will be rendered in browsers
3. **Dependencies**: Keep HTMLskill and its dependencies up to date
4. **Code review**: Review generated HTML in security-sensitive contexts

### Known Security Considerations

- HTMLskill does not automatically sanitize HTML input. If you pass user-generated content to components, sanitize it first using libraries like `bleach` or `html.escape()`
- Generated HTML should be served with appropriate Content Security Policy (CSP) headers
- When using in web frameworks, ensure proper authentication and authorization are in place

## Hall of Fame

We will acknowledge security researchers who responsibly disclose vulnerabilities (with their permission):

- *No reports yet*

Thank you for helping keep HTMLskill and its users safe!
