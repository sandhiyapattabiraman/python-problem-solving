def sum_of_nums(number):
    total=0
    for num in number:
        total+=num
    return total
number=[1,2,3,4,5,6]
print(sum_of_nums(number))


def sums(n):
    total=0
    for i in range(1,n+1):
        total+=i
        i+=1
    return total
n=6
print(sums(n)) 