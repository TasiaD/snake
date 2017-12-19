class Board:
    def __init__(self, width, height, cell_size):
        self.grid = [[0 for j in range(width)] for i in range(height)]
        self.cell_size = cell_size
        self.fruit_color = (209, 56, 14)
        self.snake_color = (157, 239, 33)
        """Marks the cells to denote fruit and snake cells. Fruit cells are marked with -1. Snake cells are marked with positive non-zero integers.

         Notice the use of += for the snake cells. This makes the snake longer because it makes existing positive values larger.

        If the snake begins at 1 cell, then marking yields a single cell on the board which = 1.
        When the snake grows by one cell, then marking yields a cell which = 1 + 1 = 2, plus the existing cell which = 1, making the snake 2 cells long after rendering.

         """
    def mark_cell(self, type, col, row, increment=1):
        if(type == 'f'):
            self.grid[row][col] = -1
        elif(type == 's'):
            self.grid[row][col] += increment

    """Fills cells based on their marking. Negative cells become fruit cells, cells with positive non-zero integers become snake cells."""
    def render(self, pen, surface):
        for y in range(len(self.grid)):
            for x in range(len(self.grid[0])):
                if (self.grid[y][x] > 0):
                    pen.draw.rect(surface, self.snake_color, (x, y, self.cell_size, self.cell_size))
                elif (self.grid[y][x] < 0):
                    pen.draw.rect(surface, self.fruit_color, (x, y, self.cell_size, self.cell_size))
    """Clears the cells to begin the game again."""
    def reset(self):
        self.grid = [[0 for j in range(len(self.grid))] for i in range(len(self.grid[0]))]
