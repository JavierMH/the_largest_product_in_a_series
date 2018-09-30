#!/usr/bin/env python


class LargestProductInASeries():
    def _constraints_for_N(self, N, N_length, K):
        if N_length != len(N):
            raise ValueError(
                'The number of digits must be iqual to {}'.format(N_length)
            )
        if K > N_length:
            raise ValueError('N must be greater than or equal to K')

    def _constraints_for_K(self, K):
        if K > 7:
            raise ValueError('N must be lower than 7')
        if K < 1:
            raise ValueError('N must be greater than 1')

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
        N_length, K = list(map(
            int,
            input(
                'Enter "N_length" & "K" '
                'separated by space "N_length K"\n>>>> '
            ).split()
        ))
        N = input('Enter N digit integer"\n>>>> ')
        return N_length, K, N

    def _constraints_for_number_of_test_cases(self, number_of_test_cases):
        if (isinstance(number_of_test_cases, str) and
                not number_of_test_cases.isdigit()):
            raise ValueError('Please enter an integer number!')
        if number_of_test_cases < 1 or number_of_test_cases > 100:
            raise ValueError(
                'Please enter an integer number between 1 and 100'
            )

    def _obtain_T_by_input(self):
        number_of_test_cases = input('Enter T\n>>>> ')
        self._constraints_for_number_of_test_cases(number_of_test_cases)
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
