nums = [int(x) for x in input()]
print([(nums[x] + nums[x + 1]) / 2 for x in range(len(nums) - 1)])