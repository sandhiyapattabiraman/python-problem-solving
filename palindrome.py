def palindrome(str):
    st=""
    for i in range(len(str)-1,0-1,-1):
        st+=str[i]
    if st==str:
        print("Its a palindrome")
    else:
        print("Its not a palindrome")
        
palindrome("madam")