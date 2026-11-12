
"""
Codeforces Round 1090 Div 4, Problem A

Macaque given integer x. Need to:
choose integer y s.t. the value of min(x, y)* is maximized
if there are multiple value y, you can output any of them
* - min(x,y) is defined as the minimum of integers x and y.

Input:
each test contains multiple test cases. the first line contains the number
of test cases 1 <= t <= 6767.
each test case contains single integer -67 <= x <= 67.

output:
for each case, output one int -67 <= y <= 67 s.t. min(x,y) is maximized.
"""

import sys
input = sys.stdin.readline


t = int(input())

def main():
    for _ in range(t):
        x = int(input())
        print(x)

if __name__ == "__main__":
    main()