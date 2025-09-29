data_type = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
data_type = list(data_type)
letters = []
numbers = []
for i in data_type:
    if type(i) == str:
        letters.append(i)
    else:
        numbers.append(i)

data_type = list(data_type)

numbers.remove(6.13)

if True in numbers:
    numbers.remove(True)
    letters.append('True')
    
if 3 in numbers and 1 in numbers:
    index_1 = numbers.index(1)
    numbers.insert(index_1, 2)

numbers.sort()

letters.reverse()

letters = list("hello teacher") 

letters_tuple = tuple(letters)
numbers_tuple = tuple(numbers)

print("Слово:", ''.join(letters))
print("Кортеж letters:", letters_tuple)
print("Кортеж numbers:", numbers_tuple)


    