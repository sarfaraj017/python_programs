list=[]
list.append(input("ente4r 1st elem"))
list.append(input("ente4r 2nd elem"))
list.append(input("ente4r 3rd elem"))
list.append(input("ente4r 4th elem"))
copy_list= list.copy()
copy_list.reverse()
if(copy_list== list):
    print("Palindrome")
else:
    print("NOT Palimdrome")