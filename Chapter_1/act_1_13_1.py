


class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return f"{self.num}/{self.den}"
    
    def show(self):
        print(f'{self.num}/{self.den}')

    def __add__(self, other_fraction):
        new_num = (self.num * other_fraction.den)+  (self.den * other_fraction.num)

        new_den = self.den * other_fraction.den

        return Fraction(new_num, new_den)
    
    def gcd(m,n):
        while m % n != 0:
            m, n = n, m % n
        return n

    

if __name__ == "__main__":
    test = Fraction(3,5)
    # test.show()

    test.__str__()
    str(test)
    print(test.gcd(20, 10))



