class car:

    def __init__(self, body, engine, tyre):
        self.body = body
        self.engine = engine
        self.tyre = tyre

    def milage(self):
        print("Please find the Milage")

class tata(car):
    def car_details(self):
        print("Please print the tata car details: ")

class toyota(tata):
    pass



c= tata("Solid", "V6", "Radial")
print(c.body)
print(c.engine)
print(c.tyre)
print(c.milage())
