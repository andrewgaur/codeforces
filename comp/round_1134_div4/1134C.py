"""
There are n
 books, and the height of the i
-th book is hi
. You put all the books on a shelf in a row in any order you like.

A book is visible from the left if it is strictly taller than every book to its left. A book is visible from the right if it is strictly taller than every book to its right. In particular, the leftmost book is visible from the left, and the rightmost book is visible from the right.

Find the maximum possible number of books that are visible from at least one side, and any arrangement of the books with this number of visible books.

Input
Each test contains multiple test cases. The first line contains the number of test cases t
 (1≤t≤104
). The description of the test cases follows.

The first line of each test case contains a single integer n
 (1≤n≤2⋅105
) — the number of books.

The second line of each test case contains n
 integers h1,h2,…,hn
 (1≤hi≤109
) — the heights of the books.

It is guaranteed that the sum of n
 over all test cases does not exceed 2⋅105
.

Output
For each test case, print two lines.

In the first line, print a single integer k
 — the maximum possible number of books that are visible from at least one side.

In the second line, print n
 integers — the heights of the books from left to right in an arrangement in which exactly k
 books are visible from at least one side. These n
 integers must be the integers h1,h2,…,hn
 in some order.

If there are several such arrangements, print any of them.

Example
InputCopy
5
6
1 2 2 3 3 3
1
5
3
7 7 7
4
4 1 3 2
11
3 1 4 1 5 9 2 6 5 3 5
OutputCopy
5
2 3 3 3 2 1
1
5
2
7 7 7
4
3 4 2 1
10
1 3 4 5 9 5 6 5 3 2 1
Note
In the first test case, in the arrangement [2,3,3,3,2,1]
, the first book of height 2
 and the first book of height 3
 are visible from the left. The book of height 1
, the last book of height 2
, and the last book of height 3
 are visible from the right. In total, 5
 books are visible.

In the third test case, the leftmost book is visible from the left and the rightmost book is visible from the right, but the middle book is visible from neither side."""


import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    
    n = int(input())
    heights = list(map(int, input().split()))
    
    heights.sort()
    
    unique = []
    extras = []
    
    for height in heights:
        if not unique or height != unique[-1]:
            unique.append(height)
        else:
            extras.append(height)
            
    extras.reverse()
    
    right = len(unique)
    prev = None
    for height in extras:
        if height != prev:
            right += 1
            prev = height
            
    print(right)
    print(*unique, *extras)
    
    """
    visible = [False] * n
    
    #from left
    max_seen = None
    for book in range(n):
        if max_seen is None or heights[book] > max_seen:
            visible[book] = True
            max_seen = heights[book]
            
    #from right
    max_seen = None
    for book in range(n-1,-1,-1):
        if max_seen is None or heights[book] > max_seen:
            visible[book] = True
            max_seen = heights[book]
            
    print(sum(visible))
    visible_heights = [heights[i] for i in range(n) if visible[i]]
    print(*visible_heights)
    """