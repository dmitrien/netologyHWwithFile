from pprint import pprint
#Задание№1
with open('file_1.txt', 'rt', encoding='utf-8') as file:
    cook_book = {}
    for txt in file:
        reception_name = txt.strip()
        line_count = int(file.readline())
        dish = []
        for _ in range(line_count):
            name, count, type_count = file.readline().strip().split(' | ')
            dish.append({"indigrient": name,
                         "quantity": count,
                         "measure": type_count})
        file.readline()
        cook_book[reception_name] = dish
    # pprint(cook_book, sort_dicts = False)

# #Задание№2
def get_shop_list_by_dishes(dishes, person_count = 1):
    product_dict = {}
    for dish in dishes:
        dish_indigrient = cook_book.get(dish)
        for indigrient in dish_indigrient:
            sum_count = int(indigrient.get('quantity')) * person_count
            poftor = indigrient.get('indigrient')
            if poftor in product_dict.keys():
                sum_count = int(product_dict.get(poftor).get('quantity')) + sum_count
            indigrient['quantity'] = sum_count
            product_dict[indigrient.pop('indigrient')] = indigrient

    return pprint(product_dict, sort_dicts = False)

get_shop_list_by_dishes(['Фахитос', 'Омлет'], 2)

#Задание3
def sorted_files():
    count_lines = {}
    with open('1.txt', 'rt', encoding='utf-8') as file_1:
        text_1 = file_1.readlines()
        info_text_1 = {}
        info_text_1[file_1.name] = text_1
        lines_text_1 = len(text_1)
        count_lines[lines_text_1] = info_text_1
    with open('2.txt', 'rt', encoding='utf-8') as file_2:
        text_2 = file_2.readlines()
        info_text_2 = {}
        info_text_2[file_2.name] = text_2
        lines_text_2 = len(text_2)
        count_lines[lines_text_2] = info_text_2
    with open('3.txt', 'rt', encoding='utf-8') as file_3:
        text_3 = file_3.readlines()
        info_text_3 = {}
        info_text_3[file_3.name] = text_3
        lines_text_3 = len(text_3)
        count_lines[lines_text_3] = info_text_3

    return count_lines

def created_sort_file():
    with open('sorted_text.txt', 'w', encoding='utf-8') as sort_file:
        for i in sorted(sorted_files().keys()):
            file_name = "".join(list(sorted_files().get(i).keys()))
            sort_file.write(file_name)
            sort_file.write('\n')
            sort_file.write(str(i))
            sort_file.write('\n')
            sort_file.write("".join(list(sorted_files().get(i).get(file_name))))
            sort_file.write('\n')

created_sort_file()




