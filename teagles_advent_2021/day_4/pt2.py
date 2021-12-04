import sys

from .lib import BingoBoard, numerals_from_input


def main():
    game_input = sys.stdin.readlines()
    game_numbers = map(int, game_input[0].split(','))
    boards = []
    stream = iter(game_input[1:])
    while True:
        board = numerals_from_input(stream)
        if board:
            boards.append(BingoBoard(board))
        else:
            break
    for number in game_numbers:
        for board in boards.copy():
            result = board.play_numeral(number)
            if result:
                boards.remove(board)
                if not boards:
                    print(result)
                    return


if __name__ == '__main__':
    main()
