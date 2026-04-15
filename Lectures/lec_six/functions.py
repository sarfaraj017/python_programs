# def avrg(a,b,c):
#     return((a+b+c)/3)
# print(avrg(3,2,4))
# def sum(a,b):
#     s=a+b
#     return s
# print (sum(2,3)) 
# num=["good","hennai","mumbai","gu"]
# def len_list(list):
#     print(len(list))
# len_list(num)
# def print_list(list):
#     for elem in list:
#         print (elem, end=" ")
# cities= ["gu","hagu","mutu"]
# print_list(cities)

# def calc_fact(n):
#     fact=1
#     for i in range (1,n+1):
#         fact *=i 
#     print (fact)
# calc_fact(4)
def converter(usd_money):
    ind_val=usd_money*90
    print(usd_money, "USD=", ind_val, "INR")
converter(2)