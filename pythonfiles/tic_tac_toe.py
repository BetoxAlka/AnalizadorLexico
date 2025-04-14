import math

class TicTacToe:
    def __init__(self):
        self.board = [" " for _ in range(9)]

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print("| " + " | ".join(row) + " |")

    def make_move(self, position, letter):
        if self.board[position] == " ":
            self.board[position] = letter
            return True
        return False

    def is_winner(self, letter):
        b = self.board
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # cols
            [0, 4, 8], [2, 4, 6]              # diags
        ]
        for cond in win_conditions:
            if all(b[i] == letter for i in cond):
                return True
        return False

    def is_draw(self):
        return " " not in self.board

    def empty_positions(self):
        return [i for i, spot in enumerate(self.board) if spot == " "]

    def minimax(self, is_maximizing):
        if self.is_winner("O"):
            return {"score": 1}
        elif self.is_winner("X"):
            return {"score": -1}
        elif self.is_draw():
            return {"score": 0}

        if is_maximizing:
            best = {"score": -math.inf}
            for pos in self.empty_positions():
                self.board[pos] = "O"
                score = self.minimax(False)
                self.board[pos] = " "
                score["position"] = pos
                if score["score"] > best["score"]:
                    best = score
            return best
        else:
            best = {"score": math.inf}
            for pos in self.empty_positions():
                self.board[pos] = "X"
                score = self.minimax(True)
                self.board[pos] = " "
                score["position"] = pos
                if score["score"] < best["score"]:
                    best = score
            return best

    def get_computer_move(self):
        if len(self.empty_positions()) == 9:
            return 0
        move = self.minimax(True)
        return move["position"]

    def play_game(self):
        print("Welcome to Tic Tac Toe!")
        self.print_board()

        while True:
            position = int(input("Choose your move (0-8): "))
            if self.make_move(position, "X"):
                if self.is_winner("X"):
                    self.print_board()
                    print("You win!")
                    break
                elif self.is_draw():
                    self.print_board()
                    print("It's a draw!")
                    break

                comp_move = self.get_computer_move()
                self.make_move(comp_move, "O")
                print("Computer moved:")
                self.print_board()

                if self.is_winner("O"):
                    print("Computer wins!")
                    break
                elif self.is_draw():
                    print("It's a draw!")
                    break
            else:
                print("Invalid move. Try again.")

if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
