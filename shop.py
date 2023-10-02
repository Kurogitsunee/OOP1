class Human:
    
    def __init__(self, surname, name, second_name):
        self.__surname = surname
        self.__name = name
        self.__second_name = second_name

    @property
    def name(self):
        return self.__name

    @property
    def surname(self):
        return self.__surname
    
    @property
    def second_name(self):
        return self.__second_name

    @name.setter
    def name(self, name):
        self.__name = name

    @surname.setter
    def surname(self, surname):
        self.__surname = surname

    @second_name.setter
    def second_name(self, second_name):
        self.__second_name = second_name


class Employee(Human):

    def __init__(self, surname, name, second_name, salary):
        super().__init__(surname, name, second_name)
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        self.__salary = salary


class Customer(Human):

    def __init__(self, surname, name, second_name, card_number, avg_cheque):
        super().__init__(surname, name, second_name)
        self.__card_number = card_number
        self.__avg_cheque = avg_cheque

    @property
    def card_number(self):
        return self.__card_number

    @property
    def avg_cheque(self):
        return self.__avg_cheque

    @card_number.setter
    def card_number(self, card_number):
        self.__card_number = card_number

    @avg_cheque.setter
    def avg_cheque(self, avg_cheque):
        self.avg_cheque = avg_cheque
        

n_employees = int(input("Количество сотрудников: "))

employees = []
customers = []

for i in range(n_employees):
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    second_name = input("Введите отчество: ")
    salary = input("Введите зарплату: ")
    new_employee = Employee(surname, name, second_name, salary)
    employees.append(new_employee)

n_customers = int(input("Количество клиентов: "))

for i in range(n_customers):
    surname = input("Введите фамилию: ")
    name = input("Введите имя: ")
    second_name = input("Введите отчество: ")
    card_number = input("Введите номер карты: ")
    avg_cheque = input("Введите средний чек: ")
    new_customer = Customer(surname, name, second_name, card_number, avg_cheque)
    customers.append(new_customer)

employees_out = open("employees_out.txt", 'w')
customers_out = open("customers_out.txt", 'w')

employees_out.write("Фамилия | Имя | Отчество | Зарплата\n")
customers_out.write("Фамилия | Имя | Отчество | Номер карты | Средний чек\n")

for employee in employees:
    employees_out.write(f"{employee.surname} | {employee.name} | {employee.second_name} | {employee.salary}\n")

for customer in customers:
    customers_out.write(f"{customer.surname} | {customer.name} | {customer.second_name} | {customer.card_number} | {customer.avg_cheque}\n")

employees_out.close()
customers_out.close()
