data_tuple = ('h', 6.13, 'C', 'e', 'T', True, 'k', 'e', 3, 'e', 1, 'g')
letters = []
numbers = []
for a in data_tuple:
    if isinstance(a, str):
        letters.append(a)
    else:
        numbers.append(a)
numbers.pop(0)
deleted = numbers.pop(0)
letters.append(deleted)
numbers.insert(1, 2)
numbers.sort()
letters.reverse()
letters [1] = 'G'
letters [-2] = 'c'
numbers = [x**2 for x in numbers]
numbers_tuple = tuple(numbers)
letters_tuple = tuple(letters)
print(letters_tuple)
print(numbers_tuple)


