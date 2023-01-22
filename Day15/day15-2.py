# -- Day 15: Beacon Exclusion Zone ---
# You feel the ground rumble again as the distress signal leads you to a large network of subterranean tunnels. 
# You don't have time to search them all, but you don't need to: your pack contains a set of deployable sensors that you imagine 
# were originally built to locate lost Elves.

# The sensors aren't very powerful, but that's okay; your handheld device indicates that you're close enough to the source of 
# the distress signal to use them. You pull the emergency sensor system out of your pack, hit the big button on top, and the sensors 
# zoom off down the tunnels.

# Once a sensor finds a spot it thinks will give it a good reading, it attaches itself to a hard surface and begins monitoring 
# for the nearest signal source beacon. Sensors and beacons always exist at integer coordinates. 
# Each sensor knows its own position and can determine the position of a beacon precisely; 
# however, sensors can only lock on to the one beacon closest to the sensor as measured by the Manhattan distance. 
# (There is never a tie where two beacons are the same distance to a sensor.)

# It doesn't take long for the sensors to report back their positions and closest beacons (your puzzle input). For example:

# Sensor at x=2, y=18: closest beacon is at x=-2, y=15
# Sensor at x=9, y=16: closest beacon is at x=10, y=16
# Sensor at x=13, y=2: closest beacon is at x=15, y=3
# Sensor at x=12, y=14: closest beacon is at x=10, y=16
# Sensor at x=10, y=20: closest beacon is at x=10, y=16
# Sensor at x=14, y=17: closest beacon is at x=10, y=16
# Sensor at x=8, y=7: closest beacon is at x=2, y=10
# Sensor at x=2, y=0: closest beacon is at x=2, y=10
# Sensor at x=0, y=11: closest beacon is at x=2, y=10
# Sensor at x=20, y=14: closest beacon is at x=25, y=17
# Sensor at x=17, y=20: closest beacon is at x=21, y=22
# Sensor at x=16, y=7: closest beacon is at x=15, y=3
# Sensor at x=14, y=3: closest beacon is at x=15, y=3
# Sensor at x=20, y=1: closest beacon is at x=15, y=3
# So, consider the sensor at 2,18; the closest beacon to it is at -2,15. For the sensor at 9,16, the closest beacon to it is at 10,16.

# Drawing sensors as S and beacons as B, the above arrangement of sensors and beacons looks like this:

#                1    1    2    2
#      0    5    0    5    0    5
#  0 ....S.......................
#  1 ......................S.....
#  2 ...............S............
#  3 ................SB..........
#  4 ............................
#  5 ............................
#  6 ............................
#  7 ..........S.......S.........
#  8 ............................
#  9 ............................
# 10 ....B.......................
# 11 ..S.........................
# 12 ............................
# 13 ............................
# 14 ..............S.......S.....
# 15 B...........................
# 16 ...........SB...............
# 17 ................S..........B
# 18 ....S.......................
# 19 ............................
# 20 ............S......S........
# 21 ............................
# 22 .......................B....
# This isn't necessarily a comprehensive map of all beacons in the area, though. Because each sensor only identifies its closest beacon, 
# if a sensor detects a beacon, you know there are no other beacons that close or closer to that sensor. 
# There could still be beacons that just happen to not be the closest beacon to any sensor. Consider the sensor at 8,7:

#                1    1    2    2
#      0    5    0    5    0    5
# -2 ..........#.................
# -1 .........###................
#  0 ....S...#####...............
#  1 .......#######........S.....
#  2 ......#########S............
#  3 .....###########SB..........
#  4 ....#############...........
#  5 ...###############..........
#  6 ..#################.........
#  7 .#########S#######S#........
#  8 ..#################.........
#  9 ...###############..........
# 10 ....B############...........
# 11 ..S..###########............
# 12 ......#########.............
# 13 .......#######..............
# 14 ........#####.S.......S.....
# 15 B........###................
# 16 ..........#SB...............
# 17 ................S..........B
# 18 ....S.......................
# 19 ............................
# 20 ............S......S........
# 21 ............................
# 22 .......................B....

# This sensor's closest beacon is at 2,10, and so you know there are no beacons that close or closer (in any positions marked #).

# None of the detected beacons seem to be producing the distress signal, so you'll need to work out where the distress beacon 
# is by working out where it isn't. For now, keep things simple by counting the positions where a beacon cannot possibly be along just a single row.

# So, suppose you have an arrangement of beacons and sensors like in the example above and, just in the row where y=10, 
# you'd like to count the number of positions a beacon cannot possibly exist. 
# The coverage from all sensors near that row looks like this:

#                  1    1    2    2
#        0    5    0    5    0    5
#  9 ...#########################...
# 10 ..####B######################..
# 11 .###S#############.###########.
# In this example, in the row where y=10, there are 26 positions where a beacon cannot be present.

# Consult the report from the sensors you just deployed. In the row where y=2000000, how many positions cannot contain a beacon?

# readfile and parse sensor and beacon locations
# create a data structure that tracks sensor and closest beacon
# add manhattan distance to the structure/dict

# create grid based on min/max coordinates 
# mark with sensor and beacon locations

# for each sensor mark its range based on the closest beacons manhattan distance

import re
import time

def parse_coords(string):
    reg = "-?\d+"
    points = re.findall(reg, string)
    points = [int(el) for el in points]
    sensor = (points[0], points[1])
    beacon = (points[2], points[3])
    return sensor, beacon

def get_points(filename):
    f = open(filename, "r").readlines()

    sensor_list = []
    beacon_list = []
    for line in f:
        sensor, beacon = parse_coords(line.strip())
        sensor_list.append(sensor)
        beacon_list.append(beacon)

    return sensor_list, beacon_list

def get_manhattan(coords1, coords2):
    x1, y1 = coords1
    x2, y2 = coords2
    return abs(x1-x2) + abs(y1-y2)

def get_manhattan_list(sensor_list, beacon_list):
    md = []
    for ind in range(len(sensor_list)):
        sensor = sensor_list[ind]
        beacon = beacon_list[ind]
        manhattan_dist = get_manhattan(sensor, beacon)
        # md.append({'sensor': sensor, 'md': manhattan_dist})
        md.append([sensor, manhattan_dist])
    return md

def eval_row(row_no, manhattan_list):
    row_ranges = []
    for ml in manhattan_list:
        sensor, md = ml
        x,y = sensor
        row_dist = abs(row_no-y)
        if row_dist > md:
            continue
        row_range = [x-md+row_dist, x+md-row_dist+1]
        row_ranges.append(row_range)
    return row_ranges

def consolidate_range_list(range_list):
    range_list.sort()
    stack = []
    stack.append(range_list[0])
        
    for range in range_list[1:]:
        # Check for overlapping interval
        if stack[-1][0] <= range[0] <= stack[-1][-1]:
            stack[-1][-1] = max(stack[-1][-1], range[-1])
        else:
            stack.append(range)
    return stack

def eval_row_coverage(row_no, sensor_list, beacon_list, manhattan_list, minx, maxx):
    sensor_list = list(set(sensor_list))
    beacon_list = list(set(beacon_list))
    sensors_in_row = list(filter(lambda sens: sens[1] == row_no, sensor_list))
    beacons_in_row = list(filter(lambda beac: beac[1] == row_no, beacon_list))
    row_ranges = eval_row(row_no, manhattan_list)
    row_intervals = consolidate_range_list(row_ranges)
    count = 0
    for interval in row_intervals:
        x0 = minx if interval[0] <= minx else interval[0]
        x1 = maxx if interval[1] > maxx else interval[1]
        count += (x1 - x0)
    return count - len(beacons_in_row) - len(sensors_in_row)


testfile = "/Users/raymondoh/Documents/AdventOfCode2022/Day15/test.txt"
file = "/Users/raymondoh/Documents/AdventOfCode2022/data/day15.txt"

sensor_list, beacon_list = get_points(file)
# print(f"{maxx - minx = }")
# print(f"{sensor_list = }, {beacon_list = }")
ml = get_manhattan_list(sensor_list, beacon_list)
# print(f"{ml = }")

largest = 2000000
minx = -100000000
maxx = 100000000
start = time.time()
covered = eval_row_coverage(largest, sensor_list, beacon_list, ml, minx, maxx)
print(f"{covered = }")

end = time.time()
print("The time of execution of above program is :",
      (end-start), "s")


# --- Part Two ---
# Your handheld device indicates that the distress signal is coming from a beacon nearby. The distress beacon is not detected by any sensor, 
# but the distress beacon must have x and y coordinates each no lower than 0 and no larger than 4000000.

# To isolate the distress beacon's signal, you need to determine its tuning frequency, 
# which can be found by multiplying its x coordinate by 4000000 and then adding its y coordinate.

# In the example above, the search space is smaller: instead, the x and y coordinates can each be at most 20. 
# With this reduced search area, there is only a single position that could have a beacon: x=14, y=11. 
# The tuning frequency for this distress beacon is 56000011.

# Find the only possible position for the distress beacon. What is its tuning frequency?

def eval_row_coverage2(row_no, manhattan_list):
    row_ranges = eval_row(row_no, manhattan_list)
    row_intervals = consolidate_range_list(row_ranges)
    # count = 0
    # for interval in row_intervals:
    #     x0 = minx if interval[0] <= minx else interval[0]
    #     x1 = maxx if interval[1] > maxx else interval[1]
    #     count += (x1 - x0)
    if len(row_intervals) > 1:
        return row_intervals[0][1]
    else:
        return None

sensor_list, beacon_list = get_points(file)
# print(f"{maxx - minx = }")
# print(f"{sensor_list = }, {beacon_list = }")
ml = get_manhattan_list(sensor_list, beacon_list)
# print(f"{ml = }")


minx = 0
maxx = 4000000
start = time.time()
for y in range(maxx):
    covered = eval_row_coverage2(y, ml)
    if covered is not None:
        print(f"x = {covered}, {y = }")
        print(f"tuning freq: {4000000 * covered + y}")
        break

end = time.time()
print("The time of execution of above program is :",
      (end-start), "s")
