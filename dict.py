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

print('----------------------------------')
#要素の追加
test_dict_2 = {}
test_dict_2['YEAR'] = '2017'
test_dict_2['MONTH'] = '3'
test_dict_2['DAY'] = '19'
print(test_dict_2)

print('----------------------------------')
#要素の削除
del test_dict_1['MONTH']
print(test_dict_1)

print('----------------------------------')
#keyやvalueだけを取得する
print(test_dict_2.keys())
print(test_dict_2.values())

print('----------------------------------')
#keyとvalueの同時取得
for key, value in test_dict_2.items():
    print(key, value)

print('----------------------------------')
#keyを保持しているか確認
print('YEAR' in test_dict_2)
print('YEARS' in test_dict_2)