print("Enter integer:")

num = int(input())

if num % 7 == 0:
    print("Магическое число!")
else:
    sum = 0
    for i in str(num):
        sum += int(i)
    print(sum)