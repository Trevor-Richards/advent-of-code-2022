input_file = open("input.txt")
file_contents = input_file.read()
contents_split = file_contents.splitlines()

input_file.close()

# Part 1
answer = 0
for sections in contents_split:
    first_elf_section = range(int(sections.split(',')[0].split('-')[0]), int(sections.split(',')[0].split('-')[1]) + 1)
    second_elf_section = range(int(sections.split(',')[1].split('-')[0]), int(sections.split(',')[1].split('-')[1]) + 1)

    if set(first_elf_section).issubset(second_elf_section) or set(second_elf_section).issubset(first_elf_section):
        answer += 1

print(answer)

# Part 2
answer = 0
for sections in contents_split:
    first_elf_section = range(int(sections.split(',')[0].split('-')[0]), int(sections.split(',')[0].split('-')[1]) + 1)
    second_elf_section = range(int(sections.split(',')[1].split('-')[0]), int(sections.split(',')[1].split('-')[1]) + 1)

    if any(i in first_elf_section for i in second_elf_section):
        answer += 1

print(answer)
