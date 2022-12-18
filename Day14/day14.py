# --- Day 14: Regolith Reservoir ---
# The distress signal leads you to a giant waterfall! Actually, hang on - the signal seems like it's coming from the waterfall itself, and that doesn't make any sense. 
# However, you do notice a little path that leads behind the waterfall.

# Correction: the distress signal leads you behind a giant waterfall! There seems to be a large cave system here, and the signal definitely leads further inside.

# As you begin to make your way deeper underground, you feel the ground rumble for a moment. Sand begins pouring into the cave! 
# If you don't quickly figure out where the sand is going, you could quickly become trapped!

# Fortunately, your familiarity with analyzing the path of falling material will come in handy here. 
# You scan a two-dimensional vertical slice of the cave above you (your puzzle input) and discover that it is mostly air with structures made of rock.

# Your scan traces the path of each solid rock structure and reports the x,y coordinates that form the shape of the path, 
# where x represents distance to the right and y represents distance down. Each path appears as a single line of text in your scan. 
# After the first point of each path, each point indicates the end of a straight horizontal or vertical line to be drawn from the previous point. For example:

# 498,4 -> 498,6 -> 496,6
# 503,4 -> 502,4 -> 502,9 -> 494,9
# This scan means that there are two paths of rock; the first path consists of two straight lines, and the second path consists of three straight lines. 
# (Specifically, the first path consists of a line of rock from 498,4 through 498,6 and another line of rock from 498,6 through 496,6.)

# The sand is pouring into the cave from point 500,0.

# Drawing rock as #, air as ., and the source of the sand as +, this becomes:


#   4     5  5
#   9     0  0
#   4     0  3
# 0 ......+...
# 1 ..........
# 2 ..........
# 3 ..........
# 4 ....#...##
# 5 ....#...#.
# 6 ..###...#.
# 7 ........#.
# 8 ........#.
# 9 #########.
# Sand is produced one unit at a time, and the next unit of sand is not produced until the previous unit of sand comes to rest. 
# A unit of sand is large enough to fill one tile of air in your scan.

# A unit of sand always falls down one step if possible. If the tile immediately below is blocked (by rock or sand), the unit of sand attempts 
# to instead move diagonally one step down and to the left. If that tile is blocked, the unit of sand attempts to instead move diagonally 
# one step down and to the right. 
# Sand keeps moving as long as it is able to do so, at each step trying to move down, then down-left, then down-right. 
# If all three possible destinations are blocked, the unit of sand comes to rest and no longer moves, at which point the next unit of sand is created back at the source.

# So, drawing sand that has come to rest as o, the first unit of sand simply falls straight down and then stops:

# ......+...
# ..........
# ..........
# ..........
# ....#...##
# ....#...#.
# ..###...#.
# ........#.
# ......o.#.
# #########.
# The second unit of sand then falls straight down, lands on the first one, and then comes to rest to its left:

# ......+...
# ..........
# ..........
# ..........
# ....#...##
# ....#...#.
# ..###...#.
# ........#.
# .....oo.#.
# #########.
# After a total of five units of sand have come to rest, they form this pattern:

# ......+...
# ..........
# ..........
# ..........
# ....#...##
# ....#...#.
# ..###...#.
# ......o.#.
# ....oooo#.
# #########.
# After a total of 22 units of sand:

# ......+...
# ..........
# ......o...
# .....ooo..
# ....#ooo##
# ....#ooo#.
# ..###ooo#.
# ....oooo#.
# ...ooooo#.
# #########.
# Finally, only two more units of sand can possibly come to rest:

# ......+...
# ..........
# ......o...
# .....ooo..
# ....#ooo##
# ...o#ooo#.
# ..###ooo#.
# ....oooo#.
# .o.ooooo#.
# #########.
# Once all 24 units of sand shown above have come to rest, all further sand flows out the bottom, falling into the endless void. Just for fun, the path any new sand takes before falling forever is shown here with ~:

# .......+...
# .......~...
# ......~o...
# .....~ooo..
# ....~#ooo##
# ...~o#ooo#.
# ..~###ooo#.
# ..~..oooo#.
# .~o.ooooo#.
# ~#########.
# ~..........
# ~..........
# ~..........
# Using your scan, simulate the falling sand. How many units of sand come to rest before sand starts flowing into the abyss below?

def parse_bounds_from_line(line:str):
    str_coords = line.split(' -> ')
    coords = [sc.split(',') for sc in str_coords]
    return [[int(el[0]), int(el[1])] for el in coords]

def get_coords_from_bounds(bound_one, bound_two):
    points = []
    xs = [bound_one[0], bound_two[0]]
    ys = [bound_one[1], bound_two[1]]
    for x in range(min(xs), max(xs)+1):
        for y in range(min(ys), max(ys)+1):
            points.append([x, y])
    return points

def get_line_coords(bound_coords):
    all_points =[]
    for i in range(len(bound_coords) - 1):
        bound_one = bound_coords[i]
        bound_two = bound_coords[i+1]
        points = get_coords_from_bounds(bound_one, bound_two)
        for point in points:
            all_points.append(point) if point not in all_points else next
    return all_points

# method to create grid
def make_grid(all_points):
    xs = [el[0] for el in all_points]
    ys = [el[1] for el in all_points]
    min_x = min(xs)
    max_x = max(xs)
    max_y = max(ys)
    grid = []
    air = '.' * (max_x - min_x + 1)
    for _i in range(max_y + 1):
        grid.append(list(air))
    # print(f"{min_x = }, {max_x = }, {max_y = }")
    return min_x, max_x, max_y, grid

def print_grid(grid):
    for row in grid:
        print(''.join(row))

# method to define into the void
def into_void(coord, grid):
    x, y = coord
    return y < 0 or x < 0 or y >= len(grid) or x >= len(grid[0])

def staring_into_void(coord, grid):
    x, y = coord
    diag_left = [x-1, y+1]
    diag_right = [x+1, y+1]
    return (into_void(diag_left, grid) or into_void(diag_right, grid)) and blocked(grid[y+1][x])

def is_air(spot):
    return spot == '.'

def blocked(spot):
    return spot == '#' or spot == 'o'

def no_more_moves(coords, grid):
    cur_x, cur_y = coords
    no_moves_below = False
    no_moves_diag_left = False
    no_moves_diag_right = False

    if into_void([cur_x, cur_y+1], grid):
        no_moves_below = True
    elif blocked(grid[cur_y+1][cur_x]): 
        no_moves_below = True

    if into_void([cur_x-1, cur_y+1], grid):
        no_moves_diag_left = True
    elif blocked(grid[cur_y+1][cur_x-1]):
        no_moves_diag_left = True

    if into_void([cur_x+1, cur_y+1], grid):
        no_moves_diag_right = True
    elif blocked(grid[cur_y+1][cur_x+1]):
        no_moves_diag_right = True

    return no_moves_below and no_moves_diag_left and no_moves_diag_right

# method to drop and move sand
def drop_sand(start_coord, grid):
    cur_x, cur_y = start_coord
    while not no_more_moves([cur_x, cur_y], grid):
        # check moving down
        while is_air(grid[cur_y+1][cur_x]):
            cur_y += 1
        # check moving diagonally left
        if is_air(grid[cur_y+1][cur_x-1]):  
            cur_y +=1
            cur_x -=1
        # check moving diagonally right
        elif is_air(grid[cur_y+1][cur_x+1]):  
            cur_y +=1 
            cur_x +=1
        
    if not staring_into_void([cur_x, cur_y], grid):
        grid[cur_y][cur_x] = 'o'
    return grid

# method to count grains of resting sand
def count_grains(grid):
    grains = 0
    for row in grid:
        grains += row.count('o')
    return grains

# myfile = open ("/Users/raymondoh/Documents/AdventOfCode2022/Day14/test.txt", "r").readlines()
myfile = open ("/Users/raymondoh/Documents/AdventOfCode2022/data/day14.txt", "r").readlines()

# main
all_points = []
for line in myfile:
    line = line.rstrip()
    bound_coords = parse_bounds_from_line(line)
    ap = get_line_coords(bound_coords)
    all_points += ap

minx, maxx, maxy, grid = make_grid(all_points)
# define rocks in grid
for point in all_points:
    y = point[1]
    x = point[0]-minx
    grid[y][x] = '#'

start_x = 500-minx

last_count = 0
current_count = -1
while last_count != current_count:
    grid = drop_sand([start_x, 0], grid)
    last_count = current_count
    current_count = count_grains(grid)

print_grid(grid)
print(f"Part 1: {count_grains(grid) = }")

# --- Part Two ---
# You realize you misread the scan. There isn't an endless void at the bottom of the scan - there's floor, and you're standing on it!

# You don't have time to scan the floor, so assume the floor is an infinite horizontal line with a y coordinate equal to two plus the highest y coordinate of any point in your scan.

# In the example above, the highest y coordinate of any point is 9, and so the floor is at y=11. 
# (This is as if your scan contained one extra rock path like -infinity,11 -> infinity,11.) With the added floor, the example above now looks like this:

#         ...........+........
#         ....................
#         ....................
#         ....................
#         .........#...##.....
#         .........#...#......
#         .......###...#......
#         .............#......
#         .............#......
#         .....#########......
#         ....................
# <-- etc #################### etc -->
# To find somewhere safe to stand, you'll need to simulate falling sand until a unit of sand comes to rest at 500,0, 
# blocking the source entirely and stopping the flow of sand into the cave. In the example above, the situation finally looks like this after 93 units of sand come to rest:

# ............o............
# ...........ooo...........
# ..........ooooo..........
# .........ooooooo.........
# ........oo#ooo##o........
# .......ooo#ooo#ooo.......
# ......oo###ooo#oooo......
# .....oooo.oooo#ooooo.....
# ....oooooooooo#oooooo....
# ...ooo#########ooooooo...
# ..ooooo.......ooooooooo..
# #########################
# Using your scan, simulate the falling sand until the source of the sand becomes blocked. How many units of sand come to rest?

# method to create grid
def make_grid2(all_points):
    xs = [el[0] for el in all_points]
    ys = [el[1] for el in all_points]
    min_x = min(xs)
    max_x = max(xs)
    max_y = max(ys) + 1
    width = max_x - min_x
    print(width)
    grid = []
    air = '.' * (5 * width + 1)
    for _i in range(max_y + 1):
        grid.append(list(air))
    
    # define bottom
    bottom = '#' * (5 * width + 1)
    grid.append(bottom)

    # define rocks in grid
    for point in all_points:
        y = point[1]
        x = point[0] - minx + (2 * width)
        grid[y][x] = "#"

    return min_x, max_x, max_y, grid

# main
all_points = []
for line in myfile:
    line = line.rstrip()
    bound_coords = parse_bounds_from_line(line)
    ap = get_line_coords(bound_coords)
    all_points += ap

minx, maxx, maxy, grid = make_grid2(all_points)

# method to drop and move sand
def drop_sand2(start_coord, grid):
    cur_x, cur_y = start_coord
    while not no_more_moves([cur_x, cur_y], grid):
        # check moving down
        while is_air(grid[cur_y+1][cur_x]):
            cur_y += 1
        # check moving diagonally left
        if is_air(grid[cur_y+1][cur_x-1]):  
            cur_y +=1
            cur_x -=1
        # check moving diagonally right
        elif is_air(grid[cur_y+1][cur_x+1]):  
            cur_y +=1 
            cur_x +=1
        
    # if not staring_into_void([cur_x, cur_y], grid):
    grid[cur_y][cur_x] = 'o'
    return grid

# print_grid(grid)

start_x = 500-minx+(2*(maxx-minx))
last_count = 0
current_count = -1
while last_count != current_count:
    grid = drop_sand([start_x, 0], grid)
    last_count = current_count
    current_count = count_grains(grid)

# print_grid(grid)
print(f"Part2: {current_count = }")
