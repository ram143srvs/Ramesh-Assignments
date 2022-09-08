class Person:

    def __init__(self, name, surname, emailID, YOB):
        self.name = name
        self.surname = surname
        self.emailID = emailID
        self.YOB = YOB
    def age(Ramesh, current_year):
        return current_year - Ramesh.YOB

Ramesh_var = Person("Ramesh", "Rayala", "ram143srvs@gmail.com",1991)
print(Ramesh_var.name)
print(Ramesh_var.surname)
print(Ramesh_var.emailID)
print(Ramesh_var.YOB)

print(Ramesh_var.age(2022))

Sravani_var = Person("Sravani", "Rayala", "sravaniramesh2628@gmail.com",1997)
print(Sravani_var.name)
print(Sravani_var.surname)
print(Sravani_var.emailID)
print(Sravani_var.YOB)

print(Sravani_var.age(2022))