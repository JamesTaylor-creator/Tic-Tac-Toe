import Board
import Player
class Game(object):
    def isWinner(board, letter):
        return (board[7] == letter and board[8] == letter and board[9] == letter) or (board[4] == letter and board[5] == letter and board[6] == letter) or(board[1] == letter and board[2] == letter and board[3] == letter) or(board[1] == letter and board[4] == letter and board[7] == letter) or(board[2] == letter and board[5] == letter and board[8] == letter) or(board[3] == letter and board[6] == letter and board[9] == letter) or(board[1] == letter and board[5] == letter and board[9] == letter) or(board[3] == letter and board[5] == letter and board[7] == letter)
    
    #Start the game
    def engine(board):
        print('Welcome to Tic Tac Toe!')
        Board.Board.print_board(board)

        while not(board.count(' ') < 1):
            if not(Game.isWinner(board, 'O')):
                Player.Player.player_movement(board)
                #Might cause a problem
                print(Board.Board.print_board(board))
            else:
                print('Sorry, Computer won this time!')
                break

            if not(Game.isWinner(board, 'X')):
                move = Player.Player.computer_movement(board)
                if move == 0:
                    print('Tie Game!')
                else:
                    board[move] = 'O'
                    print('Computer placed an \'O\' in position', move , ':')
                    print(Board.Board.print_board(board))
            else:
                print('You won this time! Good Job!')
                break

            if board.count(' ') > 1 == False:
                print('Tie Game!')

    
