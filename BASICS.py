a=2
b=3
c=3.14
d=2+3j
e=True
str="hello"
print(type(a))  #int
print(type(c))  #float
print(type(d))  #complex
print(type(e))  #bool
print(type(str))  #str

#How to take input from user
name=input("Enter your name:")
print("my name is ",name)
#wap for taking diameter as input and
#calculate area of circle
dia=int(input("Enter the diameter:"))
area=3.14*(dia/2)**2
print("Area of circle:",area)
#WAP to take your age input and print entered value and its data type
age=int(input("Enter your age:"))
print("YOUR age is  ",age)
print(type(age))
#WAP Input two numbers and print sum of two number
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
c=int(input("Enter the value of c:"))
print("sum of numbers:",a+b)
print("average of numbers:",(a+b+c)/3)
#implicit type comversion
i=int(input("Enter the value of d:"))
fl=float(input("Enter the value of e:"))
sum=i+fl
print(sum)
print(type(sum))
#Explicit type conversion
fl1=4.56
g=int(fl1)  #int() use for changing the type manually
print(g)
print(fl1)
print(type(g))
print(type(fl1))
#Operator
#Arithmatic opetator
h=20
i=5
print(h+i)  #25
print(h-i)  #15
print(h%i)  #0
print(h*i)  #100
print(h**i) #3200000
print(h/i) #4.0
print(h//i) #4
#Comparison operator
j=34
k=43
print(j>k)
print(j==k)
print(j<k)
print(j>=k)
print(j<=k)
print(j!=k)
#logical operator
print("logical operator")
print(j<k and j!=k )  #true
print(j>k and j!=k )  #false
print(j<=k and j!=k )  #true
print(j>=k and j==k )  #false
print(j<=k or j!=k )  #true
print(j>=k or j!=k ) #true
print( not j>=k ) #true
#Assignment operator
j+=3
k-=4
print("updated value of k",k)
print("updated value of j",j)
k//=3
print("updated value of k",k)


