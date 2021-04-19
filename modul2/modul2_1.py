name= 'John'
age = 26

print("name:", name, "age: ", age)

# print="print"
#
# print("name:", name, "age: ", age)

# type function

result = type(name)
print(result)

result = type(age)
print(result)


print(5*name)
result1=5*name
result2=type(result1)
print(result2)

result = id(name)
print(result)

print(8 + 8)
print((8).__add__(8))

print(8 * " text" )
print((8).__mul__("text"))
print((" text").__mul__(8))

print(8-8)
print((8).__sub__(8))

print(8/8)
print((8).__truediv__(8))

print(8**8)
print((8).__pow__(8))
print(pow(8,8))

#Float

result=8/8
result1=type(result)
print(result1)


a=3
b=4
c=5
x1=(-b+(b**2-4*a*c)**(1/2))/(2*a)
print(x1)

x2=(-b-(b**2-4*a*c)**(1/2))/(2*a)
print(x2)

bsqr= b.__pow__(2)
multi= (4).__mul__(a.__mul__(c))
dif= bsqr.__sub__(multi)
dif=float(dif)
var=(1).__truediv__(2)
rad=dif.__pow__(var)
b= complex(b)
dif2=(-b).__sub__(rad)
mul1=(2).__mul__(a)
ec= dif2.__truediv__(mul1)
print(ec)



#Complex

nr1 = 1 + 1j
nr2 = 3 + 5j
print(nr1+nr2)
print(type(nr1+nr2))



#Strings
my_str="My string"
# dir

info=dir(my_str)
print(info)

var1 = "this is {}"
cap=var1.capitalize()
print(cap)

format1=var1.format("Sparta")
print(format1)

phone = "0747.655.444"
split1= phone.split("7")
print(split1)

#rsplit , lsplit

split1=phone.rsplit(sep="." , maxsplit=1)
print(split1)



# input
#text="This is your name: "
#name=input("give me your name")
#print(text+name)


#slice
text="My Text"
first_letter="My Text"[0]
print(first_letter)
slice1 = text[0:6:2]
print(slice1)


#text= input("insert text")
text1=text[5:]
text2=text[0:5]
print(text1+text2)

reverse = text[::-1]
print(reverse)

print(text2[::-1]+text1[::-1])

#true,false

my_bool=True
print(type(my_bool))

my_bool=False
print(type(my_bool))

print(id(True))
print(id(False))
print(id(10))

print(True+False)
print(True.__add__(False))

print(True or False)
print(True and False)

print(dir(True))


#None

my_none= None
x=print("")
print(x)

#Truth

#0 -> False
#'a'->True
#""-> False
#1 ->True

x=bool('a')
print(x)