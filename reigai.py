def excep_test(value_1, value_2):
    print('計算開始')
    result = 0

    try:
        result = value_1 + value_2
    except:
        print('計算できませんでした')
    finally:
        print('計算完了')
    return result

print(excep_test(100, 200))
print(excep_test(100, '300'))