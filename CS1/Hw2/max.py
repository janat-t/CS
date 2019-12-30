nums = list(map(int, input("Input Numbers : ").split()))

max_idx = 0

for i in range(len(nums)):
	if nums[i] > nums[max_idx]:
		max_idx = i

print("max_value =", nums[max_idx])
print("max_index =", max_idx)