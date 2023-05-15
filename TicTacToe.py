# Initialize and reset game board
def resetBoard():
    board = [[' ']*3 for _ in range(3)]
    return board

# Display game board
def printBoard(board):
    print("\n     0   1   2")
    print("   " + "-" * 13)
    for i in range(3):
        print(f" {i} | {' | '.join(board[i])} |")
        print("   " + "-" * 13)

# Check that entry location is valid (check if row/col equals one of [0,1,2])
def validateEntry(row, col, board):
    if row not in ['0', '1', '2'] or col not in ['0', '1', '2'] or board[int(row)][int(col)] != ' ':
        return False
    return True

# Check if the game is over
def checkEnd(board, playerSymbol):
    for i in range(3):
        if all(board[i][j] == playerSymbol for j in range(3)) or all(board[j][i] == playerSymbol for j in range(3)):
            return True
    if board[0][0] == board[1][1] == board[2][2] == playerSymbol or board[0][2] == board[1][1] == board[2][0] == playerSymbol:
        return True
    return False

# Assign location with symbol placed
def placeSymbol(row, col, board, playerSymbol):
    board[int(row)][int(col)] = playerSymbol
    return board

# main function, simulates the game
def main():
    while True:
        print("New Game: X goes first.")
        board = resetBoard()
        printBoard(board)
        counter = 0
        proceed = True

        while proceed:
            playerSymbol = 'X' if counter % 2 == 0 else 'O'
            print(f"\n{playerSymbol}'s turn.")
            location = input("Where do you want your symbol placed?\nPlease enter row number and column number separated by a comma.\n")

            row, col = location.split(",")
            print("You have entered row #", row)
            print("          and column #", col)
            
		# Validate input
            if validateEntry(row, col, board):
                print("Thank you for your selection.")

                # update board
                board = placeSymbol(row, col, board, playerSymbol)

                # update counter
                counter = counter + 1

                # check if winner
                if checkEnd(board, playerSymbol):
                    print(f"{playerSymbol} IS THE WINNER!!!")
                    printBoard(board)
                    proceed = False
                else:
                    if counter >= 9:
                        print("DRAW! NOBODY WINS!")
                        proceed = False
                    else:
                        printBoard(board)
            else:
                print("Invalid Entry: try again.\nRow & column numbers must be either 0, 1, or 2.")
                proceed = True

        startNewGame = input("\nAnother game? Enter Y or y for yes.\n")
        if startNewGame.lower() != "y":
            break

    print("Thank you for playing!")

if __name__ == "__main__":
    main()


           
