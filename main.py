import random

class Board:
    def __init__(self) -> None:
        self.status: list[list[str | None]] = [
            [None,None,None], 
            [None,None,None], 
            [None,None,None],
        ]
        self.empty_fields = {(0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)}

    def move(self, coordinates: tuple[int, int], sign: str) -> None:
        row, col = coordinates
        self.status[row][col] = sign
        self.empty_fields.remove((row, col))
   
    def is_draw(self) -> bool:
        if len(self.empty_fields) == 0:
            return True
        return False


def draw_board() -> None:
    print('  0','  1','  2')
    for i, j in enumerate(board.status):
        print(i,j)

def who_first() -> tuple[str, str]:
    result = random.choice(('human', 'pc'))
    if result == 'pc':
        return 'o', 'x'
    else:
        return 'x', 'o'


def get_user_coordinates(board_status):
    field_not_empty = True
    coordinates = ()
    while field_not_empty:
        raw_coordinates = input('Введите 2 координаты через пробел: ')
        try:
            coordinates = coordinates_handler(raw_coordinates)
        except ValueError:
            print('Нужны два числа через пробел, например: 0 1')
            continue
        if not is_empty(coordinates, board_status):
            print('Поле уже занято')
        else:
            field_not_empty = False
    return coordinates

def coordinates_handler(raw_coordinates: str) -> tuple[int, int]:
    row, col = [int(i) for i in raw_coordinates.split(' ')]
    if row < 3 and col < 3:
        return row, col
    raise ValueError

def is_empty(coordinates: tuple[int, int], board_status: list) -> bool:
    row, col = coordinates
    if board_status[row][col]:
        return False
    return True


def pc_move_choice(board_status: list) -> tuple[int, int]:
    
    a = random.choice([i for i, j in enumerate(board_status) if None in j])
    b = random.choice([i for i, j in enumerate(board_status[a]) if j is None])
    print(f'Ход соперника: {a, b}')
    return a, b

def is_win(board_status: list[list[str | None]]) -> bool:
    c0 = set([i[0] for i in board_status])
    c1 = set([i[1] for i in board_status])
    c2 = set([i[2] for i in board_status])
    r0 = set(board_status[0])
    r1 = set(board_status[1])
    r2 = set(board_status[2])
    d0 = set([board_status[i][i] for i in range(3)])
    d1 = set([board_status[i][j] for i, j in enumerate(reversed(range(3)))])
    for i in [c0, c1, c2 , r0, r1, r2, d0, d1]:
        if len(i) == 1 and None not in i:
            return True
    return False



human_sign, pc_sign = who_first()
if human_sign == 'o':
    first_step_skip_flag = True
else:
    first_step_skip_flag = False

board = Board()
stop_game = False

while not stop_game:
    if not first_step_skip_flag: 
        coordinates = get_user_coordinates(board.status)
        board.move(coordinates, human_sign)
        draw_board()
    if is_win(board.status) or board.is_draw():
        print('Конец игры')
        stop_game = True
        break
    board.move(pc_move_choice(board.status), pc_sign)
    draw_board()
    if is_win(board.status) or board.is_draw():
        print('Конец игры')
        stop_game = True
        break
    first_step_skip_flag = False



