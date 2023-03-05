""" 1)If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000"""
##
##listnum=[]
##for i in range(1000):
##    if i==0:
##        print("Number",i,"is not a multiple of 3 or 5")
##    elif i%3==0 or i%5==0:
##        listnum.append(i)
##    else:
##        print("Number",i,"is not a multiple of 3 or 5")
##print(listnum)
##numsum=0
##for i in range (len(listnum)):
##     numsum=numsum+listnum[i]
##print(numsum)

 
"""Each new term in the Fibonacci sequence is generated
by adding the previous two terms. By starting with 1 and 2,
the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
by considering the terms in the Fibonacci
sequence whose values do not exceed four million,
find the sum of the even-valued terms."""

##listnum=[1,2]
##evenlist=[]
##evensum=0
##while True:
##    num=listnum[len(listnum)-1]+listnum[len(listnum)-2]
##    listnum.append(num)
##    if num>=4000000:
##        break
##    elif num%2==0:
##        evenlist.append(num)
##print(listnum)
##print (evenlist)
##for i in range(len(evenlist)):
##    evensum=evensum+evenlist[i]
##print(evensum+2)
##
####################
##listnum=[1,2]
##evenlist=[]
##evensum=0
##num=0
##while num!=4000000:
##    num=listnum[len(listnum)-1]+listnum[len(listnum)-2]
##    listnum.append(num)
##    if num%2==0:
##        evenlist.append(num)
##print(listnum)
##print (evenlist)
##for i in range(len(evenlist)):
##    evensum=evensum+evenlist[i]
##print(evensum+2)

"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143"""
prime=[]
num=600851475143
for primecheck in range(2,10000):
    count=0
    for i in range(2,primecheck):
        if primecheck%i==0:
            count=count+1
    if count==0:
        prime.append(primecheck)
allprime=[]
for i in range(len(prime)):
    while num%prime[i]==0:
        print(prime[i])
        allprime.append(prime[i])
        num=num/prime[i]
print(max(allprime))
