# the_largest_product_in_a_series

This project was made to obtain the longest product in a series.

**Author: *Javier Molina***

## Technologic Stack

* Python: [Python 3.5.2](https://www.python.org/downloads/release/python-356/)

## Description

Find the greatest product of K consecutive digits in the N digit number.

### Input Format

```text
First line contains T that denotes the number of test cases.
First line of each test case will contain two integers N & K.
Second line of each test case will contain a N digit integer.
```

### Constraints

```text
1 <= T <= 100
1 <= K <= 7
K <= N <= 1000
```

### Output Format

```text
Print the required answer for each test case.
```

### Sample Input 0

```text
2
10 5
3675356291
10 5
2709360626
```

### Sample Output 0

```text
3150
0
```

### Explanation

* For 3675356291 and selecting K = 5 consecutive digits, we have 36753, 67535, 75356, 53562, 35629 and 56291. Where 6 x 7 x 5 x 3 x 5 gives maximum product as 3150.

* For 2709360626, 0 lies in all selection of 5 consecutive digits hence maximum product remains 0.

## How to

To run the program just execute the next command in the shell:

```bash
python largest_product_in_a_series.py
```

To run the test just execute the next command in the shell:

```bash
python tests.py
```
