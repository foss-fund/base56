"""The alphabet to use.

There are different alphabets in use.

Attributes:
    GO_STD: The alphajbet used by the Go package.
            See https://pkg.go.dev/toolman.org/encoding/base56
    GO_ALT: The alternative alphabet used by the Go package.
            See https://pkg.go.dev/toolman.org/encoding/base56
            See http://rossduggan.ie/blog/codetry/base-56-integer-encoding-in-php/index.html
    PY3: The alphabet used by Python 3. (default)
            See https://github.com/jyn514/base56
    DEFAULT: The default alphabet.

See also:
- A discussion on alphabets: https://github.com/tep/encoding-base56/issues/1

"""


class Alphabet:

    def __init__(self, alphabet: bytes):
        """Create a new alphabet.

        Args:
            alphabet (bytes): the alphabet to use
        """
        if not isinstance(alphabet, bytes):
            raise TypeError("Create the alphabet with a bytes object.")
        if len(set(alphabet)) != 56:
            raise ValueError("The alphabet must have 56 unique characters.")
        self._characters = alphabet
        self._reversed: list[int] = [-1] * 256

        for i, c in enumerate(alphabet):
            self.reversed[c] = i

    @property
    def characters(self) -> bytes:
        """The characters of the alphabet in correct order."""
        return self._characters

    @property
    def reversed(self) -> list[int]:
        """The alphabet reversed.

        This is 256 long and contains the characters or -1.
        """
        return self._reversed

    def __repr__(self):
        return f"{self.__class__.__name__}({self.characters})"

    def encode(self, data: bytes) -> str:
        """Encode the data bytes into a base56 string."""
        from .encoding import b56encode

        return b56encode(data, self)

    b56encode = encode

    def decode(self, data: str, skip=" \r\n\t") -> bytes:
        """Decode data bytes from a base56 string."""
        from .encoding import b56decode

        return b56decode(data, skip=skip, alphabet=self)

    b56decode = decode


GO_STD = Alphabet(b"0123456789ABCEFGHJKLMNPRSTUVWXYZabcdefghjklmnpqrstuvwxyz")
GO_ALT = Alphabet(b"23456789abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ")
PY3 = Alphabet(b"23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz")
DEFAULT = PY3

__all__ = [
    "GO_STD",
    "GO_ALT",
    "PY3",
    "Alphabet",
    "DEFAULT",
]
