"""Tests for design constraint checker."""
import pytest
from htmlskill.design.constraints import ConstraintChecker


def test_grid_check_valid():
    checker = ConstraintChecker()
    assert checker.check_grid(8) is True
    assert checker.check_grid(16) is True
    assert checker.check_grid(24) is True
    assert checker.check_grid(32) is True
    assert checker.check_grid(64) is True


def test_grid_check_invalid():
    checker = ConstraintChecker()
    assert checker.check_grid(7) is False
    assert checker.check_grid(15) is False
    assert checker.check_grid(25) is False
    assert checker.check_grid(33) is False


def test_contrast_check_pass():
    checker = ConstraintChecker()
    # Black on white: 21:1
    assert checker.check_contrast("#000000", "#FFFFFF") >= 4.5
    # Dark gray on white: 12.6:1
    assert checker.check_contrast("#333333", "#FFFFFF") >= 4.5


def test_contrast_check_fail():
    checker = ConstraintChecker()
    # Light gray on white: 1.8:1
    assert checker.check_contrast("#CCCCCC", "#FFFFFF") < 4.5


def test_font_stack_cjk_first():
    checker = ConstraintChecker()
    # CJK font first
    assert checker.check_font_stack(["Noto Sans SC", "Inter", "Arial"]) is True
    assert checker.check_font_stack(["Source Han Sans", "Helvetica"]) is True


def test_font_stack_not_cjk_first():
    checker = ConstraintChecker()
    # Latin font first
    assert checker.check_font_stack(["Inter", "Noto Sans SC"]) is False
    assert checker.check_font_stack(["Arial", "Source Han Sans"]) is False
