# sortable-float: Alphabetically sortable float representation

This is a simple algorithm for encoding float numbers as alphabetically sortable strings. The resulting string is of fixed length (significant figures + 6).

It is inspired by IEEE 754 and by [koalamer/conust](https://github.com/koalamer/conust), which proposes an "inversion" of digits to handle the sorting of negative numbers. When needed, the digits of the mantissa and the exponent are "inverted" by mapping `0-9` to the characters `j-a` (or any sequence of 10 characters in descending order), which is the key to preserve the lexicographical order for negative numbers. This approach ensures that the corresponding encoded string is decodable. Also, positive numbers with positive exponents are still somewhat human readable. For example, 3140 is encoded as `0e001x314` (314&times;10<sup>1</sup>). See more examples below:

| Input     | Encoded version<br>(3 significant figures) | Sign of the number (`-`) or padding (`0`) | Exponent sign (`-+`) or padding (`0`) | Exponent encoded<br>(decoded) | Mantissa encoded<br>(decoded) |
| --------- | ------------------------------------------ | ----------------------------------------- | ------------------------------------- | ----------------------------- | ----------------------------- |
| -100000.0 | `-e+jgxijj`                                | `-`                                       | `+`                                   | `jg`<br>(03)                  | `ijj`<br>(100)                |
| -3.1622   | `-e-02xgid`                                | `-`                                       | `-`                                   | `02`<br>(02)                  | `gid`<br>(316)                |
| 0         | `000000000`                                |                                           |                                       |                               |                               |
| 3.1622    | `0e-jhx316`                                | `0`                                       | `-`                                   | `jh`<br>(02)                  | `316`<br>(316)                |
| 100000.0  | `0e003x100`                                | `0`                                       | `0`                                   | `03`<br>(03)                  | `100`<br>(100)                |

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
print(encoded)  # '0e-jgx3142'

# Decode back to float
decoded = decode_float_sortable(encoded)
print(decoded)  # 3.142
```

More examples can be found in the [examples](examples) folder.