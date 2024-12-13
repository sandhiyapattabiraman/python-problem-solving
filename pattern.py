def pattern(n):
    for i in range(1, n+1):
        st=""
        while i>0:
            st+="*"+" "
            i-=1
        print(st)
pattern(5)