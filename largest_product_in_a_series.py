#!/usr/bin/env python


def find_the_largest_product(len_of_N, K, N):
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


find_the_largest_product(10, 5, '3675356291')
