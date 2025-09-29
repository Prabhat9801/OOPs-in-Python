class Fraction:
    def __init__(self,n,d):
        self.num=n
        self.den=d
    def __str__(self):
        return "{}/{}".format(self.num,self.den)

    def __add__(self,other):
        newnum=self.num*other.den + self.den*other.num
        newden=self.den*other.den
        return Fraction(newnum,newden)
    
    def __sub__(self,other):
        newnum=self.num*other.den - self.den*other.num
        newden=self.den*other.den
        return Fraction(newnum,newden)
    
    def __mul__(self,other):
        newnum=self.num*other.num
        newden=self.den*other.den
        return Fraction(newnum,newden)
    
    def __truediv__(self,other):
        newnum=self.num*other.den
        newden=self.den*other.num
        return Fraction(newnum,newden)
