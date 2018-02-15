#!/usr/bin/env python

from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix(rows=4, cols=8)

print_matrix(matrix)

matrix = new_matrix(rows=5, cols=5)
print_matrix(matrix)
ident(matrix)
print_matrix(matrix)

fib = new_matrix(rows=2, cols=2)
fib[0][0] = 1
fib[0][1] = 1
fib[1][0] = 1
fib[1][1] = 0
print_matrix(fib)

fibn = fib
for i in range(10):
    fibn = matrix_mult(fibn, fib)
    print_matrix(fibn)

draw_lines( matrix, screen, color )
display(screen)
