import sys
import traceback

def exceptin_test(value_1, value_2):
    print('=====計算開始=======')
    result = 0

    try:
        result = value_1 + value_2
    except:
        print('計算できませんでした')
        raise
    finally:
        print('計算終了')
    return result

try:
    print(exceptin_test(100, '200'))
except:
    print('----------------')
    print(traceback.format_exc(sys.exc_info()[2]))
    print('---------------')