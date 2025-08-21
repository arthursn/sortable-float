import unittest

from sortable_float import decode_float_sortable, encode_float_sortable


class TestSortableFloat(unittest.TestCase):
    test_values_base = [
        0,
        1e-10,
        -1e-10,
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
        -1e5,
    ]
    test_values_precision = [
        1.234,
        1.2345,
        1.23456,
    ]

    def test_encode_float_sortable(self):
        sorted_values = sorted(self.test_values_base)
        sortable_strings = [encode_float_sortable(v) for v in self.test_values_base]
        sorted_strings = sorted(sortable_strings)
        self.assertEqual(
            [encode_float_sortable(v) for v in sorted_values], sorted_strings
        )

    def test_encode_float_sortable_precision(self):
        sorted_values = sorted(self.test_values_precision)
        sortable_strings = [
            encode_float_sortable(v, 6) for v in self.test_values_precision
        ]
        sorted_strings = sorted(sortable_strings)
        self.assertEqual(
            [encode_float_sortable(v, 6) for v in sorted_values], sorted_strings
        )

    def test_encode_float_sortable_length(self):
        precision = 5
        values = self.test_values_base + self.test_values_precision
        sortable_strings = [encode_float_sortable(v, precision) for v in values]
        expected_length = precision + 6
        for s in sortable_strings:
            self.assertEqual(
                len(s),
                expected_length,
                f"String '{s}' length is {len(s)}, expected {expected_length}",
            )

    def test_decode_float_sortable(self):
        precision = 2
        values = self.test_values_base + self.test_values_precision
        sortable_strings = [encode_float_sortable(v, precision) for v in values]
        decoded_values = [decode_float_sortable(s) for s in sortable_strings]
        rounded_values = [float(f"{v:.{precision - 1}e}") for v in values]
        self.assertEqual(decoded_values, rounded_values)


if __name__ == "__main__":
    unittest.main()
