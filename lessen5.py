flags = {
    'ru': {'red blue', 'white'},
    'kg': {"red yellow", 'red'},
    'ua': {"red blue", 'red', 'blue'},
    'uk': {"yellow", "blue"},
    'kz': {'blue yellow', 'blue'}
}
flags['us'] = {'red', 'white', 'blue'}
flags['de'] = {'black', 'red', 'yellow'}
flags['fr'] = {'blue', 'white', 'red'}

print("Введите цвета флагов через пробел (например: red yellow)")
print("Для выхода введите: выход")

while True:
    user_input = input("\nЦвета: ").strip().lower()
    
    if user_input == "выход":
        print("Выход из программы.")
        break

    input_colors = set(user_input.split())

    matching_domains = []

    for domain, colors in flags.items():
        all_colors = set()
        for color_str in colors:
            all_colors.update(color_str.split())

        if input_colors.issubset(all_colors):
            matching_domains.append(domain)

    if matching_domains:
        print("Подходящие домены:", ', '.join(matching_domains))
    else:
        print("Нет подходящих доменов.")
