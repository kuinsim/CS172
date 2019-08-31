# Suin Kim CS-172 Section 061

class ComplexNumber():
    #initializes real and imaginary values for complex number
    def __init__(self, x, y):
        self.__real = x
        self.__imaginary = y

    #returns string representation of complex number
    def __str__(self):
        if (self.__imaginary >= 0):
            return str(self.__real) + '+' + str(self.__imaginary) + 'i'
        else:
            return str(self.__real) + str(self.__imaginary) + 'i'

    #returns real value of complex number
    def getReal(self):
        return self.__real

    #returns imaginary value of complex number
    def getImaginary(self):
        return self.__imag

    #adds real and imaginary values of two complex numbers
    def __add__(self, other):
        real = self.__real + other.__real
        imaginary = self.__imaginary + other.__imaginary
        return ComplexNumber(real, imaginary)

    #subtracts one complex number's real and imaginary values from another
    def __sub__(self, other):
        real = self.__real - other.__real
        imaginary = self.__imaginary - other.__imaginary
        return ComplexNumber(real, imaginary)

    #multiplies complex numbers
    def __mul__(self, other):
        real = self.__real * other.__real - self.__imaginary * other.__imaginary
        imaginary = self.__real * other.__imaginary + self.__imaginary * other.__real
        return ComplexNumber(real, imaginary)

    #divides complex number by another
    def __truediv__(self, other):
        real = (self.__real * other.__real + self.__imaginary * other.__imaginary) / (
                    other.__real ** 2 + other.__imaginary ** 2)
        imaginary = (-self.__real * other.__imaginary + self.__imaginary * other.__real) / (
                    other.__real ** 2 + other.__imaginary ** 2)
        return ComplexNumber(round(real, 2), round(imaginary, 2))

    #raises complex number to power
    def __pow__(self, exp):
        i = 2
        product = ComplexNumber(self.__real, self.__imaginary)
        while (i <= exp):
            product = product.__mul__(self)
            i = i + 1
        return product

#copy and pasted from hw2.pdf
if __name__ == "__main__":
    c1 = ComplexNumber(4, 3)
    c2 = ComplexNumber(2, 8)
    print(c1)  # 4+3i
    print(c1 + c2)  # 6+11i
    print(c1 * c2)  # -16+38i
    print(c1 / c2)  # 0.47-0.28i
    print(c1 ** 3)  # -44+117i


