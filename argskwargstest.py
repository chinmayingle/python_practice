def testfunc(v, *args, **kwargs):
    print(v)
    print(args,type(args))
    for i in args:
        print(f'awrsd {i}')
    print(kwargs,type(kwargs))
    for i in kwargs:
        print(f'kw {i}')

if __name__ == '__main__':
    print("in main")
    testfunc(13,keu="cooool",l="cpppl",a=2)