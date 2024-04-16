# Week 10 Homework - A Derivative Calculator

## Introduction
This week in CSC148, you covered what is arguably the most important topic in CSC148 that ties together everything you've learned so far: Expression Trees (aka. Abstract Syntax Trees). ASTs are a really abstract concept that can be difficult to wrap your head around, but they are a fundamental concept in computer science and are used in many different areas of computer science, including compilers, interpreters, and even in the implementation of programming languages themselves.

To help you understand the concept of ASTs, we're going to have you implement a simple derivative calculator. The derivative of a function is a fundamental concept in calculus, and is a great way to understand how ASTs can be used to represent mathematical expressions. You've all passed MAT135 by now (I'd hope....), so this should be a peice of cake for you!

## The Task
You are to implement a simple derivative calculator that can take in a mathematical expression and return its derivative. The mathematical expression will be represented as an AST, and you will need to implement the AST class and the derivative function. Starter code is provided for you, including doctests and type hints, found in [Functions.py](Functions.py). Note that you should only need to modify this file, as the other file [DerivativeCalculator.py](DerivativeCalculator.py) is the main file that will be used to test your implementation. 

The abstract idea is as follows: All parts of an arbitrary mathmatical function $f(x)$ have their own differentiation rules. For instance: Addition, subtraction, multiplication, and division dictate the order of operations, and functions of $x$ dictate the differentiation rules. For instance, the derivative of $x^2$ is $2x$, and the derivative of $sin(x)$ is $cos(x)$

In our file [Functions.py](Functions.py), we abuse Polymorphism to allow us to represent all of these different types of functions as a single class, `ElementaryFunction`. The most important method of this class is the `differentiate` method (which you will be implementing), which will return the derivative of the function. The starter code has everything you will need to get started. All you need to do is fill in the `differentiate` method for each of the different types of functions, and understand how to use the `ElementaryFunction` class to represent the AST of a mathematical expression.

## Task 1: Understanding the Starter Code
Take a moment to familiarize yourself with the starter code provided, and convince yourself that this is the correct way to represent a mathematical expression as an AST. The `ElementaryFunction` class is a recursive data structure, and the `differentiate` method is a recursive function that will traverse the AST and return the derivative of the function. The "leaves" of this tree are the `Constant` and `X` classes. These classes are subclasses of `ElementaryFunction` and represent the constant and variable parts of the function, respectively. The other classes are `Addition`, `Subtraction`, `Multiplication`, `Division`, `Exponential`, `Sin`, `Cos`, `Tan`, `Sec`, and `Log`. You will be implementing the `differentiate` method for each of these classes, so take a moment to understand how they relate to each other.

## Task 2: Implementing the different differentiation rules
This task will have you implement `Addition`, `Subtraction`, `Multiplication`, and `Division`. These will form the basis of the differentiation rules for the other functions. The key to this class is realizing that any `ElementaryFunction` passed into each of these classes is *differentiable*, and that these classes don't care what the function is, only that it can be differentiated. This is the power of polymorphism; And the part that stumps most students.

Once you understand and have implemented these classes, you can move on to Task 3.

## Task 3: Functions with respect to X
This task will have you implement the `X` class, which represents the variable part of the function. This class is the simplest to implement, as it only requires a constant and exponent to be dealt with. For simplicity, `Constant` objects can auto-simplify themselves using the defined magic methods. 

## Task 3.5: Exponential Functions
This task is an *extension* of Task 3, and will have you implement the `Exponential` class. This class is a bit more complex than the previous classes, as it requires the use of the chain rule. The chain rule states that the derivative of a function $f(g(x))$ is $f'(g(x)) \cdot g'(x)$. This is a bit more complex than the previous classes, but is a good way to test your understanding of the previous classes.

*Hint: Spam Chain rule everywhere. The function doesn't care if it's actually required.*

## Task 4: Trigonometric and Logarithmic Functions
This task will have you implement the `Sin`, `Cos`, `Tan`, `Sec`, and `Log` classes. These classes are a bit more complex than the previous classes, as they require the use of the chain rule and the quotient rule. The quotient rule states that the derivative of a function $\frac{f(x)}{g(x)}$ is $\frac{f'(x)g(x) - f(x)g'(x)}{g(x)^2}$. This is a bit more complex than the previous classes, but is a good way to test your understanding of the previous classes.

Once again, your hint is to spam everything everywhere even if you don't think it's needed. Worst-case scenario, you'll end up with an extra coefficient of 1, which can be simplified using magic methods.

# Task 5: Challenge! (Optional)
You'll notice throughout the code that all the `doctests` assume that the derivative does not get simplified (i.e: `Constant`s of value 1 don't get removed). This is because this activity is meant to be realtively low-stakes and is meant to be a learning experience. However, if you're feeling up to the challenge, you can implement the `simplify` method in the `ElementaryFunction` class, and modify the `doctests` to reflect this. This will require you to implement the `__add__`, `__sub__`, `__mul__`, and `__truediv__` magic methods in the `ElementaryFunction` class, and will require you to modify the `doctests` to reflect this. This is a good way to test your understanding of the previous classes, and is a good way to test your understanding of the previous classes.

This *is* a more difficult challenge and definitely has more room for error, so it's not required. However, if you're feeling up to the challenge, it's a good way to test your understanding of the previous classes, and to make a more functional derivative calculator.
