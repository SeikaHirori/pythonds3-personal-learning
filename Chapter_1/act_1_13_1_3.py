

# URL Link: https://runestone.academy/ns/books/published/pythonds3/Introduction/ObjectOrientedProgramminginPythonDefiningClasses.html

class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return f"{self.num}/{self.den}"
    
    def show(self):
        print(f'{self.num}/{self.den}')
    
    @staticmethod 
        # Doc about static method and to obtain output: https://python-course.eu/oop/class-instance-attributes.php
            # Section: Static Methods
    def gcd(m,n):
        while m % n != 0:
            m, n = n, m % n
        return n

    def __add__(self, other_fraction):
        new_num = (self.num * other_fraction.den)+  (self.den * other_fraction.num)
        new_den = self.den * other_fraction.den

        common = self.gcd(new_num, new_den)

        return Fraction(new_num // common, new_den // common)
    
    def __eq__(self, other_fraction):
        first_num = self.num * other_fraction.den
        second_num = other_fraction.num * self.den

        return first_num == second_num