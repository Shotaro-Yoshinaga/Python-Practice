def excep_test(value1, value2):
    print('計算開始')

    result = 0

    try:
        result = value1 + value2
    except:
        print('計算できませんでした')
        raise
    finally:
        print('計算終了')
    return result

try:
    print(excep_test(100, 300))
    print(excep_test(200, '400'))
except:
    print('エラーを受け取りました')
