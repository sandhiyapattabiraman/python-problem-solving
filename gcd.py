def gcd(a,b):
    gcd=0
    for i in range(1,max(a, b)+1):
        if a%i==0 and b%i==0:
            gcd=i
    print (gcd)
gcd(24,18)