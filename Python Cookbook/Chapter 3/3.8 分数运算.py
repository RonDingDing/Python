from fractions import Fraction
a = Fraction(5, 4)
b = Fraction(7, 16)
print(a + b)
# 27/16
print(a * b)
# 35/64

# Getting numerator/denominator
c = a * b
print(c.numerator)
# 35
print(c.denominator)
# 64

# Converting to a float
print(float(c))
# 0.546875

# Limiting the denominator of a value
print(c.limit_denominator(8))
# 4/7

# Converting a float to a fraction
x = 3.75
y = Fraction(*x.as_integer_ratio())
print(y)
# Fraction(15, 4)

 