##Single Inheritence Concept

class car:
     def __init__(self, body, engine, tyre):
         self.body = body
         self.engine=engine
         self.tyre = tyre

     def milage(self):
        print("Milage of this car")

c = car("Solid", "V6", "CEAT")
print(c)

class tata(car):
    pass

t = tata("Solid", "v8", "Radial")
print(t)
print(t.body)
print(t.engine)
print(t.milage())
print(t.tyre)


