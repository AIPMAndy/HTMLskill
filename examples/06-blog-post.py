"""Blog post example - Article layout with sidebar."""
import htmlskill as hs
from pathlib import Path


@hs.page(mode="web-prototype", design_system="huashu", brand="TechBlog")
def blog_post():
    """Create a blog post layout."""

    # Navigation
    hs.navbar(
        logo="https://via.placeholder.com/140x40/667eea/ffffff?text=TechBlog",
        links=["Home", "Articles", "About", "Contact"]
    )

    # Article content
    with hs.container(max_width="1200px"):
        with hs.section(padding="80px 0"):
            # Article header
            hs.heading("Building Scalable Web Applications with Python", level=1)
            hs.text("Published on July 6, 2026 • 10 min read", size="small", color="#666")
            hs.spacer(height="16px")
            hs.text("By John Doe", size="small", color="#999")
            hs.spacer(height="48px")

            # Featured image
            hs.image(
                "https://via.placeholder.com/1200x600/667eea/ffffff?text=Featured+Image",
                alt="Article featured image"
            )
            hs.spacer(height="48px")

            # Article content
            hs.heading("Introduction", level=2)
            hs.text(
                "Python has become one of the most popular languages for web development. "
                "In this article, we'll explore best practices for building scalable applications."
            )
            hs.spacer(height="32px")

            hs.heading("Key Principles", level=2)
            hs.text("When building web applications, keep these principles in mind:")
            hs.spacer(height="16px")

            with hs.card():
                hs.text("• Keep your codebase modular and well-organized")
                hs.text("• Write comprehensive tests for critical functionality")
                hs.text("• Use caching strategies to improve performance")
                hs.text("• Monitor your application in production")
                hs.text("• Plan for horizontal scaling from day one")

            hs.spacer(height="32px")

            hs.heading("Architecture Patterns", level=2)
            hs.text(
                "Modern web applications benefit from clean architecture. "
                "Separate your business logic from your presentation layer, "
                "and use dependency injection to keep components loosely coupled."
            )
            hs.spacer(height="32px")

            hs.heading("Performance Optimization", level=2)
            hs.text(
                "Performance is critical for user experience. Use profiling tools "
                "to identify bottlenecks, implement caching at multiple levels, "
                "and optimize your database queries."
            )
            hs.spacer(height="48px")

            # Related posts
            hs.divider()
            hs.spacer(height="48px")

            hs.heading("Related Articles", level=2, align="center")
            hs.spacer(height="32px")

            with hs.grid(columns=3, gap="24px"):
                with hs.card(title="Python Best Practices"):
                    hs.text("Essential coding standards and patterns for Python developers.")
                    hs.spacer(height="16px")
                    hs.button("Read More", style="secondary", size="small")

                with hs.card(title="Database Optimization"):
                    hs.text("Tips and tricks for optimizing your database performance.")
                    hs.spacer(height="16px")
                    hs.button("Read More", style="secondary", size="small")

                with hs.card(title="Microservices Guide"):
                    hs.text("When and how to split your monolith into microservices.")
                    hs.spacer(height="16px")
                    hs.button("Read More", style="secondary", size="small")

    # CTA section
    with hs.cta(background="linear-gradient(135deg, #667eea 0%, #764ba2 100%)"):
        hs.heading("Subscribe to Our Newsletter", level=2)
        hs.spacer(height="16px")
        hs.text("Get weekly articles about web development directly in your inbox.", size="large")
        hs.spacer(height="32px")
        hs.button("Subscribe Now", style="primary", size="large")

    # Footer
    hs.footer(
        copyright="© 2026 TechBlog. All rights reserved.",
        links=["Privacy Policy", "Terms of Service", "RSS Feed", "Contact"]
    )


if __name__ == "__main__":
    from htmlskill.renderers.web import WebPrototypeRenderer

    ctx = blog_post()
    renderer = WebPrototypeRenderer()
    html = renderer.render(ctx)

    output_dir = Path(__file__).parent / "output"
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / "blog-post.html"
    output_file.write_text(html, encoding="utf-8")

    print(f"✅ Generated: {output_file}")
    print(f"🌐 Open: file://{output_file.absolute()}")
