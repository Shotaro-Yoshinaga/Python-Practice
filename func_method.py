#関数
def test_func_4():
    print('call test_func_4')

class TestClass:
    #メソッド
    def test_method():
        print('call test_method')
    
print('-------------------')
print(test_func_4)
print(TestClass.test_method)

print('------------------')
print(type(test_func_4))
print(type(TestClass.test_method))

print('-----------------')
t = TestClass()
print(test_func_4)
print(t.test_method)