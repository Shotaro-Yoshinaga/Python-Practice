def test_func_1(*args):
    print(args)

def test_func_2(code, name, *age):
    print(code, name)
    print(age)

def test_func(code_1, name_1, kana_1, *age, **keyword):
    print(code_1, name_1, kana_1)
    print(age)
    print(keyword)

test_func_1(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
test_func_2(200, 'python', 'ABC', 'EFG')
test_func(1000, 'pyhon', 'pyton2', 'pyhon3', email = 'abcd', town = 'efgh')