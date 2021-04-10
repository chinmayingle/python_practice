try:
    10/0
    f=open("cool2","r")
    print("HI")
    f.write("lol!")
    print("not printed")

except IOError:
    print("boolloo na ")
except TypeError:
    print("hmmm")
except :
    print("all")


# Executed when no exception
else:
    print("all izzz well!")


finally:
    print("finally!!")