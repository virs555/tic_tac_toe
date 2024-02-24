import random
board_status = [[None,None,None], 
                [None,None,None], 
                [None,None,None]]

def who_first() -> list:
    result = random.choice(['human', 'pc'])
    if result == 'pc':
        return ['o', 'x']
    else:
        return ['x', 'o']

def coordinates_handler(raw_coordinates: str) -> list[int]:
    coordinates = [int(i) for i in raw_coordinates.split(' ')]
    return coordinates

def is_empty(coordinates: list, board_status: list) -> bool:
    return board_status[coordinates[0]][coordinates[1]]

def move(board_status: list, coordinates: list, sign: str) -> list[list]:
    board_status[coordinates[0]][coordinates[1]] = sign
    print('  0','  1','  2')
    for i, j in enumerate(board_status):
        print(i,j)
    return board_status

def pc_move_choice(board_status: list) -> list[int]:
    
    a = random.choice([i for i, j in enumerate(board_status) if None in j])
    b = random.choice([i for i, j in enumerate(board_status[a]) if j is None])
    print(f'Ход соперника: {a, b}')
    return [a, b]

def is_win(board_status: list) -> bool:
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
    draw = 0
    for i in [c0, c1, c2 , r0, r1, r2, d0, d1]:
        if None in i:
            draw += 1
    if draw == 0:
        return True
    return False



game = True
human_sign, pc_sign = who_first()
if human_sign == 'o':
    first_step_skip_flag = True
else:
    first_step_skip_flag = False

while True:
    if not first_step_skip_flag:
        raw_coordinates = input("Введите 2 координаты через пробел: ")
        coordinates = coordinates_handler(raw_coordinates)
        if is_empty(coordinates, board_status):
            print('Поле уже занято')
            continue
        board_status = move(board_status, coordinates, human_sign)
    if is_win(board_status):
        print('Конец игры')
        break
    board_status = move(board_status, pc_move_choice(board_status), pc_sign)
    if is_win(board_status):
        print('Конец игры')
        break
    first_step_skip_flag = False


