import random

rock = 'камень, к'
scissor = 'ножницы, н'
paper = 'бумага, б'

list = [rock, scissor, paper]

player_win = 0
pc_win = 0
draw = 0

rounds = int(input("🔥 Йо, это СУЛИФА-батл! Сколько раундов замутим? "))

for i in range(1, rounds + 1):
    pc = random.choice(list)
    player = input('👉 Твой ход: ' )
    
    if (pc == rock and player == 'камень, к') or (pc == scissor and player == 'ножницы, н') or (pc == paper and player == 'бумага, б'):
        print('😐 Ничья… так себе замес.')
        draw += 1
    
    elif (pc == scissor and player == 'камень, к') or (pc == paper and player == 'ножницы, н') or (pc == rock and player == 'бумага, б'):
        print('🔥 Раунд твой!')
        player_win += 1
    
    elif (pc == paper and player == 'камень, к') or (pc == rock and player == 'ножницы, н') or (pc == scissor and player == 'бумага, б'):
        print('💀 Компьютер тебя уделал… , это фиаско братан!')
        pc_win += 1
    else:
        print('Сходи к окулисту')
        
if player_win > pc_win:
    print('🏆 Поздравляю, ты чемпион! Машина в шоке от твоей мощи.')
    
elif player_win < pc_win:
    print('🤖 Компьютер победил! Восстание машин уже близко...')
    
elif player_win == pc_win:
    print('😐 Ничья. Ну, по крайней мере, никто не позорился.')
