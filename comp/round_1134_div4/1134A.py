import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):

    nums = list(map(int, input().split()))

    if (nums[-1] - nums[0] == 2) & (nums[0]<nums[1]<nums[2]):
        print("YES")
    else:
        print("NO") 