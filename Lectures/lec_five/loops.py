# num="I love you"
# i=1
# while i<=10:
#     print(num,i)
#     i+=1
  
     #multiplication of num
# num=int(input("Enter Your Number:"))
# i=1
# while i<= 10:
#     print(num * i)
#     i+=1
    
#qsn
# num=(1,4,9,16,25,36,49,64,81,100)
# idx=0
# while idx < len(num):
#     print(num[idx])
#     idx+=1

  #qsn
num=(1,4,9,16,25,36,49,64,81,100)
x= int(input("Enter Your Number"))
i=0
while i< len(num):
    if (num[i]==x):
        print("found at idx:",i)
        break
    else:
        print("finding....")
    i+=1
    