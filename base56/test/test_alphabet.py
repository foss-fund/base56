from base56 import DEFAULT, Alphabet, PY3, GO_STD, GO_ALT
import pytest


@pytest.mark.parametrize("alphabet", [DEFAULT, PY3, GO_STD, GO_ALT])
def test_length(alphabet):
    """We expect 56."""
    assert len(alphabet.characters) == 56


def test_invalid_type():
    """We can only use bytes."""
    with pytest.raises(TypeError):
        Alphabet(123)


def test_not_enough_characters():
    """We can only use bytes."""
    with pytest.raises(ValueError):
        Alphabet(b"123")
