

"""
n piles of stones in a row
numbered 1 to n left to right
given integer k

game:
two players take turns, alice moves first.
one move, player takes non-empty pile of stones and removes one stone from it

Then one new stone is added to each pile j
 such that max(1,i−k)≤j≤i−1
, that is, to each of the min(k,i−1)
 piles immediately to the left of pile i
. If i=1
, no stones are added. The supply of new stones is unlimited. For example, if i=5
 and k=2
, one stone is added to each of piles 3
 and 4
.

The player who cannot make a move loses. It can be shown that the game always ends after a finite number of moves.

Determine the winner if both players play optimally.
"""

import sys
input = sys.stdin.readline

t = int(input())

def move(piles, k, pick_i):
    
    piles[pick_i] -= 1
    start = max(0, pick_i - k)
    
    for j in range(start, pick_i):
        piles[j] += 1
    
    return piles
    
    
    
for _ in range(t):
    n, k = map(int, input().split())
    
    piles = list(map(int, input().split()))
    
    parity = 0
    for i in range(0, n, k + 1):
        parity ^= piles[i] & 1

    print("Alice" if parity else "Bob")
    