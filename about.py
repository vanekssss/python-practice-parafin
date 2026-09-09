# Program: personal information card
def main():
    name = "Ivan"
    surname = "Parafin"
    group = "IT-32"
    birth_year = 2009
    surname_length = len(surname)
    print(f"Name: {name} {surname}")
    print(f"Group: {group}")
    print(f"Age in 2026: {2026 - birth_year}")
    print("Favourite language: Python")


main()