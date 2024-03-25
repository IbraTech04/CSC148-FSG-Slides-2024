from __future__ import annotations
from typing import Union
from math import e


class ElementaryFunction:
    """
    Abstract class for an arbitrary function

    For obvious reasons, this class should not be modified.
    """
    
    def differentiate(self) -> 'ElementaryFunction':
        """Differentiate the function"""
        raise NotImplementedError("This is an abstract class")
    
    def __str__(self) -> str:
        """Return a string representation of the function"""
        raise NotImplementedError("This is an abstract class")


class Constant(ElementaryFunction):
    """
    Class representing a constant value. I.e: A value not dependent on x
    Representation Invariant: constant is an integer or a float

    This class is provided to you and should not be modified.
    """

    constant: Union[int, float]

    def __init__(self, constant: float) -> None:
        """Constructor for the Constant class"""
        self.constant = constant
    
    def differentiate(self) -> Constant:
        """
        Differentiates the constant value, which is always 0
        >>> str(Constant(5).differentiate())
        '0'
        """
        return Constant(0)

    def __add__(self, other: 'Constant') -> Constant:
        """
        Add two constants

        >>> str(Constant(5) + Constant(5))
        '10'
        >>> str(Constant(5) + Constant(0))
        '5'
        >>> str(Constant(5) + Constant(5.5))
        '10.5'
        """
        if isinstance(other, Constant):
            return Constant(self.constant + other.constant)
        else:
            return NotImplemented
    
    def __sub__(self, other: 'Constant') -> Constant:
        """
        Subtract two constants

        >>> str(Constant(5) - Constant(5))
        '0'
        >>> str(Constant(5) - Constant(0))
        '5'
        >>> str(Constant(5) - Constant(5.5))
        '-0.5'
        """
        if isinstance(other, Constant):
            return Constant(self.constant - other.constant)
        else:
            return NotImplemented
    
    def __mul__(self, other: Constant) -> Constant:
        """
        Multiply two constants

        >>> str(Constant(5) * Constant(5))
        '25'
        >>> str(Constant(5) * Constant(0))
        '0'
        >>> str(Constant(5) * Constant(5.5))
        '27.5'
        """
        if isinstance(other, Constant):
            return Constant(self.constant * other.constant)
        else:
            return NotImplemented
    
    def __truediv__(self, other: Constant) -> Constant:
        """
        Divide two constants
        Precondition: other is of type Constant and other.constant is not 0

        >>> str(Constant(5) / Constant(5))
        '1.0'
        >>> str(Constant(5) / Constant(2))
        '2.5'
        >>> str(Constant(5) / Constant(0))
        Traceback (most recent call last):
        ZeroDivisionError: division by zero
        """
        if isinstance(other, Constant):
            return Constant(self.constant / other.constant)
        else:
            return NotImplemented
    
    def __str__(self) -> str:
        """
        Return a string representation of the constant
        >>> str(Constant(5))
        '5'
        >>> str(Constant(5.5))
        '5.5'
        >>> str(Constant(0) + Constant(5))
        '5'
        """
        return str(self.constant)


class Operator(ElementaryFunction):
    """
    Abstract class for an operator

    For obvious reasons, this class should not be modified.
    """

    def differentiate(self) -> 'ElementaryFunction':
        """
        Differentiate the operator
        """
        raise NotImplementedError("This is an abstract class")

    def __str__(self):
        """
        Return a string representation of the operator
        """
        raise NotImplementedError("This is an abstract class")


class Addition(Operator):
    """
    Class representing the addition of two functions
    =========== Public Attributes ===========
    a: ElementaryFunction - The first function to be added
    b: ElementaryFunction - The second function to be added
    
    ======== Representation Invariants ========
    a and b are of type ElementaryFunction
    """

    a: ElementaryFunction
    b: ElementaryFunction

    def __init__(self, a: ElementaryFunction, b: ElementaryFunction) -> None:
        """
        Defines addition of two arbitrary functions
        """
        self.a = a
        self.b = b

    def differentiate(self) -> ElementaryFunction:
        """
        Applies the sum and chain rules to differentiate the addition

        >>> str(Addition(Constant(5), Constant(5)).differentiate())
        '(0) + (0)'
        >>> str(X(Constant(5), Constant(5)).differentiate())
        '(25 * x^4)'
        """
        return Addition(self.a.differentiate(), self.b.differentiate())

    def __str__(self) -> str:
        """
        Return a string representation of the addition
        """
        return f"({self.a}) + ({self.b})"


class Subtraction(Operator):
    """Class representing the subtraction of two functions"""

    a: ElementaryFunction
    b: ElementaryFunction

    def __init__(self, a: ElementaryFunction, b: ElementaryFunction) -> None:
        """Constructor for the Subtraction class"""
        self.a = a
        self.b = b

    def differentiate(self) -> 'ElementaryFunction':
        """
        Differentiate the subtraction

        >>> str(Subtraction(Constant(5), Constant(5)).differentiate())
        '(0) - (0)'
        >>> str(X(Constant(5), Constant(5)).differentiate())
        '(25 * x^4)'
        >>> str(Subtraction(X(Constant(5), Constant(5)), X(Constant(5), Constant(5))).differentiate())
        '((25 * x^4)) - ((25 * x^4))'
        """
        return Subtraction(self.a.differentiate(), self.b.differentiate())

    def __str__(self) -> str:
        """Return a string representation of the subtraction"""
        return f"({self.a}) - ({self.b})"


class Multiplication(Operator):
    """
    Multiplication of two arbitrary functions
    ======== Public Attributes ========
    a: ElementaryFunction - The first function to be multiplied
    b: ElementaryFunction - The second function to be multiplied
    """
    a: ElementaryFunction
    b: ElementaryFunction

    def __init__(self, a: ElementaryFunction, b: ElementaryFunction):
        """
        Constructor for the Multiplication class
        """
        self.a = a
        self.b = b

    def differentiate(self):
        """
        Differentiate the multiplication by applying the product rule
        >>> str(Multiplication(Constant(5), Constant(5)).differentiate())
        '((0 * 5)) + ((5 * 0))'
        >>> str(Multiplication(X(Constant(5), Constant(5)), X(Constant(5), Constant(5))).differentiate())
        '(((25 * x^4) * (5 * x^5))) + (((5 * x^5) * (25 * x^4)))'
        """

        # Apply product rule: (u*v)' = u'v + uv'
        return Addition(Multiplication(self.a.differentiate(), self.b), Multiplication(self.a, self.b.differentiate()))

    def __str__(self):
        return f"({self.a} * {self.b})"

class Division(Operator):
    """
    Class representing the division of two functions
    """

    a: ElementaryFunction
    b: ElementaryFunction

    def __init__(self, a: ElementaryFunction, b: ElementaryFunction):
        """Constructor for the Division class"""
        self.a = a
        self.b = b

    def differentiate(self):
        """
        Differentiate the division by applying the quotient rule
        >>> str(Division(Constant(5), Constant(5)).differentiate())
        '(((0 * 5)) - ((5 * 0)) / (5^2))'
        >>> str(Division(X(Constant(5), Constant(5)), X(Constant(5), Constant(5))).differentiate())
        '((((25 * x^4) * (5 * x^5))) - (((5 * x^5) * (25 * x^4))) / ((5 * x^5)^2))'
        """

        # Apply quotient rule: (u/v)' = (u'v - uv') / v^2
        return Division(Subtraction(Multiplication(self.a.differentiate(), self.b), Multiplication(self.a, self.b.differentiate())), Exponential(self.b, Constant(2)))

    def __str__(self):
        """Return a string representation of the division"""
        return f"({self.a} / {self.b})"

class Exponential(Operator):
    # Class for the exponential of a function
    a: ElementaryFunction
    b: Constant

    def __init__(self, a: ElementaryFunction, b: Constant):
        self.a = a
        self.b = b

    def differentiate(self):
        """
        Applies the power + chain rule to differentiate the exponential

        >>> str(Exponential(Constant(5), Constant(5)).differentiate())
        '((5 * (5^4)) * 0)'
        >>> str(Exponential(X(Constant(5), Constant(5)), Constant(5)).differentiate())
        '((5 * ((5 * x^5)^4)) * (25 * x^4))'
        """
        # Apply power + chain rule: (u^n)' = n*u^(n-1)*u'
        return Multiplication(Multiplication(self.b, Exponential(self.a, Constant(self.b.constant - 1))), self.a.differentiate())

    def __str__(self):
        return f"({self.a}^{self.b})"


class X(ElementaryFunction):
    """
    Class representing an arbitrary function of x
    =========== Public Attributes ===========
    coefficient: Constant - The constant value of the function. I.e: The coefficient of x
    power: Constant - The power of the function. I.e: The exponent of x
    """

    coefficient: Constant
    power: Constant

    def __init__(self, constant: Constant, power: Constant) -> None:
        """Constructor for the X class"""
        self.coefficient = constant
        self.power = power
    
    def differentiate(self) -> ElementaryFunction:
        """
        Differentiate the function of x
        >>> str(X(Constant(5), Constant(5)).differentiate())
        '(25 * x^4)'
        >>> str(X(Constant(5), Constant(1)).differentiate())
        '5'
        >>> str(X(Constant(5), Constant(0)).differentiate())
        '0'
        """
        if self.power.constant == 0:
            return Constant(0)
        if self.power.constant == 1:
            return self.coefficient
        return X(self.coefficient * self.power, self.power - Constant(1))

    def __str__(self) -> str:
        """
        Return a string representation of the function of x

        >>> str(X(Constant(5), Constant(5)))
        '(5 * x^5)'
        """
        return f"({self.coefficient} * x^{self.power})"


class Sin(ElementaryFunction):
    """
    Class representing the sine of a function
    =========== Public Attributes ===========
    function: ElementaryFunction - The function to be applied the sine to
    """

    function: ElementaryFunction

    def __init__(self, function: ElementaryFunction) -> None:
        """Constructor for the Sin class"""
        self.function = function

    def differentiate(self) -> ElementaryFunction:
        """
        Differentiate the sine of a function
        >>> str(Sin(X(Constant(5), Constant(5))).differentiate())
        '(cos((5 * x^5)) * (25 * x^4))'
        """
        return Multiplication(Cos(self.function), self.function.differentiate())

    def __str__(self) -> str:
        """Return a string representation of the sine of a function"""
        return f"sin({self.function})"


class Cos(ElementaryFunction):
    """
    Class representing the cosine of a function
    =========== Public Attributes ===========
    function: ElementaryFunction - The function to be applied the cosine to
    """

    function: ElementaryFunction

    def __init__(self, function: ElementaryFunction) -> None:
        """Constructor for the Cos class"""
        self.function = function

    def differentiate(self) -> ElementaryFunction:
        """
        Differentiate the cosine of a function
        >>> str(Cos(X(Constant(5), Constant(5))).differentiate())
        '(-1 * (sin((5 * x^5)) * (25 * x^4)))'
        """
        return Multiplication(Constant(-1), Multiplication(Sin(self.function), self.function.differentiate()))

    def __str__(self) -> str:
        """Return a string representation of the cosine of a function"""
        return f"cos({self.function})"


class Tan(ElementaryFunction):
    """
    Class representing the tangent of a function
    =========== Public Attributes ===========
    function: ElementaryFunction - The function to be applied the tangent to
    """

    function: ElementaryFunction

    def __init__(self, function: ElementaryFunction) -> None:
        """Constructor for the Tan class"""
        self.function = function

    def differentiate(self) -> ElementaryFunction:
        """
        Differentiate the tangent of a function
        >>> str(Tan(X(Constant(5), Constant(5))).differentiate())
        '((sec((5 * x^5))^2) * (25 * x^4))'
        """
        return Multiplication(Exponential(Secant(self.function), Constant(2)), self.function.differentiate())

    def __str__(self) -> str:
        """Return a string representation of the tangent of a function"""
        return f"tan({self.function})"


class Secant(ElementaryFunction):
    """
    Class representing the secant of a function
    =========== Public Attributes ===========
    function: ElementaryFunction - The function to be applied the secant to
    """

    function: ElementaryFunction

    def __init__(self, function: ElementaryFunction) -> None:
        """Constructor for the Secant class"""
        self.function = function

    def differentiate(self) -> ElementaryFunction:
        """
        Differentiate the secant of a function
        >>> str(Secant(X(Constant(5), Constant(5))).differentiate())
        '((tan((5 * x^5)) * (25 * x^4)) * sec((5 * x^5)))'
        """
        return Multiplication(Multiplication(Tan(self.function), self.function.differentiate()), Secant(self.function))

    def __str__(self) -> str:
        """Return a string representation of the secant of a function"""
        return f"sec({self.function})"


class Log(ElementaryFunction):
    """
    Class representing a logarithmic function
    =========== Public Attributes ===========
    a: base of the logarithm
    function: ElementaryFunction - The function to be applied the logarithm to
    """
    
    a: Constant
    function: ElementaryFunction

    def __init__(self, a: Constant, function: ElementaryFunction) -> None:
        """Constructor for the Log class"""
        self.a = a
        self.function = function

    def differentiate(self) -> ElementaryFunction:
        """
        Differentiate the logarithm of a function
        >>> str(Log(Constant(5), X(Constant(5), Constant(5))).differentiate())
        '((1 / ((5 * x^5) * log_2.718281828459045(5))) * (25 * x^4))'
        """
        return Multiplication(Division(Constant(1), Multiplication(self.function, Log(Constant(e), Constant(self.a.constant)))), self.function.differentiate())

    def __str__(self) -> str:
        """Return a string representation of the logarithm of a function"""
        return f"log_{self.a}({self.function})"


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    import python_ta
    python_ta.check_all(config={
        'extra-imports': ['__future__', 'typing'],
        'allowed-io': [],
        'max-line-length': 100,
        'disable': ['E1136']
    })