import random
import time
import numpy
import pygame
import sys
from copy import deepcopy

# checking a valid column number is entered
def is_column_number_valid():
    while True:
        # entering column number for human player
        if piece == "X":
            column = 0
            while column not in range(1, 8):
                try:
                    column = int(input("Enter column number between 1 and 7: "))
                except ValueError:
                    print("Invalid column number")

        # generating random column number for computer player
        elif piece == "O":
            column = random.randrange(1, 8)

        # check if column full
        if check_column_full(column-1) == "Empty":
            break
        else:
            # message for human player
            if piece == "X":
                print("Column", column, "is full, please choose another")

    # -1 to account for count starting from 0, e.g. connect_four[0] = column 1
    return column-1

def available_moves():
    moves = {}

    columns = [place_in_column1, place_in_column2, place_in_column3, place_in_column4, place_in_column5,
               place_in_column6, place_in_column7]

    # producing a dictionary of all available positions for next move
    x = 0
    while x <= 6:
        if columns[x] != -1:
            moves[x] = columns[x]
        x += 1

    return moves

def try_move(piece):
    global copy_connect_four, connect_four

    # getting all the available moves
    moves = available_moves()
    copy_connect_four = deepcopy(connect_four)

    x = 1
    # in copy board change all available moves to X
    for column, row in moves.items():
        copy_connect_four[row, column] = piece
        print("Move", x)
        print(copy_connect_four)
        # undoing move after printing
        copy_connect_four[row, column] = "-"
        x += 1

    #while len(moves) > 0:
     #   try_move("X")


def check_column_full(column):
    # 0 is the top row, therefore checking if column is full
    if connect_four[0][column] == "X" or connect_four[0][column] == "O":
        return "Full"
    else:
        return "Empty"

def place_piece(column, piece):
    global connect_four
    global place_in_column1, place_in_column2, place_in_column3, place_in_column4, \
        place_in_column5, place_in_column6, place_in_column7

    # changing position in column down one if the piece is placed in that column
    if column == 0: row = place_in_column1; place_in_column1 -= 1

    elif column == 1: row = place_in_column2; place_in_column2 -= 1

    elif column == 2: row = place_in_column3; place_in_column3 -= 1

    elif column == 3: row = place_in_column4; place_in_column4 -= 1

    elif column == 4: row = place_in_column5; place_in_column5 -= 1

    elif column == 5: row = place_in_column6; place_in_column6 -= 1

    elif column == 6: row = place_in_column7; place_in_column7 -= 1

    # putting piece down
    connect_four[row][column] = piece

    return row

def check_tie():
    columns = [place_in_column1, place_in_column2, place_in_column3, place_in_column4, place_in_column5,
               place_in_column6, place_in_column7]

    # checking for a tie if neither player has won
    # if all positions equal -1 for every column then there are no more available moves
    if all(position == -1 for position in columns):
        return True

def check_winner(column, piece, row):
    # CHECK 1: checking 3 pieces to right of current piece
    try:
        if connect_four[row][(column+1)] == piece and\
                connect_four[row][(column+2)] == piece and\
                connect_four[row][(column+3)] == piece:
            return True
    except IndexError:
        pass

    # CHECK 2: checking 3 pieces to left of current piece
    try:
        if connect_four[row][(column-1)] == piece and\
                connect_four[row][(column-2)] == piece and\
                connect_four[row][(column-3)] == piece:
            return True
    except IndexError:
        pass

    # CHECK 3: checking 2 pieces to left of current piece and 1 to right
    try:
        if connect_four[row][(column-1)] == piece and\
                connect_four[row][(column-2)] == piece and\
                connect_four[row][(column+1)] == piece:
            return True
    except IndexError:
        pass

    # CHECK 4: checking 2 pieces to right of current piece and 1 to left
    try:
        if connect_four[row][(column+1)] == piece and \
                connect_four[row][(column+2)] == piece and \
                connect_four[row][(column-1)] == piece:
            return True
    except IndexError:
        pass

    # CHECK 5: checking 3 pieces below current piece
    try:
        if connect_four[row+1][column] == piece and \
                connect_four[row+2][column] == piece and \
                connect_four[row+3][column] == piece:
            return True
    except IndexError:
        pass

    # CHECK 6: checking 3 pieces diagonally above and to right of current piece
    try:
        if connect_four[row-1][(column+1)] == piece and \
                connect_four[row-2][(column+2)] == piece and \
                connect_four[row-3][(column+3)] == piece:
            return True
    except IndexError:
        pass

    # CHECK 7: checking 3 pieces diagonally above and to left of current piece
    try:
        if connect_four[row-1][(column-1)] == piece and \
                connect_four[row-2][(column-2)] == piece and \
                connect_four[row-3][(column-3)] == piece:
            return True
    except IndexError:
        pass

    # CHECK 8: checking 3 pieces diagonally below and to right of current piece
    try:
        if connect_four[row+1][(column+1)] == piece and \
                connect_four[row+2][(column+2)] == piece and \
                connect_four[row+3][(column+3)] == piece:
            return True
    except IndexError:
        pass

    # CHECK 9: checking 3 pieces diagonally below and to left of current piece
    try:
        if connect_four[row+1][(column-1)] == piece and \
                connect_four[row+2][(column-2)] == piece and \
                connect_four[row+3][(column-3)] == piece:
            return True
    except IndexError:
        pass

    # CHECK 10: checking 1 piece diagonally below and to left of current piece
    # and 2 pieces diagonally above and to right
    try:
        if connect_four[row+1][(column-1)] == piece and \
                connect_four[row-1][(column+1)] == piece and \
                connect_four[row-2][(column+2)] == piece:
            return True
    except IndexError:
        pass

    # CHECK 11: checking 2 pieces diagonally below and to left of current piece
    # and 1 piece diagonally above and to right
    try:
        if connect_four[row+1][(column-1)] == piece and \
                connect_four[row+2][(column-2)] == piece and \
                connect_four[row-1][(column+1)] == piece:
            return True
    except IndexError:
        pass

    # CHECK 12: checking 1 piece diagonally above and to left of current piece
    # and 2 pieces diagonally below and to right
    try:
        if connect_four[row-1][(column-1)] == piece and \
                connect_four[row+1][(column+1)] == piece and \
                connect_four[row+2][(column+2)] == piece:
            return True
    except IndexError:
        pass

    # CHECK 13: checking 2 pieces diagonally above and to left of current piece
    # and 1 piece diagonally below and to right
    try:
        if connect_four[row-1][(column-1)] == piece and \
                connect_four[row-2][(column-2)] == piece and \
                connect_four[row+1][(column+1)] == piece:
            return True
    except IndexError:
        pass

def check_game_over():
    global result
    if check_winner(column_number, piece, row_number):
        result = "WINNER: " + piece + " in " + str(num_of_moves) + " moves!"
        return True

    # checking for a tie if neither player has won
    elif check_tie():
        result = "DRAW - no available moves left!"
        return True

def evaluate_board():
    if check_winner(column_number, "X", row_number):
        return 1
    elif check_winner(column_number, "O", row_number):
        return -1
    else:
        return 0

def minimax(is_maximising):
    if check_game_over():
        return evaluate_board()
    if is_maximising:
        best_value = -float("Inf")
    else:
        best_value = float("Inf")
    return best_value

def draw_board():
    screen.fill(white)
    pygame.draw.rect(screen, blue, pygame.Rect(0, 100, 700, 600))

    column_pixel = 150

    # drawing the GUI board for the existing values
    # red for X, yellow for O, white for blank
    for row in range(0, 6):
        row_pixel = 50
        for column in range(0, 7):
            if connect_four[row][column] == "X":
                pygame.draw.circle(screen, red, (row_pixel, column_pixel), 45)
            elif connect_four[row][column] == "O":
                pygame.draw.circle(screen, yellow, (row_pixel, column_pixel), 45)
            elif connect_four[row][column] == "-":
                pygame.draw.circle(screen, white, (row_pixel, column_pixel), 45)
            row_pixel += 100
        column_pixel += 100

    pygame.display.update()

# initialising the empty board
connect_four = numpy.array([["-", "-", "-", "-", "-", "-", "-"],
                            ["-", "-", "-", "-", "-", "-", "-"],
                            ["-", "-", "-", "-", "-", "-", "-"],
                            ["-", "-", "-", "-", "-", "-", "-"],
                            ["-", "-", "-", "-", "-", "-", "-"],
                            ["-", "-", "-", "-", "-", "-", "-"]])

# 5 represents the bottom row, therefore empty at start
place_in_column1 = 5
place_in_column2 = 5
place_in_column3 = 5
place_in_column4 = 5
place_in_column5 = 5
place_in_column6 = 5
place_in_column7 = 5
#
# # test game state
# connect_four = numpy.array([["O", "X", "O", "O", "-", "-", "-"],
#                             ["O", "O", "X", "X", "O", "-", "X"],
#                             ["X", "X", "X", "O", "X", "O", "O"],
#                             ["X", "X", "O", "X", "X", "O", "O"],
#                             ["O", "X", "O", "O", "X", "X", "O"],
#                             ["X", "O", "O", "X", "O", "O", "X"]])
#
# # test game state
# place_in_column1 = -1
# place_in_column2 = -1
# place_in_column3 = -1
# place_in_column4 = -1
# place_in_column5 = 0
# place_in_column6 = 1
# place_in_column7 = 0


num_of_moves = 0

column_number = 0
row_number = 0
piece = ""

# colours to use in pygame in RGB
white = (255, 255, 255)
red = (255, 0, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)

pygame.init()

screen = pygame.display.set_mode((700, 700))

# displaying the empty board
draw_board()

#####
# trying each available move in first go, as player X
# print("Original board: ")
# print(connect_four)

#####

# continue game if not won or tied
while not check_game_over():
    # try_move("X")

    pygame.event.get()

    # determining which turn it is
    if num_of_moves % 2 == 0:
        piece = "X"
    else:
        piece = "O"

    # EVENT HANDLING NOT CURRENTLY WORKING
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            print("MD")

        if event.type == pygame.MOUSEMOTION:
            posx = event.pos[0]
            if piece == "X":
                pygame.draw.circle(screen, red, (posx, 50), 45)
            else:
                pygame.draw.circle(screen, yellow, (posx, 50), 45)
            pygame.display.update()

    print("\n" + piece + "'s TURN")

    # outputting standard board for X and O
    for line in connect_four:
        for item in line:
            print(item, end="")
        print()

    # prompt to enter a valid column number
    column_number = is_column_number_valid()

    num_of_moves += 1

    # time delay before computer player's turn
    if piece == "O":
        time.sleep(1)

    # row position for the piece placed
    row_number = place_piece(column_number, piece)

    draw_board()

print("\n")

# outputting final board after game is over
for line in connect_four:
    for item in line:
        print(item, end="")
    print()

# returns value of 1 is X wins, -1 if O wins or 0 if a tie
# print(minimax(True))

stalling = input(result)
