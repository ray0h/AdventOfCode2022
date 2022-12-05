# --- Day 5: Supply Stacks ---
# The expedition can depart as soon as the final supplies have been unloaded from the ships. 
# Supplies are stored in stacks of marked crates, but because the needed supplies are buried under many other crates, the crates need to be rearranged.

# The ship has a giant cargo crane capable of moving crates between stacks. 
# To ensure none of the crates get crushed or fall over, the crane operator will rearrange them in a series of carefully-planned steps. 
# After the crates are rearranged, the desired crates will be at the top of each stack.

# The Elves don't want to interrupt the crane operator during this delicate procedure, 
# but they forgot to ask her which crate will end up where, and they want to be ready to unload them as soon as possible so they can embark.

# They do, however, have a drawing of the starting stacks of crates and the rearrangement procedure (your puzzle input). For example:

#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 

# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2
# In this example, there are three stacks of crates. Stack 1 contains two crates: crate Z is on the bottom, and crate N is on top. 
# Stack 2 contains three crates; from bottom to top, they are crates M, C, and D. Finally, stack 3 contains a single crate, P.

# Then, the rearrangement procedure is given. In each step of the procedure, a quantity of crates is moved from one stack to a different stack. 
# In the first step of the above rearrangement procedure, one crate is moved from stack 2 to stack 1, resulting in this configuration:

# [D]        
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 
# In the second step, three crates are moved from stack 1 to stack 3. Crates are moved one at a time, 
# so the first crate to be moved (D) ends up below the second and third crates:

#         [Z]
#         [N]
#     [C] [D]
#     [M] [P]
#  1   2   3
# Then, both crates are moved from stack 2 to stack 1. Again, because crates are moved one at a time, crate C ends up below crate M:

#         [Z]
#         [N]
# [M]     [D]
# [C]     [P]
#  1   2   3
# Finally, one crate is moved from stack 1 to stack 2:

#         [Z]
#         [N]
#         [D]
# [C] [M] [P]
#  1   2   3
# The Elves just need to know which crate will end up on top of each stack; in this example, the top crates are C in stack 1, M in stack 2, 
# and Z in stack 3, so you should combine these together and give the Elves the message CMZ.

# After the rearrangement procedure completes, what crate ends up on top of each stack?

from typing import List
import re

# parse data
file = open("/Users/raymondoh/Documents/AdventOfCode2022/data/day5.txt", "r").readlines()

# create hash table with first data chunk
DIGITS_REGEX = "\d+"
CHAR_REGEX = "[A-Z]"
FILE_SPOT_LINE = 9
FILE_MOVES_START_LINE = 11

table_length = int(max(re.findall(DIGITS_REGEX, file[FILE_SPOT_LINE - 1])))
spots = range(1, table_length + 1)
crates_hash = {val: [] for val in spots}

def add_crates(line: str, crates_hash: dict):
    newline = '\n'
    split_line = line.split(' ')

    space_count = 0
    current_key = 1
    for el in split_line:
        if el == newline:
            return crates_hash
        elif el == '':
            if space_count == 3:
                current_key += 1
                space_count = 0
            else:
                space_count += 1
        else:  # is a crate string
            crate = re.search(CHAR_REGEX, el).group()
            crates_hash[current_key].insert(0, crate)
            if newline in el:
                return crates_hash
            current_key += 1

for ind in range(0, FILE_SPOT_LINE - 1):
    crates_hash = add_crates(file[ind], crates_hash)

# print(f"{crates_hash = }")

# create steps list with second data chunk
moves_list = file[(FILE_SPOT_LINE + 1):]
moves_list = [re.findall(DIGITS_REGEX, el) for el in moves_list]

# define function to parse steps
def move_crates_step(moves: List[str], crates_hash: dict):
    no_crates = int(moves[0])
    start = int(moves[1])
    end = int(moves[2])
    for _i in range(no_crates):
        crate = crates_hash[start].pop()
        crates_hash[end].append(crate)
    return crates_hash

# create iterator to run each step
for move in moves_list:
    crates_hash = move_crates_step(move, crates_hash)

# parse top crates
def top_crates(crates_hash):
    return ''.join([crates_hash[ind][-1] for ind in list(crates_hash.keys())])

print(f"{top_crates(crates_hash) = }")

# --- Part Two ---
# As you watch the crane operator expertly rearrange the crates, you notice the process isn't following your prediction.

# Some mud was covering the writing on the side of the crane, and you quickly wipe it away. 
# The crane isn't a CrateMover 9000 - it's a CrateMover 9001.

# The CrateMover 9001 is notable for many new and exciting features: air conditioning, leather seats, an extra cup holder, 
# and the ability to pick up and move multiple crates at once.

# Again considering the example above, the crates begin in the same configuration:

#     [D]    
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 
# Moving a single crate from stack 2 to stack 1 behaves the same as before:

# [D]        
# [N] [C]    
# [Z] [M] [P]
#  1   2   3 
# However, the action of moving three crates from stack 1 to stack 3 means that those three moved crates stay in the same order, 
# resulting in this new configuration:

#         [D]
#         [N]
#     [C] [Z]
#     [M] [P]
#  1   2   3
# Next, as both crates are moved from stack 2 to stack 1, they retain their order as well:

#         [D]
#         [N]
# [C]     [Z]
# [M]     [P]
#  1   2   3
# Finally, a single crate is still moved from stack 1 to stack 2, but now it's crate C that gets moved:

#         [D]
#         [N]
#         [Z]
# [M] [C] [P]
#  1   2   3
# In this example, the CrateMover 9001 has put the crates in a totally different order: MCD.

# Before the rearrangement process finishes, update your simulation so that the Elves know where they should stand to be 
# ready to unload the final supplies. After the rearrangement procedure completes, what crate ends up on top of each stack?

# define function to parse steps
def move_9001_crates_step(moves: List[str], crates_hash: dict):
    no_crates = int(moves[0])
    start = int(moves[1])
    end = int(moves[2])
    for ind in range(no_crates, 0, -1):
        crate = crates_hash[start][-ind]
        crates_hash[end].append(crate)
    crates_hash[start] = crates_hash[start][:-no_crates]
    return crates_hash

crates_hash_pt_two = {val: [] for val in spots}
for ind in range(0, FILE_SPOT_LINE - 1):
    crates_hash_pt_two = add_crates(file[ind], crates_hash_pt_two)

for move in moves_list:
    crates_hash_pt_two = move_9001_crates_step(move, crates_hash_pt_two)

print(f"{top_crates(crates_hash_pt_two) = }")