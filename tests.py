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
        T_isnt_a_digit_value = "50a"
        T_more_than_permited = 101
        T_less_than_permited = 0
        T_in_a_correct_range = 50

        with self.assertRaises(ValueError):
            LargestProductInASeries()._constraints_for_number_of_test_cases(
                T_isnt_a_digit_value
            )
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

    def test_constraints_for_N(self):
        N_correct_value = '1234567890'
        N_length_correct_value = 10
        K_correct_value = 5

        N_less_than_permited = '1234'
        with self.assertRaises(ValueError):
            LargestProductInASeries()._constraints_for_N(
                N_less_than_permited,
                N_length_correct_value,
                K_correct_value
            )

        N_length_less_than_N = 9
        with self.assertRaises(ValueError):
            LargestProductInASeries()._constraints_for_N(
                N_correct_value,
                N_length_less_than_N,
                K_correct_value
            )

        N_length_less_than_permited = 4
        with self.assertRaises(ValueError):
            LargestProductInASeries()._constraints_for_N(
                N_correct_value,
                N_length_less_than_permited,
                K_correct_value
            )

        self.assertIsNone(
            LargestProductInASeries()._constraints_for_N(
                N_correct_value,
                N_length_correct_value,
                K_correct_value
            ),
            None
        )

    def test_constraints_for_K(self):
        K_more_than_permited = 8
        K_less_than_permited = 0
        K_correct_value = 5

        with self.assertRaises(ValueError):
            LargestProductInASeries()._constraints_for_K(
                K_more_than_permited
            )

        with self.assertRaises(ValueError):
            LargestProductInASeries()._constraints_for_K(
                K_less_than_permited
            )

        self.assertIsNone(
            LargestProductInASeries()._constraints_for_K(
                K_correct_value
            ),
            None
        )


if __name__ == '__main__':
    unittest.main()
