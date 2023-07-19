import os
import time
from colorama import Fore, Style, init

init()


class Cell:
    def __init__(self, alive=False):
        self.alive = alive


class Grid:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[Cell() for _ in range(cols)] for _ in range(rows)]

    def get_neighbors(self, row, col):
        neighbors = []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == 0 and j == 0:
                    continue
                new_row = row + i
                new_col = col + j
                if 0 <= new_row < self.rows and 0 <= new_col < self.cols:
                    neighbors.append(self.grid[new_row][new_col])
        return neighbors

    def update(self):
        new_grid = [[Cell() for _ in range(self.cols)] for _ in range(self.rows)]
        for row in range(self.rows):
            for col in range(self.cols):
                cell = self.grid[row][col]
                neighbors = self.get_neighbors(row, col)
                living_neighbors = sum(1 for neighbor in neighbors if neighbor.alive)
                if cell.alive:
                    if living_neighbors < 2 or living_neighbors > 3:
                        new_grid[row][col].alive = False
                    else:
                        new_grid[row][col].alive = True
                else:
                    if living_neighbors == 3:
                        new_grid[row][col].alive = True
        self.grid = new_grid

    def display(self):
        for row in self.grid:
            for cell in row:
                if cell.alive:
                    print(Fore.LIGHTCYAN_EX + "■" + Style.RESET_ALL, end=" ")
                else:
                    print(Fore.BLACK + "□" + Style.RESET_ALL, end=" ")
            print()


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def main():
    rows = 29
    cols = 31
    grid = Grid(rows, cols)

    grid.grid[14][15].alive = True

    grid.grid[15][16].alive = True
    grid.grid[16][17].alive = True
    grid.grid[17][18].alive = True
    grid.grid[18][19].alive = True
    grid.grid[19][18].alive = True
    grid.grid[20][17].alive = True
    grid.grid[21][16].alive = True

    grid.grid[13][14].alive = True
    grid.grid[12][13].alive = True
    grid.grid[11][12].alive = True
    grid.grid[10][11].alive = True
    grid.grid[9][12].alive = True
    grid.grid[8][13].alive = True
    grid.grid[7][14].alive = True

    grid.grid[13][16].alive = True
    grid.grid[12][17].alive = True
    grid.grid[11][18].alive = True
    grid.grid[10][19].alive = True
    grid.grid[11][20].alive = True
    grid.grid[12][21].alive = True
    grid.grid[13][22].alive = True

    grid.grid[15][14].alive = True
    grid.grid[16][13].alive = True
    grid.grid[17][12].alive = True
    grid.grid[18][11].alive = True
    grid.grid[17][10].alive = True
    grid.grid[16][9].alive = True
    grid.grid[15][8].alive = True

    while True:
        clear_screen()
        grid.display()
        grid.update()
        time.sleep(0.2)


if __name__ == "__main__":
    main()
