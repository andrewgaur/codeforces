""" example
In the first test case, one operation with x=c
 turns abca into the palindrome abba.

In the second test case, you can perform operations with x=d
, x=c
, and x=b
: abdc →
 abcc →
 abbb →
 aaaa. The second operation changes both letters c, and the third operation changes all three letters b.

In the third test case, the string is already a palindrome.

In the fourth test case, you can perform operations with x=d
 and x=b
: cbad →
 cbac →
 caac.

In the fifth test case, the operations with x=z,y,…,b
 in this order turn zaza into aaaa.


"""


import sys
input = sys.stdin.readline

t = int(input())
alphabet = list("abcdefghijklmnopqrstuvwxyz")
alphabet_indices = {
    char: index for index, char in enumerate(alphabet)
}

def is_palindrome(string_i):
    return string_i == string_i[::-1]

for _ in range(t):
    n = int(input())
    string = list(input().strip())
    string_i = [alphabet_indices[char] for char in string]
    
    moves = 0
    while not is_palindrome(string_i):
        shift = -1
        # number of moves to make string a palindrome
        # move makes all characters of one letter equal to the letter before it in the alphabet
        
        for i in range(n // 2):
            
            left = string_i[i]
            right = string_i[n-1-i]
            
            if left != right:
                shift = max(shift, left, right)
        
        string_i = [letter-1 if letter == shift else letter for letter in string_i]
        moves += 1
        
                
    print(moves)
    
    
    