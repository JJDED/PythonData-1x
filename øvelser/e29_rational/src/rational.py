#!/usr/bin/env python3

from math import gcd

class Rational(object):
    def __init__(self, numerator, denominator): #numerator = tæller og denominator = nævner
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        d = gcd(self.numerator, self.denominator)
        return f"{self.numerator // d}/{self.denominator // d}"
 
    def __add__(self, r):
        if isinstance(r, Rational):
            return Rational(
                self.numerator * r.denominator + r.numerator * self.denominator, 
                self.denominator * r.denominator)
        elif isinstance (r, int):
            return Rational(self.denominator+self.numerator*r, self.denominator)
        else:
            raise Exception("Invalid type.")
    
def main():
    r1=Rational(1,4)
    r2=Rational(2,3)
    print(r1)
    print(r2)
    #print(r1*r2)
    #print(r1/r2)
    print(r1+r2)
    #print(r1-r2)
    #print(Rational(1,2) == Rational(2,4))
    #print(Rational(1,2) > Rational(2,4))
    #print(Rational(1,2) < Rational(2,4))

if __name__ == "__main__":
    main()
