import random

plates_count = 15

def generate_path(length: int) -> list:
    right_path = [
        [random.choice(('■','=')) for _ in range(plates_count)],
    ]
    right_path.append(['■' if right_path[0][i] == '=' else '=' for i in range(plates_count)])
    return right_path

def print_path(path_to_print: list, now_plate: int) -> None:
    print()
    print(f"{''.join(list('  ' for _ in range(now_plate)))} ↓")
    print(f'={'='.join(path_to_print[0])}')
    print(f'={'='.join(path_to_print[1])}')
    print(f"{''.join(list('  ' for _ in range(now_plate)))} ↑")
    print()

def player_move(user_choice: int, now_plate: int, true_path: list) -> bool:
    result = True if '■' == true_path[user_choice][now_plate] else False
    return result

def main():
    # Видимый игроку путь
    current_path = [
        ['■' for _ in range(plates_count)],
        ['■' for _ in range(plates_count)],
    ]

    current_plate = 0
    lives_lost = 0
    dies = False
    right_path = generate_path(plates_count)

    print("\nДобро пожаловать в 'Стеклянный мост'!")
    while True:
        if current_plate == plates_count:
            print(f'\nПобеда! Для достижения успеха Вы убили всего лишь {lives_lost} человек! \nНа Ваш счёт Сбербанк зачислено +1.000.000$, поздравляем!')
            break
        print_path(current_path, current_plate)
        if dies:
            print('Неверно! Ещё один человек погиб по Вашей вине ツ')
            dies = False
        try:
            user_choice = int(input("На какую плиту прыгнуть (1 - верхняя, 2 - нижняя): ")) - 1
            if user_choice not in (0,1):
                print("Ошибка! Неверный ввод.")
                continue
        except ValueError:
            print("Ошибка! Неверный ввод.")
            continue
        if player_move(user_choice, current_plate, right_path):
            current_plate += 1
            continue
        else:
            current_plate += 1
            dies = True
            lives_lost += 1
            current_path[user_choice][current_plate-1] = '='
            continue

if __name__ == '__main__':
    main()
