"""Portfolio page example - Showcase projects and skills."""
import htmlskill as hs
from pathlib import Path


@hs.page(mode="web-prototype", design_system="huashu", brand="Jane Doe - Developer")
def portfolio():
    """Create a personal portfolio page."""

    # Navigation
    hs.navbar(
        logo="https://via.placeholder.com/100x40/667eea/ffffff?text=JD",
        links=["About", "Projects", "Skills", "Contact"]
    )

    # Hero section
    with hs.hero(gradient="purple"):
        hs.heading("Hi, I'm Jane Doe 👋", level=1)
        hs.text(
            "Full-Stack Developer passionate about building elegant solutions to complex problems.",
            size="large"
        )
        hs.spacer(height="32px")
        hs.button("View My Work", style="primary", size="large")
        hs.spacer(height="16px")
        hs.button("Download Resume", style="secondary", size="large")

    # About section
    with hs.section(padding="80px 0"):
        with hs.container(max_width="800px"):
            hs.heading("About Me", level=2, align="center")
            hs.spacer(height="32px")
            hs.text(
                "I'm a software developer with 5+ years of experience building web applications. "
                "I specialize in Python, React, and cloud infrastructure. I love turning ideas "
                "into reality through clean, maintainable code.",
                align="center"
            )

    # Projects section
    with hs.section(padding="80px 0"):
        with hs.container(max_width="1200px"):
            hs.heading("Featured Projects", level=2, align="center")
            hs.spacer(height="48px")

            with hs.grid(columns=3, gap="32px"):
                # Project 1
                with hs.card(title="E-Commerce Platform"):
                    hs.text("Full-stack e-commerce solution with payment integration.")
                    hs.spacer(height="16px")
                    hs.text("Tech: React, Django, PostgreSQL, Stripe", size="small", color="#666")
                    hs.spacer(height="24px")
                    hs.button("View Project", style="primary", size="small")

                # Project 2
                with hs.card(title="Task Management App"):
                    hs.text("Collaborative task manager with real-time updates.")
                    hs.spacer(height="16px")
                    hs.text("Tech: Vue.js, FastAPI, Redis, WebSocket", size="small", color="#666")
                    hs.spacer(height="24px")
                    hs.button("View Project", style="primary", size="small")

                # Project 3
                with hs.card(title="Analytics Dashboard"):
                    hs.text("Real-time analytics dashboard for business metrics.")
                    hs.spacer(height="16px")
                    hs.text("Tech: Next.js, Python, ClickHouse, D3.js", size="small", color="#666")
                    hs.spacer(height="24px")
                    hs.button("View Project", style="primary", size="small")

    # Skills section
    with hs.section(padding="80px 0"):
        with hs.container(max_width="1200px"):
            hs.heading("Skills & Technologies", level=2, align="center")
            hs.spacer(height="48px")

            hs.features(items=[
                {
                    "icon": "🐍",
                    "title": "Backend Development",
                    "description": "Python, Django, FastAPI, Flask, Node.js, PostgreSQL, Redis"
                },
                {
                    "icon": "⚛️",
                    "title": "Frontend Development",
                    "description": "React, Vue.js, TypeScript, Next.js, Tailwind CSS, HTML/CSS"
                },
                {
                    "icon": "☁️",
                    "title": "Cloud & DevOps",
                    "description": "AWS, Docker, Kubernetes, CI/CD, Terraform, GitHub Actions"
                },
                {
                    "icon": "🔧",
                    "title": "Tools & Practices",
                    "description": "Git, TDD, Agile, Code Review, System Design, Documentation"
                },
                {
                    "icon": "📊",
                    "title": "Data & Analytics",
                    "description": "SQL, Data Modeling, ETL, Analytics, Pandas, Visualization"
                },
                {
                    "icon": "🎨",
                    "title": "Design",
                    "description": "UI/UX Principles, Figma, Responsive Design, Accessibility"
                },
            ])

    # Testimonials section
    with hs.section(padding="80px 0"):
        with hs.container(max_width="1000px"):
            hs.heading("What People Say", level=2, align="center")
            hs.spacer(height="48px")

            with hs.grid(columns=2, gap="32px"):
                with hs.card():
                    hs.text(
                        '"Jane is an exceptional developer. She delivered our project ahead of schedule '
                        'with code that was clean, well-tested, and maintainable."',
                        size="medium"
                    )
                    hs.spacer(height="24px")
                    hs.text("— Mike Chen, CTO at TechCorp", size="small", color="#666")

                with hs.card():
                    hs.text(
                        '"Working with Jane was a pleasure. Her technical expertise and communication '
                        'skills made the entire development process smooth and efficient."',
                        size="medium"
                    )
                    hs.spacer(height="24px")
                    hs.text("— Sarah Johnson, Product Manager", size="small", color="#666")

    # Contact CTA
    with hs.cta(background="linear-gradient(135deg, #667eea 0%, #764ba2 100%)"):
        hs.heading("Let's Work Together", level=2)
        hs.spacer(height="24px")
        hs.text(
            "I'm available for freelance projects and full-time opportunities. "
            "Let's discuss how I can help bring your ideas to life.",
            size="large"
        )
        hs.spacer(height="32px")
        hs.button("Get in Touch", style="primary", size="large")

    # Footer
    hs.footer(
        copyright="© 2026 Jane Doe. Built with HTMLskill.",
        links=["GitHub", "LinkedIn", "Twitter", "Email"]
    )


if __name__ == "__main__":
    from htmlskill.renderers.web import WebPrototypeRenderer

    ctx = portfolio()
    renderer = WebPrototypeRenderer()
    html = renderer.render(ctx)

    output_dir = Path(__file__).parent / "output"
    output_dir.mkdir(exist_ok=True)
    output_file = output_dir / "portfolio.html"
    output_file.write_text(html, encoding="utf-8")

    print(f"✅ Generated: {output_file}")
    print(f"🌐 Open: file://{output_file.absolute()}")
