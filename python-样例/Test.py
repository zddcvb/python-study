from functools import reduce
import hashlib

def test1():
    print("test1");


class Test(object):
    def __init__(self, func):
        print ("init")
        self.func = func;

    def __call__(self, *args, **kwargs):
        print (1)
        self.func();


t = Test(test1);
t();

t = reduce(lambda x, y: x + y, [1, 5, 3, 9])
t1 = reduce(lambda x, y: x + y, [1, 3, 5, 9], 10)
t2 = map(lambda x, y: x + y, [1, 3, 5, 9], [2, 5, 9, 20])
t3 = filter(lambda x: x > 7, [5, 6, 9, 10])
print (t3)
print (t2)
print (t1)
print(t)

m=hashlib.md5();
m.update("hahah")
print m.hexdigest();