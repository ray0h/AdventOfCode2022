# --- Day 8: Treetop Tree House ---
# The expedition comes across a peculiar patch of tall trees all planted carefully in a grid. 
# The Elves explain that a previous expedition planted these trees as a reforestation effort. 
# Now, they're curious if this would be a good location for a tree house.

# First, determine whether there is enough tree cover here to keep a tree house hidden. 
# To do this, you need to count the number of trees that are visible from outside the grid when looking directly along a row or column.

# The Elves have already launched a quadcopter to generate a map with the height of each tree (your puzzle input). For example:

# 30373
# 25512
# 65332
# 33549
# 35390
# Each tree is represented as a single digit whose value is its height, where 0 is the shortest and 9 is the tallest.

# A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. 
# Only consider trees in the same row or column; that is, only look up, down, left, or right from any given tree.

# All of the trees around the edge of the grid are visible - since they are already on the edge, there are no trees to block the view. 
# In this example, that only leaves the interior nine trees to consider:

# The top-left 5 is visible from the left and top. (It isn't visible from the right or bottom since other trees of height 5 are in the way.)
# The top-middle 5 is visible from the top and right.
# The top-right 1 is not visible from any direction; for it to be visible, there would need to only be trees of height 0 between it and an edge.
# The left-middle 5 is visible, but only from the right.
# The center 3 is not visible from any direction; for it to be visible, there would need to be only trees of at most height 2 between it and an edge.
# The right-middle 3 is visible from the right.
# In the bottom row, the middle 5 is visible, but the 3 and 4 are not.
# With 16 trees visible on the edge and another 5 visible in the interior, a total of 21 trees are visible in this arrangement.

# Consider your map; how many trees are visible from outside the grid?

from multiprocessing.dummy import current_process


# myfile = open("/Users/raymondoh/Documents/AdventOfCode2022/Day8/test.txt", "r").readlines()

myfile = open("/Users/raymondoh/Documents/AdventOfCode2022/data/day8.txt", "r").readlines()

# create 2x2 grid
grid = []
for line in myfile:
    chars = list(line.rstrip())
    grid.append([int(c) for c in chars])


width = len(grid[0])
height = len(grid)

def is_edge(x: int, y: int):
    return x == 0 or y == 0 or x == (width-1) or y == (height-1)

def has_north_viz(x: int, y: int, grid): 
    tree_height = grid[y][x]
    is_tallest = True
    for i in range(y-1, -1, -1):
        if grid[i][x] >= tree_height:
            is_tallest = False
            break
    return is_tallest

def has_south_viz(x: int, y: int, grid): 
    tree_height = grid[y][x]
    is_tallest = True
    for i in range(y+1, height, 1):
        if grid[i][x] >= tree_height:
            is_tallest = False
            break
    return is_tallest

def has_west_viz(x: int, y: int, grid): 
    tree_height = grid[y][x]
    is_tallest = True
    for i in range(x-1, -1, -1):
        if grid[y][i] >= tree_height:
            is_tallest = False
            break
    return is_tallest

def has_east_viz(x: int, y: int, grid): 
    tree_height = grid[y][x]
    is_tallest = True
    for i in range(x+1, width, 1):
        if grid[y][i] >= tree_height:
            is_tallest = False
            break
    return is_tallest

visible_tree_count = 0
for y in range(height):
    for x in range(width):
        if is_edge(x=x, y=y):
            visible_tree_count += 1
        else:
            if has_north_viz(x, y, grid) or has_south_viz(x, y, grid) or has_west_viz(x, y, grid) or has_east_viz(x, y, grid):
                visible_tree_count +=1 
        
print(f"{visible_tree_count = }")

# --- Part Two ---
# Content with the amount of tree cover available, the Elves just need to know the best spot to build their tree house: 
# they would like to be able to see a lot of trees.

# To measure the viewing distance from a given tree, look up, down, left, and right from that tree; 
# stop if you reach an edge or at the first tree that is the same height or taller than the tree under consideration. 
# (If a tree is right on the edge, at least one of its viewing distances will be zero.)

# The Elves don't care about distant trees taller than those found by the rules above; 
# the proposed tree house has large eaves to keep it dry, so they wouldn't be able to see higher than the tree house anyway.

# In the example above, consider the middle 5 in the second row:

# 30373
# 25512
# 65332
# 33549
# 35390
# Looking up, its view is not blocked; it can see 1 tree (of height 3).
# Looking left, its view is blocked immediately; it can see only 1 tree (of height 5, right next to it).
# Looking right, its view is not blocked; it can see 2 trees.
# Looking down, its view is blocked eventually; it can see 2 trees (one of height 3, then the tree of height 5 that blocks its view).
# A tree's scenic score is found by multiplying together its viewing distance in each of the four directions. 
# For this tree, this is 4 (found by multiplying 1 * 1 * 2 * 2).

# However, you can do even better: consider the tree of height 5 in the middle of the fourth row:

# 30373
# 25512
# 65332
# 33549
# 35390
# Looking up, its view is blocked at 2 trees (by another tree with a height of 5).
# Looking left, its view is not blocked; it can see 2 trees.
# Looking down, its view is also not blocked; it can see 1 tree.
# Looking right, its view is blocked at 2 trees (by a massive tree of height 9).
# This tree's scenic score is 8 (2 * 2 * 1 * 2); this is the ideal spot for the tree house.

# Consider each tree on your map. What is the highest scenic score possible for any tree?

def get_north_viz(x: int, y: int, grid): 
    tree_height = grid[y][x]
    dist = 1
    i = y-1
    while (grid[i][x] < tree_height):
        i -= 1
        if i < 0:
            break 
        dist += 1
    return dist

def get_south_viz(x: int, y: int, grid): 
    tree_height = grid[y][x]
    dist = 1
    i = y+1
    while (grid[i][x] < tree_height):
        i += 1
        if i >= height:
            break
        dist += 1
    return dist


def get_west_viz(x: int, y: int, grid): 
    tree_height = grid[y][x]
    dist = 1
    i = x-1
    while (grid[y][i] < tree_height):
        i -= 1
        if i < 0:
            break
        dist += 1
    return dist


def get_east_viz(x: int, y: int, grid): 
    tree_height = grid[y][x]
    dist = 1
    i = x+1
    while (grid[y][i] < tree_height):
        i += 1
        if i >= width:
            break
        dist += 1
    return dist
    
max_viz_score = 0
for y in range(1, height-1):
    for x in range(1, width-1):
        north = get_north_viz(x, y, grid)
        south = get_south_viz(x, y, grid)
        west = get_west_viz(x, y, grid)
        east = get_east_viz(x, y, grid)
        current_viz_score =  north * south * west * east
        if current_viz_score > max_viz_score:
            max_viz_score = current_viz_score
        
print(f"{max_viz_score = }")

