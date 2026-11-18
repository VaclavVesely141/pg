from abc import ABC, abstractmethod


class Piece(ABC):
    def __init__(self, color, position):
        
        self.__color = color
        self.__position = position

    @abstractmethod
    def possible_moves(self):
        
        pass

    @staticmethod
    def is_position_on_board(position):
        return 1 <= position[0] <= 8 and 1 <= position[1] <= 8

    @property
    def color(self):
        return self.__color

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, new_postion):
        self.__position = new_postion

    def __str__(self):
        return f'Piece({self.color}) at position {self.position}'


class Pawn(Piece):
    def possible_moves(self):
        row, col = self.position

        if self.color == "white":
            move = (row + 1, col)
        elif self.color == "black":
            move = (row - 1, col)
        else:
            return []

        if self.is_position_on_board(move):
            return [move]
        return []

    def __str__(self):
        return f'Pawn({self.color}) at position {self.position}'


class Knight(Piece):
    def possible_moves(self):
        
        row, col = self.position
        moves = [
            (row + 2, col + 1), (row + 2, col - 1),
            (row - 2, col + 1), (row - 2, col - 1),
            (row + 1, col + 2), (row + 1, col - 2),
            (row - 1, col + 2), (row - 1, col - 2)
        ]

        final_moves = []
        for move in moves:
            if self.is_position_on_board(move):
                final_moves.append(move)
        return final_moves

    def __str__(self):
        return f'Knight({self.color}) at position {self.position}'


class Bishop(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []

        for direction_row, direction_col in [
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]:
            for step in range(1, 8):
                move = (
                    row + direction_row * step,
                    col + direction_col * step
                )
                if self.is_position_on_board(move):
                    moves.append(move)
                else:
                    break

        return moves

    def __str__(self):
        return f'Bishop({self.color}) at position {self.position}'


class Rook(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []

        for direction_row, direction_col in [
            (1, 0), (-1, 0), (0, 1), (0, -1)
        ]:
            for step in range(1, 8):
                move = (
                    row + direction_row * step,
                    col + direction_col * step
                )
                if self.is_position_on_board(move):
                    moves.append(move)
                else:
                    break

        return moves

    def __str__(self):
        return f'Rook({self.color}) at position {self.position}'


class Queen(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []

        directions = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]

        for direction_row, direction_col in directions:
            for step in range(1, 8):
                move = (
                    row + direction_row * step,
                    col + direction_col * step
                )
                if self.is_position_on_board(move):
                    moves.append(move)
                else:
                    break

        return moves

    def __str__(self):
        return f'Queen({self.color}) at position {self.position}'


class King(Piece):
    def possible_moves(self):
        row, col = self.position
        moves = []

        for direction_row in (-1, 0, 1):
            for direction_col in (-1, 0, 1):
                if direction_row == 0 and direction_col == 0:
                    continue

                move = (row + direction_row, col + direction_col)
                if self.is_position_on_board(move):
                    moves.append(move)

        return moves

    def __str__(self):
        return f'King({self.color}) at position {self.position}'


if __name__ == "__main__":
    piece = Knight("black", (1, 2))
    print(piece)
    print(piece.possible_moves())
