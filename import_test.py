import testmod

test_class_1 = testmod.TestClass()
test_class_1.test_method('1')

from testmod import TestClass

test_class_2 = TestClass()
test_class_2.test_method('2')

import testmod as ts

test_class = ts.TestClass()
test_class.test_method('3')