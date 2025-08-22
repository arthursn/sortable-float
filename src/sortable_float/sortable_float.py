def _inv(numstr: str) -> str:
    return "".join(chr(154 - ord(s)) for s in numstr)


def encode_float_sortable(number: float, precision: int = 3) -> str:
    """
    Encodes a floating-point number into a string format that maintains sort order.

    This function converts a float to a string representation where lexicographical
    sorting of the strings corresponds to numerical sorting of the original values.

    Args:
        number: The floating-point number to encode
        precision: The number of significant digits to preserve (default: 3)

    Returns:
        A string representation that can be lexicographically sorted

    Example:
        >>> encode_float_sortable(1.2345)
        '0e-jhx123'
    """
    assert precision > 0, "precision must be > 0"
    # raw
    rman, rexp = f"{number:.{precision - 1}e}".split("e")
    # is positive (number/exponent), encoded (mantissa/exponent)
    ispn, eman = rman[0] != "-", rman.replace("-", "").replace(".", "")
    ispe, eexp = rexp[0] != "-", rexp.replace("-", "").replace("+", "")
    # zero is special
    if set(eman) == {"0"}:
        return "0" * (precision + 6)
    # encode matissa for positive number
    if not ispn:
        eman = _inv(eman)
    # encode exponent for sign(number) xor sign(exponent)
    if ispn != ispe:
        eexp = _inv(eexp)
    # signs
    sign = "-0"[ispn]
    sexp = "+--0"[(ispe == ispn) + (ispn << 1)]
    return f"{sign}e{sexp}{eexp}x{eman}"


def decode_float_sortable(encoded_number: str) -> float:
    """
    Decodes a string created by encode_float_sortable back to a floating-point number.

    This function reverses the encoding process performed by encode_float_sortable,
    converting the specially formatted string back to its original float value.

    Args:
        encoded_number: The string representation created by encode_float_sortable

    Returns:
        The original floating-point number

    Example:
        >>> decode_float_sortable('0e-jhx123')
        1.23
    """
    if set(encoded_number) == {"0"}:
        return 0.0
    sign = encoded_number[0]
    sexp = encoded_number[2]
    exp = encoded_number[3:5]
    man = encoded_number[6:]
    if ord(exp[0]) >= 97:
        exp = _inv(exp)
    if ord(man[0]) >= 97:
        man = _inv(man)
    man = f"{man[0]}.{man[1:]}"
    return float(f"{sign}{man}e{sexp}{exp}")
