
class Rational:

    @staticmethod
    def gcd(a, b):
        # Euclid's Algorithm for Greatest Common Divisor, 300 BCE
        # (https://en.wikipedia.org/wiki/Euclidean_algorithm)

        if (b == 0):
            return a;
        return Rational.gcd(b, a % b)
    
    def __init__(self, numerator, denominator = 1):
        if (denominator < 0):
            numerator, denominator = numerator * -1, denominator * -1
        
        g = Rational.gcd(numerator, denominator)
        self._fraction = (numerator // g, denominator // g)

    def __repr__(self):
        return "Rational({0}, {1})".format(self.numerator(), self.denominator())
    
    def __str__(self):
        if self.denominator() == 1:
            return str(self.numerator())
        return "{0}/{1}".format(self.numerator(), self.denominator())

    def numerator(self):
        return self._fraction[0]

    def denominator(self):
        return self._fraction[1]

    def reciprocal(self):
        return Rational(self.denominator(), self.numerator())

    @staticmethod
    def add(x, y):
        n = x.numerator() * y.denominator() + y.numerator() * x.denominator()
        d = x.denominator() * y.denominator()
        return Rational(n, d)

    @staticmethod
    def sub(x, y):
        return Rational.add(x, -y)

    @staticmethod
    def mul(x, y):
        return Rational(x.numerator() * y.numerator(), x.denominator() * y.denominator())

    @staticmethod
    def div(x, y):
        return Rational.mul(x, y.reciprocal())
    
    def __neg__(self):
        return Rational(-1 * self.numerator(), self.denominator())

    def __add__(self, x):
        return Rational.add(self, x) 

    def __sub__(self, x):
        return Rational.sub(self, x) 

    def __mul__(self, x):
        return Rational.mul(self, x) 

    def __truediv__(self, x):
        return Rational.div(self, x) 

    def __int__(self):
        return self.numerator() // self.denominator()
    
    def __float__(self):
        return self.numerator() / self.denominator()


    def _compare_normalized_numerators_(self, x, comparator): 
        if type(x) == int:
            x = Rational(x)

        a = self.numerator() * x.denominator()
        b = x.numerator() * self.denominator()
        return comparator(a, b)
        
    def __eq__(self, x):
        return self._compare_normalized_numerators_(x, lambda a, b: (a == b))

    def __lt__(self, x):
        return self._compare_normalized_numerators_(x, lambda a, b: (a < b))
    
    def __le__(self, x):
        return self._compare_normalized_numerators_(x, lambda a, b: (a <= b))

    def __gt__(self, x):
        return self._compare_normalized_numerators_(x, lambda a, b: (a > b))

    def __ge__(self, x):
        return self._compare_normalized_numerators_(x, lambda a, b: (a >= b))

    def __ne__(self, x):
        return not (self == x)

third = Rational(1, 3)
one_over_three = Rational(1, 3)

# normalization
assert(Rational(1, 3) == Rational(10, 30))
assert(Rational(-1, -3) == Rational(1, 3))
assert(Rational(1, -3) == Rational(-1, 3))

# repr, str, and format work correctly
assert(eval(repr(third)) == third)
assert(str(third) == '1/3')
assert("{0}".format(third) == '1/3')

# some maths
assert(Rational(-1, 3) == -Rational(1, 3))
assert(third * Rational(3) == Rational(1))
assert(third * Rational(3) == 1)
assert(Rational(2, 3) - Rational(1, 3) == Rational(1, 3))
assert(Rational(2, 3) / Rational(2, 1) == Rational(1, 3))

# tests
assert(Rational(1, 3) < Rational(11, 30))
assert(Rational(1, 3) <= Rational(1, 3))
assert(Rational(1, 3) != Rational(3, 1))
assert(Rational(-1, 3) == -Rational(1, 3))

