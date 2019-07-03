print('python')
print("python1")

abc_str = """
123
456
"""
print(abc_str)

ab_str = 'aaa'
ab_str = ab_str + '-'
ab_str = ab_str + 'bb'
print(ab_str)

abb_str = '  python-bbBbb'
print(abb_str.replace('aaaaa', 'rr'))
print(abb_str.split('-'))
print(abb_str.rjust(20, '9'))
print('s' in abb_str)
print('b' in abb_str)
print(abb_str.upper())
print(abb_str.lower())
abb_str = abb_str.lstrip()
print(abb_str)
abb_str = abb_str.lstrip('pytho')
print(abb_str)
abb_str = abb_str.rstrip('b')
print(abb_str)