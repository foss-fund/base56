# base56

Human-readable binary encoding base56.

> Base56 is a variant of [Base58] encoding which further sheds the '1' and the lowercase 'o' characters in order to minimise the risk of fraud and human-error.
>
> [Base58]  is similar to [Base64], but modified to avoid both non-alphanumeric characters (+ and /) and
> letters that might look ambiguous when printed (0 – zero, I – capital i, O – capital o and l – lower-case L).
> Base58 is used to represent bitcoin addresses.[citation needed] Some messaging and social media systems break lines on non-alphanumeric strings. This is avoided by not using URI reserved characters such as +.

See also:

- [Binary-to-text_encoding](https://en.wikipedia.org/wiki/Binary-to-text_encoding)
- [jyn514/base56](https://github.com/jyn514/base56/)

[Base58]: https://en.wikipedia.org/wiki/Base58
[Base64]: https://en.wikipedia.org/wiki/Base64

## Technical details

`base56` translates the binary values from 0-55 to their counterpart
in the following alphabet:
`23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz`

## Usage

```python
>>> from base56 import b56encode, b56decode
>>> b56encode(b"Hello World!")
'JjTDmGcemeMrgbs73'
>>> b56decode('JjTDmGcemeMrgbs73')
b'Hello World!'

```

### Compatibility

We have different alphabets defined because the Go package and other packages
use different alphabets.

```python
>>> from base56 import PY3, GO_STD, GO_ALT, DEFAULT
>>> DEFAULT == PY3
True
>>> DEFAULT
Alphabet(b'23456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnpqrstuvwxyz')
>>> DEFAULT.b56encode(b"Hello World!") # same as above
'JjTDmGcemeMrgbs73'
>>> GO_STD.b56decode(GO_STD.b56encode(b"Hello World!")) # from the Go implementation
b'Hello World!'
>>> GO_ALT.b56decode(GO_ALT.b56encode(b"Hello World!")) # from the PHP/Java implementation
b'Hello World!'

```

## Development

This project is created with tests.
To run them, install `tox`.

```sh
tox
```

To create a new release, push a new tag.

```sh
git tag v0.1.0
git push origin v0.1.0
```

## Changelog

- v0.1.0: Initial release: Alphabets, encode, decode
