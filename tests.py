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

    def test_obtain_T_by_input(self):
        T_more_than_permited = 101
        T_less_than_permited = 0
        T_in_a_correct_range = 50

        with self.assertRaises(ValueError):
            LargestProductInASeries()._constraints_for_number_of_test_cases(
                T_more_than_permited
            )
        with self.assertRaises(ValueError):
            LargestProductInASeries()._constraints_for_number_of_test_cases(
                T_less_than_permited
            )
        self.assertIsNone(
            LargestProductInASeries()._constraints_for_number_of_test_cases(
                T_in_a_correct_range
            ),
            None
        )


if __name__ == '__main__':
    unittest.main()
