with open('input.txt', 'r') as f:
    lines = f.readlines()
    rucksacks = [entry.strip() for entry in lines]

rucksack_sum = 0
for rucksack in rucksacks:
    # split in half 
    first_half = set(rucksack[:len(rucksack)//2])
    second_half = set(rucksack[len(rucksack)//2:])
    # get overlap through set logic (intersection of two sets)
    overlap_char = (first_half.intersection(second_half)).pop()

    # translate to ascii and substract the base ('A' is 65, 'B' is 66 and so on) and add the new base
    if overlap_char.isupper():
        rucksack_sum += ord(overlap_char) - ord('A') + 27
    else:
        rucksack_sum += ord(overlap_char) - ord('a') + 1

print(rucksack_sum)