def sum_of_even_numbers(number):
    sum_counter = 0
    for number in range(number + 1):
        if number % 2 == 0:
            sum_counter += number

    print(f"Сумма четных чисел от 1 до {number} равна {sum_counter}.\n")


def square_of_odd_numbers(number):
    squres = [number ** 2 for number in range(number + 1) if number % 2 != 0]
    print(f"Квадраты всех нечетных чисел от 1 до {number}: {squres}\n")


def counting_numbers():
    flag = True
    counter = 0

    try:
        while flag:
            user_number_input = int(input("Введите число: "))
            if user_number_input >= 0:
                counter += 1
            else:
                print(f"Количество введенных чисел: {counter}.")
                flag = False
    except ValueError:
        print("Ошибка ввода.")


sum_of_even_numbers(100)
square_of_odd_numbers(10)

print("Добро пожаловать.\nДанная программа делает подсчет введеных пользователем целых чисел.\n"
      "Чтобы завершить программу, введите отрицательное число.")
counting_numbers()