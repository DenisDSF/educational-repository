data_list = [1, 4, 1, 6, 'hello', 'a', 5, 'hello', 1, 'hello']
intersections_list =[]
for i in data_list:
    if data_list.count(i) > 1 and i not in intersections_list:
        intersections_list.append(i)
print(intersections_list)