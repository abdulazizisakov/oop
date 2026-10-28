class Student:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def show_info(self):
        print("Men o'quvchiman")


s01 = Student("Vali", "Asrorov", 21)
s02 = Student("Adham", "Bahromov", 18)

s01.show_info()
s02.show_info()
