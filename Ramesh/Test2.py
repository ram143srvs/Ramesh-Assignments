import logging
logging.basicConfig(filename="List.log", level = logging.DEBUG, format ="%(levelname)s %(name)s %(asctime)s")

class list:
    logging.info("We are going to access the list class")

    def extract_list(self, l):
        logging.info("We are extracted the list function")
        try:
            self.l=l
            for i in self.l:
                if type(i) == list:
                    print(i)
        except Exception as e:
            logging.exception(e, "Please enter the iterate collection")

        def extract_Interra(self,m):
            logging.info("Inside function extract_Interra")
            try:
                self.m = m
                for i in self.m:
                    if type(i) !=dict:
                        for j in i:
                            if j == "Interra":
                                logging.info(j)
                                return j
                    else:
                        for j in i:
                            if i[j] == "interra":
                                logging.info(i[j])
                                return i[j]
            except Exception as e:
                logging.Exception(e)

        def flat_list(self, l):
            logging.info("Inside flat_list fundtion")
            try:
                self.l=l
                self.p=[]
                for i in l:
                    if type(i) !=dict:
                        logging.info("data : %s", i)
                        self.p.extend(i)
                    else:
                        logging.info("values inside dict %s", i)
                        self.p.extend(i.keys())
                        self.p.extend(i.values())
                return self.p
                logging.info("output %s",p)
            except Exception as e:
                logging.exception(e)
                return e

    def print_prime(self):
        """  To create list of prime numbers between 1 to 100"""
        logging.info("Inside print_prime function")
        try:
            self.l = []
            for i in range(1, 100):
                c = 0
                for j in range(2, i):
                    if i % j == 0:
                        c = 1
                if c != 1:
                    self.l.append(i)
            logging.info("Output %s",self.l)
            return self.l
        except Exception as e:
            logging.exception(e)
            return e

l = [[1, 2, 3, 4], (2, 3, 4, 5, 6), (3, 4, 5, 6, 7), set([23, 4, 5, 45, 4, 4, 5, 45, 45, 4, 5]),
     {'k1': "Ramesh", 'k2': "Interra", 'k3': "Rayala", 3: 6, 7: 8}, ["Interra", "Mainframes"]]

list_var = list()


print(list_var.print_prime())
print(list_var.extract_interra)