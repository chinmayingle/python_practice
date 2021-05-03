#removes punctuation using asccii values
def remove_punctuations(s):
    cool=""
    for i in s:
        if (ord(i)>=97 and ord(i)<=122) or (ord(i)>=65 and ord(i)<=90 ):
            cool=cool+i
            # print(s)
        elif ord(i)==32:
            cool=cool+i
    # print("this is string",cool)
    return cool

#returns the average of word lengths
def count_average(s):
    # print("in ca")
    sum=0
    sp=s.split(" ")
    for i in sp:
        sum+=len(i)
    print(sum/len(sp))

if __name__ == '__main__':
    print("hi in the main")
    s="Hi! said the elevated jenny; gave ram a vehement hug as if she was mending all the cracks in this soul!"
    ns=remove_punctuations(s)
    print(ns)
    sum=0
    count_average(s)