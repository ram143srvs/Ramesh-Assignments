import T2
print(T2)

obj3 = T2.person1("Ramesh", "Ray", 1990)
print(obj3._person1__name)
print(obj3._surname)
print(obj3.dob)

class person:

    _name = "Ramesh"
    __surname = "Rayala"
    dob=1991

    def _age(self, current_year):
        return current_year - self.dob
    def __age(self, current_year):
        return current_year - self.dob

obj = person()
print(obj)
print(obj._age(2022))


class employee(person):
    _name = "Sravani"
    __Surname = "Ram"
    dob = 1999

obj1 = employee()
print(obj1)
print(obj1.dob)
print(obj1._name)
print(obj1._employee__Surname)
print(obj1._person__age(2022))