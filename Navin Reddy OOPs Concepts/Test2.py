##Multilevel Inheritence Concept

class bank:

    def trans(self):
        print("Total transaction value")

    def ac_open(self):
        print("This will show your account opening status")

    def depo(self):
        print("This will show your deposited account")

class hdfc_bank(bank):
    def hdfc_to_icici(self):
        print("this will show all your transaction from hdfc to icici")

class icici(hdfc_bank):
    pass

i = icici()
i.hdfc_to_icici()
i.depo()
i.trans()
i.ac_open()
