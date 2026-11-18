#classes
#are a constructor, like a cookie cutter for standardissed object
#class is the highest level object
#self - allows the init class variables to be referenced. - cant use functional variables to be shared. But class using this avia self, allows the parameters to have a knowledge of self, and allows local vars to be shared

##__init__ is a constructor which constructs the class.


class Calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def get_sum(self): #every method within a class uses self, so that it can references all variables within teh class
        return self.a + self.b
    
    def nirrosh_index(self):
        ans = (self.a * self.b)
        return ans
    
    #add deduction, multiplication and division

    def get_deduct(self):
        return self.a - self.b
    
    def multiply(self):
        return self.a * self.b
    def divide(self): 
        return self.a / self.b



if __name__ == "__main__":
    myCalc = Calculator(a=5,b=6) ##define the name of the class, and the parameters you want to use
    print(myCalc.get_deduct())

###so how do we build in a test. Unitest and pytest. unitest is more manual