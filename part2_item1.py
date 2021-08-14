class InvalidChoiceError(Exception):
    def __str__(self):
        return "You've entered an invalid option!\n"


# class PerformArithmetic():
#     def __init__(self, number1, number2):
#         self.number1 = number1
#         self.number2 = number2
#
#     def get_sum(self):
#         return 'Result - ' + self.number1 + self.number2
#
#     def get_difference(self):
#         return 'Result - ' + self.number1 - self.number2
#
#     def get_product(self):
#         return 'Result - ' + self.number1 * self.number2
#
#     def get_quotient(self):
#         return 'Result - ' + self.number1 / self.number2
def perform_arithmetic():
    """
    User will choose an operation to perform between two numbers
    An error will be raised for wrong input.
    """
    operation_choices = ['a', 'b', 'c', 'd']
#     print('''a - Addition
# b - Subtraction
# c - Multiplication
# d - Division\n''')
    print(
        'a - Addition\n'
        'b - Subtraction\n'
        'c - Multiplication\n'
        'd - Division\n'
    )

    while True:
        try:
            operation = input("Please select an operation: ").lower()
            if operation not in operation_choices:
                raise ValueError
            else:
                while True:
                    try:
                        number1 = int(input('Give first number: '))
                        break

                    except ValueError:
                        print('Please input a valid number!\n')
                while True:
                    try:
                        number2 = int(input('Give second number: '))
                        if number2 != 0:
                            break
                        elif number2 == 0 and operation == 'd':
                            print("You cannot divide a number by zero!")
                            continue
                    except ValueError:
                        print('Please input a valid number!\n')
                if operation == 'a':
                    result = number1 + number2
                elif operation == 'b':
                    result = number1 - number2
                elif operation == 'c':
                    result = number1 * number2
                elif operation == 'd':
                    result = number1 / number2
                return f"Result: {result}"
        except ValueError:
            print("You have entered an invalid option!")


if __name__ == '__main__':
    print(perform_arithmetic())











