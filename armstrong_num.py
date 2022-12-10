# Program to check Armstrong numbers in a certain interval

a, b = input().split()
a, b = int(a), int(b)

for i in range(a, b + 1):
    num_digits = len(str(a))
    temp = i
    count = 0
    while temp != 0:
        last_digit = temp % 10
        count += 1
        temp //= 10 

    temp = i
    total = 0
    while temp != 0:
        last_digit = temp % 10
        total += last_digit ** count
        temp //= 10
    
    if total == i:
        print(total)
    


