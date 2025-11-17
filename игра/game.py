from player import Player, Computer
from exceptions import InvalidMoveException

def play_game():
    player_win = 0
    pc_win = 0
    draw = 0

    rounds = int(input("🔥 Йо, это СУЛИФА-батл! Сколько раундов замутим? "))

    player = Player("Игрок")
    computer = Computer()

    for i in range(1, rounds + 1):
        pc_move = computer.make_move()
        try:
            player_move = player.make_move()
        except InvalidMoveException as e:
            print(e)
            continue

        print(f'Компьютер выбрал: {pc_move}')

        if pc_move == player_move:
            print('😐 Ничья… так себе замес.')
            draw += 1
        elif (pc_move == 'ножницы' and player_move == 'камень') \
             or (pc_move == 'бумага' and player_move == 'ножницы') \
             or (pc_move == 'камень' and player_move == 'бумага'):
            print('🔥 Раунд твой!')
            player_win += 1
        else:
            print('💀 Компьютер тебя уделал… , это фиаско братан!')
            pc_win += 1

    # Финальный результат
    if player_win > pc_win:
        print('🏆 Поздравляю, ты чемпион! Машина в шоке от твоей мощи.')
    elif player_win < pc_win:
        print('🤖 Компьютер победил! Восстание машин уже близко...')
    else:
        print('😐 Ничья. Ну, по крайней мере, никто не позорился.')
