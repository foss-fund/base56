"""Test configuration."""

import pytest

try:
    import base64
except ImportError:
    import sys
    import pathlib

    sys.path.append(pathlib.Path(__file__) / ".." / "..")

from base56 import PY3, GO_STD, GO_ALT, Alphabet


@pytest.fixture(params=[PY3, GO_STD, GO_ALT])
def alphabet(request) -> Alphabet:
    """Return the alphabets."""
    return request.param
