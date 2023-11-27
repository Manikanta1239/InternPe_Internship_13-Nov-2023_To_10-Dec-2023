import random

class TicTacToe:
    def __init__(self):
        self.board = []

    def creat_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('~')
            self.board.append(row)

    def get_random_first_player(self):
        return random.randint(0, 1)
    
    def fix_loc(self, row, column, player):
        self.board[row][column] = player

    def is_player_win(self, player):
        win = None

        n = len(self.board)

        #checking the rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win
            
        #checking the column
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win
            
        #checking for the diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win
        
        win = True
        for i in range(n):
            if self.board[i][n-1-i] != player:
                win = False
                break
        if win:
            return win
        return False
    
        for row in self.board:
            for item in row:
                if item == '~':
                    return False
        return True
    
    def is_board_filled(self):
        for row in self.board:
            for item in row:
                if item == '~':
                    return False
        return True
    
    def swap_player_turn(self, player):
        return 'X' if player == 'O' else 'O'
    
    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()
    
    def start(self):
        self.creat_board()

        player = 'X' if self.get_random_first_player() == 1 else 'O'
        while True:
            print(f"Player {player} turn")
            self.show_board()

            #taking the user's input
            row, column = list(
                map(int, input("Enter the Row & Column number to fix location:").split())
            )
            print()

            #fixing the location
            self.fix_loc(row-1,column-1,player)

            #checking whether the current player is won or not
            if self.is_player_win(player):
                print(f"Player {player} wins the game !...")
                break

            #checking whether the game is drawn or not
            if self.is_board_filled():
                print("Match tie \n Run and play again..")
                break

            #swapping the turn
            player = self.swap_player_turn(player)

        #showing the view of board finally
        print()
        self.show_board()

#starting the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()