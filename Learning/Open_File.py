import random
def max_number(nums):
  max_num = nums[0]
  for num in nums:
    if num > max_num:
      max_num = num
  return max_num

def min_number(nums):
  min_num = nums[0]
  for num in nums:
    if num < min_num:
      min_num = num
  return min_num

arr = [random.randint(1, 100) for _ in range(10)]

print(arr)
print(max_number(arr))
print(min_number(arr))