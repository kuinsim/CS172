#Suin Kim CS-172 Section 061

#import ComplexNumber class from complex.py
import sys
from complex import ComplexNumber

#function for a(c, k)
def a(c, k):
    sum = ComplexNumber(0, 0)
    for n in range(k+1):
        sum+=c.__pow__(n)
    sum+=ComplexNumber(1, 0)
    sum-= c
    return sum

#function for b(c, k)
def b(c, k):
    numerator = ComplexNumber(1, 0) - (c.__pow__(k+1))
    denominator = ComplexNumber(1, 0) - c
    return numerator/denominator

#command line prompt
if __name__ == "__main__":
    xValue = float(sys.argv[1])
    yValue = float(sys.argv[2])
    kValue = float(sys.argv[3])
    c = ComplexNumber(xValue, yValue)

    A = a(c, kValue)
    B = b(c, kValue)

    print("a(" + str(c) + ", " + str(kValue) + ") = " + str(A))
    print("b(" + str(c) + ", " + str(kValue) + ") = " + str(B))