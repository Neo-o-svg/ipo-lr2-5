n = int(input()) 
first_num = n // 10000000
second_num =  n // 1000000 % 10
third_num =   n // 100000 % 10
fourth_num =   n // 10000 % 10
fifth_num =   n // 1000 % 10
sixth_num =   n // 100 % 10
seventh_num = n // 10 % 10
eighth_num = n % 10
sum = first_num + second_num + third_num + fourth_num + fifth_num + sixth_num + seventh_num + eighth_num
print(f"Сумма всех цифр числа {n} равна {sum}")

