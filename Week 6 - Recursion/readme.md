# Week Six Recap - Recursion 

This week, we talked about the key terms that you should add to your UltraSheets for future midterm prep. We also discussed the practice problems found in [slides.pdf](slides.pdf).

## Solutions: 
All solutions can be found in the [solutions.py](solutions.py) file, paired with descriptive comments and writeups for each problem. 

All solutions provided are provided outside of FSG hours, and **are not endorsed neither by the UTM RGASC nor the CSC148H5 Course Staff.** These solutions are meant to be used as a reference, and not a replacement for the problem solving process. Use at your own risk. You are encouraged to attend office hours and ask questions during lectures if there are any parts of the solution that you do not understand. Should you find anything that is incorrect, please open an issue on this repository and I will address it as soon as possible.

## Homework Hint: 
If you're struggling with the homework question, before looking at the solution try reading the following

Recall in MAT102, we defined an even number as a number in the form $2n, n \in \mathbb{Z}$ and an odd number as a number in the form $2n+1, n \in \mathbb{Z}$. Consider the amount of times we subtract from the number to reach 0. **If that number is odd, the number is odd. If that number is even, the number is even.** Can we keep track of how many times we subtract from the number using recursion? 

In other words: If we recurse an odd number of times, which function do we end up in (The original or the helper function)? If we recurse an even number of times, which function do we end up in?
