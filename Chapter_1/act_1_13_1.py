


class Fraction:
    def __init__(self, top, bottom):
        self.num = top
        self.den = bottom

    def __str__(self):
        return f"{self.num}/{self.den}"
    
    def show(self):
        print(f'{self.num}/{self.den}')

    

if __name__ == "__main__":
    test = Fraction(3,5)
    # test.show()

    test.__str__()
    str(test)

