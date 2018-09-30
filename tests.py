#!/usr/bin/env python

import unittest
from unittest.mock import patch
from largest_product_in_a_series import LargestProductInASeries


class ContainersTestCase(unittest.TestCase):
    def test_get_input_stacks_processed_input_correctly(self):
        user_input = [
            2,
            '10 5',
            '3675356291',
            '10 5',
            '2709360626',
        ]
        expected_stacks = [
            3150,
            0
        ]
        with patch('builtins.input', side_effect=user_input):
            stacks = LargestProductInASeries().run()
        self.assertEqual(stacks, expected_stacks)


if __name__ == '__main__':
    unittest.main()
