class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def describe(self):
        return f"{self.name} {self.surname}"


class Student(Person):
    def __init__(self, name, surname, group):
        super().__init__(name, surname)
        self.group = group

    def describe(self):
        return f"{super().describe()}, {self.group}"


class GroupLeader(Student):
    def __init__(self, name, surname, group, phone):
        super().__init__(name, surname, group)
        self.phone = phone

    def describe(self):
        return f"{super().describe()}, group leader, {self.phone}"


person = Person("Ivan", "Parafin")
student = Student("Ivan", "Parafin", "IT-32")
leader = GroupLeader("Group", "Leader", "IT-32", "+380 00 000 00 00")

objects = [person, student, leader]
classes = [Person, Student, GroupLeader]

print("isinstance:")
for obj in objects:
    for cls in classes:
        print(f"{obj.__class__.__name__} is {cls.__name__}: {isinstance(obj, cls)}")

print("\nissubclass:")
for child in classes:
    for parent in classes:
        print(f"{child.__name__} is subclass of {parent.__name__}: "
              f"{issubclass(child, parent)}")

print("\nGroupLeader MRO:")
for cls in GroupLeader.__mro__:
    print(cls.__name__)

print("\nDescribe:", leader.describe())
