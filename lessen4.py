# Простой словарь флагов: страна и её цвета
flags = {
    'ru': {'red', 'blue', 'white'},
    'kg': {'red', 'yellow'},
    'ua': {'blue', 'yellow'},
    'uk': {'blue', 'yellow'},
    'kz': {'blue', 'yellow'},
    'us': {'red', 'white', 'blue'},
    'de': {'black', 'red', 'yellow'},
    'fr': {'blue', 'white', 'red'}
}
print("Введите цвета флага через пробел (например: red yellow)")
print("Чтобы выйти, введите: выход")
while True:
    user_input = input("\nЦвета: ").strip().lower()
    if user_input == "выход":
        print("Выход из программы.")
        break
    input_colors = set(user_input.split())
    result = []
    for country, colors in flags.items():
        if input_colors.issubset(colors):
            result.append(country)
    if result:
        print("Подходящие домены:", ', '.join(result))
    else:
        print("Ничего не найдено.")
