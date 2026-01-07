def get_book_text(path):
    with open(path) as f:
        return f.read()

def words_count(path):
    return get_book_text(path).split()

def chara_count(path):
    cha_count = {}
    lower_case = get_book_text(path).lower()
#    print(lower_case)
    lower_case_list = list(lower_case)
#    print(lower_case_list)
    for chara in lower_case_list:
        if chara not in cha_count:
            cha_count[chara] = 1
        else:
            cha_count[chara] += 1
    return cha_count

def dict_to_list(dict):
    list_sort = []
    for chara in dict:
        temp_dict = {}
        temp_dict["chara"] = chara
        temp_dict["num"] = dict[chara]
        list_sort.append(temp_dict)
    return list_sort

def sort_on(items):
    return items["num"]

