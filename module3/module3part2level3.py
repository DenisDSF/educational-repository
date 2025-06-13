def changing_places(data_dict):
    temp_dict = {}
    for key, value in data_dict.items():
        temp_dict[value] = key
    return temp_dict


data_dict = {
    'name1': 'id1',
    'name2': 'id2',
    'name3': 'id3'
}
data_dict = changing_places(data_dict)

print('Словарь с поменявшимися местами ключами и значениями:')
for key in data_dict:
    print(key, data_dict[key])