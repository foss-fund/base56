"""This tests compatibility with other packages."""

import pytest

from base56.alphabet import Alphabet


@pytest.mark.parametrize(
    "data",
    [
        "\x80\x81\x99\x10\x54",
        "hi",
        "there",
        "let's try Unicode",
        "μ",
        "Α α",
        "Β β",
        "Γ γ",
        "Ξ ξ",
        "[ð]",
        "εγγεγραμμένος",
        "𐀆",
        "dskfjlkdsjflkjdslkjflksdjlkfjldskjffkjsdlkjflsdjlkfjlskdjflkjsdlkfjlsdkjfflksdjlkfjdslkjflksdjdlkfjldsjlkfj",
    ],
)
def test_encode_and_decode(data: str, alphabet: Alphabet):
    """Test all the alphabets."""
    d = data.encode("utf-8")
    v = alphabet.encode(d)
    assert alphabet.decode(v) == d
    assert all(ord(c) in alphabet.characters for c in v)
