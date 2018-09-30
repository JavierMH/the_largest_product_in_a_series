#!/usr/bin/env python


def find_the_largest_product(len_of_N, K, N):
    largestProduct = 0
    for consec_digit in range(len(N) - K):
        product = 1
        for digit_position in range(consec_digit, consec_digit + K):
            product *= int(N[digit_position: digit_position + 1])
        if product > largestProduct:
            largestProduct = product

    print(largestProduct)


find_the_largest_product(10, 5, '3675356291')
