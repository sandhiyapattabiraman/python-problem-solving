def leapyear(year):
    if (year%4==0 and year%100 != 0) or (year%400==0):
        print("its leap year")
    else:
        print("its not a leap year")
    
year= int(input("Enter the year:"))
leapyear(year)