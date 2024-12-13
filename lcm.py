def lcm(a, b):
    z=a*b
    gcd=0
    for i in range(1, min(a,b)+1):
        if a%i==0 and b%i==0:
            gcd=i
    result=z/gcd
    print(result)
lcm(6, 18)