"""
Sorting example
"""

from sortable_float import decode_float_sortable, encode_float_sortable

if __name__ == "__main__":
    numbers = [
        1.23e-10,
        -1.2e-10,
        -1.3e-10,
        -1.23e-10,
        1e-5,
        -1e-5,
        0.1,
        0,
        -0.1,
        1,
        -1,
        10,
        -10,
        100,
        -100,
        1e5,
        -1.23456e-10,
        -1e5,
    ]

    precision = 3

    encoded_numbers = [encode_float_sortable(v, precision) for v in numbers]
    decoded_numbers = [decode_float_sortable(v) for v in encoded_numbers]

    print(f" Encoded{' ' * precision}   Original    Decoded")
    print("-" * (31 + precision))
    for num, enc_num, dec_num in sorted(
        zip(encoded_numbers, numbers, decoded_numbers),
        key=lambda v: v[1],
    ):
        print(
            f"{num} {enc_num:13g} {dec_num:10g}",
            end="  << loss of precision\n" if enc_num != dec_num else "\n",
        )
