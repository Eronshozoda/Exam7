class Calculator:
    @staticmethod
    def factorial(n):        
        if n < 0:
            return "Factorial vujud nadorad"
        elif n == 0:
            return 1
        else:
            result = 1
            for i in range(1, n + 1):
                result *= i
            return result

    @staticmethod
    def power(a, b):      
        return a ** b

    @staticmethod
    def sqrt(n):        
            return n ** 0.5


print(f"Factorial: {Calculator.factorial(5)}")
print(f"Daraja:{Calculator.power(2, 3)}")
print(f"Resha az adadamon: {Calculator.sqrt(16)}")
