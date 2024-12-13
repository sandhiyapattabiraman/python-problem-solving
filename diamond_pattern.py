def diamond(n):
    for i in range(1,n+1):
        sym=""
        gap=""
        result=""
        for j in range(i,0,-1):
            sym+="*"+" "
        for k in range(n-i,0,-1):
            gap+=" "   
        result=gap+sym
        print(result)
    for i in range(n-1,0,-1):
        sym=""
        gap=""
        result=""
        for j in range(0,i):
            sym+="*"+" "
        for k in range(i,n):
            gap+=" "
        result=gap+sym
        print(result) 
diamond(5)       