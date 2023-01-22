# --- Day 16: Proboscidea Volcanium ---
# The sensors have led you to the origin of the distress signal: yet another handheld device, just like the one the Elves gave you. 
# However, you don't see any Elves around; instead, the device is surrounded by elephants! They must have gotten lost in these tunnels, 
# and one of the elephants apparently figured out how to turn on the distress signal.

# The ground rumbles again, much stronger this time. What kind of cave is this, exactly? You scan the cave with your handheld device; 
# it reports mostly igneous rock, some ash, pockets of pressurized gas, magma... this isn't just a cave, it's a volcano!

# You need to get the elephants out of here, quickly. Your device estimates that you have 30 minutes before the volcano erupts, 
# so you don't have time to go back out the way you came in.

# You scan the cave for other options and discover a network of pipes and pressure-release valves. You aren't sure how such a system got into a volcano, 
# but you don't have time to complain; your device produces a report (your puzzle input) of each valve's flow rate if it were opened
#  (in pressure per minute) and the tunnels you could use to move between the valves.

# There's even a valve in the room you and the elephants are currently standing in labeled AA. You estimate it will take you one minute to 
# open a single valve and one minute to follow any tunnel from one valve to another. What is the most pressure you could release?

# For example, suppose you had the following scan output:

# Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
# Valve BB has flow rate=13; tunnels lead to valves CC, AA
# Valve CC has flow rate=2; tunnels lead to valves DD, BB
# Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
# Valve EE has flow rate=3; tunnels lead to valves FF, DD
# Valve FF has flow rate=0; tunnels lead to valves EE, GG
# Valve GG has flow rate=0; tunnels lead to valves FF, HH
# Valve HH has flow rate=22; tunnel leads to valve GG
# Valve II has flow rate=0; tunnels lead to valves AA, JJ
# Valve JJ has flow rate=21; tunnel leads to valve II
# All of the valves begin closed. You start at valve AA, but it must be damaged or jammed or something: its flow rate is 0, 
# so there's no point in opening it. However, you could spend one minute moving to valve BB and another minute opening it; 
# doing so would release pressure during the remaining 28 minutes at a flow rate of 13, a total eventual pressure release of 28 * 13 = 364. 
# Then, you could spend your third minute moving to valve CC and your fourth minute opening it, providing an additional 26 minutes 
# of eventual pressure release at a flow rate of 2, or 52 total pressure released by valve CC.

# Making your way through the tunnels like this, you could probably open many or all of the valves by the time 30 minutes have elapsed. 
# However, you need to release as much pressure as possible, so you'll need to be methodical. Instead, consider this approach:

# == Minute 1 ==
# No valves are open.
# You move to valve DD.

# == Minute 2 ==
# No valves are open.
# You open valve DD.

# == Minute 3 ==
# Valve DD is open, releasing 20 pressure.
# You move to valve CC.

# == Minute 4 ==
# Valve DD is open, releasing 20 pressure.
# You move to valve BB.

# == Minute 5 ==
# Valve DD is open, releasing 20 pressure.
# You open valve BB.

# == Minute 6 ==
# Valves BB and DD are open, releasing 33 pressure.
# You move to valve AA.

# == Minute 7 ==
# Valves BB and DD are open, releasing 33 pressure.
# You move to valve II.

# == Minute 8 ==
# Valves BB and DD are open, releasing 33 pressure.
# You move to valve JJ.

# == Minute 9 ==
# Valves BB and DD are open, releasing 33 pressure.
# You open valve JJ.

# == Minute 10 ==
# Valves BB, DD, and JJ are open, releasing 54 pressure.
# You move to valve II.

# == Minute 11 ==
# Valves BB, DD, and JJ are open, releasing 54 pressure.
# You move to valve AA.

# == Minute 12 ==
# Valves BB, DD, and JJ are open, releasing 54 pressure.
# You move to valve DD.

# == Minute 13 ==
# Valves BB, DD, and JJ are open, releasing 54 pressure.
# You move to valve EE.

# == Minute 14 ==
# Valves BB, DD, and JJ are open, releasing 54 pressure.
# You move to valve FF.

# == Minute 15 ==
# Valves BB, DD, and JJ are open, releasing 54 pressure.
# You move to valve GG.

# == Minute 16 ==
# Valves BB, DD, and JJ are open, releasing 54 pressure.
# You move to valve HH.

# == Minute 17 ==
# Valves BB, DD, and JJ are open, releasing 54 pressure.
# You open valve HH.

# == Minute 18 ==
# Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
# You move to valve GG.

# == Minute 19 ==
# Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
# You move to valve FF.

# == Minute 20 ==
# Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
# You move to valve EE.

# == Minute 21 ==
# Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
# You open valve EE.

# == Minute 22 ==
# Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
# You move to valve DD.

# == Minute 23 ==
# Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
# You move to valve CC.

# == Minute 24 ==
# Valves BB, DD, EE, HH, and JJ are open, releasing 79 pressure.
# You open valve CC.

# == Minute 25 ==
# Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

# == Minute 26 ==
# Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

# == Minute 27 ==
# Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

# == Minute 28 ==
# Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

# == Minute 29 ==
# Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

# == Minute 30 ==
# Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.
# This approach lets you release the most pressure possible in 30 minutes with this valve layout, 1651.

# Work out the steps to release the most pressure in 30 minutes. What is the most pressure you can release?

# This is a queue problem.  
# Each value/tunnel is a key with values of:
# - flow rate
# - list of adjacent valves
# e.g.:
# {
#   'AA': {'flow rate': 0, 'adjacents': ['DD', 'II', 'BB']},
#   'BB': {'flow rate': 13, 'adjacents': ['CC', 'AA']},
#   'CC': {'flow rate': 2, 'adjacents': ['DD', 'BB']},
#   'DD': {'flow rate': 20, 'adjacents': ['CC', 'AA', 'EE']},
#   'EE': {'flow rate': 3, 'adjacents': ['FF', 'DD']},
#   'FF': {'flow rate': 0, 'adjacents': ['EE', 'GG']},
#   'GG': {'flow rate': 0, 'adjacents': ['FF', 'HH']},
#   'HH': {'flow rate': 22,'adjacents': ['GG']},
#   'II': {'flow rate': 0, 'adjacents': ['AA', 'JJ']},
#   'JJ': {'flow rate': 21,'adjacents': ['II']}
# }

# since you are timeboxed at 30 minutes, can set up a queue that takes a tuple of:
# - list of open valves
# - current flow rate
# - cummulative pressure
# - current valve
# - time left

# pop the current queue value and then break it down and calculate the next moves, simulating the time countdown and assessing if you've reached max presure release

testfile = "/Users/raymondoh/Documents/AdventOfCode2022/Day16/test.txt"
file = "/Users/raymondoh/Documents/AdventOfCode2022/data/day16.txt"
import re
import time


def parse_valves(filename):
    digitsregex = r"\d+"
    valveregex = r"[A-Z][A-Z]"
    valve_dict = {}

    f = open(filename, 'r').readlines()
    for line in f:
        flow_rate = re.search(digitsregex, line).group(0)
        valves = re.findall(valveregex, line)
        first = valves.pop(0)
        valve_dict[first] = {"flow_rate": int(flow_rate), "adjacents": valves}
    return valve_dict

def get_relevant_valves(valves):
    relevant_valves = []
    for valve in valves:
        if valves[valve]['flow_rate'] != 0:
            relevant_valves.append(valve)
    
    return relevant_valves

def get_relevant_valve_distances(valves):
    # start is always AA
    dist_dict = {}
    aa_dists = get_shortest_distances('AA', valves)
    relevant_valves = aa_dists.keys()
    dist_dict['AA'] = aa_dists
    for valve in relevant_valves:
        dist_dict[valve] = get_shortest_distances(valve, valves)

    return dist_dict


def get_shortest_distances(current_valve, valves):
    # tuple: (current valve, dict of relevant valves and their distance, distance traveled)
    visited = []
    distances = {}
    init_tuple = (current_valve, 0)
    queue = [init_tuple]

    while len(queue) > 0:
        current, traveled = queue.pop(0)

        if current in visited:
            next
        else:
            current_valve_flow_rate = valves[current]["flow_rate"]
            current_valve_adjacents = valves[current]["adjacents"]
            if current != current_valve and current_valve_flow_rate > 0:
                if current not in distances.keys():
                    distances[current] = traveled
                else:
                    if distances[current] > traveled:
                        distances[current] = traveled

            if current not in visited:
                visited.append(current)
            for neighbor in current_valve_adjacents:
                if neighbor not in visited:
                    queue.append((neighbor, traveled+1))

    return distances

def get_open_valve_mapping(init_tuple, dist_dict, relevant_valves):
    start = init_tuple[3]
    queue = [init_tuple]
    open_valve_mapping = {}

    while len(queue) > 0:
        current_valve, opened_valves, total_pressure_released, min_left = queue.pop(0)

        if min_left > 0:
            current_valve_flow_rate = valves[current_valve]['flow_rate']
            updated_open_valves = opened_valves.copy()
            # unique case where start has openable valve, consider moving to other locations first
            if current_valve == 'AA' and min_left == start:
                for next_valve in relevant_valves:
                    next_valve_dist = dist_dict[current_valve][next_valve]
                    elapsed_time = next_valve_dist if next_valve_dist < min_left else min_left
                    queue.append((next_valve, [], total_pressure_released, min_left - elapsed_time))

            if current_valve_flow_rate != 0:
                updated_open_valves.append(current_valve)
                min_left -= 1
                newly_released = current_valve_flow_rate * min_left
                total_pressure_released += newly_released
                
                key = frozenset(updated_open_valves)
                if key in open_valve_mapping.keys():
                    if open_valve_mapping[key] < total_pressure_released:
                        open_valve_mapping[key] = total_pressure_released
                else:
                    open_valve_mapping[key] = total_pressure_released

                remaining_valves = list(set(relevant_valves) - set(updated_open_valves))

                for next_valve in remaining_valves:
                    next_valve_dist = dist_dict[current_valve][next_valve]
                    if next_valve_dist < min_left:
                        queue.append((next_valve, updated_open_valves, total_pressure_released, min_left - next_valve_dist))
    
    return open_valve_mapping

import pprint

start = time.time()

valves = parse_valves(file)
dist_dict = get_relevant_valve_distances(valves)
relevant_valves = get_relevant_valves(valves)

# pprint.pp(valves)
# pprint.pp(relevant_valves)
# pprint.pp(dist_dict)

#  max pressure algorithm - worked out some of it myself, but alot of this leaned on reddit threads; especially around mapping the possible initial sets
#  relevant tuple: (current_valve, valves_open_list, total_pressure_released, min_left)

init_tuple = ('AA', [], 0, 30)
open_valve_mapping = get_open_valve_mapping(init_tuple, dist_dict, relevant_valves)
# pprint.pp(open_valve_mapping)

print(f"Part 1 - total pressure released: {max(open_valve_mapping.values())}")
end = time.time()
print("The time of execution of above program is :",
      (end-start), "s")

# --- Part Two ---
# You're worried that even with an optimal approach, the pressure released won't be enough. What if you got one of the elephants to help you?

# It would take you 4 minutes to teach an elephant how to open the right valves in the right order, leaving you with only 26 minutes to actually execute your plan. Would having two of you working together be better, even if it means having less time? (Assume that you teach the elephant before opening any valves yourself, giving you both the same full 26 minutes.)

# In the example above, you could teach the elephant to help you as follows:

# == Minute 1 ==
# No valves are open.
# You move to valve II.
# The elephant moves to valve DD.

# == Minute 2 ==
# No valves are open.
# You move to valve JJ.
# The elephant opens valve DD.

# == Minute 3 ==
# Valve DD is open, releasing 20 pressure.
# You open valve JJ.
# The elephant moves to valve EE.

# == Minute 4 ==
# Valves DD and JJ are open, releasing 41 pressure.
# You move to valve II.
# The elephant moves to valve FF.

# == Minute 5 ==
# Valves DD and JJ are open, releasing 41 pressure.
# You move to valve AA.
# The elephant moves to valve GG.

# == Minute 6 ==
# Valves DD and JJ are open, releasing 41 pressure.
# You move to valve BB.
# The elephant moves to valve HH.

# == Minute 7 ==
# Valves DD and JJ are open, releasing 41 pressure.
# You open valve BB.
# The elephant opens valve HH.

# == Minute 8 ==
# Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
# You move to valve CC.
# The elephant moves to valve GG.

# == Minute 9 ==
# Valves BB, DD, HH, and JJ are open, releasing 76 pressure.
# You open valve CC.
# The elephant moves to valve FF.

# == Minute 10 ==
# Valves BB, CC, DD, HH, and JJ are open, releasing 78 pressure.
# The elephant moves to valve EE.

# == Minute 11 ==
# Valves BB, CC, DD, HH, and JJ are open, releasing 78 pressure.
# The elephant opens valve EE.

# (At this point, all valves are open.)

# == Minute 12 ==
# Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

# ...

# == Minute 20 ==
# Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.

# ...

# == Minute 26 ==
# Valves BB, CC, DD, EE, HH, and JJ are open, releasing 81 pressure.
# With the elephant helping, after 26 minutes, the best you could do would release a total of 1707 pressure.

# With you and an elephant working together for 26 minutes, what is the most pressure you could release?

import itertools

start = time.time()

init_tuple = ('AA', [], 0, 26)
combo_open_valve_mapping = get_open_valve_mapping(init_tuple, dist_dict, relevant_valves)

combos = itertools.combinations(combo_open_valve_mapping, 2)
max_combo_pressure = 0
for combo in combos:
    me, elephant = combo
    if len(list(me & elephant)) == 0:
        possible_pressure = combo_open_valve_mapping[me] + combo_open_valve_mapping[elephant]

        if possible_pressure > max_combo_pressure:
            max_combo_pressure = possible_pressure

print(f"Part 2 - max combined pressure released: {max_combo_pressure}")

end = time.time()
print("The time of execution of above program is :",
      (end-start), "s")