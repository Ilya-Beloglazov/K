#Здравствуйте , это ученик Илья Белоглазов PDEF-35 / Раздел введение в Python/ ИТОГОВОЕ ЗАДАНИЕ .крестики-нолики
#Кол-во клеток
board_size=3
# Игровое поле (клетки )
board=[1,2,3,4,5,6,7,8,9]
def draw_board():
    """Вывод игрового поля """
    print("_"* 4 * board_size)
    for i in range(board_size):
        print((" " * 3 + "|" )*3)
        print("", board[i*3], "|", board[1+i*3],"|",board[2+i*3], "|")
        print(("_"*3+"|")*3)
    pass

def game_step(index, char):
    """Выполняем ход"""
    if (index>9 or index<1 or board[index-1] in ("X","O")):
        return False

    board[index - 1]=char
    return True

def check_win():
    '''Проверяем победу одного из игроков '''
    win=False

    win_combination=(
        (0,1,2),(3,4,5),(6,7,8), # горизонтальные линии
        (0,3,6),(1,4,7),(2,5,8), # вертикальные линии
        (0,4,8),(2,4,6)          # диагональные линии
    )
    for pos in win_combination:
        if(board[pos[0]]== board [pos[1]] and board[pos[1]]== board [pos[2]]):
            win=board[pos[0]]

    return win

def start_game():
    current_player="X"
    #номер шага
    step=1
    draw_board()

    while (step<=9) and (check_win()==False):
        index=int(input("Ходит игрок " + current_player + " . Введите номер поля (0 - выход):"))

        if(int(index)==0):
            break

        #Если получилось сделать шаг
        if (game_step(int(index), current_player)):
            print("Ход")

            if (current_player=="X"):
                current_player="O"
            else:
                current_player="X"

            draw_board()
            #увеличиваем номер хода
            step += 1
        else:
            print("Неверный ход ! Пожалуйста, повторите попытку ")
    if (step ==10 ):
        print("Ничья")
    else:
        print("Выиграл" + check_win())

print("Добро пожаловать в игру")
start_game()
input()