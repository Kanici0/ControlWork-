Geeks = {
    'address': 'Toktogula 175',
    'courses': ['Android', 'Backend', 'Frontend'],
    'bag': {'fails', 'errors', 'stack'}
}
Geeks.pop('bag')
Geeks['address'] = 'Ибраимова 103/1'
Geeks['phone '] = ' 996777123456'
Geeks['instagram '] = ' @geeks.edu'
Geeks1 = ['UX/UI', ' KMM', "1C"]
Geeks['courses'] = list(str(Geeks['courses'] + Geeks1))
Geeks['data_of_foundation  '] = '2018'
print(f'количество курсов: {len('courses')}')
for key, value in Geeks.items():
    print(f'{key}: {value}')
