def is_symmetrical(num):
    num_str = str(num)
    return num_str == num_str[::-1]
