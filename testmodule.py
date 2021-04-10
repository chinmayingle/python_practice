coolvar="this is coool variable"

def tellmestory():
    print("here is a story ")

def outer_function():
    global a
    a = 20

    def inner_function():
        # global a
        # b = 30
        print('a =', a)

    inner_function()
    print('a =', a)




def __main__():
    print("in main()")

#this would run when the script is run directly
if __name__ == '__main__':
    print("i am in __main__ sugoi")
    a = 10  #this is inherently global variable
    outer_function()
    print('a =', a)
    # print("last no is ",b)

#this would run when the module is imported
if __name__=='testmodule':
    print("******************************************right!!",dir())