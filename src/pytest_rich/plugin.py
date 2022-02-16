from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from _pytest.config.argparsing import Parser


def pytest_addoption(parser: Parser):
    """
    Add options to the pytest command line for the rich plugin

    :param parser: The pytest command line parser
    """
    group = parser.getgroup("rich")
    group.addoption(
        "--rich",
        action="store_true",
        dest="rich",
        default=False,
        help="Enable rich output for the terminal reporter (default: False)",
    )
