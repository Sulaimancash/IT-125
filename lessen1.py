data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')

letters = []
numbers = []

for item in data_tuple:
    if isinstance(item, str):
        letters.append(item)
    else:
        numbers.append(item)

if 6.13 in numbers:
    numbers.remove(6.13)

if True in numbers:
    numbers.remove(True)
    letters.append('True')

if 3 in numbers and 1 in numbers:
    index_1 = numbers.index(1)
    numbers.insert(index_1, 2)

numbers.sort()

letters.reverse()

letters[0] = 'H' 
letters[1] = 'i'  

word = ''.join(letters)
print("Слово из букв:", word)

letters_tuple = tuple(letters)
numbers_tuple = tuple(numbers)

print("Кортеж letters:", letters_tuple)
print("Кортеж numbers:", numbers_tuple)
