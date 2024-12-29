"""Test configuration."""

import pytest

from base56 import PY3, GO_STD, GO_ALT, Alphabet


@pytest.fixture(params=[PY3, GO_STD, GO_ALT])
def alphabet(request) -> Alphabet:
    """Return the alphabets."""
    return request.param
