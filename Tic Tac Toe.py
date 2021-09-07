#create a tic tac toe game using the numpad as the board

from random import randint

#this is for the greetings of the user

player1 = input("Please enter player 1 name here: ")
player2 = input("Please enter player 2 name here: ")

print("Welcome players " + player1 + " and " + player2)

#this is for the roll of the players who will determine who is X or O

play = ["X", "Y"]

roll = play[randint(0, 1)]

if roll == "X":
    X = player1  #this will set the player 1 to Y if the roll is X
    print(player1 + " should take X")
elif roll == "Y":
    Y = player2 #this will set the player 2 to Y if the roll is Y
    print(player2 + " should take X")


#create a dictionary of the numpad because of {key: value} pairs

board = {"7": " " , "8": " " , "9": " ",
         "4": " " , "5": " " , "6": " ",
         "1": " " , "2": " " , "3": " " }

board_keys = [] #empty array

for key in board: #defining of the keys in the numpad

    board_keys.append(key) #appending of the keys

#defining the printboard(), we are using the printboard() to print the board that is updated everytime

def printboard(board): #this will be printed repeatedly
    print(board["7"] + "|" + board["8"] + "|" + board["9"])
    print("-+-+-")
    print(board["4"] + "|" + board["5"] + "|" + board["6"])
    print("-+-+-")
    print(board["1"] + "|" + board["2"] + "|" + board["3"])

#this is the main function of the game, this will verify if the input from the player is valid or not

def game():

    turn = "X" #this is for the move X, and this is the primary move
    count = 0 #this is the start of the count

    for i in range(10):
        printboard(board) #this will print the board repeatedly
        print("Its your turn, " + turn + " at which place?")

        move = input() #this is for the input of the user

        if board[move] == " ": #empty strings to accept the X or O input

            board[move] = turn #this means that if the user enter the X character

            count += 1 #this will increase the count

        else:
            print("the place is already filled, move to which place? ")
            continue

#this is for the conditions of the X or O has won in 5 moves

        if count >= 5: #this is for the total moves

            if board["7"] == board["8"] == board["9"] != "": #this is for the top layer
                printboard(board)
                #this is for declaring the winner
                if roll == "X":
                    print("GAME OVER! " + player1 + " wins!")
                elif roll == "Y":
                    print("GAME OVER! " + player2 + " wins!")
                break #to stop the loop

            elif board["4"] == board["5"] == board["6"] != "": #this is for the middle layer
                printboard(board)
                # this is for declaring the winner
                if roll == "X":
                    print("GAME OVER! " + player1 + " wins!")
                elif roll == "Y":
                    print("GAME OVER! " + player2 + " wins!")
                break  # to stop the loop

            elif board["1"] == board["2"] == board["3"] != "": #this is for the bottom layer
                printboard(board)
                # this is for declaring the winner
                if roll == "X":
                    print("GAME OVER! " + player1 + " wins!")
                elif roll == "Y":
                    print("GAME OVER! " + player2 + " wins!")
                break  # to stop the loop

            elif board["1"] == board["4"] == board["7"] != "": #this is for the left vertical layer
                printboard(board)
                # this is for declaring the winner
                if roll == "X":
                    print("GAME OVER! " + player1 + " wins!")
                elif roll == "Y":
                    print("GAME OVER! " + player2 + " wins!")
                break  # to stop the loop

            elif board["2"] == board["5"] == board["8"] != "": #this is for the vertical mid layer
                printboard(board)
                # this is for declaring the winner
                if roll == "X":
                    print("GAME OVER! " + player1 + " wins!")
                elif roll == "Y":
                    print("GAME OVER! " + player2 + " wins!")
                break  # to stop the loop

            elif board["3"] == board["6"] == board["9"] != "": #this is for the right vertical layer
                printboard(board)
                # this is for declaring the winner
                if roll == "X":
                    print("GAME OVER! " + player1 + " wins!")
                elif roll == "Y":
                    print("GAME OVER! " + player2 + " wins!")
                break  # to stop the loop

            elif board["1"] == board["5"] == board["9"] != "": #this is for diagonal
                printboard(board)
                # this is for declaring the winner
                if roll == "X":
                    print("GAME OVER! " + player1 + " wins!")
                elif roll == "Y":
                    print("GAME OVER! " + player2 + " wins!")
                break  # to stop the loop

            elif board["3"] == board["5"] == board["7"] != "": #this is for the diagonal
                printboard(board)
                # this is for declaring the winner
                if roll == "X":
                    print("GAME OVER! " + player1 + " wins!")
                elif roll == "Y":
                    print("GAME OVER! " + player2 + " wins!")
                break  # to stop the loop

#this is if neither X or O wins and the board is full

        if count == 9: #if the 9 tiles is filled

            print("GAME OVER! ITS A TIE!")

#this is for the change of play per move

        if turn == "X": #this if the first player is X
            turn ="O"

        else: #otherwise if the first player is O
            turn = "X"


    restart = input("do you want to play again?(y/n): ")

    if restart == "y" or restart == "Y": #this is for the input of the user
        for key in board_keys:

            board[key] = " "


        game()

if __name__ == "__main__": #this is for the call function of the game
    game()



















