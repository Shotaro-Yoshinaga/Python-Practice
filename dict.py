test_dict_1 = {'YEAR':'2015', 'MONTH':'4', 'DAY':'6'}
print(test_dict_1)
print('========================')

for i in test_dict_1:
    print(i)
    print(test_dict_1[i])
    print('------------------')

print(test_dict_1['YEAR'])

print('----------------------------------')
#keyの取得→valueの取得
print(test_dict_1.get('YEAR'))
print(test_dict_1.get('YEARS'))

print('----------------------------------')
#valueの取得
print(test_dict_1.get('YEAR', 'NOT FOUND'))
print(test_dict_1.get('YEARS', 'NOT FOUND'))