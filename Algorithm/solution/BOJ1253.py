# 좋다
### 찰스 ###
import sys
from bisect import bisect_left


n = int(input())
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()

count = 0
for idx_i, result in enumerate(nums): # result : 합의 결과    
    for j in range(n):
        if idx_i == j : continue    # 자기 자신을 제외한 다른 두 수의 합이므로 자신(result) 제외
        target = result - nums[j]
        target_idx = bisect_left(nums,target)  
        
        # nums[j] + target = result 이고, nums[j], target, result 는 모두 다른 수

        if not(0 <= target_idx < n): continue   # target_idx 가 list 를 벗어나는 경우 제외 (out of index 방지)

        if target_idx == idx_i or target_idx == j:     # 같은 idx 인 경우
            if target_idx+1 >= n : continue
            if target_idx+1 == j or target_idx+1 == idx_i: continue 
            if (nums[target_idx+1] == target): target_idx += 1  # 중복되는 수가 있는경우, 무조건 오른쪽에 있을 것
            else : continue

        if nums[target_idx] == target:
            # print(f"{result} is a good number! {nums[j]}:{j}, {target}:{target_idx}")
            count += 1
            break

print(count)