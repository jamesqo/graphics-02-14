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

# Transformation matrix is 4x4
# Edge matrix is 4xN
edge_mat  = new_matrix(rows=4, cols=0)
edge_mat = add_edge(edge_mat, 0, 0, 0, 300, 90, 0)
edge_mat = add_edge(edge_mat, 0, 0, 0, 100, 40, 0)
print("edge_mat:")
print_matrix(edge_mat)

print("Testing add_edge()")
edge_mat = add_edge(edge_mat, 0, 0, 0, 100, 100, 0)
print("edge_mat after add_edge((0, 0, 0), (100, 100, 0)):")
print_matrix(edge_mat)

print("Testing add_point()")
edge_mat = add_point(edge_mat, 30, 10, 0)
edge_mat = add_point(edge_mat, 80, 20, 0)
print("edge_mat after add_point((30, 10, 0)) and add_point((80, 20, 0)):")
print_matrix(edge_mat)

print("Drawing lines")
draw_lines( edge_mat, screen, color )
display(screen)
save_extension(screen, "out.png")
