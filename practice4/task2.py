y = 2007

def print_age(year):
    age = 2026 - year
    print("Вік:", age)

def get_age(year, current_year=2026):
    if year > current_year or year < 0:
        return -1
    return current_year - year
    print("after return")

print_age(y)

age = get_age(y)
print("Вік:", age)

print(print_age(y))

print("Вік у місяцях:", age * 12)
print("Вік у тижнях:", age * 52)

print("Вік у 2030 році:", get_age(y, 2030))

print("Перевірка 3000:", get_age(3000))