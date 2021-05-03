def testf():
    t=10
    l="coools"
    print("in tesf symtable:\n",locals())
    print("globals:\n",globals())


if __name__ == '__main__':
    a="Hi this is  CRI"
    b=100
    print("testing what locals give\n",locals())
    print("globals:\n",globals())
    if(globals()==locals()):
        print("You are right they are equal")

    testf()

# if __name__ == '__main__':
#     print("i am in __main__ sugoi")

print("hi")