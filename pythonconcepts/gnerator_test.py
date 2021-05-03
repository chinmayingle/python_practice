def gtest():
    print("inside generator")
    for i in range(10):
        yield i

def generatorfunction():
    print('in')
    yield 1
    yield 2

print("this is test")
for value in generatorfunction():
    print(value)
# print(generatorfunction())
# print(generatorfunction())
# print(generatorfunction())
