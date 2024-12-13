def anagram(a,b):
    if len(a)!=len(b):
        print("Its not a anagram")
    st=0    
    for i in range(0,len(a)):
        for j in range(0,len(b)):
            if a[i]==b[j]:
                st+=1
    if st==len(a):
        print("It a anagram")
    else:
        print("Its not a anagram")
anagram("hello","world")