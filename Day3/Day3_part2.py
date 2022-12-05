rucksack_sum = 0
while len(rucksacks) > 0:
    # take out first 3 entries
    first_rucksack = set(rucksacks.pop())
    second_rucksack = set(rucksacks.pop())
    third_rucksack = set(rucksacks.pop())
    # get overlap through set logic (intersection of two sets applied twice)
    overlap_char = ((first_rucksack.intersection(second_rucksack)).intersection(third_rucksack)).pop()

    # translate to ascii and substract the base ('A' is 65, 'B' is 66 and so on) and add the new base
    if overlap_char.isupper():
        rucksack_sum += ord(overlap_char) - ord('A') + 27
    else:
        rucksack_sum += ord(overlap_char) - ord('a') + 1
print(rucksack_sum)