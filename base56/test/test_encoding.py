from base56 import b56encode, b56decode, DEFAULT
from string import printable
import pytest


@pytest.mark.parametrize("i,char", enumerate(DEFAULT.characters))
def test_encode_until_56(i, char):
    """Encode until 56."""
    assert b56encode(bytes([i])) == chr(char) + "2"


@pytest.mark.parametrize("i,char", enumerate(DEFAULT.characters))
def test_decode_until_56(i, char):
    """Encode until 56."""
    assert b56decode(chr(char) + "2") == bytes([i])


@pytest.mark.parametrize("i,char", enumerate(DEFAULT.characters))
def test_encode_until_112(i, char):
    """Encode until 56."""
    assert b56encode(bytes([i + 56])) == chr(char) + "3"


@pytest.mark.parametrize("i,char", enumerate(DEFAULT.characters))
def test_decode_until_112(i, char):
    """Encode until 56."""
    assert b56decode(chr(char) + "3") == bytes([i + 56])


def test_printable_letters():
    """Check all printables."""
    for char in printable:
        c = char.encode("utf-8")
        assert b56decode(b56encode(c)) == c


@pytest.mark.parametrize(
    "data",
    [
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
        "𐀅",
    ],
)
def test_unicode(data):
    """Unicode is alright."""
    d = data.encode("utf-8")
    assert b56decode(b56encode(d)) == d


@pytest.mark.parametrize("data", [b"\x80\x81\x99\x10\x54"])
def test_binary(data):
    """Test binary encode/decode."""
    assert b56decode(b56encode(data)) == data


@pytest.mark.parametrize("char", list(range(256)))
@pytest.mark.parametrize("length", list(range(56)))
def test_long_data(char, length):
    """long data can be encoded and decoded."""
    data = bytes([char] * length)
    assert b56decode(b56encode(data)) == data


def test_empty():
    """Empty string should return empty string"""
    assert b56decode(b56encode(b"")) == b""


def test_error_encode():
    """Test encoding errors."""
    with pytest.raises(TypeError):
        b56encode("")
    with pytest.raises(TypeError):
        b56encode(74887)


def test_error_decode():
    """Test decoding errors."""
    with pytest.raises(TypeError):
        b56decode(b"")
    with pytest.raises(ValueError):
        b56decode("", skip="a")


def test_decode_with_skip():
    """Test decoding with skip."""
    assert b56decode(" " + b56encode(b"abc") + " ", skip=" ") == b"abc"


@pytest.mark.parametrize("s", ["-", ";.,"])
def test_cannot_decode_invalid_character(s):
    """Test decoding errors."""
    with pytest.raises(ValueError):
        b56decode(s, skip=",")
