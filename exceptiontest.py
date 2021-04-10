try:
    f=open("cool2","w")
    # print("HI")
    f.write("lol!")
    # print("not printed if encounted error")

except IOError:
    print("file io error ")
except TypeError:
    print("different type than excepted")
#catches all the exceptions
except Exception as e:
    print("Exception: ", e)

# Executed when no exception
else:
    print("all izzz well!")

finally:
    print("finally!!")