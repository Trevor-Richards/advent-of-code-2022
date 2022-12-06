input_file = open("input.txt")
file_contents = input_file.read()
contents_split = file_contents.splitlines()

input_file.close()

def find_nth(word, phrase, n):
    start = word.find(phrase)
    while start >= 0 and n > 1:
        start = word.find(phrase, start+len(phrase))
        n -= 1
    return start

def generate_box_map(crates):
    box_map = {}
    for boxes in crates:
        for box in range(0, boxes.count('[')):
            index = find_nth(boxes, "[", box + 1)
            box = boxes[index + 1]
            box_column = (index / 4) + 1
            if box_column not in box_map:
                box_map[box_column] = [box]
            else:
                box_map[box_column].extend(box)
    return box_map

index = [idx for idx, s in enumerate(contents_split) if 'move' in s][0]
crates = contents_split[0 : index - 2]
instructions = contents_split[index : len(contents_split)]

# Part 1
answer = ''
box_map = generate_box_map(crates)

for instruction in instructions:
    number_of_boxes_to_move = int(instruction.split()[1])
    origin_column = int(instruction.split()[3])
    destination_column = int(instruction.split()[5])
    for _ in range(0, number_of_boxes_to_move):
        box_to_move = box_map.get(origin_column)[0 : 1]
        box_map[destination_column][:0] = box_to_move
        box_map[origin_column] = box_map.get(origin_column)[1:]

for key in box_map:
    letter = box_map.get(key)[0]
    answer += letter

print(answer)

# Part 2
answer = ''
box_map = generate_box_map(crates)

for instruction in instructions:
    number_of_boxes_to_move = int(instruction.split()[1])
    origin_column = int(instruction.split()[3])
    destination_column = int(instruction.split()[5])
    box_to_move = box_map.get(origin_column)[0 : number_of_boxes_to_move]
    box_map[destination_column][:0] = box_to_move
    box_map[origin_column] = box_map.get(origin_column)[number_of_boxes_to_move:]
    
for key in box_map:
    letter = box_map.get(key)[0]
    answer += letter

print(answer)