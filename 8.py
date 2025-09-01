def pyramid(nums):
    print(nums)
    if len(nums) == 1:
        return nums[0]
    else:
        next_row = []
        for i in range(len(nums) - 1):
            next_row.append(nums[i] + nums[i + 1])
        pyramid(next_row)

pyramid([3, 2])