new_dict = {}
for num in range(1, 51):
    if num % 2 == 0 and num % 7 == 0:  # if the number is divisible by 2 and 7 the value should be the key multiplied by 2
        new_dict[num] = num * 2
    elif num % 2 == 0:  # if the number is divisible by 2 the value should be one more than the key
        new_dict[num] = num + 1
    elif num % 7 == 0:  # if the number is divisible by 7 the value should be one less than the key
        new_dict[num] = num - 1
    else:  # otherwise the value should be the same number as the key
        new_dict[num] = num

print(new_dict)
