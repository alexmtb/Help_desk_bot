lst_in = ['Муму', 'Евгений Онегин', 'Сияние', 'Мастер и Маргарита', 'Пиковая Дама', 'Колобок']

# здесь продолжайте программу (используйте список lst_in)
i = 0
while i < len(lst_in):
    if len(lst_in[i].split()) > 1:
        del lst_in[i]

    i += 1

print(*lst_in)
