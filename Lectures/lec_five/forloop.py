list=(1,4,9,16,25,36,49,64,81,100)
i=0
x=int(input("Enter Your Number:"))
for val in list:
    if(val==x):
        print("Number Found at idx", i)
        break
    i+=1
