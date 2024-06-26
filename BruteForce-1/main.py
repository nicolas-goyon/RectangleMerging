from base import *
from Grid import *
from Rectangle import *
from generalUtils import *
import time

# ---------------------------------------------------------------------------- #
#                                     MAIN                                     #
# ---------------------------------------------------------------------------- #


testArr = [
    [1, 1, 1, 1],
    [0, 1, 1, 0],
    [0, 0, 2, 0],
    [1, 1, 1, 1],
]



big = testArr

testGrid = SolveGrid(big)
display_array(big)
print("-----------------")
startTime = time.time()
# testGrid.solve(5)
numberOfSteps = testGrid.solveMax()
endTime = time.time()
testGrid.display()
print("Number of steps : ", numberOfSteps)
print("Time : ", endTime - startTime)
