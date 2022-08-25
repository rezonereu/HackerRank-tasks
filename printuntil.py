"""
The included code stub will read an integer 'n', from STDIN.

Without using any string methods, try to print the following: 123...n

Note that "..." represents the consecutive values in between.

Example
n=5
Print the string
12345

Input Format

The first line contains an integer n

Constraints
1 <= n <= 150
"""

if __name__ == '__main__':
    n = int(input())
    current_number = 1
    if n >= 1 and n <= 150:
        while current_number <= n:
            print(current_number, end = '')
            current_number += 1
