# # # # # age=12
# # # # # print("my age is :",age)
# # # # # print(f"my age is :{age}")
# # # # # # we start index always 0
# # # # # name="surya"
# # # # # age=22
# # # # # # print("my name is {} and age is {}".format(name , age))
# # # # # #place holder
# # # # # be="cs"
# # # # # print("my name is {firstname} and age is {firstage}".format(firstname=name , firstage=age))
# # # # # print(f"my name is {name} and my  age is {age} and my degree is {be} ")
# # # # # age=12
# # # # # if age<=18:
# # # # #     print("you are eligible to vote")
# # # # age=int(input("enter your age"))
# # # # if age>=18 and age<=32:
# # # #     print("you are eligible to vote")
# # # # account_money=int(input("enter money"))
# # # # if account_money>=1000:
# # # #     print("you buy a product my shop you get 20percent discount",account_money)
# # # # else:
# # # #     print("you buy a product my shop you get 30percent discount",account_money)

# # # # #single statement
# # # # val=int(input("enter the name"))
# # # # if(val<=99): print("hello")

# # # # j_age=23
# # # # while(j_age<60):
# # # #     j_age+=1
# # # #     print(j_age)

# # # # ## while loop
# # # # aomunt_money=1000
# # # # while(aomunt_money!=0):
# # # #     print(aomunt_money)
# # # #     aomunt_money-=100
    
# # # # else:
# # # #     print("puy money in bank")
# # # # #for loop    

# # # lst=["hello",1,2,3,4]
# # # # for i in range(len(lst)):
# # # #     print(lst[i])
# # # # fruit="mangeo"
# # # # for i in fruit:
# # # #     print(i)
# # # # print(fruit[2])
# # # # for i in lst:
# # # #     if i==4:
# # # #         print("lsit element is 4")
# # # #         break
# # # #     print(i)

# # # # for i in lst:
# # # #     if i==2:
# # # #         print("lsit element is 4")
# # # #         continue
# # # #     print(i)

# # # # # in time pass it not de any change

# # # def pyramid(n):
# # #     k=n*2-2
# # #     for i in range(0,n):
# # #         for j in range(0,k):
# # #             print(end=" ")
# # #         k=k-2
# # #         for j in range(0,i+1):
# # #             print("*",end=" ")
# # #         print("\r")
# # # pyramid(5)

# # import multiprocessing
# # def sender(conn,msg):
# #     for i in msg:
# #         conn.send(i)
# #     conn.close()
# # def recieve(conn):
# #     while True:                                                                          
# #         try:
# #             msg=conn.recv()
# #         except Exception as e:
# #             print(e)
# #             break
# #         print(msg) 
# # if __name__=='__main__':
# #     msg=["i am s","you ar e"]
# #     parent_c,child_c=multiprocessing.Pipe()
# #     m1=multiprocessing.Process(target=sender,args=(parent_c,msg))
# #     m2=multiprocessing.Process(target=recieve,args=(child_c,))
# #     m1.start()
# #     m2.start()
# #     m1.join()
# #     child_c.close()

# #     m2.join()
# #     parent_c.close()

# # def isprime(x):
# #     f=True
# #     if (i%2==0):
# #             f=False
# #     else:
# #             return f
# # for i in range(2,50):
# #     if (isprime(i)):
# #         print(i," is prime no")
# #     else:
# #         print(i, "is not prime no ")

# # def slcm(x,y):
# #     if(x>y):
# #         g=x
# #     else:
# #         g=y
# #     while(True):
# #         if(g%x==0 and g%y==0 ):   
# #             lcm=g
# #             break
# #         g+=1
# #     return lcm    

# # print(slcm(12,14))
# def ghcf(x,y):
#     if(x<y):
#         s=x
#     else:
#         s=y
#     for i in range(1,s+1):
#         if(x%i==0 and y%i==0):
#             hcf=i
        
#     return hcf
# print(ghcf(24,54))
# n=int(input("enter the mo"))
# sum=0
# temp=n
# while(temp > 0):
#     digit=temp%10
#     sum+=digit**3
#     temp//=10
# if(n==sum):
#     print("amstrong no is",n)
# else:
#    print("not amstrong no",n)

# n=(input("enter the palindrome no"))
# str=n[::-1]
# if(n==str):
#     print(n,"is pallindrome")
# if(n==str):
#     print(n,"is not  pallindrome")
    
def fib(n):
    if(n==0 and n==1):
        return n
    t1=0
    t2=1
    while(n>0):
        t3=t1+t2
        t1=t2
        t2=t3

        n-=1
    print(t2)
fib(5)