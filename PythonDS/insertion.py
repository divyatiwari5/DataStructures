#def func(a, b):
 #   print(a+b)


#func(102,  58.9)
#func("a", "ahsf josdf jsof")
#func(['a', 1,  3], ['asj'])

#a = 10
#a = "tr"


x = "Divya"
a = 20

print("My name is: " + x)
print("My age is:" , str(a))
print(10, 20, 30, 40)
print("My age is: %d and I am %s and I got %.99f" % (a, "awesome", 8.5129))

print("Divya is sexy".count("i"))
print("Divya is sexy".split("i", 2))
print("divya IS Fexy".capitalize())


def func(*args, **kwargs):
    print("Testing")


def func2(fu):
    fu()
    return 1, "abcdf"


x = func2(func)
type(x)

