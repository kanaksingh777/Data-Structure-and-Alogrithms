def sum_digits(num):
    if num//10 ==0 :return

    sum = num % 10 + sum_digits(num//10)
    return sum








num = 1342

ans = sum_digits(num)
print(ans)