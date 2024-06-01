class Calculator:
    def __init__(self, first_num, second_num, operation):
        self.first_num = first_num
        self.second_num = second_num
        self.operation = operation

    def summa(self):
        return self.first_num + self.second_num

    def subtract(self):
        return self.first_num - self.second_num

    def multi(self):
        return self.first_num * self.second_num

    def division(self):
        if self.second_num == 0:
            # return "Error: Division by zero."
            return self.first_num / self.second_num


while True:

    first_number = int(input("The first number is: "))
    operation = input("The operation is: ")
    second_number = int(input("The second number is: "))

    calc = Calculator(first_number, second_number, operation)
    match operation:
        case '+':
            print(f"{first_number} + {second_number} = {calc.summa()}")
        case '-':
            print(f"{first_number} - {second_number} = {calc.subtract()}")
        case '*':
            print(f"{first_number} * {second_number} = {calc.multi()}")
        case '/':
            print(f"{first_number} / {second_number} = {calc.division()}")    


  