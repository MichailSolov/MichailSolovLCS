cook_book_d = {}
cook_book_i_a = []
save_name = ''


def cook_bool_i(setup):
    cook_book_i_a.append(dict(zip(['ingredient_name', 'quantity', 'measure'], setup)))
    return cook_book_i_a


def get_shop_list_by_dishes(dishes, person_count):
    shop_list_by_dishes = {}
    for j in dishes:
        for i in cook_book_d[j]:
            if i['ingredient_name'] not in shop_list_by_dishes:
                shop_list_by_dishes[i['ingredient_name']] = \
                    {'measure': i['measure'], 'quantity': int(i['quantity']) * person_count}
            else:
                shop_list_by_dishes[i['ingredient_name']]['quantity'] += int(i['quantity']) * person_count
    return shop_list_by_dishes


with open("txt", 'r', encoding="utf-8") as RBook:
    s = RBook.readline()

    while s:
        if '|' in s:
            v = s.rstrip().split(' | ')
            cook_bool_i(v)

        elif s != '\n' and not s.rstrip().isdigit():
            cook_book_d[s.strip()] = None
            save_name = s.strip()

        elif s:
            cook_book_d[save_name] = cook_book_i_a
            cook_book_i_a = []

        s = RBook.readline()

        if not s:
            break


print(get_shop_list_by_dishes(['Запеченный картофель', 'Запеченный картофель1'], 2))
