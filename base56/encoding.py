"""encoding and decoding in base56"""

from .alphabet import DEFAULT, Alphabet


def b56encode(data: bytes, alphabet: Alphabet = DEFAULT) -> str:
    """Return data encoded in base56

    Throws

    Args:
        data (bytes): the data to encode

    Returns:
        bytes: the data encoded in base56

    Raises:
        TypeError: if data is not bytes
    """
    if not isinstance(data, bytes):
        raise TypeError("data should be bytes or string")

    characters = alphabet.characters
    result = []
    value = 0
    max_value = 1

    for c in data:
        value += max_value * c
        max_value <<= 8

    while max_value:
        result.append(characters[value % 56])
        value //= 56
        max_value //= 56

    return bytes(result).decode("ascii")
    #     print("c", c)
    #     value = (value << 8) + c
    #     max_value <<= 8
    #     while max_value >= 56:
    #         print(f"c {c}, value {value}, max_value {max_value}")
    #         result.append(characters[value % 56])
    #         value //= 56
    #         max_value //= 56
    # if max_value > 0:
    #     result.append(characters[value % 56])
    # return bytes(result).decode("ascii")


def b56decode(data: str, skip: str = " \r\n\t", alphabet: Alphabet = DEFAULT) -> bytes:
    """Decode the base56 encoded data.

    Parameters:
        data (str): data to decode

    Returns:
        bytes: decoded bytes

    Raises:
        ValueError:
            if data is not a valid base56 string
            if a skip value is in the alphabet
        TypeError: if data is not a string
    """

    if not isinstance(data, str):
        raise TypeError("Data should be a string.")
    if any(ord(c) in alphabet.characters for c in skip):
        raise ValueError("Skip values must not be in the alphabet.")

    reversed_alphabet = alphabet.reversed
    result = []
    value = 0
    max_value = 1

    for s in data:
        c = reversed_alphabet[ord(s)]
        if c == -1:
            if s in skip:
                continue
            raise ValueError(
                f'Cannot decode character {repr(s)}. It is not in "{alphabet}".'
            )
        value += c * max_value
        max_value *= 56

    while max_value >= 256:
        result.append(value & 255)
        value >>= 8
        max_value >>= 8

    return bytes(result)


__all__ = ["b56encode", "b56decode"]
