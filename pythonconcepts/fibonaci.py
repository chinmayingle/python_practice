def getfibo():
    a,b=0,1
    # c = 1
    for _ in range(100):
        yield a
        a,b=b,a+b
        



if __name__== '__main__':
    
    #notice creating an instance of the function and not just calling the function
    it=getfibo()
    for num in it:
        if num > 10:
            break
        print(num)
