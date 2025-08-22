# sortable-float: Alphabetically sortable float representation

This is a simple algorithm for encoding float numbers as alphabetically sortable strings. The resulting string is of fixed length (significant figures + 6).

It is inspired by IEEE 754 and by [koalamer/conust](https://github.com/koalamer/conust), which proposes an "inversion" of digits to handle the sorting of negative numbers. When needed, the digits of the mantissa and the exponent are "inverted" by mapping `0-9` to the characters `j-a` (or any sequence of 10 characters in descending order), which is the key to preserve the lexicographical order for negative numbers. This approach ensures that the corresponding encoded string is decodable.

The encoding represents numbers in a format similar to scientific notation, where the decimal point is positioned after the first digit of the mantissa (similar to IEEE 754). For example, 31.4 is encoded as `0e001x314` (3.14&times;10<sup>1</sup>). See more examples below:

| Input    | Encoded version<br>(3 significant figures) | Sign of the number (`-`) or padding (`0`) | Exponent sign (`-+`) or padding (`0`) | Exponent encoded<br>(decoded) | Mantissa encoded<br>(decoded) |
| -------- | ------------------------------------------ | ----------------------------------------- | ------------------------------------- | ----------------------------- | ----------------------------- |
| -10.0    | `-e+jixijj`                                | `-`                                       | `+`                                   | `ji`<br>(01)                  | `ijj`<br>(1.00)               |
| -0.31622 | `-e-01xgid`                                | `-`                                       | `-`                                   | `01`<br>(01)                  | `gid`<br>(3.16)               |
| 0        | `000000000`                                |
| 0.31622  | `0e-jix316`                                | `0`                                       | `-`                                   | `ji`<br>(01)                  | `316`<br>(3.16)               |
| 10.0     | `0e001x100`                                | `0`                                       | `0`                                   | `01`<br>(01)                  | `100`<br>(1.00)               |

Notice that `+` cannot be used as the sign of the number because `+` precedes `-`. However, for that exact same reason, it can be used as a padding when the number is negative, but the exponent is positive. `0` was chosen as a padding character in place of `+` because it simply looks as the obvious choice.

And of course you could drop the `e` and `x`, but then the output would be less readable.

## Install

```sh
pip install git+https://github.com/arthursn/sortable-float
```

## Examples

```python
from sortable_float import encode_float_sortable, decode_float_sortable

# Encode a float to a sortable string representation
encoded = encode_float_sortable(3.1415, precision=4)
print(encoded)  # '0e000x3142'

# Decode back to float
decoded = decode_float_sortable(encoded)
print(decoded)  # 3.142
```

More examples can be found in the [examples](examples) folder.
