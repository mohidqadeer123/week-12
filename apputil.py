import numpy as np
from IPython.display import clear_output
import time
import seaborn as sns
import matplotlib.pyplot as plt


def update_board(current_board):
    '''Update the board accordingly for next step in Conway's game'''
    rows, cols = update_board.shape
    updated_board = np.zeros((rows, cols), dtype=int)
    
    for i in range (rows):
        for j in range (cols):
            # Region around (r,c)
            live_neighbors = np.sum(
                current_board[max(0, i-1):min(rows, i+2), max(0, j-1):min(cols, j+2)]
            ) - current_board[i, j]

            # Apply rules
            if current_board[i, j] == 1:
                if live_neighbors < 2 or live_neighbors > 3:
                    updated_board[i, j] = 0
                else:
                    updated_board[i, j] = 1
            else:
                if live_neighbors == 3:
                    updated_board[i, j] = 1

    return updated_board


def show_game(game_board, n_steps=10, pause=0.5):
    """
    Show `n_steps` of Conway's Game of Life, given the `update_board` function.

    Parameters
    ----------
    game_board : numpy.ndarray
        A binary array representing the initial starting conditions for Conway's Game of Life. In this array, ` represents a "living" cell and 0 represents a "dead" cell.
    n_steps : int, optional
        Number of game steps to run through, by default 10
    pause : float, optional
        Number of seconds to wait between steps, by default 0.5
    """
    for step in range(n_steps):
        clear_output(wait=True)

        # update board
        game_board = update_board(game_board)

        # show board
        sns.heatmap(game_board, cmap='tab20c_r', 
                    cbar=False, square=True, linewidths=1)
        plt.title(f'Board State at Step {step + 1}')
        plt.show()

        # wait for the next step
        if step + 1 < n_steps:
            time.sleep(pause)