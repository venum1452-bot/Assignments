def multiply_nums(nums_str):
    nums = [int(num) for num in nums_str.split(", ")]
    result = 1
    for num in nums:
        result *= num
        return result
