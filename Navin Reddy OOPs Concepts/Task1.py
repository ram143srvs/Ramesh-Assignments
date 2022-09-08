import logging

logging.basicConfig(filename="task1.log", level=logging.DEBUG, format= "%(asctime)s %(levelname)s")

class tutorial:

    def __init__(self, name, surname, rollno, course):
        self.name = name
        self.surname = surname
        self.rollno = rollno
        self.course = course

class t1(tutorial):
    try:
        def st_perf(self):
            logging.info("Please find the student Performance details:")
    except Exception as e:
        logging.Exception(e, "Please enter the student correct details.")

s=tutorial("Ramesh", "Rayala", 12345, "Data Science")
print(s.name)
print(s.surname)
print(s.rollno)
print(s.course)

