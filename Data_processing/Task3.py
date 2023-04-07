"""
Напишите функцию которая будет принимать список чисел и выводить на экран надпись "сегодня x градусов" столько раз
сколько значений в списке.
"""
def print_temperature(temperatures):
    for t in temperatures:
        print("Сегодня", t, "градусов")

temperatures = [25, 2, 14, 49]
print_temperature(temperatures)