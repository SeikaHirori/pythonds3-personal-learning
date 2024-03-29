

import sys

# URL: https://runestone.academy/ns/books/published/pythonds3/Introduction/Exercises.html

import fractions
from multiprocessing.sharedctypes import Value


class Fraction:
    def __init__(self, top, bottom):

        try: #p5
            top = int(top)
        except ValueError:
            print(f"{top} is not an integer!")
            sys.exit()

        try: #p5
            bottom = int(bottom)
        except ValueError:
            print(f"{bottom} is not an integer!")
            sys.exit()

        common = self.gcd(top,bottom)

        self.num = top / common
        self.den = bottom / common

        self.check_negative_denominator()
    
    
    def check_negative_denominator(self): #6
        if self.den < 0:
            self.num *= -1
            self.den *= -1            

    # Imported code === START ===

    def __str__(self):
        return f"{self.num}/{self.den}"
    
    def show(self):
        print(f'{self.num}/{self.den}')
    
    @staticmethod 
        # Doc about static method and to obtain output: https://python-course.eu/oop/class-instance-attributes.php
            # Section: Static Methods
    def gcd(top,bottom):
        
        while top % bottom != 0:
            top, bottom = bottom, top % bottom
        return bottom
        

    def __add__(self, other_fraction):
        new_num = (self.num * other_fraction.den)+  (self.den * other_fraction.num)
        new_den = self.den * other_fraction.den

        return Fraction(new_num, new_den)
    
    def __eq__(self, other_fraction):
        first_num = self.getDecimalVersion()
        second_num = self.getDecimalVersion()

        return first_num == second_num
    
    def __sub__(self, other_fraction):
        new_num = (self.num * other_fraction.den) - (other_fraction.num * self.den)
        new_den = self.den * other_fraction.den

        return Fraction(new_num, new_den)
    
    def __mul__(self, other_fraction):
        new_num = self.num * other_fraction.num
        new_den = self.den * other_fraction.den

        # common = self.gcd(new_num, new_den)
        
        # return Fraction(new_num // common, new_den // common)

        return Fraction(new_num,new_den)
    
    def __truediv__(self, other_fraction):
        new_num = self.num * other_fraction.den
        new_den = other_fraction.num * self.den

        # common = self.gcd(new_num, new_den)

        # return Fraction(new_num // common, new_den // common)

        return Fraction(new_num, new_den)
    
    
    def __gt__(self, other_fraction):
        # f1 = self.num / self.den
        # f2 = other_fraction.num / other_fraction.den

        f1 = self.getDecimalVersion()
        f2 = other_fraction.getDecimalVersion()

        return f1 > f2

    def __lt__(self, other_fraction):
        f1 = self.num / self.den
        f2 = other_fraction.num / other_fraction.den

        return f1 < f2
    # Import code === ENDS ===

    #p1
    def getNum(self):
        return self.num
    
    #p1
    def getDen(self):
        return self.den
        
    def getDecimalVersion(self):
        converted = self.getNum()/self.getDen()
        return converted

    #p4
    def __ge__(self, other_fraction): 

        f1 = self.getDecimalVersion()
        f2 = other_fraction.getDecimalVersion()

        return f1 >= f2
    
    #p4
    def __le__(self, other_fraction):
        f1 = self.getDecimalVersion()
        f2 = other_fraction.getDecimalVersion()


        return f1 <= f2 
    
    #p4
    def __ne__(self, other_fraction):
        f1 = self.getDecimalVersion()
        f2 = other_fraction.getDecimalVersion()

        return f1 != f2

    #p7
    def __radd__(self, other_obj):
        sum_num = (self.num * other_obj.den) + (other_obj.num * self.den)
        sum_den = self.den * other_obj.den

        return Fraction(sum_num, sum_den)
    
    #p8:
    def __iadd__(self, other_obj):
        sum_num = sum_num = (self.num * other_obj.den) + (other_obj.num * self.den)
        sum_den = self.den * other_obj.den

        return Fraction(sum_num, sum_den)

    #p9
    def __repr__(self):
        return f'Fraction({(self.num)}, {self.den})'
        
class testRaddFraction: # TESTING ONLY FOR #p7
        # reference: https://stackoverflow.com/a/38196153
    def __init__(self, top, bottom) -> None:
        self.num = top
        self.den = bottom
class demo_fraction(Fraction):

    def __init__(self, top, bottom):
        super().__init__(top, bottom)

    def demo_set1():
        f1 = Fraction(1,10)
        f2 = Fraction(7,10)

        print(f1 + f2)
        print()

        print(f1 - f2)
        print()
        
        print(f1 * f2)
        print()

        print(f1 / f2)
        print()

        print(f1 == f2)
        print()

        print(f1 < f2)
        print()

        print(f1 > f2)
        print()

if __name__ == "__main__":

    # test1 = demo_fraction
    # test1.demo_set1()

    f1 = Fraction(-1,5)

    print(f1)
    print()
    print(repr(f1))