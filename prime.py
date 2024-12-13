def prime(num):
    prime=True
    if num==2 or num==1:
        print("its a prime")
    for i in range(2,num):
        if(num%i==0):
            prime=False
            break
    if(prime):
        print("Its a Prime")
    else:
        print("Its Not a Prime")
n=15
prime(n)   

numbers = [1, 2, 3, 4]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)