import numpy as np

nums = np.array([10,6,8,13,14,4,2,7])
Filter = []

for element in nums:
  if element > 5:
    Filter.append(True)
  else:
    Filter.append(False)
    
filtered = nums[Filter]
print(np.sort(filtered))
