class shape:
    def sides(self):
        pass



class circle(shape):
    def sides(self):
        print("No sides")


#cannot access private variable 
class A:
    def _init_(self):
        self.__b=10

a=circle()
a.sides()
b=shape()
b.sides()

c=A()
print(c.dir())