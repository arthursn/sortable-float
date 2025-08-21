"""
Basic example
"""

from sortable_float import decode_float_sortable, encode_float_sortable

if __name__ == "__main__":
    # Encode a float to a sortable string representation
    encoded = encode_float_sortable(3.1415, precision=4)
    print(encoded)  # '0e-jgx3142'

    # Decode back to float
    decoded = decode_float_sortable(encoded)
    print(decoded)  # 3.142
