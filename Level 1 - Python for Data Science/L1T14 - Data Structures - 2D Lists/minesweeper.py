# The input grid
input_grid = [
    ["-", "-", "-", "#", "#"],
    ["-", "#", "-", "-", "-"],
    ["-", "-", "#", "-", "-"],
    ["-", "#", "#", "-", "-"],
    ["-", "-", "-", "-", "-"]
    ]

# Since grid will work 3 by 3 , directions to surrounding 8 grids
# Allows them to be 'scanned'
directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1),
              (1, -1), (1, 0), (1, 1)]

# Variables used to determine the row and column length
rows = len(input_grid)
column = len(input_grid[0])


# Define the mine position, and calculate the cells around it's value
# Based on how many # is in their 3*3 zone.
def mine_position(rows_index, column_index):

    # Define the row and column position('_pos') and count
    count = 0
    row_pos = 0
    column_pos = 0

    # Use for loop to allow rerun for every row and column position
    # Using the directions, new row and column can be created
    for row_pos, column_pos in directions:
        new_row = rows_index + row_pos
        new_column = column_index + column_pos

        # Boundary Check: ensure that the new row/column is greater than
        # Or equal to 0, but less than the max length of the row/column index
        if rows > new_row >= 0 and column > new_column >= 0:

            # The '#' will serve as mines, and surrounding values will
            # Get  +1 count when in the 3*3 grid of a '#'.
            if input_grid[new_row][new_column] == '#':
                count += 1

    return count


# Create a function that will read input grid and '-'
def mine_sweeper(input_grid):

    # Utilise row[:] to create a copy of each row in grid for iteration
    result = [row[:] for row in input_grid]

    # Determine the range of both indexes, and then assign value to
    # It based on the amount of # in its 3*3 grid
    for rows_index in range(rows):
        for column_index in range(column):
            if input_grid[rows_index][column_index] == '-':
                result[rows_index][column_index] = str(
                    mine_position(rows_index, column_index))

    return result


# Define a variable to print and call the function
swept_field = mine_sweeper(input_grid)

# Print every row of the grid in a separate line
for rows in swept_field:
    print(rows)
