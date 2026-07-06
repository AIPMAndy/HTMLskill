# Security Policy

## Supported Versions

We release security updates for the following versions:

| Version | Supported          |
| ------- | ------------------ |
| 0.1.x   | :white_check_mark: |

## Reporting a Vulnerability

We take security seriously. If you discover a security vulnerability, please follow these steps:

### 1. Do Not Open a Public Issue

Please do not create a public GitHub issue for security vulnerabilities.

### 2. Report Privately

Send an email to: **security@htmlskill.dev** (or open a private security advisory on GitHub)

Include:
- Description of the vulnerability
- Steps to reproduce
- Potential impact
- Suggested fix (if any)

### 3. Response Timeline

- **Initial Response**: Within 48 hours
- **Status Update**: Within 7 days
- **Fix Timeline**: Depends on severity
  - Critical: Within 7 days
  - High: Within 14 days
  - Medium: Within 30 days
  - Low: Next regular release

### 4. Disclosure Policy

- We will acknowledge your report within 48 hours
- We will provide a detailed response indicating next steps
- We will notify you when the issue is fixed
- We will publicly disclose the issue after a fix is released
- We will credit you in the security advisory (unless you prefer to remain anonymous)

## Security Best Practices

When using HTMLskill:

### 1. User-Generated Content

Always sanitize user input before passing to HTMLskill:

```python
import html

user_input = html.escape(untrusted_input)
hs.text(user_input)
```

### 2. External Resources

Be cautious when including external resources:

```python
# ❌ Don't use untrusted URLs
hs.image(user_provided_url, alt="Image")

# ✅ Validate and whitelist URLs
if is_trusted_domain(url):
    hs.image(url, alt="Image")
```

### 3. Template Injection

HTMLskill uses Jinja2 templates. Never pass untrusted input directly:

```python
# ❌ Don't do this
template_string = user_input
renderer.render_template(template_string)

# ✅ Use the provided APIs
hs.text(user_input)
```

### 4. Dependency Management

Keep dependencies up to date:

```bash
pip install --upgrade htmlskill
```

### 5. CSP Headers

When deploying HTMLskill-generated pages, use Content Security Policy headers:

```html
<meta http-equiv="Content-Security-Policy" 
      content="default-src 'self'; script-src 'self' 'unsafe-inline';">
```

## Known Security Considerations

### 1. Server-Side Rendering Only

HTMLskill is designed for server-side HTML generation. Do not use it to generate client-side templates.

### 2. No Built-in XSS Protection

HTMLskill does not automatically sanitize input. You must sanitize user-provided content.

### 3. Template Access

The Jinja2 template engine has access to Python objects. Ensure template files are not user-modifiable.

## Security Acknowledgments

We thank the following researchers for responsibly disclosing security issues:

- (None yet - help us by reporting issues!)

## Security Updates

Subscribe to security updates:
- Watch this repository for security advisories
- Check [CHANGELOG.md](CHANGELOG.md) for security fixes
- Follow [@HTMLskill on Twitter](https://twitter.com/htmlskill) (if available)

## Questions?

For security questions that aren't vulnerabilities, please open a regular GitHub issue or discussion.
