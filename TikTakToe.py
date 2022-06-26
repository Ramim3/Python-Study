import os

board = ["-","-","-",
         "-","-","-",
         "-","-","-",]

menu_answers = {"1": "statistic", "2": "Playgame"}

game_working = True

#players score
x_stats = 0
o_stats = 0
winner = None
current_player = "x"



def show_board():
    print(board[0] + "│" + board[1] + "│" + board[2])
    print(board[3] + "│" + board[4] + "│" + board[5])
    print(board[6] + "│" + board[7] + "│" + board[8])


def show_menu():
    os.system('cls')
    print("Hello And Welcome To 'Tic Tac Toe' Game")
    print("            ___MENU___                ")
    print("        1. Show statistic            ")
    print("        2. Play the game\n           ")

    answer = get_answer()
    while not answer:
        print("Please pick the right option")
        answer = get_answer()
    return answer

def get_answer():
    answer = input("Your choise: ")
    return  menu_answers.get(answer)

def main():
    answer = show_menu()
    if answer == "statistic":
        show_statistics()
    else:
        play_game()


def show_statistics():
    print("********************")
    print("   ((statistics))   ")
    print("********************")
    print("Player O's Score Is" + " " + str(o_stats) + " " + "Point's")
    print("Player X's Score Is" + " " + str(x_stats) + " " +  "Point's")
    

    
    

def play_game():
    global x_stats, o_stats

    show_board()

    while game_working:

      player_turn(current_player)
      end_game()
      change_player()

    if winner == "x":
        x_stats+= 1
        print("'X' Has Won The Game !!! ")
    elif winner == "o":
        o_stats += 1
        print("'O' Has Won The Game !!! ")
    elif winner == None:
        print("Its A Tie, Good Luck Next Time")
    score_score()
    show_statistics()
   


def player_turn(player):
    print(player +"'s turn")
    position = input("Pick a position from 1-9")

    if position not in ["1","2","3","4","5","6","7","8","9"]:
        position = input("please pick a postion only from 1-9")
    position = int(position) - 1

    if board[position] == "-":
        print("choose another position")
    board[position]= player
    show_board()


def end_game():
    game_winner()
    tie_no_win()


def game_winner():
    global winner
    row_winner = row_win()
    column_winner = column_win()
    diagonal_winner = axis_win()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
        #no win
    return


def row_win():
    global game_working
    first_row = board[0] == board[1] == board[2] != "-"
    second_row = board[3] == board[4] == board[5] != "-"
    third_row = board[6] == board[7] == board[8] != "-"

    if first_row or second_row or third_row:
        game_working = False
    #return winner
    if first_row:
        return board[0]
    elif second_row:
        return board[3]
    elif third_row:
        return board[6]
    return


def column_win():
    global game_working
    first_col = board[0] == board[3] == board[6] != "-"
    seccond_col = board[1] == board[4] == board[7] != "-"
    third_col = board[2] == board[5] == board[8] != "-"
    if first_col or seccond_col or third_col:
        game_working = False

    if first_col:
        return board[0]
    elif seccond_col:
        return board[1]
    elif third_col:
        return board[2]
    return
   

def axis_win():
    global game_working
    first_axis = board[0] == board[4] == board[8] != "-"
    second_axis = board[6] == board[4] == board[2] != "-"
    if first_axis or second_axis:
        game_working = False
    
    if first_axis:
        return board[0]
    elif second_axis:
        return board[6]
    return
    
    
def tie_no_win():
    global game_working
    if "-" not in board:
        game_working = False
    return


def change_player():
    global current_player
    if current_player == "x":
        current_player = "o"
    elif current_player == "o":
        current_player ="x"
        return

def score_score():
    file = open("score.txt","a")
    file.write(str(score_score))
    file.close()   
    while True:
        change_player()
        print("Player O's Score Is" + " " + str(o_stats) + " " + "Point's")
        print("Player X's Score Is" + " " + str(x_stats) + " " +  "Point's")
        return
    

if __name__ == '__main__':
    main()
    

        

	