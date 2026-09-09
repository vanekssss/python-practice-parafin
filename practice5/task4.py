def read_grade(prompt):
    """Зчитує оцінку від 0 до 100."""
    while True:
        try:
            grade = int(input(prompt))
            if 0 <= grade <= 100:
                return grade
            print("Оцінка повинна бути від 0 до 100.")
        except ValueError:
            print("Введіть ціле число.")


def to_letter(grade):
    """Перетворює оцінку на буквену оцінку."""
    if grade >= 90:
        return "A"
    if grade >= 82:
        return "B"
    if grade >= 74:
        return "C"
    if grade >= 64:
        return "D"
    if grade >= 60:
        return "E"
    return "F"


def average(grades):
    """Повертає середнє арифметичне оцінок."""
    return sum(grades) / len(grades)


def count_above(grades, limit):
    """Рахує оцінки, більші за задане значення."""
    count = 0

    for grade in grades:
        if grade > limit:
            count += 1

    return count


def print_report(name, group, grades):
    """Друкує звіт про оцінки."""
    avg = average(grades)

    print("Ім'я:", name)
    print("Група:", group)
    print("Оцінки:", grades)
    print("Середнє:", f"{avg:.2f}")
    print("Буквена оцінка:", to_letter(avg))
    print("Найкращий бал:", max(grades))
    print("Найгірший бал:", min(grades))
    print("Оцінок вище середнього:", count_above(grades, avg))


def main():
    """Запускає основну частину програми."""
    name = "Ivan"
    group = "IT-32"

    n = len(name)

    if n < 3:
        n = 3

    grades = []

    for i in range(n):
        grade = read_grade("Введіть оцінку: ")
        grades.append(grade)

    print_report(name, group, grades)


main()