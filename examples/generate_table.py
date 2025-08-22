"""
Generate a markdown table of sortable float examples
"""

import argparse
import sys
from collections import namedtuple

from sortable_float.sortable_float import _inv, encode_float_sortable

DecodedFloat = namedtuple(
    "DecodedFloat",
    [
        # signs
        "sign",
        "sexp",
        # encoded
        "eexp",
        "eman",
        # decoded
        "dexp",
        "dman",
    ],
)


def decode_float_sortable_to_tuple(encoded_number: str) -> DecodedFloat:
    if set(encoded_number) == {"0"}:
        return DecodedFloat("", "", "", "", "", "")
    sign = encoded_number[0]
    sexp = encoded_number[2]
    eexp = dexp = encoded_number[3:5]
    eman = dman = encoded_number[6:]
    if ord(dexp[0]) >= 97:
        dexp = _inv(dexp)
    if ord(dman[0]) >= 97:
        dman = _inv(dman)
    dman = f"{dman[0]}.{dman[1:]}"
    return DecodedFloat(sign, sexp, eexp, eman, dexp, dman)


def generate_example_table(numbers, precision: int = 3, sort: bool = False) -> str:
    """
    Generate a markdown table showing how each number is encoded.
    """
    table = f"| Input | Encoded version<br>({precision} significant figures) | Sign of the number (`-`) or padding (`0`) | Exponent sign (`-+`) or padding (`0`) | Exponent encoded<br>(decoded) | Mantissa encoded<br>(decoded) |\n"
    table += "| --- | --- | --- | --- | --- | --- |\n"

    num_pairs = [
        (
            encode_float_sortable(num, precision=precision),
            num,
        )
        for num in numbers
    ]

    if sort:
        num_pairs = sorted(num_pairs)

    for encoded, num in num_pairs:
        (sign, sexp, eexp, eman, dexp, dman) = decode_float_sortable_to_tuple(encoded)

        table += "| "
        table += f"{num} |"
        table += f"`{encoded}` | "
        table += f"`{sign}` | " if sign else ""
        table += f"`{sexp}` | " if sexp else ""
        table += f"`{eexp}`<br>({dexp}) | " if eexp else ""
        table += f"`{eman}`<br>({dman}) |" if eman else ""
        table += "\n"

    return table


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-p",
        "--precision",
        type=int,
        default=3,
        help="Number of significant digits to use in encoding (default: 3)",
    )
    parser.add_argument(
        "-s",
        "--sort",
        action="store_true",
        help="Sort input numbers by encoded representation",
    )
    parser.add_argument(
        "-r",
        "--rich",
        action="store_true",
        help="Output formatted text using rich",
    )
    parser.add_argument(
        "numbers",
        nargs="*",
        type=float,
        default=[-10.0, -0.31622, 0, 0.31622, 10.0],
        help="List of numbers to encode (default: [-10.0, -0.31622, 0, 0.31622, 10.0])",
    )
    args = parser.parse_args()

    markdown_table = generate_example_table(
        args.numbers,
        precision=args.precision,
        sort=args.sort,
    )

    if args.rich:
        try:
            from rich import print
            from rich.markdown import Markdown

            markdown_table = Markdown(markdown_table)
        except ImportError:
            sys.stderr.write(
                "Warning: rich package not installed. Install it with `pip install rich`\n"
                "Falling back to raw markdown output.\n",
            )
    print(markdown_table)
