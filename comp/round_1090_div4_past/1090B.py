
import sys
input = sys.stdin.readline

t = int(input())

def main():
    a = list(map(int, input().split()))
    pos = max(a)
    a.remove(pos)
    max_sum = pos - sum(a)
    print(max_sum)

if __name__ == "__main__":
    for _ in range(t):
        main()