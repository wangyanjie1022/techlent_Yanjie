class calculator():
    def add(self, num1, num2):
        return num1+num2
    def substract(self, num1, num2):
        return num1 - num2
    def multiple(self, num1, num2):
        return num1 *  num2
    def devide(self, num1, num2):
        if num2 == 0:
            return 0
        else:
            return num1/num2    
if __name__ == "__main__":
    cal = calculator()
    
    print (cal.add(1,8))
    print(cal.substract(1,8))
    print(cal.multiple(1,8))
    print(cal.devide(1,8))
