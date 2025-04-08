class Fraction: 
    def __init__(x,n,d):

        x.num = n
        x.den =d
        print(f"{x.num}/{x.den}")

    # this add is a magic method, special method that is a dunder ,method 

    def __add__(self,other):    # so x's num and den will go to self , and y's num and den will go to other 
        temp_num = (self.num * other.den) + (other.num *self.den)
        temp_den = self.den * other.den

        return temp_num/temp_den
    
    def __sub__(self,other):
        temp_num = (self.num * other.den) - (other.num *self.den)
        temp_den = self.den * other.den
        return temp_num/temp_den






x = Fraction(2,2)    
y = Fraction(9,3)

print(x+y)
