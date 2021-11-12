key_list = ['name', 'age', 'address', 'Nationality']
value_list = ['Victor', '19', 'Rio de Janeiro', 'Brazilian']

def CreatorDict(key_list, value_list):
    dict_from_list = dict(zip(key_list, value_list))
    print(dict_from_list)
CreatorDict(key_list, value_list)