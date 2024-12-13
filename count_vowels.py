def count_vowels(st):
    
    vowels = "aeiouAEIOU"  
    count = 0

    for char in st:
        if char in vowels:
            count += 1

    print(count)

count_vowels("Hello World")