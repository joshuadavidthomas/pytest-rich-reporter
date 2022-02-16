from __future__ import annotations


def test_help_message(testdir):
    result = testdir.runpytest(
        "--help",
    )
    # fnmatch_lines does an assertion internally
    result.stdout.fnmatch_lines(
        [
            "rich:",
            "*--rich*Enable rich output for the terminal reporter (default:",
            "*False)",
        ]
    )
