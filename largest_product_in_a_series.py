#!/usr/bin/env python


class LargestProductInASeries():
    def find_the_largest_product(self, len_of_N, K, N):
        if len_of_N != len(N):
            raise ValueError(
                'The number of digits must be iqual to {}'.format(len_of_N)
            )

        if K > len_of_N:
            raise ValueError('N must be greater than or equal to K')

        largestProduct = 0
        for consec_digit in range(len(N) - K):
            product = 1
            for digit_position in range(consec_digit, consec_digit + K):
                product *= int(N[digit_position: digit_position + 1])
            if product > largestProduct:
                largestProduct = product

        print(largestProduct)
        return largestProduct

    def run(self):
        number_of_test_cases = int(input('Enter T\n>>>> '))
        if number_of_test_cases > 100 and number_of_test_cases < 1:
            raise ValueError()


if __name__ == '__main__':
    result = LargestProductInASeries().run()
