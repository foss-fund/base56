"""Make sure that the results are the same for ambiguous chracters."""

import pytest

from base56.alphabet import Alphabet, PY3, GO_ALT, GO_STD


@pytest.mark.parametrize(
    "ambiguous_char",
    [
        b"1",
        b"l",
        b"I",
        b"o",
        b"O",
        b"0",
    ],
)
@pytest.mark.parametrize("alphabet", [PY3, GO_ALT])
def test_result_is_the_same(ambiguous_char, alphabet: Alphabet):
    """Check that we get the same results."""
    for c in ambiguous_char:
        assert c not in alphabet.characters, f"char: {chr(c)}"


@pytest.mark.parametrize("ambiguous_chars", [b"1lI", b"0oO"])
def test_ambiguity_is_considered(ambiguous_chars, alphabet: Alphabet):
    """Check that the ambiguity is considered if in the alphabet."""
    if not any(c in alphabet.characters for c in ambiguous_chars):
        return
    for c1 in ambiguous_chars:
        for c2 in ambiguous_chars:
            assert alphabet.decode(f"{chr(c1)}2") == alphabet.decode(
                f"{chr(c1)}2"
            ), f"{chr(c1)} should be treated as {chr(c2)}"
