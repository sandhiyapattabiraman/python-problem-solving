def grading(n):
    if n>=90:
        print("Grade A")
    elif n>=80 and n<=89:
        print("Grade B")
    elif n>=70 and n<=79:
        print("Grade C")
    elif n>=60 and n<=69:
        print("Grade D")
    else:
        print("Fail")
        
n = int(input("Enter your mark:"))
grading(n)