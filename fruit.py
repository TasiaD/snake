import random
"""Class representing a Fruit object.

Each fruit object should be placed at a random x,y coordinate which is calculated
through the gen_crds function.

"""
class Fruit:
    def __init__(self, grid, cell_size):
        self.spawn(grid, cell_size)

    """
    generates pseudo-random x,y coordinate using python's random module
    grid = context (i.e. width, height) in which to generate coordinate,
    cell_size = width of cell
    """
    def gen_crds(self, grid, cell_size):
        self.x = random.randrange(0, (len(grid[0]) - cell_size + 1), cell_size)
        self.y = random.randrange(0, (len(grid) - cell_size + 1), cell_size)
    def spawn(self, grid, cell_size):
        self.gen_crds(grid, cell_size)
        while grid[self.y][self.x] > 0:
            self.gen_crds(grid, cell_size)
