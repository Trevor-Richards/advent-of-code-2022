import string

input_file = open("input.txt")
file_contents = input_file.read()
contents_split = file_contents.splitlines()

input_file.close()

def get_priority(str):
    priority = string.ascii_lowercase.index(str.lower()) + 1
    if str.isupper():
        priority += 26
    return priority

# Part 1
sum = 0
for str in contents_split:
    compartment_1 = str[0:len(str)/2]
    compartment_2 = str[len(str)/2:len(str)]
    common_item = list(set(compartment_1).intersection(compartment_2))[0]
    priority = get_priority(common_item)
    sum += priority

print(sum)

# Part 2
sum = 0
for i in range(0,len(contents_split),3):
    rucksack_1 = contents_split[i]
    rucksack_2 = contents_split[i + 1]
    rucksack_3 = contents_split[i + 2]
    badge = list(set(rucksack_1).intersection(rucksack_2, rucksack_3))[0]
    priority = get_priority(badge)
    sum += priority

print(sum)