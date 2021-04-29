import Game
class Player(object):
    _move = int()

    #Setter
    def set_move(move):
        self._move = move

    #Getter
    def get_move():
        return self._move

    #Player keeps up with its own movement
    def player_movement(board):
        run = True
        while run:
            move = input('Please select a position to place an \'X\' (1-9): ')
            try:
                move = int(move)
                if move > 0 and move < 10:
                    run = False
                    board[move] = 'X'
                    #if Player.spaceIsFree(move):    
                    #else:
                        #print('Sorry, this space is occupied!')
                else:
                    print('Please type a number within the range!')
            except:
                print('Please type a number!')
    
    #Computer keeps up with its movement
    def computer_movement(board):
        possibleMoves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
        move = 0

        for let in ['O', 'X']:
            for i in possibleMoves:
                boardCopy = board[:]
                boardCopy[i] = let
                if Game.Game.isWinner(boardCopy, let):
                    move = i
                    return move

        cornersOpen = []
        for i in possibleMoves:
            if i in [1,3,7,9]:
                cornersOpen.append(i)
            
        if len(cornersOpen) > 0:
            move = Player.selectRandom(cornersOpen)
            return move

        if 5 in possibleMoves:
            move = 5
            return move

        edgesOpen = []
        for i in possibleMoves:
            if i in [2,4,6,8]:
                edgesOpen.append(i)
            
        if len(edgesOpen) > 0:
            move = selectRandom(edgesOpen)
        
        return move

    def spaceIsFree(pos):
        return board[pos] == ' '

    def selectRandom(li):
        import random
        ln = len(li)
        r = random.randrange(0,ln)
        return li[r]