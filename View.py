import Game
class View(object):
    
    def play():
        while True:
            answer = input('Do you want to play? (Y/N)')
            if answer.lower() == 'y' or answer.lower == 'yes':
                _board = [' ' for x in range(10)]
                print('-----------------------------------')
                Game.Game.engine(_board)
            else:
                break





