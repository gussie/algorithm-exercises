'''
Given a list of lists, where '1' = land and '0' = water, count the 
number of islands. An island is defined as contiguous land mass -- 
1's above, below, or to either side are one island; diagonal 1's are not

Once we've found all islands, return a nested list with the coordinates
for each island

I: python lonely_island.py < input1.txt

example input1.txt: 
0001110000
1100110010
1000101111
1110000001
0000101110

1 = land
0 = water

'''


def validate(matrix, x, y):
  return x >= 0 and x < len(matrix[0]) and y >= 0 and y < len(matrix)


def explore_island(matrix, x, y, island_locs):
  # We've left the map; go back where we came from.
  if not validate(matrix, x, y):
    return

  # Base case: we hit water; go back where we came from.
  if matrix[y][x] == 0:
    return

  # Recursion case: we're still on the island; keep exploring.
  matrix[y][x] = 0
  island_locs.append((x,y))
  explore_island(matrix, x+1, y, island_locs)
  explore_island(matrix, x-1, y, island_locs)
  explore_island(matrix, x, y+1, island_locs)

  return


def read_input():
  matrix = []

  n_lines = int(input())
  for n in range(n_lines):
    row = []
    for i in input():
      row.append(int(i))
    matrix.append(row)
  
  return matrix


def main():
  matrix = read_input()
  n_islands = 0
  islands = []

  for y, row in enumerate(matrix): #0to4
    for x, item in enumerate(row): #0to9
      island_locs = []
      if matrix[y][x] == 1: 
        explore_island(matrix, x, y, island_locs)
        n_islands += 1
        islands.append(island_locs)

  
  print(n_islands)
  print(islands)

    
if __name__ == '__main__':
  main()