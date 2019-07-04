test_list_1 = ['python', 'abc', 'efg', 'python', '1000', 'abc', 'abc']
print(test_list_1)

print('-----------------------------')

for i in test_list_1:
    print(i)

test_list_2 = []
print(test_list_2)

print('-------------------------------')
#要素の追加
test_list_2.append('python')
test_list_2.append('web')
test_list_2.append('aaaaa')
test_list_2.append('zzzzz')
print(test_list_2)

print('-------------------------------')
#インデックスを指定して追加
test_list_1.insert(1,',')
test_list_1.insert(3, '-')
print(test_list_1)

print('----------------------------------')
#要素の削除_1
test_list_1.remove('abc')
print(test_list_1)

print('----------------------------------')
#要素の削除_2
print(test_list_2.pop(3))
print(test_list_2)

print(test_list_2.pop())
print(test_list_2)

print('----------------------------------')
#要素のインデックスを取得
print(test_list_1.index('efg'))

print('----------------------------------')
#リスト内での要素数の取得
print(test_list_1.count('python'))