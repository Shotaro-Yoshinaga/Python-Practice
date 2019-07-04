import datetime

def get_today():
    today = datetime.datetime.today()
    #カンマがあるとタプルになる
    value = today.year, today.month, today.day

    return value

test_tuple = get_today()

print(test_tuple)
print(test_tuple[0])
print(test_tuple[1])
print(test_tuple[2])

a = {}
a[0, 0] = "ABC"
print(a)