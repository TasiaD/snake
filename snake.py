"""Class modeling a Snake object.

x, y = coordinates of top left corner of first snake cell
tx, ty = coordinates of top left corner of last snake cell
hval = the number corresponding to the beginning of the snake

The snake's sections are modeled through numbers in the game's grid. The highest number belongs to the snake's beginning section, whereas the lowest number (1) would correspond to its last section.

"""
class Snake:
    def __init__(self, x, y):
        self.x, self.tx = (x,) * 2
        self.y, self.ty = (y,) * 2
        self.hval = 1
    """finds the x and y coordinates of the snake's first section
    grid = context (width, height) in which to operate
    """
    def find_head(self, grid):
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if(grid[y][x] > grid[self.y][self.x]):
                    self.x = x
                    self.y = y
                    self.hval = grid[y][x]
    """finds x and y coordinates of the snake's last section
    grid = context (width, height) in which to operate
    """
    def find_tail(self, grid):
        min_val = self.hval
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if(grid[y][x] < min_val and grid[y][x] > 0):
                    min_val = grid[y][x]
                    self.tx = x
                    self.ty = y
    """removes the snake's last section
    The snake is modeled through positive non-zero numbers in the game grid. Decrementing each positive number on the grid will result in the lowest section ending up with
    values of 0, which will not display as a snake cell. Thus the last section is erased.

    if the snake scores, then the hval is increased to trigger addition of new cells ("growth")
    return values indicates whether game can continue and whether player has scored/the reason they lost

    """
    def remove_tail(self, grid):
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if(grid[y][x] > 0):
                    grid[y][x] -= 1
    def move(self, dr, grid, cell_size, mcell):
        self.find_head(grid)
        nx = (dr[0] * cell_size) + self.x
        ny = (dr[1] * cell_size) + self.y
        in_bounds = nx < len(grid[0]) and nx >= 0 and ny < len(grid) and ny >= 0
        empty = in_bounds and grid[ny][nx] <= 0
        if in_bounds and empty:
            scoring = grid[ny][nx] == -1
            mcell('s', nx, ny, self.hval+1)
            self.x = nx
            self.y = ny
            if not scoring:
                self.remove_tail(grid)
            else:
                self.hval += 4
            return (True, scoring)
        else:
            #it's okay to use ternary here because one or the other is true
            reason = "You went out of bounds." if not in_bounds else "You collided with yourself."
            return (False, reason)
