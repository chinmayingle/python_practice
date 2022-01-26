def gtest():
    print("inside generator")
    for i in range(10):
        yield i

def generatorfunction():
    # print('in')
    for i in range(10):
        print("=",i)
        yield i
    # yield 1
    # yield 2

def tt():
    yield 1
    yield 2
    yield 3
    yield 4


#these all will give output as 1
#why?? coz we are creating new instances and then calling __next__() 
#to avoid this create an instance and then call next like inst=tt() then inst.__next__()
tocalltt=tt()
# for i in tocalltt():
#     print(i)
print(tocalltt.__next__())
print(tocalltt.__next__())
print(tocalltt.__next__())
# print("this is test")
# for value in generatorfunction():
#     print(value)
# print(generatorfunction().__next__(),generatorfunction().__next__(),generatorfunction().__next__())
# print(generatorfunction().__next__())
# print(generatorfunction().__next__())
