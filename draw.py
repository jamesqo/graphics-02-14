from display import *
from matrix import *


def draw_lines( matrix, screen, color ):
    for col in transpose(matrix):
        draw_line(*col, screen, color)

def add_edge( matrix, x0, y0, x1, y1 ):
    newmat = new_matrix(rows=nrows(matrix), cols=ncols(matrix) + 1)
    c = ncols(matrix)

    for i in range(nrows(matrix)):
        for j in range(ncols(matrix)):
            newmat[i][j] = matrix[i][j]

    newmat[0][c] = x0
    newmat[1][c] = y0
    newmat[2][c] = x1
    newmat[3][c] = y1
    return newmat

def add_point( matrix, x, y ):
    return add_edge(matrix, x, y, x, y)

def draw_line( x0, y0, x1, y1, screen, color ):

    #swap points if going right -> left
    if x0 > x1:
        xt = x0
        yt = y0
        x0 = x1
        y0 = y1
        x1 = xt
        y1 = yt

    x = x0
    y = y0
    A = 2 * (y1 - y0)
    B = -2 * (x1 - x0)

    #octants 1
    if ( abs(x1-x0) >= abs(y1 - y0) ):

        #octant 1
        if A > 0:
            d = A + B/2

            while x < x1:
                plot(screen, color, x, y)
                if d > 0:
                    y+= 1
                    d+= B
                x+= 1
                d+= A
            #end octant 1 while
            plot(screen, color, x1, y1)
        #end octant 1
#end draw_line
