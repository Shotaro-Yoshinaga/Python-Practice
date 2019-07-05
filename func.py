def test_func_1():
    print('call test_func')

def test_func_2(num_1, num_2, oprn):
    if oprn == 1:
        print('足し算開始')
        print(num_1 + num_2)
    elif oprn == 2:
        print('引き算開始')
        print(num_1 - num_2)
    elif oprn == 3:
        print('掛け算開始')
        print(num_1 * num_2)
    elif oprn == 4:
        print('割り算開始')
        print(num_1 / num_2)
    else:
        print('不明なオペレーションです')

def test_func_3(num_a, num_b, oprn_1 = 1):
    if oprn_1 == 1:
        print('足し算開始')
        print(num_a + num_b)
    elif oprn_1 == 2:
        print('引き算開始')
        print(num_a - num_b)
    elif oprn_1 ==3:
        print('掛け算開始')
        print(num_a * num_b)
    elif oprn_1 == 4:
        print('割り算開始')
        print(num_a / num_b)
    else:
        print('不明なオペレーション指定です')

test_func_1()
test_func_2(100, 500, int(input('>>>')))
test_func_3(300, 600)