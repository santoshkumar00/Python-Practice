#with out aruments:
def d1():
    print("hello world")
d1()
#with arguments:
def d1(myname):
    print(myname)
d1("santosh kumar")

#function using key values pair:
def d1(fname,lname):
    print(fname,lname)
d1(fname="santosh",lname="kumar")
d1(fname="meena",lname="rao")

# passing default values:
def d1(book="ABC"):
    print(book)
d1()
d1("santosh")
d1("santosh kumar")

# *arguments:
def b(*colors):
    print(colors)
b("green","blue","red")

#  ** arguments:
def d1(** names):
    print(names)
d1(fname="santosh",lname="kumar")

def d1(** names):
    for i in names .items ():
        print(i)
d1(A="santosh",B="kumar",C="santosh kumar")

# return key value:
def d1():
    a,b=10,20
    return a,b
d=d1()
print(d)

def d1():
    a,b=5,10
    return a,b
print(d1())

def d1():
    a,b=5,10
    print(a,b)
    a,b=20,50
    return a,b
print(d1())

# retun data stuructures:
def f1():
    return ["santosh","kumar"],(1,2,3),{1,2,3,2}
d=f1()
print(d)
print(d[0])
print(d[0][0])
print(d[2])

def d1():
    return {10:"santosh",101:"kumar",1001:"santosh kumar"}
print(d1())

# boolen validation:
def na(santo):
    if na:
        print("True")
    else:
        print("False")
na({})

# globle variable:
a=10
def d1():
    print(a)
d1()
print(a)

#local variable:
b=100
def d():
    print(b)
d()
print(b)

# globle variable:
x=1000
def d1():
    x=101
    print("local variable",x)
    print("globale variable",globals()["x"])
d1()
print(x)

# local variable:
y=100
def d1():
    y=102
    print("local variable",y)
    print("global variable",globals()["y"])
    globals()["y"]=30
    print("global variable",globals()["y"])
d1()
print(y)

# locals :
def d1():
    x=105
    print("local variable",x)
    print("local variable",locals()["x"])
    locals()["x"]=200
    print("local ",locals()["x"])
d1()

x,y,z=10,20,30
def d1():
    print(globals())
def d2():
    a,b,c=100,200,300
    print(locals())
print(d1())
print(d2())

# globals and locals scope:
print(locals()== globals())
print(globals()== locals())

def d1():
    print(locals()is globals())
    print(globals()is locals())
d1()

# global key word:
x=10
def d1():
    global y
    y=100
    print("local ",y)
d1()
print("global",x)
print("local ",y)

# assignment functions:
def d1(a,b):
    print(a,b)
d=d1
d(5,50)

# function inside another function;
def f1():
    print("outer function")
    def d2():
        print("inner function")
    return d2()
f1()

def d1(a,b):
    def d2():
        print(a+b)
    return d2()
d1(10,20)


# with arguments:
def d1(fname,lname):
    print(fname,lname)
d1(fname="santosh",lname="kumar")

# with out arguments:
def d1():
    print("santosh kumar")
d1()

# globle variable:
x=10
def d1():
    y=20
    print("local variable",y)
d1()
print("globle variable",x)

# globels:
x=20
def d1():
    # global:
    print("local variable",x)
d1()
print(x)