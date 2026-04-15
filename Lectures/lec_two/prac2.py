# num= int(input("Enter Your number:"))
# #reminder= num%2
# if(num % 2 == 0):
#     print("even number")
# else:
#     print(" odd number")

a= int(input("Enter first number:"))
b= int(input("Enter second number:"))
c= int(input("Enter third number:"))
d= int(input("Enter fourth number:"))

if(a>=b and a>=c and a>=d):
    print("first is largest")
elif(b>=c and b>=d):
    print("second is largest")
elif(c>=d):
    print("third is largest")
else:
    print("fourth is largest")