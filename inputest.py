from sys import stdin, stdout

def get_ints(): return map(int, sys.stdin.readline().strip().split())
def get_list(): return list(map(int, sys.stdin.readline().strip().split()))


# a=input("enter")
# print(a)
# b=raw_input("hola put something")

n=stdin.readline()
print(type(n))
print(n)

l=stdin.readline()
print(type(l))
stdout.write("Holla::l")