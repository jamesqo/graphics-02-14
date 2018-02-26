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

print("Testing ident()")
ident(matrix)
print_matrix(matrix)

print("Testing matrix_mult()")
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

# Transformation matrix is 6x6
# Edge matrix is 6xN
edge_mat  = new_matrix(rows=4, cols=2)
# Add edges [(3, 5), (4, 1)], [(7, 6), (9, 10)]
edge_mat[0] = [3,  7]
edge_mat[1] = [5,  6]
edge_mat[2] = [4,  9]
edge_mat[3] = [1, 10]

draw_lines( edge_mat, screen, color )
display(screen)
