# Calculator
Simple Text Calculator

In this project, you are required to create a Python program that will take a text file
that contains lines of mathematical and logical operations and output the result to another
text file.
The variables that contain the names of input and output files should be in the given
format below. You are required to use this naming convention in your project.

FILE_INPUT = “input.txt”
this file will be in the same folder as your source code file.

FILE_OUTPUT = “<student_number>_<student_name>_<student_surname>_output.txt”
this file will be created by your program to store your output of given input file. You should use the same name format as your source file.

Your program should check the text file one by one, if the given operation is valid, the
result of this operation should be written to the output file. If the given operation is NOT
valid or contains errors, the text “ERROR” should be written to corresponding row. If the
given row is empty and does not contain any text (used as a space between operations to
increase readability), an empty row should also inserted to output file.
# Example inputs, outputs and their explanation are given in table below.

![image](https://github.com/hlnarya/Calculator/assets/142156676/e1fd3734-f1b3-4f90-a75c-f83d2dffccc5)

![image](https://github.com/hlnarya/Calculator/assets/142156676/f4aaa001-2a28-4c1f-97fe-9c74c8882760)

Even though it is not given here, multiple operations in a single line is possible, except
for logical comparison operators. They should only be used once in a line but they can be
used with other operators.

For multiple operation calculation, you need to consider operator precedence of Python
programming language. You can find this information in the following website
“https://docs.python.org/3/reference/expressions.html#operator-precedence”.

You should only consider the arithmetic and logical operators given in the table above,
any other operator or non-digit character should be treated as an “ERROR”.
