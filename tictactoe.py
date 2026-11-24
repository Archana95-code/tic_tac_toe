
# Displaying the board

board = [" ", " ", " ",
         " ", " ", " ",
         " ", " ", " "]


def display_board():
    print("-------------")
    for i in range(0, 9, 3):
        print("|", board[i], "|", board[i+1], "|", board[i+2], "|")
        print("-------------")


# Check winner

def check_position():

    # Check rows
    if board[0] == board[1] == board[2] != " ":
        return True

    elif board[3] == board[4] == board[5] != " ":
        return True

    elif board[6] == board[7] == board[8] != " ":
        return True

    # Check columns
    elif board[0] == board[3] == board[6] != " ":
        return True

    elif board[1] == board[4] == board[7] != " ":
        return True

    elif board[2] == board[5] == board[8] != " ":
        return True

    # Check diagonals
    elif board[0] == board[4] == board[8] != " ":
        return True

    elif board[2] == board[4] == board[6] != " ":
        return True

    else:
        return False


# Check draw

def check_draw():
    if " " not in board:
        return True
    return False


# Main game

def play_game():

    player = "X"

    while True:

        display_board()

        position = int(input("Enter position (1-9): "))

        if position < 1 or position > 9:
            print("Invalid position! Enter 1-9")
            continue

        if board[position - 1] != " ":
            print("Position already occupied!")
            continue

        board[position - 1] = player

        # Check winner
        if check_position():
            display_board()
            print(player, "won the game!")
            break

        # Check draw
        if check_draw():
            display_board()
            print("Match Draw!")
            break

        # Change player
        if player == "X":
            player = "O"
        else:
            player = "X"


play_game()
