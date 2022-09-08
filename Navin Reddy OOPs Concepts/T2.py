class person1:
    def __init__(self, name,surname,dob):
        self.__name=name
        self._surname=surname
        self.dob=dob

Ramesh = person1("Ramesh", "Rayala", 1991)
print(Ramesh._person1__name)
print(Ramesh._surname)
print(Ramesh.dob)