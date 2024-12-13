def fibonacci(n):
    f1=0
    f2=1
    i=3
    st=str(f1)+","+str(f2)+","
    while i<=n:
        temp=f1+f2
        st+=str(temp)+","
        f1=f2
        f2=temp
        i+=1
    print(st[:-1])
n=10
fibonacci(n)