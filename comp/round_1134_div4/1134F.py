import sys
input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    heights = list(map(int, input().split()))
    heights.append(heights[0])
    
    steepness = [abs(heights[i]-heights[i+1]) for i in range(len(heights)-1)]
    
    if sum(slope for slope in steepness) < k:
        print(0)
        continue
    
    for _ in range(k):
        
        max_index = steepness.index(max(steepness))
        if heights[max_index] < heights[max_index+1]:
            heights[max_index] += 1
        else:
            heights[max_index+1] += 1
        steepness = [abs(heights[i]-heights[i+1]) for i in range(len(heights)-1)]
        
    print(max(steepness))