"""Tests for CLI commands."""
import pytest
from click.testing import CliRunner
from htmlskill.cli.main import cli
import tempfile
import os
from pathlib import Path


def test_cli_help():
    runner = CliRunner()
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "HTMLSkill" in result.output
    assert "init" in result.output
    assert "build" in result.output
    assert "check" in result.output


def test_cli_version():
    runner = CliRunner()
    result = runner.invoke(cli, ["version"])
    assert result.exit_code == 0
    assert "0.1.0" in result.output


def test_cli_init():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(cli, ["init", "test-project"])
        assert result.exit_code == 0
        assert "Created project" in result.output

        # Check project structure
        project_path = Path("test-project")
        assert project_path.exists()
        assert (project_path / "app.py").exists()
        assert (project_path / "htmlskill.config.py").exists()
        assert (project_path / "README.md").exists()
        assert (project_path / "assets").exists()
        assert (project_path / "output").exists()


def test_cli_check():
    runner = CliRunner()
    result = runner.invoke(cli, ["check", "examples/01-landing-page.py"])
    assert result.exit_code == 0
    assert "Checking design constraints" in result.output
