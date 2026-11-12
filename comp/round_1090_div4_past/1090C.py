"""FAILED ON TIME"""

import sys
input = sys.stdin.readline

cases = int(input())

def main():
    n = int(input())
    perm = []
    
    low = 1
    high = 3*n
    
    for _ in range(n):
        perm.append(low)
        perm.append(high)
        perm.append(high-1)
        low += 1
        high -= 2
    
    print(*perm)

if __name__ == "__main__":
    for _ in range(cases):
        main()