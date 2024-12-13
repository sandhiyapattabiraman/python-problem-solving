def even_num(n):
    num=""
    for i in range(1,n+1):
        if i%2==0:
            num+=str(i)+","
    print(num[:-1])
even_num(10)