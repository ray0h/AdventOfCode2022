# --- Day 12: Hill Climbing Algorithm ---
# You try contacting the Elves using your handheld device, but the river you're following must be too low to get a decent signal.

# You ask the device for a heightmap of the surrounding area (your puzzle input). 
# The heightmap shows the local area from above broken into a grid; 
# the elevation of each square of the grid is given by a single lowercase letter, 
# where a is the lowest elevation, b is the next-lowest, and so on up to the highest elevation, z.

# Also included on the heightmap are marks for your current position (S) and the location that should get the best signal (E). 
# Your current position (S) has elevation a, and the location that should get the best signal (E) has elevation z.

# You'd like to reach E, but to save energy, you should do it in as few steps as possible. 
# During each step, you can move exactly one square up, down, left, or right. 
# To avoid needing to get out your climbing gear, the elevation of the destination square can be at most one higher
#  than the elevation of your current square; that is, if your current elevation is m, you could step to elevation n, but not to elevation o. 
# (This also means that the elevation of the destination square can be much lower than the elevation of your current square.)

# For example:

# Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi
# Here, you start in the top-left corner; your goal is near the middle. You could start by moving down or right, 
# but eventually you'll need to head toward the e at the bottom. From there, you can spiral around to the goal:

# v..v<<<<
# >v.vv<<^
# .>vv>E^^
# ..v>>>^^
# ..>>>>>^
# In the above diagram, the symbols indicate whether the path exits each square moving up (^), down (v), left (<), or right (>). 
# The location that should get the best signal is still E, and . marks unvisited squares.

# This path reaches the goal in 31 steps, the fewest possible.

# What is the fewest steps required to move from your current position to the location that should get the best signal?


# test_path = "/Users/raymondoh/Documents/AdventOfCode2022/Day12/"
# filename = "test.txt"

test_path = "/Users/raymondoh/Documents/AdventOfCode2022/data/"
filename = "day12.txt"

def make_map(filename: str, path: str):
    mapfile = open(path+filename, "r").readlines()
    start = [0,0]
    end = [0,0]
    grid = []
    for idx, line in enumerate(mapfile):
        row = list(line.rstrip())
        if 'S' in row:
            start = [idx, row.index('S')]
        if 'E' in row:
            end = [idx, row.index('E')]
        grid.append(row)
    
    return start, end, grid

def in_bounds(current_coord, grid):
    x, y = current_coord
    return x >= 0 and y >= 0 and x < len(grid) and y < len(grid[0])

def get_neighbors(current_coord, grid):
    x, y = current_coord
    neighbors = []
    moves = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    for move in moves:
        x_add, y_add = move
        neighbor = [x+x_add, y+y_add]
        if in_bounds(neighbor, grid):
            neighbors.append(neighbor)
    return neighbors

def is_passable(current_spot, next_spot):
    return ord(next_spot) - ord(current_spot) in list(range(-25, 2, 1))

# set up loop
start, end, grid = make_map(filename, test_path)

start_obj = {
    'coords': start,
    'path': [],
}
# create a list of visited spots to not backtrack
visited = []
shortest_path = len(grid) * len(grid[0]) + 1

# create a queue to evaluate all paths
queue = [start_obj]

# start loop with starting coord (run until queue is empty)
while len(queue) > 0:
    
    # pop the first item in queue
    current = queue.pop(0)
    if current['coords'] in visited:
        continue
    # see if current is at the end.
    # if at the end, check the path length and see if it is the shortest.  
    if current['coords'] == end:
        if len(current['path']) < shortest_path:
            # if it is, mark it so.
            shortest_path = len(current['path'])
            continue

    if current['coords'] not in visited:
        visited.append(current['coords'])

    # get the neighboring coords
    neighbors = get_neighbors(current['coords'], grid)
    for neighbor in neighbors:
        # see if these have been visited 
        if neighbor not in visited:
            # see if passable
            cur_char = grid[current['coords'][0]][current['coords'][1]]

            neighbor_char = grid[neighbor[0]][neighbor[1]]
            if cur_char == 'S':
                cur_char = 'a'
            if neighbor_char == 'E':
                neighbor_char = 'z'
            if is_passable(cur_char, neighbor_char):
                # add current coord to visited list
                next_path = current['path'].copy()
                next_path.append(current['coords'])
                queue.append(
                    {
                        'coords': neighbor,
                        'path': next_path,
                    }
                )
print(f"Part 1: {shortest_path = }")

# --- Part Two ---
# As you walk up the hill, you suspect that the Elves will want to turn this into a hiking trail. 
# The beginning isn't very scenic, though; perhaps you can find a better starting point.

# To maximize exercise while hiking, the trail should start as low as possible: elevation a. 
# The goal is still the square marked E. However, the trail should still be direct, taking the fewest steps to reach its goal. 
# So, you'll need to find the shortest path from any square at elevation a to the square marked E.

# Again consider the example from above:

# Sabqponm
# abcryxxl
# accszExk
# acctuvwj
# abdefghi
# Now, there are six choices for starting position (five marked a, plus the square marked S that counts as being at elevation a). 
# If you start at the bottom-left square, you can reach the goal most quickly:

# ...v<<<<
# ...vv<<^
# ...v>E^^
# .>v>>>^^
# >^>>>>>^
# This path reaches the goal in only 29 steps, the fewest possible.

# What is the fewest steps required to move starting from any square with elevation a to the location that should get the best signal?

# work in reverse, starting at end!
# 1778 'a's in this case.

# logic for passability is different in reverse
def is_passable_reverse(current_spot, next_spot):
    return ord(next_spot) - ord(current_spot) in list(range(-1, 26, 1))

start_obj = {
    'coords': end,
    'path': [],
}
# create a list of visited spots to not backtrack
visited = []
shortest_path = len(grid) * len(grid[0]) + 1
# create a queue to evaluate all paths
queue = [start_obj]

# start loop with starting coord (run until queue is empty)
while len(queue) > 0:
    # pop the first item in queue
    current = queue.pop(0)
    if current['coords'] in visited:
        continue
    # see if current is at the end.
    # if at the end, check the path length and see if it is the shortest.  
    if grid[current['coords'][0]][current['coords'][1]] == 'a':
        if len(current['path']) < shortest_path:
            # if it is, mark it so.
            shortest_path = len(current['path'])
        continue

    if current['coords'] not in visited:
        visited.append(current['coords'])

    # print(f"{current['coords'] = }, {grid[current['coords'][0]][current['coords'][1]] = }")
    # get the neighboring coords
    neighbors = get_neighbors(current['coords'], grid)
    for neighbor in neighbors:
        # see if these have been visited 
        if neighbor not in visited:
            # see if passable
            cur_char = grid[current['coords'][0]][current['coords'][1]]

            neighbor_char = grid[neighbor[0]][neighbor[1]]
            if cur_char == 'E':
                cur_char = 'z'
            if neighbor_char == 'S':
                neighbor_char = 'a'
            if is_passable_reverse(cur_char, neighbor_char):
                # add current coord to visited list
                next_path = current['path'].copy()
                next_path.append(current['coords'])
                queue.append(
                    {
                        'coords': neighbor,
                        'path': next_path,
                    }
                )
print(f"Part 2: {shortest_path = }")