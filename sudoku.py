from pulp import *

# the puzzle is in 'data.in' and it will be stored in a matrix
f=open("data.in")
matrix=[]

for line in f:
    matrix.append([int(x) for x in line.split()])

# print(matrix)

# printing the sudoku puzzle

print("Sudoku Problem")

for r in range(len(matrix)):
    if r==0 or r==3 or r==6:
        print("+-------+-------+-------+")
    for c in range(len(matrix[r])):
        if c==0 or c==3 or c==6:
            print("| ", end="")
        if matrix[r][c]!=0:
            print(matrix[r][c], end=" ")
        else:
            print(" ",end=" ")
        if c==8:
            print("|")
print("+-------+-------+-------+")

# Making a sequence form 1 to 9

sequence=[x for x in range(1,10)]
# print(sequence)

# All the values, rows and columns can be stored as a sequence of integers from 1 to 9

vals=sequence
rows=sequence
cols=sequence

# Making a list with all 9 charts/boxes from the puzzle

squareBoxes=[]

for i in range(3):
    for j in range(3):
        squareBoxes.append([(rows[3*i+k], cols[3*j+l]) for k in range(3) for l in range(3)])

# print(squareBoxes)

# Define problem Sudoku

problem=LpProblem("Sudoku_Problem", LpMinimize)

# Making a set of variables
# Set up the choices for Sudoku
# We will use tuple (x, y, z) storing a binary value
# 1 means value x is in row y and column z; 0 means the opposite

choices=LpVariable.dicts("Choice", (vals, rows, cols), 0, 1, LpInteger)

# print(choices)


# Set up the constraints
# There must be only one number from 1 to 9 in each box; same rule for rows and columns

# Adding arbitrary objective function
problem+=0

for r in rows:
    for c in cols:
        problem+=lpSum([choices[v][r][c] for v in vals])==1

for v in vals:
    for r in rows:
        problem+=lpSum([choices[v][r][c] for c in cols])==1

    for c in cols:
        problem+=lpSum([choices[v][r][c] for r in rows])==1

    for b in squareBoxes:
        problem+=lpSum([choices[v][r][c] for (r,c) in b])==1

# The values already given in the input are fixed, so there's one extra constraint

for r in range(len(matrix)):
    for c in range(len(matrix[r])):
        value=matrix[r][c]
        if value!=0:
            problem+= choices[value][r+1][c+1]==1

# Solving the Sudoku problem

problem.solve()

# print("Status: ", LpStatus[problem.status])

# Printing the solution


for r in rows:
    if r==1 or r==4 or r==7:
        print("+-------+-------+-------+")
    for c in cols:
        for v in vals:
            if choices[v][r][c].varValue ==1:
                if c==1 or c==4 or c==7:
                    print('|', end=" ")
                print(v, end=" ")

                if c==9:
                    print('|')

print("+-------+-------+-------+")











