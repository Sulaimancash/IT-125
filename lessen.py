data_types = ['hi', 12, True, 'db', 12.43, 'qwrty0', 'frend']
data_types2 = [12, 13]

#перемещение элементов из одного списка в другой 
data_types2.append(data_types.pop(-2))

#data_types2.extend(data_types)

print(data_types2)