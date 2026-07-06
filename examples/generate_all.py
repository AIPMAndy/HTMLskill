#!/usr/bin/env python3
"""
Generate all example HTML files.

Run this script to build all examples into the output directory.
"""

from pathlib import Path
import sys

# Add parent directory to path to import htmlskill
sys.path.insert(0, str(Path(__file__).parent.parent))

from htmlskill.renderers.web import WebPrototypeRenderer


def generate_example(example_file: Path, output_dir: Path):
    """Generate HTML from an example Python file."""
    print(f"Generating {example_file.stem}...", end=" ")

    try:
        # Execute the example file
        example_code = example_file.read_text()

        # Check if it has a generate function or main execution
        if "if __name__" in example_code:
            # Import and execute
            import importlib.util
            spec = importlib.util.spec_from_file_location(
                example_file.stem,
                example_file
            )
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)

            print("✅")
            return True
        else:
            print("⏭️  (no main execution)")
            return False

    except Exception as e:
        print(f"❌ Error: {e}")
        return False


def main():
    """Generate all examples."""
    examples_dir = Path(__file__).parent
    output_dir = examples_dir / "output"
    output_dir.mkdir(exist_ok=True)

    # Find all example files
    example_files = sorted(examples_dir.glob("[0-9]*.py"))

    if not example_files:
        print("No example files found!")
        return

    print(f"Found {len(example_files)} example files\n")
    print("=" * 60)

    success_count = 0
    for example_file in example_files:
        if generate_example(example_file, output_dir):
            success_count += 1

    print("=" * 60)
    print(f"\n✨ Generated {success_count}/{len(example_files)} examples")
    print(f"📁 Output directory: {output_dir.absolute()}")
    print(f"\n🌐 Open examples:")

    for html_file in sorted(output_dir.glob("*.html")):
        print(f"   file://{html_file.absolute()}")


if __name__ == "__main__":
    main()
