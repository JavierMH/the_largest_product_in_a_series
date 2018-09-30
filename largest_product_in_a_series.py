#!/usr/bin/env python

import sys


class LargestProductInASeries():
    def _constraints_for_N(self, N, N_length, K):
        if N_length != len(N):
            raise ValueError(
                '\nThe number of digits must be iqual to {}\n'
                .format(N_length)
            )
        if K > N_length:
            raise ValueError('\nN must be greater than or equal to K\n')

    def _constraints_for_N_length_and_k(self, N_length_and_K):
        try:
            N_length, K = list(map(
                int,
                N_length_and_K.split()
            ))
        except ValueError:
            raise ValueError(
                '\nEntry Error: Arguments are spected in the form '
                '"int_1 int_2"\n'
            )
        if K > N_length:
            raise ValueError(
                '\nEntry Error: N must be greater than or equal to K \n'
            )

    def _constraints_for_K(self, K):
        if K > 7:
            raise ValueError('\nN must be lower than 7\n')
        if K < 1:
            raise ValueError('\nN must be greater than 1\n')

    def find_the_largest_product(self, N_length, K, N):
        self._constraints_for_N(N, N_length, K)
        self._constraints_for_K(K)
        largestProduct = 0
        for consec_digit in range(len(N) - K):
            product = 1
            for digit_position in range(consec_digit, consec_digit + K):
                product *= int(N[digit_position: digit_position + 1])
            if product > largestProduct:
                largestProduct = product

        print(largestProduct)
        return largestProduct

    def _obtain_k_N_and_N_length_by_input(self):
        while True:
            N_length_and_K = input(
                'Enter "N_length" & "K" '
                'separated by space "N_length K"\n>>>> '
            )
            if N_length_and_K == 'exit':
                sys.exit()
            try:
                self._constraints_for_N_length_and_k(N_length_and_K)
            except ValueError as ve:
                print(ve)
                continue
            while True:
                N_length, K = list(map(
                    int,
                    N_length_and_K.split()
                ))
                N = input('Enter N digit integer"\n>>>> ')
                if N == 'exit':
                    sys.exit()
                try:
                    self._constraints_for_N(N, N_length, K)
                except ValueError as ve:
                    print(ve)
                    continue
            return N_length, K, N

    def _constraints_for_number_of_test_cases(self, number_of_test_cases):
        if isinstance(number_of_test_cases, str):
            if not number_of_test_cases.isdigit():
                raise ValueError('Please enter an integer number!')
            number_of_test_cases = int(number_of_test_cases)
        if number_of_test_cases < 1 or number_of_test_cases > 100:
            raise ValueError(
                'Please enter an integer number between 1 and 100'
            )

    def _obtain_T_by_input(self):
        while True:
            print('\nPress "ctrl + C" or type "exit" to exit')
            number_of_test_cases = input('Enter T\n>>>> ')
            if number_of_test_cases == 'exit':
                sys.exit()
            try:
                self._constraints_for_number_of_test_cases(
                    number_of_test_cases
                )
                number_of_test_cases = int(number_of_test_cases)
            except ValueError as ve:
                print(ve)
                continue
            return number_of_test_cases

    def run(self):
        number_of_test_cases = self._obtain_T_by_input()
        the_largest_product_list = []
        exit = False
        while exit is not True:
            the_largest_product_list.append(
                self.find_the_largest_product(
                    *self._obtain_k_N_and_N_length_by_input()
                )
            )
            number_of_test_cases -= 1
            if not number_of_test_cases:
                exit = True
        return the_largest_product_list


if __name__ == '__main__':
    result = LargestProductInASeries().run()
