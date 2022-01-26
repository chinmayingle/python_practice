def decofunc(varfunc):
    def infunc():
        print("hi")
        varfunc()
        print("bye")
    return infunc


@decofunc
def printname():
    print("chinmay")

# printname()


def tempdecorate(tempfunc):
    def temp():
        print("hi")
        tempfunc()
        print("bye")

    return temp

# @tempdecorate
@decofunc
def prname():
    print("chinmay")

prname()



# def abc(func):
#     def cd():
#         print("ah haa")
#         func()
#         print("hmm")
#     return cd


# @abc
# def lol():
#     print("cri")

# lol()