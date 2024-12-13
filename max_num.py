def max_num(list):
    for num in list:
        count=0
        for n in list:
            if num>=n:
                count+=1
        if count == len(list):
            print(num)

max_num([1,2,3,4,5])