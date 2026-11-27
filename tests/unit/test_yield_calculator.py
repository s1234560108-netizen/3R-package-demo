"""Tests for the yield calculator."""

import pytest
from click.testing import CliRunner

from three_r_package.demo_module import calculate_yield
from three_r_package.scripts.three_r_package_script import three_r_package_cli


@pytest.mark.parametrize(
    "passed, total, expected",
    [
        (965, 1000, 96.5),
        (80, 100, 80.0),
        (0, 100, 0.0),
        (100, 100, 100.0),
    ],
)
def test_calculate_yield(passed, total, expected):
    assert calculate_yield(passed, total) == pytest.approx(expected)


@pytest.mark.parametrize(
    "passed, total",
    [(110, 100), (0, 0), (-1, 100), (10, -100)],
)
def test_invalid_input(passed, total):
    with pytest.raises(ValueError):
        calculate_yield(passed, total)


def test_yield_cli():
    runner = CliRunner()
    result = runner.invoke(three_r_package_cli, ["--passed", "965", "--total", "1000"])
    assert result.exit_code == 0
    assert "Yield rate: 96.50%" in result.output
