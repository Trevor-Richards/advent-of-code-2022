input_file = open("input.txt")
file_contents = input_file.read()
contents_split = file_contents.splitlines()

input_file.close()

# Part 1
sum_array = []
sum = 0
for num in contents_split:
    if num == '':
        sum_array.append(sum)
        sum = 0
    else:
        sum += int(num)
sum_array.sort()
print(sum_array[-1])

# Part 2
print(sum_array[-1] + sum_array[-2] + sum_array[-3])